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
