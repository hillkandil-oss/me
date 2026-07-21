# BeepWear — Plugin Stack

Milestone 3. Every plugin earns its place with a purpose and a rationale. Fewer, well-
chosen plugins = faster, safer, easier to maintain. Prefer capabilities BeepWear already
owns (Elementor Pro, WooCommerce) over adding new plugins.

## Core (required)

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **WooCommerce** | Commerce engine, source of truth | Non-negotiable per brief |
| **Elementor** + **Elementor Pro** | Page building + Theme Builder + Forms | Storefront composition, header/footer/templates, contact forms (no separate forms plugin needed) |
| **Hello Elementor** (parent theme) | Minimal base for the child theme | Fast, unopinionated |

## SEO & schema

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **Rank Math SEO** | Titles, meta, canonicals, sitemaps, Open Graph/Twitter, breadcrumbs, schema | Robust, WooCommerce-aware, Merchant-friendly rich results |
| **Google Site Kit** | Search Console, Analytics (GA4), PageSpeed insights in wp-admin | Official Google integration; indexing/CWV visibility for the SEO milestone |

**Schema de-duplication decision:** Rank Math owns Product/Breadcrumb schema in
production. Set `BEEPWEAR_EMIT_SCHEMA` to **false** in the child theme so the two don't
emit duplicate JSON-LD. The theme's built-in Organization/WebSite/Product schema is the
**fallback** for environments without an SEO plugin (it stays guarded by that flag).

## Performance

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **LiteSpeed Cache** | Full-page cache, object cache, critical CSS, image WebP, lazy-load | Native to Hostinger's LiteSpeed servers; one plugin covers caching + image optimization |

(If the host is not LiteSpeed: WP Rocket + ShortPixel as the equivalent pair.)

**No separate image-optimization plugin:** LiteSpeed Cache already handles WebP/AVIF
conversion, compression, and lazy-load — adding a second image plugin would duplicate
function, against the plugin policy. AVIF where the browser supports it, WebP otherwise.

## Merchant Center & Ads

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **Google for WooCommerce** (Google Listings & Ads) | Product feed → Merchant Center, attribute mapping, diagnostics | Official integration; live sync of price/availability; surfaces policy issues directly |

## Trust, compliance & security

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **Complianz** (GDPR/CCPA) | Cookie consent + privacy/consent management | Required for EU markets and a Merchant Center trust signal |
| **Wordfence Security** | Firewall, malware scan, login protection | WordPress hardening (M14) |

## Deliverability & operations

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **WP Mail SMTP** | Authenticated transactional email (order confirmations, account, contact) | WordPress' default `mail()` lands in spam; reliable order/account email is a Merchant Center trust + CX requirement |
| **Redirection** | 301 redirect management, 404 monitoring | Preserve link equity on URL changes; catch broken paths (SEO milestone) |
| **Broken Link Checker (cloud engine)** | Detect broken internal/external links | QA/SEO hygiene; use the cloud-scanning mode so scans don't tax the server |

## Customer experience

| Plugin | Purpose | Rationale |
|--------|---------|-----------|
| **TI WooCommerce Wishlist** | Wishlist | Lightweight; expected in luxury retail; `Add to wishlist` on cards/PDP |

## Deferred (add only when the need is real)

| Plugin | Trigger to add |
|--------|----------------|
| Multi-currency (CURCY free / Aelia paid) | When you actually sell in multiple currencies |
| Automated tax (WooCommerce Tax / Avalara) | When manual tax tables become unmanageable |
| UpdraftPlus | If Hostinger's native backups prove insufficient |
| Reviews enrichment (native Woo reviews first) | Only if native reviews are outgrown — never fake reviews |

## Guardrails

- No plugin that injects fake reviews, badges, countdowns, or "trust" seals.
- Payments via a PCI-compliant gateway's official plugin (Stripe / PayPal) — configured
  in M8, never a custom card handler.
- Audit plugin count each milestone; remove anything unused. Every active plugin is
  attack surface and load time.
