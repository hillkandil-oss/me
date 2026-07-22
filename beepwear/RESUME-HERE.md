# BeepWear — Resume Here (live-site work)

Everything design/content/CSV is committed on branch `claude/hello-lz33xo`. The remaining
work is on the **live site** and was blocked in a prior session because the environment's
network could not reach `beepwear.com` (egress proxy returned 403 for all external domains).

## To continue

1. **Enable network access:** claude.ai/code → this repo's environment → Network access →
   allow `beepwear.com` and `*.hostingersite.com` (or "allow all domains").
2. **Start a NEW session** (network policy is fixed at container start).
3. **Provide, in the new session:**
   - WooCommerce **REST API keys** (WooCommerce → Settings → Advanced → REST API → Read/Write).
   - Remaining business facts: business hours, return window, shipping costs/estimates,
     governing-law state (fills the last `[confirm: …]` markers in `content/`).

## First actions in the new session (in order)

1. **Audit the live site first** — `beepwear.com` likely already runs WordPress/WooCommerce
   (product images + the CSV export come from it). Check existing products BEFORE importing so
   we don't create duplicates.
2. **Import approved products** — `data/products-mc-cleaned.csv` (269 compliant candidates)
   via the WooCommerce importer or the REST API. See `docs/MERCHANT-CENTER-CSV-AUDIT.md`.
3. **Assign brands** to the 47 kept products flagged in `data/products-mc-audit.csv`.
4. **Verify descriptions** on the 269 are original + accurate (not copied manufacturer copy).
5. **Publish content** — policies/about/FAQ/guides from `content/`, business facts filled.
6. **Run the live audits** — `docs/QA-TEST-PLAN.md`, `docs/SEO-IMPLEMENTATION.md`,
   `docs/MERCHANT-CENTER-AUDIT.md` (§9 matrix) — fix findings.
7. **Merchant Center** — only submit on the custom domain `beepwear.com` (never a preview
   URL), after all BLOCKERs in the audit clear. Approval is never guaranteed.

## Key files

- Theme: `theme/beepwear/` · Content: `content/` · Cleaned feed: `data/products-mc-cleaned.csv`
- Runbooks: `docs/DEPLOY-RUNBOOK.md`, `docs/LAUNCH-CHECKLIST.md`, `docs/MASTER-BLUEPRINT.md`
