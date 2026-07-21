# BeepWear — Deploy Runbook (Hostinger)

Master Prompt Part 12 (Phases 2 & 7). How to stand up, deploy, and verify BeepWear on
Hostinger. Owner milestone **M14**. These steps run on the live host — this repository is
the code-of-record; nothing here executes from the repo alone.

## 1. Environment (Phase 2)

Provision on Hostinger (upgrade to **VPS** if shared cannot sustain WordPress + WooCommerce
+ LiteSpeed + Redis — see `ARCHITECTURE.md §6`):

- Latest **PHP** supported by WordPress (8.1+), **MySQL/MariaDB** latest, **OPcache** on.
- **HTTPS + SSL** (Let's Encrypt/host), force redirect, HSTS; **HTTP/2 or HTTP/3**.
- **GZIP/Brotli** compression; server-side + LiteSpeed cache.
- **Cron** (real system cron, disable WP pseudo-cron), **email** (SMTP via WP Mail SMTP).
- **Staging** environment; **backups** (below).

Install: WordPress → WooCommerce → Hello Elementor → **BeepWear child theme** (zip
`theme/beepwear/`) → Elementor Pro → the plugins in `PLUGINS.md`. Import `.mcp.json`/registry
are dev-only and not part of the production site.

## 2. Configuration

- **Permalinks:** Post name (`/%postname%/`); confirm the clean URLs in
  `INFORMATION-ARCHITECTURE.md §2`.
- **Fonts:** already bundled in the theme (`assets/fonts/*.woff2`) — no action.
- **Schema de-dup:** set `BEEPWEAR_EMIT_SCHEMA` to `false` once Rank Math owns schema
  (`wp-config.php` or a small mu-plugin) — see `PLUGINS.md`.
- **WooCommerce:** currency, tax classes/zones, shipping zones for the 13 target markets,
  payment gateways (Stripe/PayPal official plugins), emails.
- **Announcement bar:** Customizer → Announcement Bar (messages, speed, enable).
- **Security hardening** (`ARCHITECTURE.md §4`): disable file editing + XML-RPC, limit login,
  security headers, 2FA for admins, DB-prefix, least-privilege roles.

## 3. Backups (Phase 2 / ongoing)

| Target | Frequency |
|--------|-----------|
| Database | Daily |
| Uploads | Daily |
| Theme + plugins | Daily |
| Full site | Weekly |

Retain multiple versions; **test restoration** periodically (a backup is only real if it
restores). Hostinger automatic backups + a weekly manual export.

## 4. Deployment process (Phase 7)

**Before:** create a backup · confirm staging tests passed · confirm version numbers ·
review this checklist · notify stakeholders if appropriate.

**Promote:** apply the change on **staging** first, validate, then promote to production
(never edit production directly). Theme/plugin code changes flow through this Git repo →
staging → production.

**After:** verify homepage · test checkout end-to-end · submit a test contact + newsletter ·
review error logs · confirm GA4 events fire · confirm payment gateway works (test mode →
live) · validate product-feed generation · confirm SSL (no mixed content) · submit sitemap
in Search Console.

## 5. Domain & Merchant Center (Phase 7)

Production uses the **custom domain** only — never a Hostinger preview/staging URL in
Merchant Center. Complete the `MERCHANT-CENTER.md` §9 audit (all BLOCKERs resolved) before
connecting the Google for WooCommerce feed.

## 6. Rollback

If a deploy misbehaves: restore the pre-deploy backup (fastest safe path) or revert the
offending commit and re-promote from staging. Prefer rollback over untested hotfixes on
production. Record the incident (`OPERATIONS.md §incident response`).
