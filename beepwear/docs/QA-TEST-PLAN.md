# BeepWear — Pre-Launch QA Test Plan (Milestone 13)

Executable test plan run against the **release candidate on staging** before deployment.
Record each result (PASS / FAIL + note) in the grids below; **no critical issue may remain
open at launch**. Complements `OPERATIONS.md §2–3`.

## 1. Functional

| Test | Expected | Result |
|------|----------|:------:|
| Primary nav + mega menu | All links resolve to complete pages | ⬜ |
| Search + autocomplete | Relevant results; helpful no-results state | ⬜ |
| Category filters + sort | Correct products; state in URL; clearable | ⬜ |
| PDP variations | Image/price/SKU/availability update | ⬜ |
| Add to cart / update qty / remove | Cart + fragments update correctly | ⬜ |
| Coupon | Valid applies; invalid shows clear error | ⬜ |
| Checkout (guest + account) | Completes; correct totals, shipping, tax | ⬜ |
| Payment (test mode → live) | Gateway authorizes; order created | ⬜ |
| Order confirmation + emails | On-screen + confirmation/shipping emails sent | ⬜ |
| Account: register/login/reset | All flows work; validation clear | ⬜ |
| Wishlist add/move/remove | Works; empty state shown | ⬜ |
| Contact + newsletter forms | Submit, validate, deliver; privacy notice shown | ⬜ |
| 404 + empty states | Branded, route back into browsing | ⬜ |

## 2. Responsive (large-desktop → small-mobile)

| Breakpoint | Layout / type / nav / images / forms / checkout | Result |
|------------|--------------------------------------------------|:------:|
| ≥1440 · 1280 · 1024 · 768 · 414 · 360 | No overflow, no overlap, no broken layout | ⬜ |

Verify: no horizontal scroll; tap targets ≥ 44px; mobile menu + filters drawer; sticky header.

## 3. Browser compatibility

Current **Chrome · Edge · Firefox · Safari** (desktop + iOS/Android): render, fonts,
interactions, checkout. | ⬜ per browser.

## 4. Performance (Core Web Vitals, mobile + desktop)

| Metric | Budget | Home | PLP | PDP | Cart | Checkout |
|--------|--------|:----:|:---:|:---:|:----:|:--------:|
| LCP | < 2.5s | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| INP | < 200ms | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| CLS | < 0.1 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Check: images WebP/AVIF + sized, LiteSpeed cache/critical-CSS, deferred JS, font preload, DB.

## 5. Accessibility (WCAG 2.2 AA spot-check)

Keyboard path through nav → PLP → PDP → cart → checkout; visible focus everywhere; contrast
≥ 4.5:1 (text); form labels + accessible errors; alt text; heading order; reduced-motion;
state not by colour alone (status pills/alerts). Run axe/Lighthouse a11y. | ⬜

## 6. Security

HTTPS + no mixed content; SSL valid; login rate-limit + 2FA; file editing/XML-RPC disabled;
input sanitisation + output escaping (core/Woo); nonce-protected forms; plugin integrity;
security headers. | ⬜ (see `ARCHITECTURE.md §4`, executed M14).

## 7. SEO / structured data validation

Titles + meta unique; one H1; canonicals; robots.txt; sitemaps submit; Rich Results Test
passes for Product/Breadcrumb/FAQ/Organization; broken-link scan clean. | ⬜

## Sign-off

QA sign-off (all criticals resolved) is required before deployment (M14). Record the final
verdict and any accepted minor issues in `REVIEW-LOG.md`.
