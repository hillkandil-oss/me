# BeepWear — Google Merchant Center Readiness (Verified Status)

**Site:** https://beepwear.com
**Verified live:** 2026-07-22
**Verified by:** direct WooCommerce/WordPress REST + HTTP checks against the live site.

> **Honest scope note.** This document records what was *verified on the live
> site*. It is **not** a guarantee of Merchant Center approval. Compliance is
> ultimately Google's determination, made after Google crawls and reviews the
> site and the submitted product feed. No one can certify guaranteed approval
> from the website alone.

---

## 1. On-site requirements — VERIFIED IN PLACE ✅

| Requirement | Status | Evidence |
|---|---|---|
| Secure checkout (HTTPS/SSL) | ✅ Valid | `ssl_verify_result = 0`, homepage HTTP 200 |
| Privacy Policy | ✅ Live | `/privacy-policy/` (200) |
| Terms & Conditions | ✅ Live | `/terms-and-conditions/` (id 630, 200) |
| Returns & Refunds policy | ✅ Live | `/returns/` (id 625, 200) |
| Shipping Policy | ✅ Live | `/shipping-policy/` (id 624, 200) |
| Payment Policy | ✅ Live | `/payment-policy/` (id 627) |
| Warranty Policy | ✅ Live | `/warranty-policy/` (id 626) |
| Authenticity Guarantee | ✅ Live | `/authenticity-guarantee/` (id 621) |
| Contact — email/phone/address | ✅ Visible | header utility bar + `/contact/` + store settings |
| Business identity consistency | ✅ | 510 Main St, Wall, SD 57790 · USD · US:SD |
| Google Map on Contact page | ✅ | keyless embed present on `/contact/` |
| Store publicly visible | ✅ | `woocommerce_coming_soon = no` |

## 2. Product data — VERIFIED IN PLACE ✅

| Requirement | Status | Evidence |
|---|---|---|
| Products published | ✅ 269 | `X-WP-Total: 269` |
| Product images | ✅ 269 / 269 | 0 missing across all pages |
| Brand attribute | ✅ 269 / 269 | 0 missing |
| Condition = Used | ✅ 269 / 269 | global `pa_condition` attribute, visible=true |
| Original descriptions | ✅ | rewritten to remove duplicate-content risk |

## 3. Payments — VERIFIED IN PLACE ✅

| Method | Status |
|---|---|
| PayPal (`ppcp-gateway`) | ✅ enabled, `needs_setup = false` (account linked) |
| Bank Transfer (`bacs`) | ✅ enabled |
| Checkout terms-acceptance checkbox | ✅ active (terms page id 630) |

## 4. Steps that live INSIDE Merchant Center — owner-handled ⏳

These are **not** website settings and cannot be verified from the site:

- [ ] **Verify & claim** the domain `beepwear.com` in Merchant Center.
- [ ] **Submit the product feed.** No feed plugin is installed; the feed is
      built/submitted by the owner. The feed file must itself carry the required
      attributes: `id`, `title`, `description`, `link`, `image_link`, `price`,
      `availability`, `brand`, `condition: used`, and a unique identifier
      (`gtin`/`mpn`, or `identifier_exists: no` for vintage pieces without one).
      The site data supports all of these; feed-file correctness is confirmed at
      upload time.
- [ ] **Tax settings** for SD, if applicable to the business.

## 5. Known higher-scrutiny factors (honest risk) ⚠️

Not blockers — context for realistic expectations:

- **Pre-owned luxury / branded watches** receive heavier counterfeit-risk
  review. Mitigations already in place: Authenticity Guarantee page,
  `condition: used` on every product, honest original descriptions.
- **Bank Transfer** as a payment method can attract scrutiny; the live
  **PayPal** gateway alongside it is a meaningful mitigation.

## 6. Not a compliance item

- **Higgsfield editorial imagery** (hero, lifestyle band, category cards) is
  visual polish only. It is **blocked on Higgsfield credits** (account is on the
  free plan with 0 credits; a generation attempt returned "Out of credits in the
  selected workspace"). It does **not** affect Merchant Center compliance.

---

## Bottom line

**Site-side readiness: complete** — every requirement controllable and verifiable
from the website is met. **Actual approval is Google's decision**, made after it
reviews the site and the submitted feed. Given the used-luxury category, odds are
reasonable but not guaranteed. If Google returns a specific rejection reason, it
is normally fixable and they state the cause.
