# Site Audit — kaisercontainers.de

_Live read-only audit via WordPress REST API · 2026-08-04_

## Platform
- **WordPress** on **Hostinger** · LiteSpeed cache · Jetpack.
- **Theme:** `Tranzix` v1.0.1 (logistics/transport premium theme — suitable for containers).
- **Plugins detected (via REST namespaces):** WooCommerce (+ Store API, + WC POS),
  Elementor (+ Elementor AI, Elementor One), Contact Form 7, LiteSpeed Cache, Jetpack,
  Redux (theme-options framework), Hostinger tools/onboarding, MCP.
- **No dedicated SEO plugin** (no Yoast/Rank Math namespace) → metadata/schema/sitemap
  need a plugin or theme/manual implementation.
- "Flux" from the brief: **not found** as a plugin namespace — likely a mislabel of the
  Hostinger/Elementor stack. To confirm with owner.

## Current configuration — ❌ wrong for a German store
| Setting | Current | Should be |
|---|---|---|
| Site language | `en_US` | `de_DE` |
| Timezone | *(empty / GMT 0)* | `Europe/Berlin` |
| Currency | `USD` | `EUR` (symbol right, comma decimal, e.g. `2.450,00 €`) |
| Store country | `US:CA` | `DE` |
| Store address / city / postcode | *(empty)* | *(street ⏳)* / Duisburg / 47138 |
| Homepage | `show_on_front = posts` (no page) | dedicated Home page |
| Site tagline | *(empty)* | German tagline |

> Prices are already stored as plain numbers (e.g. `2450.00`) clearly intended as EUR;
> switching the currency label USD→EUR changes only the symbol, not the amounts.

## Content inventory
- **Pages (6):** Shop, Cart, Checkout, My account (Woo defaults, published) · Privacy Policy
  + Refund/Returns Policy (both **draft**, WooCommerce stubs — English boilerplate).
  → **Missing:** Home, Über uns, Kontakt, FAQ, Versand, Widerruf, AGB, **Impressum**,
  Zahlung, Cookie, Barrierefreiheit.
- **Products (20, published, German):** 6–40 ft Seecontainer, High Cube, Doppeltür,
  Open-Side, Garagencontainer, Lagercontainer, and 3 **Gebrauchtcontainer** (used).
  Prices €990–€3,850.
- **Categories (German):** Seecontainer (14), 40 Fuß (4), 20 Fuß (6), 10 Fuß (2), 8/6 Fuß,
  Garagencontainer (2), Lagercontainer (1), Gebrauchtcontainer (3), + empty Uncategorized.
- **Menus (2):** "Main Menu", "One Page Menu" — **assigned to no theme location** → nav
  likely not rendering. Needs building + assignment.
- **Contact Form 7:** one default "Contact form 1" — needs German fields, recipient
  (`info@kaisercontainers.de`), consent checkbox, spam protection.

## Product-data / feed readiness (sample: id 36, "20 Fuß Seecontainer")
✅ SKU (`GC-SC-20`), price, 6 images, 2,798-char description, short description, categories,
`instock`.
❌ **No attributes**, **no dimensions**, **no weight**, **no brand**, **no GTIN/MPN**,
**no condition attribute** (new vs used) → all needed for a clean Merchant Center feed.

## Prioritised findings
**🔴 Blockers (config — safe to fix, verified facts):** language, timezone, currency,
country, postcode/city, set a homepage.
**🔴 Blockers (need owner facts):** exact street address, correct store phone, Impressum
(owner name, VAT, registration, legal form) → German legal requirement.
**🟠 High:** build German legal pages; build nav menus + assign; German header contact bar +
footer; homepage; LocalBusiness/Product schema; German CF7 form; SEO metadata/sitemap.
**🟡 Medium:** product attributes (dimensions/condition/brand), feed export, performance,
accessibility, cookie consent, real store/product photography.
