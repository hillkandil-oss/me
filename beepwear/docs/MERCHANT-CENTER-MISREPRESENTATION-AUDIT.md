# BeepWear — Google Merchant Center Audit Board Report

**Audited property:** `beepwear.com` (live) + repository content in `beepwear/content/` and `beepwear/data/`
**Business type:** Online reseller of pre-owned / vintage **luxury watches** (Rolex ×103, Omega, Tudor, TAG Heuer, Zenith, Ulysse Nardin, Tiffany & Co., etc.)
**Audit date:** 2026-07-23
**Standard applied:** Google Merchant Center program policies — Misrepresentation, Counterfeit goods, and Editorial/Professional requirements (2026 enforcement).

> **Board verdict: NOT SUBMIT-READY.** One live fabrication and an undefined authenticity/sourcing model are both direct misrepresentation triggers, and a luxury-watch reseller draws the strictest counterfeit review in Merchant Center. Clear the P0/P1 items below **before** connecting the feed. You get ~3 review attempts after a suspension — do not spend one on a site that still has known defects.

---

## How Google enforces this (why each finding matters)

- **Misrepresentation is a "no-warning" suspension.** Unlike most issues, Google can suspend the whole account immediately, with no grace period, and support will not tell you what to fix — the burden of proof is entirely on the merchant. ([Google Misrepresentation policy](https://support.google.com/merchants/answer/6150127), [StubGroup 2026](https://stubgroup.com/blog/fix-your-google-merchant-center-misrepresentation-suspension/))
- **Google checks four things for identity/trust:** complete & reachable contact info, original & complete policies, a consistent business identity, and a checkout that doesn't raise trust questions. ([Feedonomics](https://feedonomics.com/blog/resolving-a-google-merchant-center-account-suspension-misrepresentation-of-self-or-product/))
- **Counterfeit is zero-tolerance and often permanent.** Luxury watches receive disproportionate enforcement because they are the most-counterfeited category. Only sellers who can substantiate that goods are genuine survive review; a "counterfeit" label can even be applied to genuine goods that lack documentation. ([Google Counterfeit policy](https://support.google.com/merchants/answer/6149993), [Luxury GMC guide](https://gmccheck.com/industries/luxury-goods-gmc))

---

## Findings — severity-ranked

| # | Severity | Finding | Policy | State |
|---|----------|---------|--------|-------|
| 1 | 🔴 **P0 — Blocker** | Fabricated founder persona "Charles Beep" on the live `/about/` page | Misrepresentation (false business identity) | **LIVE** |
| 2 | 🔴 **P0 — Blocker** | Authenticity / sourcing model is undefined — the one page a luxury reseller is judged on is entirely `[confirm: …]` placeholder | Misrepresentation + Counterfeit | Draft; **must exist & be true before submit** |
| 3 | 🔴 **P0 — Blocker** | No retained authenticity/sourcing documentation for heavily-scrutinised brands (Rolex ×103, Omega, etc.) as a **non-authorized** reseller | Counterfeit goods | Owner records |
| 4 | 🟠 **P1 — High** | Unfilled `[confirm: …]` placeholders in published policy copy (confirmed live: returns page shows "within `** business days**`") | Misrepresentation (incomplete/unclear terms) | ≥1 **LIVE**, 25 total in repo |
| 5 | 🟠 **P1 — High** | 47 of 269 products have **no brand** assigned | Product data / Misrepresentation | Feed |
| 6 | 🟡 **P2 — Medium** | No GTIN/UPC/EAN on any product | Product data quality | Feed |
| 7 | 🟡 **P2 — Medium** | Descriptions "unique in file" ≠ "original" — spot-check for copied manufacturer copy | Misrepresentation / copyright | Feed |
| 8 | 🟡 **P2 — Medium** | Business-identity consistency: `/about/` (Charles Beep) vs. admin `tcoculick@gmail.com` vs. images sourced from `citysvending.com`; verify one coherent legal entity everywhere (WHOIS, Merchant Center, checkout, policies) | Misrepresentation | Cross-property |
| 9 | 🟢 **P3 — Verify** | Feed price/availability must match live product pages **exactly** at submission time | Misrepresentation (price/availability mismatch) | Feed↔site |
| 10 | 🟢 **P3 — Verify** | Reviews/testimonials, trust badges, and "free worldwide shipping" claims must reflect real, operational services only | Misrepresentation | Homepage |

---

## Detailed findings & required corrections

### 1 — 🔴 Fabricated founder "Charles Beep" (LIVE)
**Evidence:** `/about/` states *"BeepWear was founded in 2023 by **Charles Beep**, a longtime watch collector…"* No such named individual is substantiated; the name mirrors the brand ("BeepWear" → "Beep"), and the account is administered by `tcoculick@gmail.com`.
**Why it's a takedown risk:** Inventing a named founder with a fabricated biography is a textbook **false business identity** — one of the exact things Google's identity check targets. It also contradicts the site's own stated value ("no fabricated claims").
**Correction (safe, applied in repo):** `content/about.md` rewritten to remove the invented person and tell the brand's story truthfully without a fictional individual. **Owner action:** either (a) publish the de-personified version, or (b) replace with the *real* founder's actual name and true history. **Do not invent a person.** Then update the live `/about/` page to match.

### 2 — 🔴 Undefined authenticity / sourcing model
**Evidence:** `content/authenticity.md` — sourcing, inspection, and verification are all `[confirm: …]` placeholders. The About page points buyers to an "Authenticity Guarantee" that has no real content behind it.
**Why:** For a luxury reseller this is *the* page Google (and buyers) scrutinise. A guarantee that promises authenticity without describing how it is achieved is an unsubstantiated claim; publishing it with brackets visible is worse.
**Correction:** The owner must state the **real** sourcing model in plain language — e.g. "sourced from verified private sellers and estate collections; we are an independent reseller and **not** an authorized dealer of any brand," plus the **actual** inspection steps performed. Never imply authorized-dealer status unless a signed agreement exists. Draft scaffolding with truthful defaults is provided in `content/authenticity.md`; fill each `[confirm:]` with a fact you can defend.

### 3 — 🔴 Authenticity documentation for scrutinised brands
**Evidence:** Feed carries Rolex ×103, Omega, Tudor, Ulysse Nardin, Zenith, TAG Heuer as an independent reseller. Pricing is *realistic* for genuine pre-owned (median **$6,800**, min **$225**, max **$72,100**; only 2 luxury items under $1,500) — which is **good** (no "too-cheap-to-be-real" flag), but does not remove counterfeit scrutiny.
**Why:** Counterfeit enforcement is zero-tolerance and can be permanent; genuine goods still get flagged without documentation.
**Correction (owner):** Retain, per unit where possible, proof of legitimate sourcing (purchase invoices, serial/reference records, authentication/service receipts, provenance). Be ready to produce it on review. Consider third-party authentication for the highest-value references. Keep prices explainable (condition, year, box/papers status).

### 4 — 🟠 Unfilled `[confirm: …]` placeholders in policies
**Evidence (live-confirmed):** `/returns/` renders *"refunded within `** business days**`"* — a visible blank. Repo contains **25** `[confirm:]` markers across payment, shipping, warranty, privacy, cookies, accessibility, returns, terms, contact, authenticity, and FAQ.
**Why:** Incomplete or vague terms fail the "original and complete policies" check and read as an unfinished/untrustworthy store.
**Correction (owner):** Resolve every marker with a real value before publish. Full list in the appendix below. At minimum fix the live returns page immediately (state the real refund-processing window, e.g. 5–10 business days).

### 5 — 🟠 47 products with no brand
**Evidence:** `data/products-mc-cleaned.csv` — 222/269 branded, 47 blank (per prior CSV audit). Merchant Center expects `brand` for watches.
**Correction:** Assign the true brand to each of the 47 (flagged in `data/products-mc-audit.csv`). If a watch is genuinely unbranded/generic, set the appropriate attribute rather than guessing a marque.

### 6 — 🟡 No GTIN/UPC/EAN
**Correction:** Add real identifiers where they exist; for items with none, set `identifierExists = no`. **Never invent identifiers** — fabricated GTINs are themselves a violation.

### 7 — 🟡 Description originality
**Correction:** Spot-check the 269 kept descriptions for verbatim manufacturer/marketplace copy. "Unique within this file" is not the same as "original." Rewrite any lifted text; ensure specs are accurate to the actual item.

### 8 — 🟡 Business-identity consistency
**Correction:** Verify a single coherent legal entity across: WHOIS/domain registrant, Merchant Center business info, checkout/receipt name, policy pages, and the physical address (510 Main St, Wall, SD 57790). The domain should be a verified, claimed store URL in Merchant Center (never a preview/staging URL). Confirm phone `+1 605-361-9867` and `info@beepwear.com` are monitored and appear consistently.

### 9 — 🟢 Feed ↔ site parity
**Correction:** At submission, price, currency (USD), and availability in the feed must match each live product page exactly. Draft products won't serve — publish the products first. Mismatches are a common auto-suspension trigger.

### 10 — 🟢 Truthful marketing claims
**Correction:** Only show reviews that are real and verifiable (the homepage copy already gates this correctly — keep it gated until real reviews exist). "Free worldwide shipping," "secure checkout," and trust badges must each reflect a service actually provided. Remove any that aren't live.

---

## Google Misrepresentation checklist — BeepWear status

| Google expectation | Status | Note |
|--------------------|--------|------|
| Complete, reachable contact info (email, phone, address) | ✅ Pass | Present on `/contact/`; verify all monitored |
| Accurate business identity, consistently presented | ❌ **Fail** | Fabricated founder (Finding 1); verify entity (Finding 8) |
| Original, complete policy pages (returns, shipping, privacy, terms) | ⚠️ Partial | Live placeholder(s) + 25 `[confirm:]` markers (Finding 4) |
| Transparent authenticity/product claims | ❌ **Fail** | Authenticity page undefined (Finding 2) |
| Secure, trustworthy checkout (SSL, clear billing) | ⚠️ Verify | Confirm HTTPS end-to-end + clear charge descriptor |
| Genuine goods only / no counterfeit | ⚠️ High-risk | Documentation required (Finding 3) |
| Price & availability match the feed | ⚠️ Verify at submit | Finding 9 |

---

## Owner action list (in order)

1. **Fix the live `/about/` page** — remove "Charles Beep" (use the corrected `about.md`, or the real founder's true details).
2. **Write a truthful Authenticity page** — real sourcing model + real inspection steps; state clearly you are an independent reseller, not an authorized dealer.
3. **Resolve all 25 `[confirm:]` markers** with real values; fix the live returns-page blank first.
4. **Assemble authenticity documentation** for luxury inventory; be ready to submit on review.
5. **Assign brands** to the 47 unbranded products; add real GTINs or set `identifierExists=no`.
6. **Spot-check descriptions** for copied copy; rewrite as needed.
7. **Publish products & policy pages**, verify feed↔page parity, confirm one consistent legal identity + verified domain.
8. **Only then** connect Google for WooCommerce and request review. Approval is never guaranteed; luxury brands may still get manual review.

---

## Reusable audit checklist (run before every Merchant Center submission or re-review)

- [ ] No fabricated people, awards, partnerships, or "authorized dealer" claims anywhere.
- [ ] Authenticity/sourcing page describes only real, defensible operations.
- [ ] Every policy page complete — zero brackets/blanks/TBD, real numbers for windows & fees.
- [ ] Contact email + phone + address present, consistent, and monitored.
- [ ] One legal identity across WHOIS, Merchant Center, checkout, and policies.
- [ ] Verified store domain claimed (never a preview/staging URL).
- [ ] HTTPS everywhere; clear billing/charge descriptor.
- [ ] Every product: true brand, accurate title/spec, original description, real image of the item.
- [ ] GTINs where real; `identifierExists=no` otherwise (never invented).
- [ ] Feed price/currency/availability match each live page exactly.
- [ ] Reviews/testimonials/badges reflect only real, operational services.
- [ ] Authenticity documentation retained and retrievable for scrutinised brands.

---

### Sources
- [Google — Misrepresentation policy](https://support.google.com/merchants/answer/6150127)
- [Google — Counterfeit goods policy](https://support.google.com/merchants/answer/6149993)
- [StubGroup — Fix GMC Misrepresentation Suspension (2026)](https://stubgroup.com/blog/fix-your-google-merchant-center-misrepresentation-suspension/)
- [Feedonomics — Resolving a GMC suspension (misrepresentation of self or product)](https://feedonomics.com/blog/resolving-a-google-merchant-center-account-suspension-misrepresentation-of-self-or-product/)
- [GMC Checker — Luxury Goods compliance guide (2026)](https://gmccheck.com/industries/luxury-goods-gmc)
- [KeyCommerce — Fix GMC Misrepresentation Suspension (2026)](https://keycommerce.com/fix-google-merchant-center-misrepresentation-suspension/)

> This report is an internal compliance audit, not legal advice or any guarantee of Merchant Center approval. Google's reviews are discretionary.
