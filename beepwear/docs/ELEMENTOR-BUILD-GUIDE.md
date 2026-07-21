# BeepWear — Elementor Build Guide: Homepage

How to assemble the homepage in Elementor Pro so it matches the approved design
(`preview/homepage.html`) and inherits the child-theme design system. Copy is in
`content/homepage.md`; imagery prompts in `docs/IMAGE-PROMPTS.md`.

## Before you start

1. **Global fonts/colors:** In Elementor → Site Settings, set Global Colors and Fonts to
   the BeepWear tokens so widgets inherit them (don't restyle per-widget):
   - Primary `#141310` · Secondary `#FFFFFF` · Accent `#C2A15C` · Text `#3A3733`.
   - Primary font (headings) **Cormorant Garamond**; Secondary (body) **Manrope**
     (both already self-hosted by the theme — add as Custom Fonts if Elementor needs them).
2. **Performance:** Use **Flexbox/Grid containers**, not the legacy section/column stack,
   and keep nesting shallow (Part 3). One container per section; avoid deep wrappers.
3. **Announcement bar & header/footer** are the theme + Theme Builder, **not** this page —
   see `ARCHITECTURE.md §2`. Build the announcement bar via Customizer → Announcement Bar.

## Section-by-section (order matches `PAGE-INVENTORY.md §B`)

| # | Section | Elementor build | Dynamic? |
|---|---------|-----------------|----------|
| 3 | **Hero** | Full-width container, dark bg image (hero art), inner max-1240 container: eyebrow (label), H1 (Cormorant), lead paragraph, two buttons (`.bw-btn`, `.bw-btn--ghost`), trust row. Set the H1 as the page's single H1. | No |
| 4 | **Featured Categories** | Grid container, 4 cols → 2 on tablet/mobile. Each = image + overlay title/desc/link. Use the `.cat` pattern or Image Box. | Optional (link to category archives) |
| 5 | **Featured Brands** | Logo grid/carousel; **only real brands**. Hide the section until brand partnerships exist. | Woo `brand` query |
| 6 | **Best Sellers** | **WooCommerce Products** widget, "Best Selling", 4 cols. | Yes (Woo) |
| 7 | **New Arrivals** | **WooCommerce Products** widget, "Latest", 4 cols + View All button → `/new-arrivals/`. | Yes (Woo) |
| 8 | **Staff Picks** | WooCommerce Products by hand-picked list or a "staff-picks" product tag. | Yes (Woo) |
| 9 | **Why Choose BeepWear** | 3×2 grid of icon-boxes (thin line icons); copy from content file. | No |
| 10 | **Editorial Banner** | Full-width container with Higgsfield lifestyle image + headline + CTA (the dark "lifestyle" band). | No |
| 11 | **Testimonials** | Reviews widget bound to genuine Woo reviews. **Hide until real reviews exist.** | Yes (Woo) |
| 12 | **Latest Articles** | **Posts** widget, 3 latest from Journal, card style (image, category, date, reading time, excerpt, Read More). | Yes (posts) |
| 13 | **Newsletter** | Container (dark) with the signup form (Elementor Form or the newsletter plugin). Include the privacy notice line. | Form |
| 14 | **Instagram** | Only if social integration is connected; otherwise omit (don't ship an empty embed). | Optional |

Trust band (Secure Payments · SSL · Support · Easy Returns · Transparent Policies) sits
just above the footer — a simple flex container of labelled items.

## Design-system hooks

The child theme exposes reusable classes — add them in each widget's **CSS Classes** field
instead of restyling: `.bw-btn` / `.bw-btn--secondary` / `.bw-btn--ghost`, `.bw-eyebrow`,
`.bw-section` / `.bw-section--soft`, `.bw-onDark`, `.bw-reveal` (fade-in on scroll).
Alternate section backgrounds white / off-white (`.bw-section--soft`) for rhythm.

## Gate checklist before publishing the page

- One H1 (hero); H2 per section; logical order (SEO).
- Every image has descriptive alt text; hero image sized to avoid CLS.
- All CTAs point to real destinations; every section links onward (internal linking).
- No testimonials/ratings/brands shown unless genuine.
- Mobile: categories/products 2-up, bands stack, tap targets ≥ 44px, no horizontal scroll.
- Title + meta description set (content file); Rank Math schema on.

---

# Header, Mega Menu, Mobile & Footer (Milestone 5)

Built in **Elementor Pro Theme Builder** as site-wide Header and Footer templates (display
condition: Entire Site). Reference design: `preview/nav.html` (desktop mega + mobile drawer).

## Header

- **Container:** sticky, white background, `1px` hairline bottom border, 78px tall; logo left,
  nav center, icons right (Search · Wishlist · Account · Cart). Logo is "Beep" + gold "Wear".
- **Sticky effect:** Elementor motion → sticky on scroll; keep it solid (not transparent) for
  legibility over light pages; announcement bar (theme Customizer) sits above it.
- **Icons:** thin-line style, consistent size; Cart shows live count.

## Mega menu

Use Elementor Pro's **Mega Menu** (or a Nav Menu with a full-width dropdown). Structure for
**Shop** (four columns): *By Gender* (Men/Women/Unisex) + *Accessories*; *By Style* (Dress,
Sports, Diver, Chronograph, Pilot, GMT, Skeleton, Moonphase); *By Movement* (Automatic,
Quartz, Mechanical) + *Shop* (New Arrivals, Best Sellers, Limited Editions, Sale); and a dark
**Featured** promo card linking to a collection. Mirror the pattern for **Collections** and
**Brands** (brand list + "View all brands").
- Open on hover (desktop) and focus (keyboard); `aria-expanded` on the trigger.
- Links map to the clean URLs in `INFORMATION-ARCHITECTURE.md §2`.

## Mobile menu

Elementor's mobile menu / off-canvas drawer (< 960px): hamburger opens a left drawer with a
search field, expandable Shop/Brands/Collections sections, the full nav list, and an
Account/Wishlist/Cart footer row. Tap targets ≥ 44px; drawer traps focus; overlay closes it.

## Footer (built in M4 preview; formalize here)

Five columns — brand blurb · Shop · Customer Service · Company · Legal — over a dark ground,
then a bottom bar with copyright + accepted payment marks. Include newsletter, social, and
business info. Matches `preview/homepage.html` footer. All links resolve (no dead links).

---

# Collections: Shop, Category, Brand, Collection, Search (Milestone 6)

Reference design: `preview/category.html`. Built as Elementor Pro **Theme Builder**
templates over WooCommerce archives, inheriting the design system. One template pattern
serves shop/category; brand and collection are variations with an extra content block.

## Products Archive template (shop + category)

Display condition: Products archive + `product_cat`. Structure, top to bottom:
1. **Breadcrumb** (Rank Math) → `BreadcrumbList` schema.
2. **Category hero** — eyebrow + H1 (category name) + SEO description (unique per category,
   editable in the term description / an ACF-style field).
3. **Toolbar** — result count · sort (Featured, Newest, Price ↑/↓, Best Selling, Highest
   Rated) · mobile "Filters" button.
4. **Layout** — filter sidebar + product grid.
   - **Filters** (faceted): Brand, Movement, Case material, Case size, Dial color, Water
     resistance, Price, Availability (+ Band material/color, Style, Collection where useful).
     Use a filter plugin evaluated against `PLUGINS.md`; filter URLs `noindex,follow` +
     canonical to base archive.
   - **Grid** — WooCommerce Products widget styled by `.woocommerce ul.products` (theme):
     3-up desktop, 2-up mobile; card = image (badge + wishlist), brand eyebrow, model
     (Cormorant), price. Sale/New/Limited badges via `.bw-badge`/`onsale`.
5. **Pagination.**
6. **Buying-guide band** — links the category to the relevant guide (internal linking).
7. **FAQ** — accordion (category-appropriate) → `FAQPage` schema.
8. **Related collections** + **newsletter**.

Avoid thin, grid-only category pages — the hero description, buying-guide band, and FAQ
carry the SEO content (`SEO-STRATEGY.md §6`).

## Brand template

Same archive base filtered to a `brand` term, plus original brand content blocks: history,
philosophy, signature collections, featured products, buying advice, FAQ, related articles.
All copy original (`content/brands/{brand}.md`).

## Collection template

Same base for a `collection` term, plus overview, curated featured products, buying
recommendations, related collections, educational content.

## Search results

WooCommerce search template: search term, result count, product results (same card),
suggested categories/articles, and a helpful **no-results** state (popular brands + shop
link) — never a dead end (`INFORMATION-ARCHITECTURE.md §3`).

---

# Product Page / PDP (Milestone 7)

Reference design: `preview/product.html`. Built as an Elementor Pro **Single Product**
Theme Builder template; dynamic fields bind to WooCommerce product data. Never publish a
PDP with unverified specs, invented identifiers, or fabricated reviews.

## Layout (14 blocks, per PRODUCT-EXPERIENCE.md §2)

1. **Breadcrumb** (Home / Shop / Category / Product) → `BreadcrumbList` schema.
2. **Gallery** — thumbnail rail + main image; Woo gallery zoom/lightbox/slider (enabled in
   `inc/setup.php`); optional video/360°. Images must depict the actual product.
3. **Summary** — brand eyebrow, model (H1), reference + variant, price, availability
   indicator (green in-stock dot), short description, **highlights** list, **variation
   selectors** (strap, dial → update image/price/SKU/availability), quantity, **Add to Bag**,
   Wishlist, Compare, trust row, payment marks.
4. **Info tabs** — Description (original prose) · **Specifications table** (fields from
   `DATA-MODEL.md §8`) · **What's Included** · Shipping & Returns · Warranty. Tabs in
   Elementor; keyboard accessible.
5. **Shipping / Returns / Warranty** summary cards, each linking to the full policy.
6. **Reviews** — genuine only; the empty state states plainly that BeepWear never publishes
   fabricated testimonials. Shows stars/text/date/verified indicator once real reviews exist.
7. **Product FAQ** accordion → `FAQPage` schema.
8. **Related products** + **Recently viewed**.

## Data & schema

- Specs render from a "Specifications" custom-field group + global attributes; **omit any
  field without a verified value** (accuracy rule).
- **Product schema:** name, sku, brand, `gtin`/`mpn` **only when real**, description, image,
  `offers` (price, priceCurrency, availability, url). Rank Math owns it in prod; theme JSON-LD
  (`inc/schema.php`) is the fallback.
- PDP SEO: unique title (`{Brand} {Model} | BeepWear`), unique meta, clean
  `/product/{slug}/` URL, descriptive image alt/filenames, internal links to brand, category,
  and the relevant buying guide.

---

# Checkout: Cart, Checkout, Order Confirmation (Milestone 8)

Reference designs: `preview/cart.html`, `preview/checkout.html`,
`preview/order-confirmation.html`. **Style WooCommerce's own cart/checkout — never rebuild
it in Elementor.** Security and update-safety depend on using Woo's native flow; the child
theme only restyles it to the design system.

## Cart

Line items (image, brand, model, variant, qty stepper, remove), coupon field, order-summary
card (subtotal, shipping, estimated tax, total), Proceed to Checkout, Continue Shopping, and
a small trust list. Empty-cart state per `INFORMATION-ARCHITECTURE.md §5`.

## Checkout

Simple, distraction-free: **minimal header** (logo + "Secure Checkout", no nav). Numbered
steps — Contact · Shipping address · Shipping method · Payment — with a sticky Order Summary,
Terms acceptance, Privacy notice, secure-checkout messaging, and Place Order. Guest checkout
+ account login. Payment note: PCI-compliant gateway, encrypted, card details never stored.
Keep it HTTPS and free of upsell clutter.

## Order confirmation

Success check + "Thank you for your order," order number, Shipping-to + Estimated-delivery
cards, order summary (items, totals), and support/continue-shopping. Mirrors the Woo
`order-received` endpoint.

## Build notes

- Configure gateways with **official plugins** (Stripe/PayPal) — never a custom card handler.
- Cart/checkout/account excluded from full-page cache and set `noindex` (SEO/robots).
- Transactional emails (order/shipping/delivery confirmations) styled to brand — see
  `CONTENT-STRATEGY.md` (`content/emails/`), owner M8/M10.

---

# Customer Account & Wishlist (Milestone 10)

Reference design: `preview/account.html`. **Style WooCommerce's native My Account
endpoints** (`/my-account/…`) — never rebuild them; the child theme restyles the account
templates to the design system. Account/cart/checkout stay `noindex` and out of full-page cache.

## My Account

- **Sidebar nav** — Dashboard, Orders (count), Wishlist (count), Addresses, Account Details,
  Password, Log out. Active item filled black with a gold count.
- **Dashboard** — welcome band + stat cards (orders / wishlist / addresses) + recent-orders table.
- **Orders** — table with order #, date, **status pill** (Processing / In transit / Delivered
  — state conveyed by label + dot, not colour alone), total, View.
- **Addresses** — shipping + billing cards with Edit.
- **Account details** — first/last name, email, and a separate **Password** change screen.
- **Downloads** — only if digital products are ever sold (hidden otherwise).
- **Log out.**

## Wishlist

TI WooCommerce Wishlist (per `PLUGINS.md`), styled to match: saved-product cards with
**Move to cart** and **Remove**; optional **Share**. Empty state per
`INFORMATION-ARCHITECTURE.md §5` (link to Shop).

## Build notes

- Login / register / lost-password use Woo's forms, restyled; keep validation + nonces intact.
- Account emails (welcome, verification, password reset) branded — `content/emails/` (M8/M10).
- Forms: labelled fields, visible focus, accessible error messages.
