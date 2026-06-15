# GitHub Pages: CEO report

This folder hosts a **static HTML** report for Petit Grande (Beds24 guest data summary).

## Enable GitHub Pages

1. Create a **new repository** on GitHub (public or private). Do **not** upload `beds24-fulldata.xlsx` or other raw guest exports; they stay local per `.gitignore`.
2. Push this project (or only the `docs/` folder if you use a dedicated repo — see below).
3. In the repo on GitHub: **Settings → Pages → Build and deployment → Source**: **Deploy from a branch**.
4. Choose branch **main** (or **master**) and folder **`/docs`**, then Save.
5. After a minute, the site URL will be shown (typically `https://<username>.github.io/<repo>/`).

If GitHub serves `docs/index.html` as the site root, open the site URL directly; if the report lives at a subpath, use `https://<username>.github.io/<repo>/` (GitHub serves `docs/index.html` as `/` when source is `/docs`).

## Password gate (important)

Access is gated in the browser with a password check (SHA-256 only in the file, not the plaintext password). **This is not strong security:** anyone can view page source or bypass the gate with enough effort. Use it only to **discourage casual viewers** and for convenience. For real confidentiality, use a **private GitHub repo** + Pages, or share a PDF over a controlled channel.

## Updating the report

Regenerate numbers from Beds24 locally, then edit `docs/index.html` or rebuild from your internal process. Never commit raw Beds24 exports to a public repository.

## Repeat guest breakdown (`repeat-guests-by-nights.json`)

The interactive name lists load from [`repeat-guests-by-nights.json`](repeat-guests-by-nights.json). That file contains **guest names (PII)**. If the GitHub repository is **public**, those names are public too (the HTML password gate does not protect JSON). Regenerate after updating the spreadsheet:

```bash
python3 scripts/build-repeat-guest-json.py
```

(Run from the project root; requires `beds24-fulldata.xlsx` and `pandas` / `openpyxl`.)
