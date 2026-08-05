# Apple-Design Audit — kaisercontainers.de

Audited against the `apple-design` skill (Apple's *Designing Fluid Interfaces*, *The Details
of UI Typography*, *Principles of Great Design*). Constraint: no build step; all CSS/JS is
injected through a WordPress footer widget, vanilla only.

## Scope judgment — what deliberately does not apply
Sections §2–§6 (1:1 drag tracking, interruptible springs, velocity handoff, momentum
projection, rubber-banding) target **gesture-driven UI**: sheets, drags, flicks, carousels.
This site has none. Adding spring physics here would be decoration, not craft, and would add
weight to a store whose job is to load fast and sell containers. Skipped on purpose.

## Findings and fixes

| # | Principle | Finding | Fix applied |
|---|---|---|---|
| 1 | §1 Response | **No press feedback.** Buttons, cards and links reacted only on `:hover`; nothing on pointer-down. Apple: feedback on press, not release, or it "feels dead". | `:active` states — buttons `scale(.97)` @100ms, cards `scale(.985)`, topbar/FAQ opacity dip. Tap-highlight removed, 44px min targets. |
| 2 | §14 Reduced motion | Blanket `*{transition:none}` killed **all** feedback. Reduced motion means gentler, not none. `prefers-reduced-transparency` and `prefers-contrast` unhandled. | Reduced motion now keeps short opacity/colour transitions and drops only transforms/parallax. Added translucency and contrast blocks. |
| 3 | §12 Materials | Sticky header was `blur(2px)` + a hard box-shadow: an opaque strip with a divider, not a material. | Real translucent layer: `rgba(255,255,255,.72)` + `blur(20px) saturate(180%)`, bright top edge, and a **scroll edge gradient** replacing the hard divider. Vibrancy: nav text darkened and weighted for legibility. |
| 4 | §15 Typography | One tracking value for every size; no optical sizing. Apple: tracking is size-specific — tighten large text, body near 0, small text slightly positive. | h1 `-.025em`/1.06, h2 `-.018em`, h3 `-.012em`, body `0`/1.62, small UI `+.01em`. Added `font-optical-sizing:auto`, `text-wrap:balance` on headings, `pretty` on prose. |
| 5 | §11 Smoothness | No `will-change` hints; only compositor-safe properties were animated (already correct). | `will-change:transform,opacity` on revealing/hover elements, released to `auto` once revealed. |
| 6 | §7 Spatial consistency | Hover in/out used one curve. | Mirrored easing: enter `cubic-bezier(.32,.72,0,1)`, return `cubic-bezier(.16,1,.3,1)`. |
| 7 | §16 Craft / wayfinding | Focus ring inconsistent across controls. | Single visible `:focus-visible` ring (corten, 3px offset) on every interactive element. |

## Verified as already correct
- Compositor-friendly animation only (`transform`/`opacity`), no layout-property animation (§11).
- Scroll-reveal enhances an already-visible default: classes are added by JS, so content is
  never hidden if JS fails (§14, and the impeccable rule about gated visibility).
- Hero glow is semi-transparent and disabled under reduced motion (§14 large-moving-object rule).
- Enter/exit paths are symmetric; no in-from-right/out-the-bottom mismatch (§7).

## Remaining, blocked by platform
- **§16 inline validation.** Contact Form 7 validates on submit, not inline per field. Fixing
  properly means switching to an API-configurable form plugin (see `contact-form-setup.md`).
- **§1 tap delay / §13 haptics.** Not applicable: no custom gesture layer, and the Vibration
  API is unsupported on iOS Safari.
