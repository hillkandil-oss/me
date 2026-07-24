# trenchsafety.org — Google Merchant Center Audit

**Audited property:** `https://trenchsafety.org` (live, WooCommerce 10.9.1 / Elementor / "Industrie" theme, Hostinger)
**What it sells:** heavy equipment — shipping containers, dump & utility trailers, **propane tanks**
**Operator:** same admin as BeepWear (`tcoculick@gmail.com`)
**Audit date:** 2026-07-23
**Method:** `gmc-audit` skill — live fetch of home, a product page, contact, and refund/returns.
**Standard:** Google Merchant Center — Misrepresentation, Editorial & professional, Product-data spec, Restricted/Dangerous products.

> **Verdict: DO NOT SUBMIT — this store would be suspended on sight.** It is a
> half-built WooCommerce shop sitting on top of an **unfinished theme demo**: every
> page shows placeholder insurance copy, a Bangladesh demo phone, a Massachusetts demo
> address, and a "Yellow Construction Company" name — while the domain says "trench
> safety" and the products are propane tanks and containers. Business identity, contact
> info, and pricing are all incoherent. This needs to be **finished and made coherent
> before Merchant Center is even a conversation.** It is currently indistinguishable
> from the deceptive-store pattern Google bans — even if the business is legitimate.

---

## Re-audit log

