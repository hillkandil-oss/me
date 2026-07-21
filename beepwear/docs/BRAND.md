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

A warm-neutral foundation with a single restrained metallic accent. Gold is the one
luxury signal — used sparingly, never as fill.

| Token | Hex | Role |
|-------|-----|------|
| `--bw-ink` | `#16130E` | Primary text, dark sections — a warm espresso-black, not pure black |
| `--bw-porcelain` | `#F4F0E8` | Primary background — warm porcelain |
| `--bw-porcelain-2` | `#EAE4D8` | Secondary surface, hairline fills |
| `--bw-champagne` | `#C1A05A` | Accent — muted champagne gold, used for rules, hovers, small marks |
| `--bw-bronze` | `#7C6230` | Deep metallic — used on porcelain for links/emphasis where champagne lacks contrast |
| `--bw-stone` | `#6B665C` | Muted text, captions, metadata |
| `--bw-line` | `rgba(22,19,14,.14)` | Hairline dividers on light |
| `--bw-line-inv` | `rgba(244,240,232,.16)` | Hairline dividers on dark |

**Accessibility:** body text is always `--bw-ink` on `--bw-porcelain`
(contrast ≈ 13:1). Champagne gold **never** carries body text on light — for links/
emphasis on porcelain use `--bw-bronze` (contrast ≈ 4.7:1). Champagne is reserved for
large type, rules, and interactive states where it passes as a non-text or large-text
element.

Semantic (checkout/forms, separate from the accent): success `#3F7A52`,
warning `#B4791F`, error `#A23A2E`.

## 3. Typography

A high-contrast display serif against a geometric grotesque — a couture pairing, not
the Inter/Space-Grotesk default.

- **Display — Cormorant Garamond** (serif). Headlines, product names, section titles.
  Used large, light-to-medium weight, tight leading, generous letter-spacing on caps.
- **Body / UI — Jost** (geometric sans). Paragraphs, navigation, buttons, prices,
  labels. Even, quiet, modern.
- **Utility — Jost, uppercase, tracked** for eyebrows, labels, and metadata. No
  separate mono; prices use `font-variant-numeric: tabular-nums`.

Self-host both (woff2) for performance — see the deploy runbook. Fallbacks:
`Cormorant Garamond → Georgia, 'Times New Roman', serif`;
`Jost → ui-sans-serif, system-ui, sans-serif`.

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
- **Corners: square.** `--radius: 0`. Luxury here is sharp and precise; the only
  softening is on form controls (`2px`).
- Dividers are **hairlines** (`1px`, `--bw-line`), never heavy borders.
- Generous gutters; let products breathe — the grid is the luxury.

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
