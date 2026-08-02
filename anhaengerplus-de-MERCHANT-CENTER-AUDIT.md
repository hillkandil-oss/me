# anhängerplus.de — Google Merchant Center Audit (Germany)

**Audited property:** `https://xn--anhngerplus-n8a.de` (= **anhängerplus.de**), live
**Platform:** WordPress + WooCommerce + Elementor (same stack/owner as beepwear & trenchsafety — admin `hillkandil@gmail.com`)
**What it sells:** used **excavators / mini-diggers** (JCB, Komatsu, Caterpillar) €9,200–€160,000; blog about shipping containers
**Market:** Germany (DE) — German legal rules apply on top of Merchant Center policy
**Audit date:** 2026-07-25
**Method:** `gmc-audit` skill — live fetch of home, a product, contact, about, and the policy pages.

> **RE-AUDIT 2026-07-26 — now essentially submit-ready.** All P0/P1 fixes landed:
> **Impressum** is live and complete (§5 DDG: "Slooterberk Billian AnhängerPlus,
> Reiherstieg-Hauptdeich 806, 21107 Hamburg", Inhaber named, phone/email, USt-IdNr
> present — full street number, no placeholders); **Widerrufsbelehrung** published +
> linked; real German site **title**; **French product terms removed** (godets/
> reconditionné/tondeuse gone from content); **personal Gmail removed** (author
> archive now 404); **prices real** (€12,500–€25,000). Remaining minor: no homepage
> meta description; one permalink slug still contains "3-godets" (cosmetic). This is
> the fully-remediated store of the group. Original findings below for the record.
>
> **Original verdict: NOT submit-ready — and currently not legally compliant for a German shop.**
> Two things are hard blockers in Germany specifically: there is **no Impressum** (legally
> mandatory) and **no Widerrufsbelehrung** (mandatory 14-day right of withdrawal). On top of
> that, the brand/domain (“AnhängerPlus” = *trailers*) doesn’t match the products (excavators),
> and the product titles are in **French** on a German site. Fix the legal pages and the
> identity/language coherence before Merchant Center.

---

## What's actually OK (so you know it's not all bad)

- **Products have real, plausible prices** (€9,200–€160,000 is realistic for used machinery) — no “too cheap to be real” flag.
- **Contact** has a German mobile (+49 152 380 8 2927), an **own-domain email** (info@anhängerplus.de), and a Hamburg address.
- **Policy pages are written in German** with real content (the Terms page has genuine AGB text: “Allgemeine Geschäftsbedingungen (AGB) … Willkommen bei AnhängerPlus”).

---

## Findings — severity-ranked

| # | Severity | Finding | Policy / Law |
|---|----------|---------|--------------|
| 1 | 🔴 **P0** | **No Impressum** — `/impressum`, `/imprint`, `/legal-notice` all 404; no Impressum link anywhere | §5 DDG (ex-TMG) — legally mandatory in DE; GMC hard requirement |
| 2 | 🔴 **P0** | **No Widerrufsbelehrung / 14-day right of withdrawal** — not present on any policy page (no “Widerruf”, no “14 Tage”) | EU/DE consumer distance-selling law; Misrepresentation |
| 3 | 🔴 **P0** | **Brand/domain ↔ product mismatch** — “AnhängerPlus” (trailers) sells **excavators** (JCB/Komatsu/Cat); blog is about shipping containers | Misrepresentation (identity) |
| 4 | 🔴 **P0** | **Language incoherence** — German site chrome, but **French product titles** (“3 GODETS”, “tondeuse à gazon”, “reconditionné”) and English page slugs | Misrepresentation / Editorial |
| 5 | 🟠 **P1** | **Placeholder site title** “anhngerplus.de” on every page (raw domain, umlaut broken); no meta descriptions | Editorial / professional |
| 6 | 🟠 **P1** | **Personal Gmail exposed** — `hillkandil@gmail.com` as the WordPress author (`/author/hillkandilgmail-com`) and on the homepage | Misrepresentation (identity) |
| 7 | 🟠 **P1** | **Incomplete Impressum data** — address “Reiherstieg-Hauptdeich, 21107 Hamburg” has no house number; no operator legal name / legal form / VAT-ID (USt-IdNr.) shown | §5 DDG |
| 8 | 🟡 **P2** | **High-value machinery** (€9k–€160k, branded used JCB/Komatsu/Cat) — fraud-scrutiny category; likely B2B | Counterfeit/legitimacy + channel fit |
| 9 | 🟡 **P2** | No GTIN (expected for used machinery — set identifier-exists = no; never invent) | Product data |

---

## Detail & fixes

### 1 — 🔴 No Impressum (German legal must-have)
**Evidence:** `/impressum` → 404; the word “Impressum” appears nowhere on the homepage (footer has Datenschutz/Versand/Zahlung but no Impressum/AGB/Widerruf links).
**Why:** German law (§5 DDG) requires every commercial site to have a reachable, complete Impressum. Its absence is a legal violation **and** a standard Google Merchant Center DE rejection reason.
**Fix:** Publish a proper `/impressum` with: operator’s full legal name (and legal form, e.g. Einzelunternehmen/GmbH), full street address **with house number**, email, phone, and — if applicable — VAT-ID (USt-IdNr.) and register entry. Link it in the footer on every page. *(Owner must provide the real legal details — do not invent them.)*

