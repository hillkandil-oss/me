# bwcontainers.com — Google Merchant Center Audit (Australia)

**Audited property:** `https://bwcontainers.com` (live)
**Platform:** WordPress + WooCommerce + Elementor (same owner as beepwear/trenchsafety/anhängerplus — `hillkandil@gmail.com`)
**What it sells:** new & used **shipping containers** (10ft/20ft, reefers, flat racks, open-tops) — AUD $1,420–$4,200
**Market:** Australia (AU)
**Audit date:** 2026-07-26
**Method:** `gmc-audit` skill — live fetch of home, 6 products, contact, about, and policy pages.

> **Verdict: the closest-to-ready of the group — a short punch-list, not a rebuild.**
> Unlike trenchsafety.org, this store is coherent: the brand, domain and products all agree,
> **every product is priced**, the contact email is on the own domain, and the policy pages
> exist. The remaining issues are a handful of P1/P2 fixes: a **Plus-Code “address”**, a
> **personal Gmail** exposed on the front end, a **placeholder site title**, and a **missing
> ABN**. Clear those, verify GST-inclusive pricing, and it’s in good shape to submit.

---

## What's already right (most of it)

- ✅ **Coherent identity** — “BWContainers … quality new and used shipping containers for customers across Australia.” Brand = domain = products.
- ✅ **Every product is priced** (6/6 sampled: AUD $1,420–$4,200 — realistic for containers).
- ✅ **Own-domain email** (info@bwcontainers.com) + an Australian phone (+61 489 99 5663).
- ✅ **Policy pages present** — shipping, return & refund, warranty, payment, terms, privacy.
- ✅ **No theme-demo leftovers** — none of the placeholder/demo junk seen on the other sites.
- ✅ **Blog + product titles are on-topic and in English** (correct for the AU market).

---

## Findings — severity-ranked

| # | Severity | Finding | Policy |
|---|----------|---------|--------|
| 1 | 🟠 **P1** | **Address is a Google Plus Code** — “5RVJ+3J2 Sunshine West, Victoria, Australia” on the Contact page; not a verifiable street address | Misrepresentation (contact) |
| 2 | 🟠 **P1** | **Personal Gmail exposed** — `hillkandil@gmail.com` on the homepage and as the WordPress author (`/author/hillkandilgmail-com`) | Misrepresentation (identity) |
| 3 | 🟠 **P1** | **Placeholder site title** “bwcontainers.com” on every page; no meta descriptions | Editorial / professional |
| 4 | 🟡 **P2** | **No ABN shown** — Australian businesses are expected to display an ABN; also needed for GST/trust | AU trust / tax transparency |
| 5 | 🟡 **P2** | **Verify GST-inclusive pricing** — Australian Consumer Law requires the single total price incl. GST to be displayed; confirm feed/page prices are GST-inclusive and shipping is clear | Misrepresentation (price) |
| 6 | 🟡 **P2** | **Verify the “24/7 Support” claim** is real (homepage badge) — remove or soften if not literally true | Misrepresentation (claims) |
| 7 | 🟢 **P3** | No GTIN (expected for containers — set identifier-exists = no; never invent) | Product data |

---

## Detail & fixes

### 1 — 🟠 Plus-Code “address”
**Evidence:** Contact page shows *“Address 5RVJ+3J2 Sunshine West, Victoria, Australia.”*
**Why:** A Plus Code isn’t a verifiable street address; Merchant Center wants a genuine business address, and it should be consistent with the ABN/registration.
**Fix:** Replace with the real street address (street + number, suburb, state, postcode). If it’s a home-run business without a public premises, use the registered business address or a genuine contact address. *(Owner must supply the real address — do not invent.)*

### 2 — 🟠 Personal Gmail on the front end
**Evidence:** `hillkandil@gmail.com` appears on the homepage and the author archive `/author/hillkandilgmail-com`.
**Why:** Mixing a personal Gmail into a business storefront undercuts the business identity and looks unfinished. The business already has info@bwcontainers.com.
**Fix:** Remove the Gmail from the front end; change the WordPress author display name/slug so the archive no longer exposes the personal email; use the business email everywhere.

### 3 — 🟠 Placeholder title + missing meta
**Evidence:** Every page `<title>` is “bwcontainers.com”; no meta description.
**Fix:** Set a real title (e.g. “BWContainers — Shipping Containers Australia-Wide”) and meta descriptions in the SEO plugin.

### 4 — 🟡 No ABN
**Fix:** Display the ABN in the footer / Contact / Terms (standard for AU e-commerce and required context for GST). *(Owner supplies the real ABN.)*

### 5 — 🟡 GST-inclusive pricing
**Fix:** Confirm displayed prices include GST (single total price rule under Australian Consumer Law) and that shipping/delivery costs are clear; ensure the Merchant Center feed matches.

### 6 — 🟡 “24/7 Support” claim
**Fix:** Only keep it if literally true; otherwise state real support hours.

---

## Merchant Center checklist — status

| Requirement | Status |
|-------------|--------|
| Coherent business identity (brand/domain/products) | ✅ |
| Complete contact info | ⚠️ email/phone ok; **address is a Plus Code**, no ABN |
| No personal/placeholder identity leaks | ❌ personal Gmail + placeholder title |
| Original, complete policy pages | ✅ present (spot-check wording) |
| Every product priced, matching feed/checkout | ✅ (verify GST-inclusive) |
| HTTPS / purchasable | ✅ (verify checkout) |
| Genuine claims (support, delivery) | ⚠️ verify “24/7”, delivery promises |

---

## Owner action list (short)

1. **Replace the Plus-Code address** with a real street/registered address (site + Merchant Center + payment processor consistent).
2. **Remove the personal Gmail** from the homepage and the author archive; use info@bwcontainers.com only.
3. **Set a real site title + meta descriptions.**
4. **Add the ABN**; confirm **GST-inclusive** pricing and clear delivery costs.
5. Verify the “24/7 Support” claim (keep only if true).
6. Then connect Merchant Center on the verified domain and request review. Approval not guaranteed, but this store is close.

---

## Straight talk

This is the best of the four stores on the same stack — it’s coherent, priced, and mostly
complete. The fixes here are genuinely minor (address, personal-email leak, title, ABN),
not a rebuild. Get the real street address and ABN from the owner, remove the Gmail, set a
proper title, and bwcontainers.com is a realistic Merchant Center candidate.

_Internal compliance audit — not legal/tax advice. Confirm ABN/GST handling with an
Australian accountant; Google’s review is discretionary._
