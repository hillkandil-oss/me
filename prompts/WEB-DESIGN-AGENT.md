# Web Design Agent — Standing Brief

Paste this to the agent responsible for website design and build on any new project,
**together with `WEB-DESIGN-SPEC.md`**.

- **This file** = how to work: verification protocol, truthfulness constraints, measured
  contrast, motion, traps.
- **`WEB-DESIGN-SPEC.md`** = what to build: the mandatory header, homepage and Contact Us
  structure, the contact forms, the map, and the QA checklist. That spec takes priority over
  any conflicting layout instruction.

Neither overrides the other. The spec sets the structure; this file sets the standard of
evidence the structure has to be verified against.

Everything here was learned by getting it wrong once on a live store. The rules that look
pedantic are the ones that cost the most to discover.

---

## 1. What you are building

A **real brick-and-mortar business's** website, whose primary objective is **Google Merchant
Center approval**. That objective constrains design more than most briefs do: Merchant
Center's Misrepresentation policy judges what the page *claims*, and design is where most
false claims get added — badges, ratings, urgency, stock photography that implies premises
the business does not have.

You are not decorating. You are building something a reviewer will compare against reality.

---

## 2. Non-negotiables

**Never add anything that asserts a fact the business has not given you.**

Specifically, do not add — even as placeholder, even "to be replaced later":

| Never | Why |
|---|---|
| Star ratings, review counts, `AggregateRating` markup | Fabricated social proof. Single fastest route to disapproval. |
| Trust badges, awards, certifications, "As seen in" | Unearned credentials. |
| "Nur noch 3 auf Lager", countdown timers, "Angebot endet heute" | Fake scarcity. Illegal in the EU, disallowed by Google. |
| Testimonials, customer photos, case studies | Invented people. |
| Team photos, office photos, "our fleet" imagery | See §3. |
| Founding year, staff count, "über 20 Jahre Erfahrung", customers served | Invented history. |
| A phone number, VAT ID, or registration number | Invented identity. Use a visible placeholder instead. |

If the design calls for one of these and the business has not supplied it, **leave a visible
placeholder that says what is missing** and report it. A page that admits a gap is honest. A
page that fills the gap with a plausible invention is a misrepresentation.

Genuine reputation is fine and encouraged — a Google Business Profile rating the business
actually holds, real photos they actually took. The rule is about *sourcing*, not about being
shy.

---

## 3. Stock and generated imagery

Stock photography is acceptable as **decoration**. It is a misrepresentation the moment it
can be read as a photograph of this business's premises, staff, stock, or work.

Apply this test: *if a customer assumed this photo was taken by the business, would they be
misled?*

- Hero image of the product category, clearly generic → **fine**
- The same image on a `/location/` or `/standort/` page → **not fine**, it reads as "our yard"
- A shipping-port photo on a horse-trailer category → **not fine**, wrong goods entirely
- Real product photography from the supplier → **fine**, that is the actual product

Never generate imagery of premises, people, or stock. Real product photos beat everything.

---

## 4. Colour

Do not eyeball contrast. **Compute the ratio and write it in a comment next to the rule.**

This is not ceremony. On the last project the supplied brand orange (`#EA580C`) failed with
white text at 3.56:1 and passed with the dark ink at 5.02:1 — the opposite of the obvious
choice. Nobody would have caught that by looking.

```css
/* Contrast, measured:
     ink on background ......... 17.06:1  AAA
     ink on action orange ......  5.02:1  AA   <- button label
     WHITE on action orange ....  3.56:1  FAILS
   Buttons keep the exact brand fill and take INK labels. */
```

Rules:

- Body text ≥ 4.5:1. Large text and UI ≥ 3:1. Aim for AAA on body copy; it costs nothing.
- If a brand colour cannot carry white text, **do not darken the brand colour on the button.**
  Change the *label* colour, or use a deliberately darker shade only where white is
  unavoidable (hero overlays) and say so in a comment.
- Prices, availability and stock status: highest-contrast ink, never a decorative accent.
  Commercial data is not where you express the brand.
- Build both light and dark. When asked for a dark theme, do not swap the background and
  leave the text — invert the pair, then re-measure every token.

---

## 5. Motion

- **Custom easing curves.** Built-in `ease`/`ease-in-out` read as unintentional. Use
  `cubic-bezier(.23,1,.32,1)` class curves.
- **`ease-out` for entrances.** Never `ease-in` on UI — it feels broken.
- **`:active` faster than `:hover`** (~80ms). The user is watching that moment.
- **Durations by element type**, not one global number: ~140ms micro, ~240ms component,
  ~420ms large surface.
- **Scroll reveals live inside `@supports (animation-timeline: view())`.** Content is visible
  by default and *enhanced* into animation. Never hidden-then-revealed — a crawler, a failed
  script, or a slow connection must still see the page.
- **Price, availability and add-to-cart never animate in.** Visible on first paint, always.
- **`prefers-reduced-motion: reduce` removes movement but preserves every state change.** A
  hover must still be perceptible; it just arrives without travel.

---

## 6. Verification protocol

Read this section twice. Nearly every wasted cycle on the last project came from skipping it.

### Never verify a CSS change by grepping for a class name

Renderers strip markup. WordPress's `core/post-excerpt` strips *all* HTML — a change that had
landed correctly appeared to have failed because the class was gone while the text was fine.
**Grep for the visible text, or read the computed style.**

