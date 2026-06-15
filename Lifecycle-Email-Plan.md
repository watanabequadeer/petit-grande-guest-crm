# Lifecycle Email Plan

The CRM ([ClickUp-CRM-Blueprint.md](./ClickUp-CRM-Blueprint.md)) holds the records and
segments; this layer converts them into repeat stays through targeted email. In the
prototype, ClickUp flags records for handoff and a sending tool delivers the mail.

## 1. Core flows

| Flow | Trigger (from CRM) | Audience | Goal | Key content |
| --- | --- | --- | --- | --- |
| Welcome | New 1st-time guest, consent = true | Visit tier = 1st-time | Earn the second visit | Thank-you, what to do nearby, easy way to rebook |
| Post-stay survey | Stay marked complete (list: Feedback Pending) | All consented guests | Capture feedback + identify improvements | Short survey, incentive to return |
| Seasonal offer | Manual / scheduled per season | Segment by nationality + interests | Drive bookings in season | Mt. Fuji / Disneyland / Beppu offers, group packages |
| Repeat / win-back | Lapsed >12 months, tier >= 2nd (list: Win-back) | Win-back list | Reactivate lapsed repeat guests | "We miss you" + returning-guest incentive |

Tier-aware tone: 1st-time = welcoming and informative; 2nd-time = recognise loyalty +
introduce tours; 3rd+ = VIP / butler-style support + referral asks.

## 2. Metrics to track

Per the meeting's call for email metrics:

- **Open rate** and **click rate** per flow and per segment.
- **Survey response rate** (post-stay flow).
- **Rebooking / return rate** attributed to win-back and seasonal flows — the bottom-line
  number tying email back to the 20–30% / 45–50% / 70% repeat curve.
- **Unsubscribe and bounce rates** — feed `Marketing status` back into ClickUp.

## 3. Sending: Postmark handoff

Postmark is provisioned in this workspace as the intended sending layer (a `user-postmark`
MCP server is configured).

> Status flag: at the time of writing, the `user-postmark` MCP server is reporting an error
> in this workspace. Before wiring live sends, reconnect/verify it in **Cursor Settings →
> MCP**. Until then, treat the sending steps below as the target design, not an active
> integration.

Handoff design (CRM segment -> Postmark send):

1. ClickUp automation **A3/A5** flags a record into the mailable audience view
   (`Email consent = true AND Marketing status = Subscribed`).
2. Export / sync that segment (email + name + tier + language + interests as template
   variables).
3. Postmark sends the matching flow:
   - **Transactional stream** for welcome and post-stay survey (1:1, triggered).
   - **Broadcast stream** for seasonal offers and win-back (bulk, with unsubscribe handling).
4. Postmark delivery/open/click events feed the metrics in §2; bounces and unsubscribes are
   written back to the guest's `Marketing status` in ClickUp.

> Caveat: Postmark is excellent for delivery and transactional/broadcast sending and
> open/click tracking, but it is not a full marketing-automation suite. Multi-step drip
> sequences and rich audience segmentation are exactly the **ClickUp limit triggers** in the
> direction doc — reaching them is the signal to adopt a dedicated ESP (Brevo / Klaviyo /
> HubSpot) for the email layer.
