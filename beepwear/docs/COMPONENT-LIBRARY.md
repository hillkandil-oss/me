# BeepWear — Elementor Design System & Component Library

Master Prompt Part 11. The reusable component system so every page feels like one brand and
pages are composed, not designed from scratch. Tokens live in the child theme
(`style.css` `:root`); components are built once in Elementor and reused via global
templates.

> **Palette note:** Part 11's "Deep Navy / Charcoal / Warm Gold" is labeled an *example*.
> BeepWear's committed identity is the **Luxury Black / Pure White / Champagne Gold** system
> pinned in Part 4 (`BRAND.md`) and already built into the homepage and navigation. That
> stays authoritative; the token roles below map Part 11's structure onto it.

## 1. Global tokens (set once in Elementor Site Settings, mirrored from the theme)

| Elementor global | BeepWear token | Value |
|---|---|---|
| Primary | `--bw-black` | `#141310` |
| Secondary | `--bw-charcoal` | `#3A3733` |
| Accent | `--bw-champagne` | `#C2A15C` |
| Background | `--bw-white` | `#FFFFFF` |
| Surface | `--bw-offwhite` / `--bw-light` | `#F7F6F3` / `#EFEEEA` |
| Text primary / secondary | `--bw-black` / `--bw-stone` | `#141310` / `#6E6A61` |
| Success / Warning / Error / Info | semantic tokens | `#1E6B4F` / `#C58A1E` / `#B23A48` / `#2E4A8B` |

Never hardcode colors — reference globals/tokens everywhere.

**Typography presets** (Elementor Global Fonts, from `BRAND.md §3`): H1 hero, H2 section,
H3 card, H4 small, Body Large, Body, Small/Caption, Button — Cormorant Garamond (display),
Manrope (body). **Spacing:** the 8px scale (`--sp-1…7`). **Radius:** `0` cards/images,
`4px` controls. **Shadows:** `--shadow-sm/md/lg/hover` (subtle, sparse).

## 2. Components (implemented in `style.css`, reused in Elementor)

- **Buttons** — Primary (filled, invert hover), Secondary (outline→fill), Ghost/Outline,
  Text. All with hover, keyboard focus (`:focus-visible` gold ring), disabled + loading
  states. Classes: `.bw-btn`, `.bw-btn--secondary`, `.bw-btn--ghost`.
- **Forms & inputs** — text/email/phone/select/checkbox/radio/textarea, `4px` radius; states:
  default · hover · focus (black border) · valid · invalid (`--bw-error`) · disabled ·
  readonly; required indicators; accessible labels + error messages (not color-only).
- **Cards** — Product (image, brand, name, price, rating if genuine, wishlist, quick view,
  add-to-cart, hover), Category (image, name, description, button), Brand (logo, name,
  overview, button), Article (image, category, title, excerpt, date, read more), Testimonial
  (genuine only: reviewer, rating, review, date, verified indicator).
- **Badges** — `.bw-badge` + `--new/--limited/--sale/--oos/--preorder/--featured`. Use sparingly.
- **Alerts** — `.bw-alert` + `--success/--info/--warning/--error`; a state dot conveys meaning
  in addition to color (never color alone).
- **Product gallery** — thumbnails, zoom, touch gestures, keyboard access, optional
  video/360°, smooth transitions (Woo gallery features enabled in `inc/setup.php`).
- **Accordion** (FAQ, specs, shipping, warranty, returns) and **Tabs** (description, specs,
  reviews, shipping, warranty, care) — both keyboard accessible.
- **Modals** — quick view, newsletter, cookie details; never intrusive.
- **Empty states** — cart, wishlist, search, orders, categories, blog: friendly message +
  CTA back into browsing (`INFORMATION-ARCHITECTURE.md §5`).
- **Loading states** — products, search, checkout, forms, filters, pagination; no layout shift.
- **Micro-interactions** — buttons, cards, nav, product images, wishlist, cart, forms —
  fast, unobtrusive, reduced-motion respected.

## 3. Reusable Elementor templates (build once, document where used)

| Template | Used on |
|----------|---------|
| Header / Footer | Entire site (Theme Builder) |
| Homepage sections | Home |
| Single Product | All products |
| Products Archive | Shop + category |
| Brand page | Each brand |
| Collection page | Each collection |
| Buying guide | Guide articles |
| Journal article | All posts |
| Contact / About | Those pages |
| Policy page | All legal/policy pages |
| Newsletter / FAQ / CTA banner / Trust / Testimonial blocks | Reused across pages |

## 4. Performance & accessibility

Prefer global styles over per-widget CSS; keep containers shallow (fl/grid, not deep
nesting); lazy-load media; limit third-party scripts; lean DOM. Every component: keyboard
operable, visible focus, adequate contrast, alt text, ARIA where needed, descriptive labels,
never color-only signaling.

## 5. Design QA checklist (gate per component/page)

- [ ] Uses global colors + typography (no hardcoded values).
- [ ] Matches BeepWear identity; fully responsive across breakpoints.
- [ ] Meets accessibility requirements; loads efficiently; consistent spacing.
- [ ] Uses reusable components; no duplicated styling; no visual bugs.
- [ ] Works correctly with WooCommerce functionality.