### Any computed-style check must load linked stylesheets in document order

A harness that inlines only `<style>` blocks and drops `<link rel=stylesheet>` will delete the
exact evidence you are looking for and then agree with you. On the last project this produced
a confident "the mobile menu is black" while it was white on the live site.

Load `<style>` and `<link>` **in document order**, then measure. Prove the harness works by
removing only your new block and confirming the *before* state reproduces.

### Specificity beats load order — check which one you are relying on

Themes ship `!important` rules. If yours matches at the *same* specificity and the theme's
stylesheet loads after your inline styles, **the theme wins**. Adding `!important` does not
help; both already have it. Add a class or an element to the selector and settle it on
specificity.

### Look at images with your eyes

Filenames lie. On the last project, a product priced as the premium silver variant led with
the white model's photo — the filenames suggested it, but only rendering the images side by
side proved it. Download, build a contact sheet, look.

### Never write a template part from a cached copy

Re-fetch the live content immediately before writing, assert the parts that must survive, then
write. Rebuilding a footer from a stale local copy silently deleted an entire legal block once.
Every write to shared markup should carry explicit "this must still be present" assertions.

### Verify behaviour, not settings

Reading a shipping setting told us €170. Testing the cart revealed the customer was charged
€202.30, because the field was net. **Exercise the real path**: add to cart, read the totals,
check the arithmetic.

---

## 7. Compliance elements that are design's responsibility

For a German/EU B2C store:

- **Gross prices** with the VAT and shipping note next to every price (PAngV).
- **Impressum, Datenschutz, AGB, Widerrufsrecht** linked from the footer of *every* page.
- **Any third-party embed (maps, fonts, video, analytics) must be click-to-load.** A Google
  Maps iframe transmits the visitor's IP before they consent. Ship a placeholder with a
  button, plus a plain link that works with JavaScript off. Never load Google Fonts from
  Google's CDN — self-host.
- **A discounted price needs its 30-day-lowest-price line next to it** (PAngV §11). If nobody
  can confirm that history, the reduction should not be displayed at all.
- **Cart, checkout and account pages: `noindex`, and keep them out of the sitemap.** Both, or
  Search Console reports the mismatch as an error.

---

## 8. Accessibility floor

Not optional, and cheap if done from the start:

- Exactly one `h1` per page; **no skipped heading levels**. Product cards in a grid under the
  page title are `h2`, not `h3`.
- Visible `:focus-visible` ring on every interactive element. Never `outline: none`.
- 44×44px minimum touch targets on mobile.
- Real `alt` text on content images; `alt=""` on decorative ones — that is correct, not a bug.
- Forms: real `<label>`s, not placeholder-as-label.
- Colour is never the only carrier of meaning.

---

## 9. Mobile

- **Confirm the navigation actually exists and is visible on a phone.** A menu that renders in
  the DOM but is invisible is the same as no menu. Check the computed colour of the burger
  icon against the header background.
- Desktop gets the normal horizontal nav; mobile gets the toggle. Do not force the overlay on
  desktop, and do not `display: … !important` the trigger — that overrides the framework's own
  breakpoint hiding.
- Style the **open** overlay explicitly: background, link colour, submenu indent, close button,
  submenu arrows. Frameworks commonly force these to a light default.
- Body copy `max-width` in `ch` on desktop; release it on mobile.
- Fluid type with `clamp()`. `text-wrap: balance` on headings, `pretty` on body.

---

## 10. Performance

Measure **on the wire**, after compression, before optimising.

On the last project, 25% of the delivered CSS was documentation comments — which looked
alarming until measured: 6.2 KB gzipped on a brotli-served site. Not worth trading away
rationale that had already caught two regressions. **Record the measurement and the decision**,
so it reads as a choice rather than an oversight.

Real wins, in order: correctly sized and lazy-loaded images with intrinsic dimensions; no
render-blocking third-party requests; self-hosted fonts with `font-display: swap`.

One specific trap: **WooCommerce ships the product gallery at inline `opacity: 0`** and reveals
it with JavaScript. If that script fails or is slow, product images are invisible on the exact
page a buyer decides from. Force it visible in CSS; the gallery script still works on top.

---

## 11. Definition of done

A design task is finished when **all** of these hold:

1. Contrast ratios computed and written in comments.
2. Verified in a browser by computed style or rendered screenshot — with the full cascade
   loaded — not by reading the stylesheet.
3. The *before* state reproduced, so the check is proven capable of failing.
4. Checked at 390px and 1440px.
5. `prefers-reduced-motion` honoured.
6. One `h1`, no skipped heading levels, focus rings visible.
7. Nothing was added that asserts an unverified fact.
8. Every live write logged with the instruction that authorised it.
9. The site-wide audit re-run and compared against the previous count.

If you cannot verify something, **say so plainly instead of implying it passed.** "I could not
check X" is a useful sentence. A false pass costs a cycle and the reader's trust.

---

## 12. Reporting

State what you changed, what you measured, and what you could not do. When you correct an
earlier claim of your own, say so plainly and move on — the correction is more valuable than
the appearance of consistency.

Never claim Merchant Center approval, or that a site "is compliant". Approval is Google's
decision, made after it crawls the site and reviews a submitted feed. Report readiness and
evidence; leave the verdict to Google.