**2026-07-24 (re-audit #2):** Still not submit-ready; no P0 addressed. All demo strings
still present on all 8 pages. Only change: homepage SEO title improved to "Heavy Equipment,
Trailers & Storage Solutions | Trenchsafety" (cosmetic). Regression: the 5 propane tanks
sampled now show **no price** (incl. the 500-gallon that briefly showed $28k–$31k). Fixes
require a session with WordPress write-access to actually execute — repeat audits won't move
the state.

**2026-07-23 (re-audit #1):** No material change. A fresh sweep of 8 live pages (home,
about, contact, shop, refund_returns, shipping-policy, terms, privacy) shows **all**
theme-demo strings still present on every page (`+880` phone, Fall River MA address,
"Yellow Construction", `info@gmail.com`, "insurance needs", `industrie`, `vvv4+3g7`,
"coming soon"). Identity and contact are unchanged. **Partial progress on pricing only:**
some products now have prices (e.g. the 500-gallon ASME tank shows $28,000–$31,000), but
others still have none (1000-gallon and 250-gallon tanks checked = no price). **Verdict
unchanged: not submit-ready.** None of the P0 blockers have been addressed.

## The core problem, in one sentence

A domain named **trenchsafety.org** is selling **propane tanks, shipping containers and
trailers**, on a site still wearing a **construction/insurance theme demo** with **fake
placeholder contact details** — three unrelated identities at once, none verifiable.
Google's AI reviewer reads exactly these pages, and every signal it needs to approve a
store is either missing, fake, or contradictory.

---

## Findings — severity-ranked

| # | Severity | Finding | Policy |
|---|----------|---------|--------|
| 1 | 🔴 **P0** | **Unfinished theme-demo content on every page** — insurance placeholder copy, "Yellow Construction Company", demo `+880` (Bangladesh) phone, demo Fall River MA address, `info@gmail.com`, `support.industrie@gmail.com`, dozens of demo "Elements"/Services pages | Misrepresentation + Editorial |
| 2 | 🔴 **P0** | **Domain ↔ business mismatch** — "trenchsafety.org" sells propane tanks/containers/trailers, nothing to do with trench safety | Misrepresentation (identity) |
| 3 | 🔴 **P0** | **Contradictory business identities** — a construction firm (roofing/demolition/civil eng. services + team "Joshua Sendu") *and* a "heavy-equipment reseller" on the same site | Misrepresentation (identity) |
| 4 | 🔴 **P0** | **No genuine, consistent contact info** — `info@gmail.com` + a Bangladesh demo phone are not real; 5 different emails; two addresses incl. a Google **Plus Code** ("VVV4+3G7, Watertown SD") that isn't a verifiable street address | Misrepresentation (contact) |
| 5 | 🔴 **P0** | **Products have no price** — e.g. the 500-gallon ASME propane tank page shows no price; add-to-cart with no price | Product data / Misrepresentation |
| 6 | 🟠 **P1** | **"Coming soon" plugin active** + a public `/coming-soon` — under-construction signal | Editorial (landing page) |
| 7 | 🟠 **P1** | **Restricted/dangerous category** — propane tanks are pressurized fuel vessels; heavy equipment is a high-fraud-scrutiny category | Restricted/Dangerous products |
| 8 | 🟠 **P1** | **Policy pages sit inside the same demo shell** — returns/shipping/etc. exist but render under the placeholder header/footer; must be verified real & consistent | Misrepresentation (policies) |
| 9 | 🟡 **P2** | **Same operator as a second store** (BeepWear) — cross-account association risk if either is suspended | Account structure |
| 10 | 🟡 **P2** | **Dozens of theme demo pages public** ("Icon Box Elements", "Pricing Elements", service pages, etc.) — thin/irrelevant/duplicate content | Editorial / quality |

---

## Detail & fixes

### 1 — 🔴 Unfinished theme-demo content site-wide (the big one)
**Evidence (present on home, product, contact, and returns pages — it's in the header/footer):**
- *"When we go to the office every day… personally meeting their **insurance needs**."*
- *"Welcome To **Yellow Construction Company**."*
- Phone *"(+880)155-69566"* — **+880 is Bangladesh**, the theme's demo number.
- Address *"374 William S Canning Blvd, **Fall River MA** Road 2721, USA"* — theme demo.
- Emails `info@gmail.com` and `support.industrie@gmail.com` (**"Industrie" is the theme name** — leftover demo).
**Why:** A reviewer (human or AI) reading placeholder copy, a foreign demo phone, and a demo brand name concludes the store is unfinished and untrustworthy — a direct misrepresentation + editorial failure. This alone is an instant suspension.
**Fix:** Replace **all** theme demo content with the real business's header, footer, menu, address, phone, and email. Delete the "Industrie/Yellow Construction" demo pages. Nothing placeholder may remain on any public page.

### 2 — 🔴 Domain ↔ business mismatch
**Evidence:** Domain `trenchsafety.org`; catalog = propane tanks, shipping containers, dump/utility trailers.
**Why:** Google checks that the store's identity is coherent. A safety-themed domain selling fuel tanks reads as a repurposed/deceptive domain.
**Fix:** Align the two — either sell under a domain that matches the business (e.g. an equipment/containers name) or, if "trenchsafety" is the intended brand, make the site clearly and consistently explain that brand and what it sells. The name and the goods must tell one story.

### 3 — 🔴 Contradictory identities
**Evidence:** Nav includes construction **Services** (Project Management, Civil Engineering, Demolition, General Contracting, Roofing, Pre-construction), a **Team** page ("Joshua Sendu"), and **Pricing Plans** — alongside a WooCommerce **Shop** of equipment. Hero copy calls it a "trusted reseller."
**Why:** Two different businesses (a contractor vs. an equipment reseller) on one site is exactly the incoherence misrepresentation targets.
**Fix:** Pick one business model. If it's an equipment store, remove the construction-services/team/pricing-plan demo sections entirely.

### 4 — 🔴 No genuine, consistent contact info
**Evidence:** Emails seen: `info@gmail.com`, `info@trenchsafety.com` (.com ≠ site .org), `info@trenchsafety.org`, `support.industrie@gmail.com`, `tcoculick@gmail.com`. Addresses: demo Fall River MA **and** "VVV4+3G7, Watertown, SD 57201" (a **Plus Code**, not a street address). Phones: `(+880)155-69566` (demo) and `+1 605-356-2237`.
**Why:** Merchant Center requires complete, genuine, consistent contact info. `info@gmail.com` and a Bangladesh number fail on their face; a Plus Code isn't a verifiable address.
**Fix:** One real business email on the site's own domain, one real monitored phone, one real street address — identical everywhere (site, policies, Merchant Center, payment processor).

### 5 — 🔴 Products have no price
**Evidence:** `/product/500-gallon-above-below-ground-steel-asme-propane-tank/` renders add-to-cart but **no price**; homepage showed only a single `$600` anywhere.
**Why:** Every product needs an accurate price that matches the feed and checkout. Missing prices = disapproval and a misrepresentation/trust flag.
**Fix:** Set a real price on every product; ensure feed price = landing-page price = checkout price.

### 6 — 🟠 "Coming soon" mode active
**Evidence:** `ultimate-coming-soon` plugin loaded; a `/coming-soon` page exists.
**Fix:** Confirm the storefront isn't behind a coming-soon wall for any region/crawler; remove it before submitting. Under-construction stores are disapproved.

### 7 — 🟠 Restricted / dangerous-goods category
**Evidence:** Propane tanks (pressurized LPG vessels).
**Why:** Pressurized-fuel equipment can fall under dangerous/restricted-products rules and shipping restrictions; high-value equipment stores draw fraud scrutiny.
**Fix:** Confirm these items are eligible to advertise, disclose shipping/handling constraints honestly, and expect manual review.

### 8 — 🟠 Verify the real policy pages
**Evidence:** `/shipping-policy`, `/refund_returns`, `/product-condition`, `/sales-tax-policy`, `/payment-policy`, `/terms-and-condition`, `/privacy-policy-2` all exist — good — but render inside the demo shell.
**Fix:** Read each; ensure it's real, original, specific (return window/fees, shipping costs/lead times for freight items), and consistent with product pages and the feed.

### 9–10 — 🟡 Account association & demo pages
- The shared admin (`tcoculick@gmail.com`) links this to BeepWear; a suspension on one can taint the other. Keep each store independently compliant.
- Delete all theme demo "Elements" and service pages — thin, irrelevant, duplicate content that drags quality down.

---

## Misrepresentation checklist — trenchsafety.org status

| Google expectation | Status |
|--------------------|--------|
| Complete, reachable, genuine contact info | ❌ fake/placeholder + inconsistent |
| Accurate, consistent business identity | ❌ three identities, demo brand |
| Domain/brand matches what's sold | ❌ trench-safety domain, propane/containers |
| Original, complete, placeholder-free pages | ❌ theme demo copy site-wide |
| Every product purchasable at a stated price | ❌ products missing prices |
| Not under construction | ⚠️ coming-soon plugin active |
| Genuine goods / eligible category | ⚠️ propane = restricted/dangerous review |

**Score: 0 of the core pillars pass.** This is not a tune-up; the store must be finished.

---

## Owner action list (in order — this is a rebuild, not a polish)

1. **Strip every trace of the theme demo** — insurance copy, "Yellow Construction",
   `+880` phone, Fall River MA address, `info@gmail.com`, `support.industrie@gmail.com`,
   all demo "Elements"/Services/Team/Pricing pages.
2. **Decide one business identity** and make the whole site tell that one story;
   reconcile the domain with what's actually sold.
3. **Put real, consistent contact info** (own-domain email, one real phone, one real
   street address) everywhere.
4. **Price every product**; verify each product page is complete and purchasable.
5. **Disable coming-soon**; confirm no page is under construction.
6. **Verify all policy pages** are real, specific, and consistent (esp. freight
   shipping + returns for large equipment).
7. **Confirm propane/dangerous-goods eligibility** and shipping disclosures.
8. Only after all of the above: connect Merchant Center on the verified domain and
   request review **once**. Approval is not guaranteed.

---

## Straight talk

I'm not accusing anyone of bad intent — but you asked for a real audit, so here it is
plainly: **right now this site looks exactly like the kind of store Google auto-bans.**
A `.org` named for trench safety, selling propane tanks and containers, with a Bangladesh
demo phone and an `info@gmail.com`, half-dressed in a construction-company theme demo —
that pattern is indistinguishable from a throwaway scam store, whether or not the business
behind it is legitimate. The good news: every item above is fixable, and the fixes are the
same things that make it a *real* store customers trust. Finish the store first; submit second.

_Internal compliance audit — not legal advice or any guarantee of Merchant Center approval._
