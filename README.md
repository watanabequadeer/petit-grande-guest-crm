# Petit Grande — Guest CRM

Internal project materials: direction docs, ClickUp blueprint, lifecycle email plan, and a **shareable CEO report** (static HTML).

## CEO report on GitHub Pages

**Live site:** [https://watanabequadeer.github.io/petit-grande-guest-crm/](https://watanabequadeer.github.io/petit-grande-guest-crm/)

The report is [`docs/index.html`](docs/index.html). Unlock with the password shared by Bananalabo (case-sensitive, all lowercase).

The gate uses a **SHA-256 check in the browser only** — it keeps casual visitors out but is **not** strong security (source is public). For stricter control, use a **private** GitHub repo (Pages may require a paid plan on some accounts) or share a PDF over email instead.

**Repository visibility:** This repo was set to **public** so free GitHub Pages could be enabled (private repos returned HTTP 422 on this account). Raw Beds24 files are still excluded via `.gitignore`, but **all Markdown in the repo is world-readable**. If that is unacceptable, create a separate public repo that contains **only** `docs/index.html` (and optionally a minimal README), or revert to private and host the HTML elsewhere (Netlify, Cloudflare Pages, S3 static site).

**Do not commit** raw Beds24 exports (`.gitignore` excludes `beds24*.xlsx`). Keep PII local.

The file `docs/repeat-guests-by-nights.json` lists repeat guest **names** for the report UI. On a **public** repo that file is world-readable; the page password does not hide it.

### First-time publish (already done for this clone)

If you recreate elsewhere:

1. Create a GitHub repository (public if you need free Pages on a free org/user plan).
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
4. Open the Pages URL shown in settings (after the first build completes, usually within 1–2 minutes).
