# Design System — kaisercontainers

_Built with the `design-taste-frontend` skill. Trust-first commerce → restrained dials._

**Design read:** trust-first commerce storefront for German container buyers (businesses,
contractors, logistics), restrained **industrial** language, applied over the **Tranzix**
WooCommerce theme + Elementor. **Dials:** VARIANCE 4 · MOTION 3 · DENSITY 4.

> Why restrained: Google Merchant Center rewards a conventional, legible, fast, trustworthy
> storefront. Experimental motion, asymmetric chaos, or AI-tell decoration would work against
> approval. Industrial character comes from **palette, type, and material**, not gimmicks.

## 1. Palette — "Corten & Graphite" (one locked accent)
| Token | Hex | Use |
|---|---|---|
| `--kc-ink` | `#1A1D21` | primary text (off-black, not pure) |
| `--kc-steel` | `#26323C` | dark surfaces: header, footer |
| `--kc-steel-700` | `#33434F` | hover on steel |
| `--kc-corten` (**accent, locked**) | `#C2522A` | CTAs, links, price, active states |
| `--kc-corten-700` | `#A2401E` | accent hover / :active |
| `--kc-paper` | `#F6F7F8` | page background |
| `--kc-surface` | `#FFFFFF` | cards, inputs |
| `--kc-line` | `#DDE1E4` | borders, dividers |
| `--kc-muted` | `#5B6670` | secondary text (AA on paper) |
| `--kc-success` | `#2E7D46` | in-stock / success |
| `--kc-warning` | `#B26A00` | limited / call-to-confirm |
| `--kc-error` | `#C0392B` | out-of-stock / errors |

Accent is used **identically across every section** (color-consistency lock). No second accent.
Corten `#C2522A` on white = 4.6:1 (AA text ✓); on `--kc-steel` use white text.

## 2. Typography
- **Headings:** `Archivo` (700/800) — sturdy industrial grotesk, full German diacritics.
- **Body/UI:** `Inter` (400/500/600) — legible, trust-standard, umlaut-safe.
- Self-hosted `font-display: swap`. Two families only.

**Type scale (desktop / mobile):** H1 44/32 · H2 32/26 · H3 24/20 · H4 19/18 · body 17/16 ·
small 14. Line-height: headings 1.15, body 1.6. Body measure ≤ 68ch.

## 3. Spacing & layout
- Scale (px): 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96.
- Container max-width **1280px**, gutter 20px (mobile 16px).
- Section padding: desktop `64px` (hero 96), mobile `40px`. Density 4 = daily-app rhythm.
- Grid over flex-math; product grids `repeat(auto-fill, minmax(260px,1fr))`.

## 4. Radius, shadow, borders (shape lock)
- **One radius scale:** buttons/inputs/cards all **6px** (industrial = slightly squared).
- Shadows tinted to steel, not pure black: `0 1px 2px rgba(26,29,33,.06)`,
  card hover `0 8px 24px rgba(26,29,33,.10)`.
- 1px `--kc-line` borders do most of the structural work (density 4).

## 5. Components
- **Buttons:** primary = corten fill / white text; secondary = steel outline; ghost = text+underline.
  `:active` → `translateY(1px)`. Labels ≤ 3 words, one line. Min touch target 44px.
- **Product card:** 4:3 image, title (H4), price in corten, condition badge (Neu/Gebraucht),
  availability line, one CTA. Hover: lift + image scale 1.02 (motion 3).
- **Forms:** label **above** input, helper below, error below in `--kc-error`. Visible focus ring
  `2px --kc-corten` offset 2px. No placeholder-as-label.
- **Badges:** `Neu` (steel), `Gebraucht` (muted), `Auf Lager` (success), `Auf Anfrage` (warning).

## 6. Motion (intensity 3, accessibility-first)
- Transitions `180ms cubic-bezier(.16,1,.3,1)`, transform/opacity only.
- Scroll-reveal (fade+8px) on section enter, once. Sticky header condense. Card hover lift.
- **All motion gated behind `@media (prefers-reduced-motion: no-preference)`** → collapses to static.
- No parallax, no autoplay carousels, no marquees, no countdown timers.

## 7. Application
Delivered as `theme/snippets/brand.css` (CSS variables + WooCommerce/Tranzix overrides).
Apply on the live site via **Appearance → Customize → Additional CSS** (or Tranzix theme
options / Elementor global kit). Fonts: enqueue Archivo + Inter (self-host or theme fonts).
