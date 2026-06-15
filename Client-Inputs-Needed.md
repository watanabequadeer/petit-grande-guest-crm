# Client Inputs Needed

To move from this plan into a working prototype, we need the following from the Petit Grande
team. Items are ordered by what unblocks the most work.

## 1. Existing customer database export (blocks Phase 1)

- A full export of the current customer database in CSV or Excel.
- We will map it to [guest-import-template.csv](./guest-import-template.csv), de-duplicate on
  email, and load it into ClickUp **Guest Records**.
- Please flag any known duplicate sources or multiple spreadsheets so we merge them correctly.

## 2. Current check-in data fields (blocks the capture SOP)

- The exact fields collected at check-in today (paper form, PMS, or spreadsheet).
- Whether email is collected at all today, and if guest **consent** for marketing is captured.
- This tells us the gap between current capture and the schema in
  [ClickUp-CRM-Blueprint.md](./ClickUp-CRM-Blueprint.md) §1.

## 3. Email sending tool confirmation (blocks Phase 3)

- Confirm the sending tool for lifecycle email. Default recommendation: **Postmark**, already
  provisioned in this workspace — but the `user-postmark` MCP server currently reports an
  error and must be reconnected/verified in **Cursor Settings → MCP**.
- Confirm the **sending domain** and who can authorise DNS records (SPF/DKIM) for it.
- Confirm whether a dedicated ESP (Brevo / Klaviyo / HubSpot) is preferred now, or only once
  the ClickUp limit triggers are reached (see [Guest-CRM-Direction.md](./Guest-CRM-Direction.md) §3).

## 4. Access and ownership

- ClickUp workspace access (or confirmation to create a new Space) and who owns it.
- Languages required for guest comms (meeting indicated Thai and Filipino primary, plus
  Japanese) so templates are prepared in the right languages.
- Confirmation of the win-back lapse window (default assumed: 12 months).
