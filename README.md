# Petit Grande — Guest CRM

Internal project materials: direction docs, ClickUp blueprint, lifecycle email plan, and a **shareable CEO report** (static HTML).

## CEO report on GitHub Pages

The report lives at [`docs/index.html`](docs/index.html). It is gated in the browser with a password (SHA-256 check; not cryptographic security — see [`docs/README.md`](docs/README.md)).

**Do not commit** raw Beds24 exports (`.gitignore` excludes `beds24*.xlsx`). Keep PII local.

### First-time publish

1. Create a new GitHub repository (recommended: **private** if the report is sensitive).
2. From this folder:

```bash
git init
git add .
git commit -m "Add guest CRM docs and password-gated CEO report for GitHub Pages"
git branch -M main
git remote add origin https://github.com/<YOUR_ORG>/<YOUR_REPO>.git
git push -u origin main
```

3. GitHub: **Settings → Pages → Source**: branch **main**, folder **`/docs`**, Save.
4. Open `https://<YOUR_ORG>.github.io/<YOUR_REPO>/` (URL is shown on the Pages settings page after deploy).

Password for the report is distributed separately by Bananalabo.
