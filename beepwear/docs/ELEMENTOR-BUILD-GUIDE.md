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