### 2 — 🔴 No Widerrufsbelehrung (right of withdrawal)
**Evidence:** None of `/refund-and-return-policy`, `/terms-and-conditions`, `/privacy-policy-2` mention “Widerruf” or a 14-day period.
**Why:** For consumer (B2C) distance sales in Germany/EU, a Widerrufsbelehrung with the statutory 14-day withdrawal right and a Muster-Widerrufsformular is mandatory. Missing it is a consumer-law violation and a trust failure Google flags.
**Fix:** Add a compliant Widerrufsbelehrung (14 days, conditions, model withdrawal form), linked in the footer. If sales are strictly B2B, state that clearly — but the current storefront reads as open B2C.

### 3 — 🔴 Brand/domain ↔ product mismatch
**Evidence:** Domain/brand “AnhängerPlus” = *trailers*; catalog = **excavators** (Komatsu PC-26, JCB 8025 ZTS, Caterpillar 305C); blog posts about **shipping containers / container houses**.
**Why:** Google checks that the store presents one coherent business. A trailer-named brand selling excavators with a container blog reads as a repurposed/incoherent store.
**Fix:** Align the brand, domain and catalog to one story. If the real business sells excavators, the brand/domain and homepage must say so; if it sells trailers, the catalog must match.

### 4 — 🔴 Language incoherence (French product titles on a German shop)
**Evidence:** Product titles like “KOMATSU PC 26 MR-3, 2,8T + **3 GODETS**”, “**tondeuse à gazon** … **reconditionné**” — French — while the site chrome is German and slugs are English.
**Why:** French product names on a German storefront signal a copied/non-localized (likely scraped or dropshipped) catalog — a quality and misrepresentation concern; German shoppers can’t understand the titles.
**Fix:** Translate all product titles/descriptions into proper German (Bagger, Löffel/Schaufel instead of “godets”, gebraucht/generalüberholt instead of “reconditionné”). Ensure specs are accurate to each machine.

### 5–7 — 🟠 Professionalism & identity
- **Title:** every page title is “… – anhngerplus.de” (raw, umlaut-broken). Set a real store title (“AnhängerPlus – …”) + meta descriptions in AIOSEO/Rank Math.
- **Personal Gmail:** remove `hillkandil@gmail.com` from the public author archive (change the author display name / posting user) and anywhere on the front end; use the business email only.
- **Impressum data completeness:** add the house number and the legally required operator details (see Finding 1).

### 8–9 — 🟡 Category & data
- Heavy machinery is high-value and fraud-scrutinised; be ready to evidence legitimate sourcing/ownership of the machines, and consider whether Shopping (vs. lead-gen) fits B2B equipment.
- Used machinery has no GTIN — set identifier-exists = no; never invent identifiers.

---

## German Merchant Center checklist — status

| Requirement | Status |
|-------------|--------|
| Impressum (complete, linked) | ❌ missing |
| Widerrufsbelehrung (14-day) | ❌ missing |
| Datenschutzerklärung | ✅ present (German) |
| AGB / Terms | ✅ present (German) |
| Versand / Zahlung policies | ✅ present |
| Coherent brand/domain ↔ products | ❌ trailer brand, excavator catalog |
| Product titles in the site’s language | ❌ French titles |
| Genuine, complete contact incl. real address | ⚠️ email/phone ok; address needs house number + operator details |
| Prices shown (incl. VAT/shipping clarity) | ⚠️ prices present; verify VAT + shipping display (Preisangabenverordnung) |
| Real store title / meta | ❌ placeholder “anhngerplus.de” |

---

## Owner action list (in order)

1. **Publish a complete Impressum** (real legal name, full address incl. house number, contact, VAT-ID if applicable); link in the footer.
2. **Add a Widerrufsbelehrung** (14-day right + model withdrawal form), linked in the footer — or clearly declare B2B-only.
3. **Make the identity coherent** — brand/domain/homepage must match what’s actually sold (excavators?), and fix the container-blog mismatch.
4. **Translate all product titles/descriptions to German** (remove French “godets/reconditionné/tondeuse”).
5. **Set a real site title + meta descriptions**; remove the personal Gmail from the public author archive.
6. Confirm **VAT + shipping** are shown per Preisangabenverordnung; be ready to evidence machine sourcing.
7. Re-run the checks, then connect Merchant Center on the verified domain and request review once. Approval not guaranteed (high-value machinery gets manual review).

---

## Straight talk

This is the third store on the same stack and owner, and it shows the same pattern as
trenchsafety.org: a half-finished WooCommerce/Elementor site where the brand, the domain, the
catalogue and the language don’t agree, and the mandatory pages aren’t all there. Here the
stakes are higher because it targets **Germany**, where a missing **Impressum** and
**Widerrufsbelehrung** aren’t just Google problems — they’re legal ones. The good news: prices
and German policy text already exist, so this is closer than trenchsafety. Fix the two legal
pages and the identity/language coherence and it becomes a genuinely submittable store.

_Internal compliance audit — not legal advice. For the Impressum/Widerruf wording, use a German
legal generator (e.g. eRecht24/Trusted Shops) or a lawyer; Google’s review is discretionary._
