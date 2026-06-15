#!/usr/bin/env python3
"""Regenerate docs/repeat-guests-by-nights.json from beds24-fulldata.xlsx (run locally)."""
import json
import re
from collections import defaultdict

import pandas as pd

XLSX = "beds24-fulldata.xlsx"
OUT = "docs/repeat-guests-by-nights.json"


def norm(n: str) -> str:
    return re.sub(r"\s+", " ", str(n)).strip().upper()


def main() -> None:
    df = pd.read_excel(XLSX, header=1)
    df = df[df["Number"].notna()].copy()
    df = df[df["Status"].isin(["Confirmed", "New"])].copy()

    def parse_d(s):
        try:
            return pd.to_datetime(re.sub(r"\s+", " ", str(s)).strip(), format="%a %d %b %Y")
        except Exception:
            return pd.NaT

    df["ci"] = df["Check In"].map(parse_d)
    df = df.sort_values("ci")
    df["nights"] = pd.to_numeric(df["Nights"], errors="coerce").fillna(0).astype(int)

    stay = df.groupby("Master Id", sort=False).agg(
        gname=("Full Name", "first"),
        nights=("nights", "max"),
    ).reset_index()
    stay["gname"] = stay["gname"].map(norm)
    stay = stay[~stay["gname"].isin(["BOOKING", "NAN", ""])]

    by_guest: dict[str, list[int]] = defaultdict(list)
    for _, r in stay.iterrows():
        by_guest[r["gname"]].append(int(r["nights"]))

    repeat_guests = {g: ns for g, ns in by_guest.items() if len(ns) >= 2}

    def bucket_n(n: int):
        if n <= 1:
            return None
        return min(n, 10)

    bucket_to_names: dict[int, set[str]] = defaultdict(set)
    for g, ns in repeat_guests.items():
        seen: set[int] = set()
        for n in ns:
            b = bucket_n(n)
            if b is None:
                continue
            if b not in seen:
                seen.add(b)
                bucket_to_names[b].add(g)

    labels = {i: f"{i} nights" for i in range(2, 10)}
    labels[10] = "10+ nights"

    rows = []
    for b in sorted(bucket_to_names.keys()):
        names = sorted(bucket_to_names[b])
        rows.append({"bucket": b, "label": labels[b], "count": len(names), "names": names})

    out = {
        "repeatGuestCount": len(repeat_guests),
        "repeatWithAnyMultiNightStay": sum(1 for _, ns in repeat_guests.items() if any(n > 1 for n in ns)),
        "repeatWhereAllStaysMultiNight": sum(1 for _, ns in repeat_guests.items() if all(n > 1 for n in ns)),
        "buckets": rows,
        "methodNote": (
            "Repeat = same normalised guest name on 2+ Master Id stays; name from earliest check-in row per stay. "
            "Buckets: repeat guests with at least one stay of that length (nights > 1); 10+ merges 10+ nights. "
            "A guest may appear in multiple buckets."
        ),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("Wrote", OUT, "| repeat guests:", out["repeatGuestCount"])


if __name__ == "__main__":
    main()
