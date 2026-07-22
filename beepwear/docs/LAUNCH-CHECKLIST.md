# BeepWear — Launch Readiness Gate (Milestones 14–15)

The final go-live gate (Master Prompt Part 14). Deployment steps live in
`DEPLOY-RUNBOOK.md`; this is the consolidated readiness review. Assign each area
**PASS / WARNING / BLOCKER** on the live/staging site. **Do not launch while any BLOCKER
remains. Do not submit the Merchant Center feed until its BLOCKERs clear** (`MERCHANT-CENTER-AUDIT.md`).

## Go-live gate

| Area | Verdict | Reference |
|------|:------:|-----------|
| Homepage | ⬜ | preview + live build |
| Navigation | ⬜ | M5 |
| Products (PDP) | ⬜ | real data + photography |
| Categories | ⬜ | M6 |
| Brands | ⬜ | real brands + copy |
| Collections | ⬜ | M6 |
| Checkout | ⬜ | live gateway + HTTPS |
| Customer account | ⬜ | M10 |
| Search | ⬜ | M6 |
| SEO | ⬜ | `SEO-IMPLEMENTATION.md` |
| Performance (CWV) | ⬜ | `QA-TEST-PLAN.md §4` |
| Accessibility | ⬜ | `QA-TEST-PLAN.md §5` |
| Security | ⬜ | `ARCHITECTURE.md §4` |
| Policies | ⬜ | facts filled + legal review |
| Content | ⬜ | no placeholders / `[confirm:]` cleared |
| Analytics | ⬜ | GA4 events verified |
| Merchant Center feed | ⬜ | `MERCHANT-CENTER-AUDIT.md` |
| Documentation | ✅ | this repo |
| Deployment plan | ✅ | `DEPLOY-RUNBOOK.md` |

## Deployment (M14) — from `DEPLOY-RUNBOOK.md`

- [ ] Environment provisioned (PHP 8.1+, MySQL, HTTPS/SSL, HTTP/2/3, OPcache, Brotli, cron, SMTP).
- [ ] Child theme + Elementor Pro + WooCommerce + plugins installed & configured.
- [ ] `BEEPWEAR_EMIT_SCHEMA=false`; permalinks; announcement bar; shipping/tax/payment zones.
- [ ] Backups scheduled (daily DB/uploads, weekly full) + a tested restore.
- [ ] Staging validated → promote to production (never edit prod directly).
- [ ] Post-deploy: verify homepage, checkout end-to-end, forms, logs, GA4 events, gateway,
      feed generation, SSL (no mixed content), submit sitemap.

## Launch (M15)

- [ ] All go-live BLOCKERs cleared; QA sign-off recorded.
- [ ] Custom domain live on HTTPS (no preview/staging URL public).
- [ ] Search Console verified + sitemap submitted; analytics collecting.
- [ ] Merchant Center: only after its audit BLOCKERs clear and diagnostics are clean.
- [ ] Post-launch monitoring armed (`OPERATIONS.md §4`, §10).

## Business-provided items that gate launch (from `MASTER-BLUEPRINT.md`)

Real brand partnerships · business facts (contact, hours, address, entity, founding) ·
product data + authorized photography · payment/shipping/tax/warranty operational details ·
Hostinger + Google (domain, GA4, Search Console, Merchant Center) access · legal review of
Privacy/Terms. These are the true remaining blockers — not design or code.
