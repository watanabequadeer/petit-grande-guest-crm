# ClickUp Guest CRM — Prototype Blueprint

This is a configuration spec the team applies in ClickUp. There is no ClickUp MCP in this
workspace, so these are the structures to build by hand, plus the import template
([guest-import-template.csv](./guest-import-template.csv)) and the check-in SOP below.

Recommended hierarchy:

```
Space: Petit Grande Guest CRM
└── Folder: Guests
    ├── List: Guest Records      (one task = one guest)
    ├── List: Feedback Pending   (post-stay survey follow-up)
    └── List: Win-back           (lapsed repeat prospects)
```

## 1. Guest record schema (custom fields)

Each guest is one task in **Guest Records**. Task name = guest full name.

| Field | ClickUp type | Notes |
| --- | --- | --- |
| Email | Email | Primary key for de-duplication. Required. |
| Phone | Phone | Include country code. |
| Nationality / language | Dropdown | e.g. Thai, Filipino, Japanese, Other. Drives language of comms. |
| Party size | Number | Group size at last stay (large family/group focus: 12–15). |
| First-stay date | Date | Set once; never overwritten. |
| Last-stay date | Date | Updated each completed stay. |
| Total stays | Number | Drives visit tier. Incremented per completed stay. |
| Visit tier | Dropdown (labelled) | 1st-time / 2nd-time / 3rd+ (see §2). |
| Source channel | Dropdown | Google Ads, Instagram, Facebook, Line, WhatsApp, Referral, Walk-in, Other. |
| Email consent | Checkbox | Must be true before any marketing email. |
| Marketing status | Dropdown | Subscribed / Unsubscribed / Bounced. |
| Tags / interests | Labels | e.g. Mt. Fuji, Disneyland, Beppu, Tour, Family. For segmentation. |
| Notes | Text / long text | Free-form service notes. |

De-duplication rule: **Email is the unique key.** On import or new entry, match on
normalised email (lowercased, trimmed); merge into the existing task rather than creating a
duplicate. Where email is missing, fall back to phone, then name + last-stay date.

## 2. Visit-count tiering model

Implements the "tablecloth color-coding" idea from the meeting — make returning guests
visible at a glance and differentiate both service and marketing.

| Tier | Total stays | Color | Expected next-visit return | Service / marketing intent |
| --- | --- | --- | --- | --- |
| 1st-time | 1 | Gray | ~20–30% | Strong welcome; earn the second visit; capture feedback. |
| 2nd-time | 2 | Blue | ~45–50% | Recognise loyalty; personalised offers; introduce tours. |
| 3rd+ | 3 or more | Gold | ~70% | VIP treatment; butler-style support; advocacy/referral asks. |

`Visit tier` is set automatically from `Total stays` (see automation A2 below) so it never
has to be maintained by hand.

## 3. Lists / pipelines

| List | Purpose | Entry condition | Exit condition |
| --- | --- | --- | --- |
| Guest Records | Master source of truth | Every guest | Never (archive only) |
| Feedback Pending | Drive post-stay survey | Stay marked complete | Survey response logged |
| Win-back | Re-engage lapsed repeat guests | No stay in N months (e.g. 12) | New booking / stay |

Recommended saved views on **Guest Records**: group by `Visit tier`; filter by
`Nationality`; filter `Email consent = true AND Marketing status = Subscribed` (the
mailable audience export for email campaigns).

## 4. Automations

Configure under ClickUp **Automations** on the relevant list. These are the prototype set;
the more complex multi-step ones are flagged as off-ramp triggers in the direction doc.

| ID | Trigger | Action | Purpose |
| --- | --- | --- | --- |
| A1 | Stay marked complete (status change / date set) | Create task in **Feedback Pending** + increment `Total stays` | Kick off survey; keep stay count current |
| A2 | `Total stays` changes | Set `Visit tier` (1 -> 1st, 2 -> 2nd, >=3 -> 3rd+) | Auto-maintain tier / color |
| A3 | `Visit tier` changes | Add tier tag + flag for the matching email campaign segment | Hand off to lifecycle email |
| A4 | `Last-stay date` older than 12 months AND tier >= 2nd | Add to **Win-back** list | Catch lapsing repeat guests |
| A5 | `Email consent` set to true | Add to mailable audience view / export queue | Keep sending list clean and consented |

> Note: ClickUp automations are single-step triggers. True multi-email drip sequences live
> in the email layer ([Lifecycle-Email-Plan.md](./Lifecycle-Email-Plan.md)); A3/A5 only flag
> records for handoff.

## 5. Check-in email-capture SOP

Goal: every guest leaves check-in with a contact record in the CRM. This is the most
important operational change — it fixes the broken data foundation.

1. **At check-in**, front desk collects: full name, email (required), phone, nationality/
   language, party size, and verbally confirms **email consent** for offers and updates.
2. **Record consent explicitly.** No consent = record the guest but leave `Email consent`
   unchecked and `Marketing status = Unsubscribed`; do not email marketing to them.
3. **Enter or import same day** into **Guest Records**, matching on email to avoid
   duplicates (see de-dup rule, §1). Returning guests: update the existing task, do not
   create a new one.
4. **Set source channel** from how the guest found Petit Grande.
5. **On checkout / stay completion**, mark the stay complete so automation A1 fires.

Practical tip: a short tablet or paper form at the desk feeding a daily CSV import (using
[guest-import-template.csv](./guest-import-template.csv)) is lower-friction than typing each
guest directly into ClickUp during a busy check-in.
