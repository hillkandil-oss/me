# BeepWear — Google Merchant Center & Shopping Readiness

Master Prompt Part 9. The compliance spec and pre-launch audit backbone. Owner milestone
**M12**, but the requirements here are enforced continuously by the Merchant Center review
gate on every milestone.

> **No approval can be guaranteed.** The goal is to maximize compliance by operating a
> transparent, trustworthy, professionally built store. Every decision favors accuracy,
> transparency, and customer trust.

## 1. Legitimacy signals (must all be true)

The site must never read as a dropshipping template, unfinished store, or copied site.
Reinforce a real business on every page:

- **Business identity:** name **BeepWear**, support email, phone, business hours, address
  (if available) — consistent site-wide (footer + Contact + About).
- **HTTPS everywhere:** valid certificate, no mixed content, secure checkout. No expired SSL.
- **Custom domain only:** never submit Hostinger preview/staging/temporary domains.
- **Completeness:** no placeholder pages, Lorem Ipsum, broken images, empty categories,
  dummy testimonials, fake reviews, or unfinished checkout at launch.

## 2. Product data requirements

Every product: clear title, original professional description, price + currency,
availability, brand, real images, specifications, SKU, category, shipping/returns/warranty
info, related products, FAQ — **accurate only**.

- **Titles** — descriptive, e.g. *"Citizen Eco-Drive Chronograph Men's Stainless Steel
  Watch."* No promo text (SALE!!!, CHEAP, 100% ORIGINAL, FREE SHIPPING).
- **Descriptions** — original, detailed, factual (materials, movement, use). No keyword
  stuffing, exaggeration, or unlicensed manufacturer copy.
- **Images** — high-res, clear, no promo overlays/watermarks/borders; no misleading AI
  images. Lifestyle shots supplement, never replace, accurate product photos.

## 3. Consistency (feed ⇄ site)

- **Price** identical on product page, cart, checkout, and feed.
- **Availability** matches WooCommerce inventory exactly (In Stock / Out of Stock /
  Pre-Order / Backorder). Never display incorrect availability.

## 4. Policies & transparency (footer-linked)

Privacy · Cookie · Terms · Shipping · Returns · Refund · Warranty · Accessibility ·
Authenticity. Shipping (costs, methods, estimates, international, tracking, restrictions),
Returns (window, eligibility, refund/exchange, contact), and Warranty (coverage, duration,
exclusions, claim) must be easy to find and summarized on PDPs with links to full policies.
Payment methods: display only options actually usable (Stripe/Visa/Mastercard/Amex/PayPal/
Apple Pay/Google Pay/bank transfer if supported).

## 5. Structured data

Valid schema, validated before launch: Organization · WebSite · Breadcrumb · Product ·
Offer · Review (genuine only) · FAQ · Article. In production Rank Math owns output
(`PLUGINS.md`); theme JSON-LD is fallback.

## 6. Feed (Google for WooCommerce)

Attributes where applicable: `id`, `title`, `description`, `link`, `image_link`,
`additional_image_link`, `availability`, `price`, `brand`, `gtin`, `mpn`, `condition`,
`shipping`, `tax`, `google_product_category`, `custom_label_*`.

- **Identifiers:** include GTIN/UPC/EAN/MPN/brand accurately when they exist; **never
  invent them.** If absent, omit (and set `identifier_exists` appropriately).
- **Google product category:** assign the most specific — "Apparel & Accessories > Jewelry >
  Watches" (201); accessories mapped to their correct nodes.

## 7. Discoverability & analytics

- **XML sitemaps:** pages, products, categories, blog (Rank Math). Submit to Search Console
  after launch.
- **robots.txt:** allow public content; disallow admin, cart, checkout, account, internal
  search results.
- **Search Console:** verify ownership, submit sitemap, monitor crawl/enhancements post-launch.
- **GA4:** page/product views, add-to-cart, checkout, purchase, search, newsletter, contact
  submits — privacy settings per applicable law (consent via Complianz).
- **GTM (if used):** clearly organized, documented tags, no duplicate tracking.

## 8. Performance & mobile

Core Web Vitals budget (LCP < 2.5s, INP < 200ms, CLS < 0.1): compress images, optimize CSS,
minify JS, minimal plugins. Mobile is the primary evaluation surface — fast, readable,
accessible forms, responsive checkout.

## 9. Pre-launch audit (M12 gate) — PASS / WARNING / BLOCKER

Audit each area and assign a verdict. **Only recommend feed submission after every BLOCKER
is resolved.**

| Area | Verdict | Notes |
|------|:------:|-------|
| Business information | ⬜ | |
| Brand consistency | ⬜ | |
| Homepage | ⬜ | |
| Navigation | ⬜ | |
| Category pages | ⬜ | |
| Brand pages | ⬜ | |
| Product pages | ⬜ | |
| Cart | ⬜ | |
| Checkout | ⬜ | |
| Customer account | ⬜ | |
| Search | ⬜ | |
| Contact page | ⬜ | |
| About page | ⬜ | |
| Policies | ⬜ | |
| Product feed | ⬜ | |
| Structured data | ⬜ | |
| SEO | ⬜ | |
| Images | ⬜ | |
| Performance | ⬜ | |
| Accessibility | ⬜ | |
| Mobile experience | ⬜ | |
| Security | ⬜ | |
| Analytics | ⬜ | |
| Search Console readiness | ⬜ | |
| Merchant feed quality | ⬜ | |

**Common risk flags:** missing contact info, broken checkout, mismatched price/availability,
broken product images, copied/misleading content, missing policies, inaccessible pages,
placeholder text, broken links, incorrect structured data, unavailable products in the feed.

## 10. Post-launch monitoring (routine)

Uptime, broken links/images, product availability, price sync, feed generation, Merchant
Center diagnostics, Search Console issues, analytics events, plugin/WordPress/WooCommerce
updates, security alerts, backup status.

## 11. Final principle (apply to every decision)

Is it accurate? Transparent? Can customers reach the business? Are policies easy to find?
Are products honestly represented? Is checkout secure? Is pricing consistent? Is the
experience professional? Does it inspire trust? Does it align with Google's published
policies? If any answer is **no**, revise before launch.
