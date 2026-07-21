# BeepWear — WordPress / WooCommerce Architecture

Milestone 3. The technical architecture of the BeepWear storefront. Classic WordPress
rendering (not headless), built visually in Elementor Pro, styled by the BeepWear child
theme. Principle: **use WordPress/WooCommerce natives; add nothing unnecessary.**

## 1. Stack & layers

| Layer | Choice | Role |
|-------|--------|------|
| Host | Hostinger (LiteSpeed; VPS if shared can't sustain load) | PHP 8.1+, MySQL, SSL, cron, staging, backups |
| CMS | WordPress 6.4+ | Content, users, media, routing |
| Commerce | WooCommerce | Source of truth: products, inventory, pricing, orders, tax, shipping, coupons, reviews |
| Base theme | Hello Elementor | Minimal, fast parent — no opinionated styling to override |
| Design | **BeepWear child theme** | Design system CSS, hooks, JSON-LD, performance/a11y helpers |
| Page building | Elementor Pro + Theme Builder | Header, footer, templates, landing sections — content management only |

The child theme owns *system-level* concerns (tokens, schema, hooks); Elementor owns
*composition* (what goes where on a page). Keeping these separate is what makes the
build maintainable: design changes happen in one CSS file, layout changes in Elementor.

## 2. Template strategy (decision)

**Elementor Pro Theme Builder** renders the site chrome and dynamic templates; the child
theme provides fallbacks and the design system. Theme Builder conditions override the WP
template hierarchy.

| Surface | Rendered by | Condition |
|---------|-------------|-----------|
| Header | Theme Builder header | Entire site |
| Footer | Theme Builder footer | Entire site |
| Homepage | Elementor page | Front page (static) |
| Shop / category archive | Theme Builder "Products Archive" | `product` archive + `product_cat` |
| Single product (PDP) | Theme Builder "Single Product" | All products |
| Blog archive / single | Theme Builder archive/single | `post` |
| Cart / Checkout / Account | WooCommerce shortcodes/blocks, styled by child theme | — |
| 404, Search | Theme Builder / child theme templates | — |

Rationale: Theme Builder gives content editors visual control without touching PHP, while
the child theme guarantees consistent design tokens, schema, and accessibility regardless
of how a page is composed. Cart/checkout stay on WooCommerce's own flow (never rebuilt in
Elementor) for security and update-safety.

## 3. Caching & performance

- **Full-page cache:** LiteSpeed Cache (native to Hostinger's LiteSpeed). Exclude
  `cart`, `checkout`, `my-account`, and any page with the cart fragment.
- **Object cache:** Redis via LiteSpeed/Hostinger where the plan supports it (VPS).
- **Assets:** child-theme CSS/JS are small and versioned; fonts self-hosted + preloaded;
  critical CSS inlined by LiteSpeed; defer non-critical JS.
- **Images:** WebP conversion + responsive `srcset` (WP native) + lazy-load; CDN
  (Cloudflare or Hostinger CDN). Product images sized to the grid (1:1) and PDP (4:5).
- **CWV budget:** LCP < 2.5s, INP < 200ms, CLS < 0.1 — verified per page milestone.

## 4. Security hardening (executed in M14, specified here)

- Force HTTPS; HSTS; security headers (`X-Content-Type-Options`, `Referrer-Policy`,
  `X-Frame-Options`/`frame-ancestors`, a Woo-compatible CSP).
- Disable file editing (`DISALLOW_FILE_EDIT`), XML-RPC; limit login attempts.
- Least-privilege roles; unique admin; app passwords for any REST use.
- Wordfence (firewall + malware scan); keep core/plugins/theme auto-updated on staging first.
- Input handled by WooCommerce/WP core (sanitized, nonce-protected); child theme escapes
  all output (`esc_*`, `wp_json_encode`).

## 5. Backup & recovery

- Hostinger automatic daily backups + weekly manual full export (files + DB).
- All code (theme, docs, content, feed) lives in this Git repo — the deployable record.
- Changes land on Hostinger **staging** first, then promote to production.

## 6. Internationalization & scalability

- Target markets (Part 1): US, CA, UK, DE, FR, IT, NL, BE, CH, AE, AU, NZ, SG.
- Shipping **zones** per region; tax/VAT per WooCommerce tax settings (EU VAT, GCC VAT).
- Multi-currency deferred (see `PLUGINS.md`, future) but the taxonomy/data model is
  currency-neutral so it can be added without re-tagging products.
- Scale path: shared → Hostinger VPS (Redis, more PHP workers) when traffic warrants.

## 7. REST API

No headless front end, so no public API surface is exposed. WooCommerce REST is used
only server-side/authenticated by the Google Listings & Ads plugin for the Merchant
Center feed. Keys are read-scoped and stored as environment secrets.
