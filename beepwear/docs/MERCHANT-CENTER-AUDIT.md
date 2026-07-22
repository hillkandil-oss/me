# BeepWear — Merchant Center Pre-Submission Audit (Milestone 12)

The `MERCHANT-CENTER.md §9` matrix, filled. Verdicts reflect the current repository state
(design + specs + content drafts). **Approval is never guaranteed; the goal is maximum
compliance.** Do **not** connect/submit the feed until every **BLOCKER** is resolved.

Verdict key: **PASS** design/spec satisfies · **WARN** ready but needs attention ·
**BLOCK** must be resolved before submission (mostly real business facts + the live site).

## Audit

| Area | Verdict | Gated on / notes |
|------|:------:|------------------|
| Business information | **BLOCK** | Contact email/phone/hours/address are `[confirm: …]` in `content/contact.md` — add real, consistent details site-wide. |
| Brand consistency | PASS | "BeepWear" used consistently across design, footer, titles, schema. |
| Homepage | PASS | Complete; testimonials/featured-brands hidden until genuine. |
| Navigation | PASS | Header/mega/mobile/footer built; all links resolve. |
| Category pages | PASS | Template ready (hero SEO copy + FAQ, not thin); needs live products. |
| Brand pages | **BLOCK** | Requires **real brands actually sold** + original brand copy. |
| Product pages | **BLOCK** | Template PASS; needs real product data, **authorized photography**, and verified specs; identifiers only when real. |
| Cart | PASS | Woo native flow styled; consistent totals. |
| Checkout | WARN | Design PASS; needs live **HTTPS + configured PCI gateway** (M14). |
| Customer account | PASS | Woo account restyled. |
| Search | PASS | Spec + no-results state defined. |
| Contact page | **BLOCK** | Same as Business information — real contact details required. |
| About page | WARN | Draft complete; owner facts flagged `[confirm: …]`. |
| Policies | WARN | Shipping/Returns/Warranty/Payment/Privacy/Terms drafts ready; **fill `[confirm:]` + legal review** of Privacy/Terms. |
| Product feed | **BLOCK** | Configure Google for WooCommerce on the live store (steps below). |
| Structured data | WARN | Emitted (theme) / Rank Math in prod; **validate with Rich Results Test** on live. |
| SEO | PASS | `SEO-IMPLEMENTATION.md` ready; execute Rank Math config on live. |
| Images | **BLOCK** | Product images must be real, accurate, high-res, no watermarks/overlays; **no misleading AI images**. |
| Performance | WARN | Theme lean + fonts optimized; **measure CWV on live**, tune LiteSpeed. |
| Accessibility | PASS | WCAG 2.2 AA targeted across templates; spot-check on live. |
| Mobile experience | PASS | All templates verified responsive at 390px. |
| Security | **BLOCK** | Execute hardening + HTTPS/SSL on live (M14, `ARCHITECTURE.md §4`). |
| Analytics | WARN | GA4/Site Kit config specified; connect on live, verify events. |
| Search Console readiness | WARN | Verify ownership + submit sitemap post-launch. |
| Merchant feed quality | **BLOCK** | Per-product checklist (`MERCHANT-CENTER.md`) must pass on real data. |

**BLOCKERs to clear before feed submission:** business/contact facts · real brands · real
product data + authorized photography · live HTTPS + gateway · security hardening · feed
configuration + per-product quality. WARN items should be closed but aren't hard stops for
a first review.

## Feed configuration (Google for WooCommerce, on live)

1. Install **Google for WooCommerce**; connect the Google account + Merchant Center.
2. Confirm business info, verified + claimed **custom domain** (never a Hostinger preview URL).
3. Map attributes: `id`, `title`, `description`, `link`, `image_link`,
   `additional_image_link`, `price`, `availability`, `brand`, `gtin`/`mpn` (only when real),
   `condition` = new, `google_product_category` = *Apparel & Accessories > Jewelry > Watches
   (201)*; accessories to their nodes.
4. Configure **shipping** (zones for target markets) and **tax** so feed matches the store.
5. Run diagnostics; resolve disapprovals; confirm price/availability sync with the site.
6. Only after all BLOCKERs clear and diagnostics are clean, keep the feed live and monitor
   (`OPERATIONS.md §4`).

## Guardrails (never)

No fabricated identifiers, reviews, badges, awards, or authorized-dealer claims. No promo
text in feed titles/descriptions. Prices/availability must match the site exactly.
