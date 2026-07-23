# BeepWear — Live Merchant Center Audit (beepwear.com)

**Audited property:** `beepwear.com` (live, rendered pages) + feed `data/products-mc-cleaned.csv`
**Category:** Independent reseller of pre-owned / vintage **luxury watches** — high-scrutiny
**Audit date:** 2026-07-23
**Method:** `gmc-audit` skill — automated scan + live page fetches of home, /about,
/contact, /authenticity-guarantee, /returns, /shipping-policy, /privacy-policy,
/terms, /shop, and a product page.
**Standard:** Google Merchant Center — Misrepresentation, Counterfeit, Editorial &
professional, Product-data specification (2026).

> **Verdict: essentially submit-ready pending feed cleanup + one identity check.**
> The store has been substantially remediated since the last audit — authenticity,
> policies, contact, and checkout now hold up. **Update (owner-confirmed): the founder
> "Charles Beep" is a real person**, so the earlier "fabricated founder" P0 is
> withdrawn. It is replaced by a lighter verification item: confirm that this real
> identity is presented *consistently* across the website, domain WHOIS, Merchant
> Center business info, and the payment processor. Clear the feed P1s (brand,
> condition), verify identity consistency, then submit. Approval is never guaranteed
> for luxury.

---

## What changed since the last audit (now compliant ✅)

| Area | Prior state | Live state now |
|------|-------------|----------------|
| Authenticity / sourcing | All `[confirm:]` placeholders | **Real:** "private collectors, estate sales, vetted trade suppliers"; explicit *"independent reseller… not an authorized dealer of, nor affiliated with, any brand"* |
| Returns policy | Blank "`** business days**`" (live) | **"5–10 business days"**, 30-day window, shipping terms clear |
| Shipping policy | Placeholder | **"$120 flat rate, tracked & insured"** (US); intl at checkout; 3–7 day estimate |
| Privacy policy | Placeholder | Complete; names **Google Analytics 4**, data collected, unsubscribe |
| Terms | Placeholder governing law | Complete; **South Dakota** governing law |
| Contact | Draft | Email + phone + address all published, no placeholders |
| Store / checkout | Products draft | **Live**, 269 products, Add-to-Cart present, prices match feed |

This is strong progress — most of the earlier misrepresentation surface is closed.

---

## Findings — severity-ranked (current live state)

| # | Severity | Finding | Policy | State |
|---|----------|---------|--------|-------|
| 1 | 🟡 **P2** | Founder **"Charles Beep"** (owner-confirmed real) — verify identity is consistent across site, WHOIS, Merchant Center & payment processor | Misrepresentation (identity consistency) | Verify |
| 2 | 🟠 **P1** | 47/269 feed products have **no brand** | Product data | Feed |
| 3 | 🟠 **P1** | **No `condition` attribute in the feed** (live pages show "Used", but the feed CSV omits it) | Product data / accuracy | Feed |
| 4 | 🟡 **P2** | **Thin, templated descriptions** ("rewards a closer look", "dive-ready build") repeated in form across products | Editorial / duplicate-content | LIVE + feed |
| 5 | 🟡 **P2** | **No GTIN/UPC** on any product | Product data quality | Feed |
| 6 | 🟡 **P2** | Luxury counterfeit scrutiny (Rolex-class inventory) — well-mitigated, but keep documentation | Counterfeit | Owner records |
| 7 | 🟢 **P3** | "Last updated" date **blank** on `/privacy-policy/` and `/terms/` | Editorial polish | LIVE |
| 8 | 🟢 **P3** | Contact page has a **"Social" heading with no links** | Editorial | LIVE |
| 9 | 🟢 **P3** | Confirm feed price/availability/condition match each live page at submit | Misrepresentation | Feed↔site |

---

## Detail & fixes

### 1 — 🟡 Founder "Charles Beep" — real; verify identity consistency
**Update:** The owner confirms **Charles Beep is a real person**. The earlier
"fabricated founder" finding is withdrawn — a named, real founder story is fine and
often *helps* trust. Because he's real, the de-personification in `content/about.md`
is optional; the original named story can stay (or be restored).
**What still matters:** Google cross-checks business identity across surfaces. A real
founder is only a risk if the identity is *inconsistent* or *unverifiable*. Reconcile
the signals that looked mismatched to an outside reviewer: the store admin email
(`tcoculick@gmail.com`) differs from both the founder name and the owner contact
(`hillkandil@gmail.com`).
**Verify (owner):** the same real legal identity appears on — (a) the website/About,
(b) domain WHOIS registrant, (c) Merchant Center business info + any business
registration, and (d) the payment processor / checkout descriptor. If those all
align, this finding closes. If any shows a different name/entity, reconcile it before
submitting — the mismatch, not the person, is what Google flags. — *Owner verification.*

### 2 — 🟠 47 products with no brand
**Fix:** Assign the true brand to each of the 47 flagged in `data/products-mc-audit.csv`; Merchant Center expects `brand` for watches. If genuinely unbranded, use the correct attribute rather than guessing. — *Owner action.*

