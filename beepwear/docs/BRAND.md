# BeepWear — Brand & Design System

The visual identity for BeepWear. Every color, type, and spacing decision on the
storefront derives from this document. It is the single source of truth; the child
theme's `style.css` implements it as CSS custom properties.

## 1. Positioning

BeepWear is a boutique for **precision timepieces** — an international retailer that
should feel like walking into a quiet, well-lit gallery of watches. The design blend:
the restraint of Aesop, the confidence of Rolex, the clarity of Apple. Not loud, not
gilded to excess. Luxury here reads as **space, precision, and material honesty**, not
ornament.

Original identity — inspired by the *principles* that make luxury watch sites feel
premium (generous whitespace, disciplined type, unhurried motion), never a copy of any
existing brand's design, assets, or content.

## 2. Color

Classic luxury: **Luxury Black · Pure White · Champagne Gold** (Master Prompt Part 4).
White/off-white grounds carry the space; black carries text and structure; gold is the
single accent — used sparingly for rules, hovers, and small marks, never as a text fill.

| Token | Hex | Role |
|-------|-----|------|
| `--bw-black` | `#141310` | Luxury Black — primary text, dark sections (a hair warm, not flat #000) |
| `--bw-white` | `#FFFFFF` | Pure White — primary background |
| `--bw-offwhite` | `#F7F6F3` | Off White — alternating/soft sections |
| `--bw-light` | `#EFEEEA` | Very Light Gray — image beds, fills |
| `--bw-champagne` | `#C2A15C` | Champagne Gold — accent (rules, hovers, marks) |
| `--bw-champagne-deep` | `#9C7E3E` | Darker gold — link hover / gold text on white |
| `--bw-charcoal` | `#3A3733` | Charcoal Gray — secondary text |
| `--bw-stone` | `#6E6A61` | Muted text, captions, metadata |
| `--bw-silver` | `#C9C6BF` | Soft Silver — hairlines, disabled, ghost borders |
| `--bw-line` | `rgba(20,19,16,.12)` | Hairline dividers on light |

**Semantic** (checkout/forms/states, separate from the accent, per Part 4):
Error — Elegant Crimson `#B23A48`; Success — Deep Emerald `#1E6B4F`;
Warning — Warm Amber `#C58A1E`; Information — Royal Blue `#2E4A8B`.

**Accessibility:** body text is `--bw-black` on white/off-white (contrast ≈ 15:1).
Champagne gold `#C2A15C` **never** carries body text on white (≈ 2.4:1 — fails). For gold-
toned text or links on white, use `--bw-champagne-deep` (≈ 4.6:1). Bright champagne is
reserved for large display type, hairlines, focus rings, and non-text marks. On black,
champagne is legible for links and accents.

## 3. Typography

A high-contrast display serif against a clean grotesque (Master Prompt Part 4 pairing).

- **Display — Cormorant Garamond** (serif). Headlines, product names, section titles.
  Used large, light-to-medium weight, tight leading, generous letter-spacing on caps.
- **Body / UI — Manrope** (grotesque sans). Paragraphs, navigation, buttons, prices,
  labels. Even, modern, highly readable. (Part 4 allowed Inter or Manrope; Manrope chosen
  for a touch more character while staying neutral.)
- **Utility — Manrope, uppercase, tracked** for eyebrows, labels, and metadata. No
  separate mono; prices use `font-variant-numeric: tabular-nums`.

Self-host both (woff2) for performance — see the deploy runbook. Fallbacks:
`Cormorant Garamond → Georgia, 'Times New Roman', serif`;
`Manrope → ui-sans-serif, system-ui, sans-serif`.

### Type scale (fluid, `clamp`)

| Token | Size | Use |
|-------|------|-----|
| `--fs-display` | `clamp(44px, 7vw, 96px)` | Hero |
| `--fs-h1` | `clamp(34px, 4.5vw, 60px)` | Page title |
| `--fs-h2` | `clamp(26px, 3vw, 40px)` | Section |
| `--fs-h3` | `clamp(20px, 2vw, 26px)` | Card / product name |
| `--fs-body` | `clamp(16px, 1.05vw, 18px)` | Paragraph |
| `--fs-small` | `14px` | Metadata |
| `--fs-label` | `12px` | Eyebrows / labels (uppercase, `.18em` tracking) |

Body line-height `1.6`; headings `1.1` with `text-wrap: balance`.

## 4. Space & layout

- Base unit **8px**; spacing scale `8 / 16 / 24 / 40 / 64 / 96 / 128`.
- Content max-width **1240px**; text measure capped near **68ch**.
- Section vertical rhythm: `clamp(64px, 10vw, 128px)`.
- **Corners:** cards, sections, and images are **square** (`--radius: 0`) — sharp and
  precise; **buttons and inputs are softly rounded** (`--radius-sm: 4px`, per Part 4).
- Dividers are **hairlines** (`1px`, `--bw-line`), never heavy borders.
- Generous gutters; let products breathe — the grid is the luxury.

### Buttons (Part 4)

Three variants, all `4px` radius, uppercase Manrope, `.08em` tracking, `200–320ms` hover.
- **Primary** — black fill, white text; hover inverts to outline (transparent + black text/border).
- **Secondary** — white fill, black border/text; hover fills black with white text.
- **Ghost** — transparent, thin silver border; hover darkens the border to black.

### Cards

Product card: square image on `--bw-light`, subtle `scale(1.03)` hover; brand eyebrow,
model in Cormorant, price in muted stone; wishlist + quick-view on hover; sale badge is a
small black pill (`onsale`). Ratings shown **only** when genuine reviews exist.

### Icons

Thin line style, consistent stroke and size, professional — no filled/cartoon icons.

## 5. Motion

Purposeful and slow. Nothing bounces.
- Transitions `200–320ms`, easing `cubic-bezier(.16,.9,.28,1)`.
- Images: subtle `scale(1.03)` on hover, `600ms`.
- Reveal on scroll: fade + 12px rise, once, staggered — never on every element.
- Respect `prefers-reduced-motion: reduce` (disable transforms/reveals).

## 6. Imagery

- **Product photography:** original, manufacturer/supplier-authorized, or licensed
  only. Never AI-generated as the primary product image. Consistent framing, neutral
  backgrounds, 1:1 for the grid, 4:5 for PDP gallery.
- **Editorial/lifestyle (hero, campaign, blog):** may be created with Higgsfield AI —
  atmospheric, warm, low-contrast, human wrist/lifestyle. Never depict a specific
  product it isn't.

## 7. Voice

Confident, precise, unhurried. Short declarative sentences. Speak to craft and
ownership, not hype. Never invent reviews, awards, certifications, or trust badges.
- Buttons say exactly what they do: **Add to bag**, **Proceed to checkout**, **View collection**.
- Prices, materials, and specs are stated plainly. Specific beats clever.

## 8. Logo (M2b)

Concepts: `preview/logo.html`. Assets: `theme/beepwear/assets/images/`.

- **Primary wordmark** — "Beep" in ink + "Wear" in deep gold, Cormorant Garamond 600
  (`beepwear-wordmark.svg`). The identity carried through the site header/footer.
- **Combination mark** — the watch-dial mark (`beepwear-mark.svg`) left of the wordmark, for
  the header lockup. The dial's single gold hand echoes the hero/PDP motif.
- **Stacked lockup** — mark over "BEEP WEAR" (tracked) with the optional line "Fine Timepieces".
- **Monogram** — "BW" inside a gold bezel circle, for compact/social use.
- **Favicon / app icon** — dial mark on warm-black (`beepwear-favicon.svg`).

**Usage:** keep clear space ≥ the mark's radius around the lockup; minimum wordmark height
~20px; never stretch, recolour outside the palette, or add effects. For the wordmark as a
flat asset (email, print, schema), export the Cormorant text to **outlines** so it renders
without the font. Provide a **512×512 PNG** export of the mark for the Organization schema
`logo` (Google prefers raster ≥112px) — the theme currently references the SVG mark as a
placeholder.