### 3 — 🟠 No `condition` in the feed
**Evidence:** Live product pages show condition "Used" under Additional information, but the exported feed CSV has no condition column.
**Why:** Condition is a standard attribute; if the feed omits it (or defaults to `new` while pages say "Used"), that's a feed↔page mismatch = misrepresentation.
**Fix:** Map WooCommerce condition into the Merchant Center feed (`used` / `refurbished` / `new`), matching each product page exactly. — *Owner action (feed config).*

### 4 — 🟡 Thin, templated descriptions
**Evidence:** Sample product: *"Understated yet unmistakable… rewards a closer look… dive-ready build,"* with a boilerplate "checked against its reference before dispatch" line — low on real specs (case size, movement, water resistance).
**Why:** Descriptions are original (good — not copied manufacturer copy) but thin and formulaic; repeated phrasing across 269 products risks a low-quality/near-duplicate read.
**Fix:** Enrich the top-selling/high-value listings with real specifics (case size, movement, materials, reference, box/papers). If AI-assisted, place generated copy in the `structured_description` attribute. — *Owner action (incremental).*

### 5 — 🟡 No GTIN/UPC
**Fix:** Add real identifiers where they exist; set `identifier_exists = no` for the rest. **Never invent GTINs.** — *Owner action.*

### 6 — 🟡 Luxury counterfeit scrutiny (well-mitigated)
**Status:** Pricing is realistic (min $225 / median $6,800 / max $72,100 — no too-cheap-to-be-real flag), and the authenticity page now discloses independent-reseller status correctly. Residual risk is inherent to the category.
**Fix:** Retain per-unit sourcing/authentication documentation and be ready to produce it; expect possible manual review on Rolex-class references. — *Owner records.*

### 7–8 — 🟢 Minor polish
- Add a real "Last updated" date to `/privacy-policy/` and `/terms/`.
- Contact `/contact/`: either add real, active social links or remove the empty "Social" heading (don't fabricate profiles).

### 9 — 🟢 Feed↔page parity at submit
Spot-check confirmed parity (e.g., Aqua Master $400 feed = $400 page). Re-verify price, availability, and condition across the feed at submission time.

---

## Misrepresentation checklist — live status

| Google expectation | Status | Note |
|--------------------|--------|------|
| Complete, reachable contact info | ✅ | email + phone + address live |
| Accurate, consistent business identity | ⚠️ | Founder confirmed real; verify identity consistent across site/WHOIS/Merchant Center/payments (Finding 1) |
| Original, complete policy pages | ✅ | returns/shipping/privacy/terms all filled |
| Transparent authenticity/product claims | ✅ | independent-reseller disclosure is exemplary |
| Secure, trustworthy checkout | ✅ (verify) | HTTPS, live cart; confirm no checkout surprises |
| Genuine goods only / no counterfeit | ⚠️ | realistic pricing + disclosure; keep docs |
| Price & availability match feed | ✅ (verify at submit) | parity confirmed on samples |

---

## Owner action list (in order)

1. **Verify founder identity is consistent** — confirm "Charles Beep" (the real
   founder) matches the name/entity on domain WHOIS, Merchant Center business info,
   and the payment processor; reconcile the differing admin email. No `/about/` change
   needed since he's real. *(The de-personified `content/about.md` is optional — you
   can keep the named story.)*
2. **Assign brands** to the 47 unbranded feed products. *(Top feed blocker.)*
3. **Add `condition`** to the Merchant Center feed, matching product pages.
4. **Add GTINs** where real; `identifier_exists=no` otherwise.
5. **Enrich thin descriptions** on top listings (specs); use `structured_description` for AI copy.
6. Add "Last updated" dates; fix the empty Social heading.
7. Retain authenticity documentation for luxury inventory.
8. Re-run the pre-submission checklist, then connect Google for WooCommerce and request review **once**.

---

## Pre-submission checklist

- [x] No fabricated people/awards/partnerships/authorized-dealer claims. *(founder confirmed real)*
- [ ] Real identity consistent across site / WHOIS / Merchant Center / payment processor. ← **verify**
- [x] Authenticity/sourcing described in real, defensible terms.
- [x] Policy pages complete — no placeholders/blanks.
- [x] Contact email + phone + address visible and consistent.
- [ ] One legal identity across WHOIS, Merchant Center, checkout, policies (verify).
- [ ] Verified store domain claimed in Merchant Center (never a preview URL).
- [x] HTTPS; live purchasable checkout (verify no surprise fees).
- [ ] Every product: true brand, accurate condition, original description, real image, price = page = checkout. ← brand/condition/description gaps
- [ ] GTINs where real; identifier_exists=no otherwise.
- [ ] Images meet current minimum size; no overlays.
- [x] Reviews/badges reflect only real services (reviews correctly gated).
- [ ] (Luxury) authenticity documentation retained.

---

_Internal compliance audit — not legal advice or any guarantee of Merchant Center
approval. Google's review is discretionary and conservative for luxury goods._
