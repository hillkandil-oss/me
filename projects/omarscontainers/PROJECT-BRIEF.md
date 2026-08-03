# omarscontainers.de — Project Brief (§44 First Response)

**Date:** 2026-08-03 · **Lead:** AI E-commerce Employee
**STATUS: DEVELOPMENT IN PROGRESS** (blocked items listed in §6)

---

## 1. Project understanding

Build omarscontainers.de into a professional, operational, policy-compliant
WordPress/WooCommerce store for the German market, selling shipping containers,
container pools, container homes and trailers, operated from a physical location in
Essen — and take it through to Google Merchant Center approval.

Current state: fresh WordPress install, WooCommerce 10.9.4, 116 products imported and
published, Hostinger AI default theme, nothing else configured. No payment method, no
shipping, no legal pages, no store address.

## 2. Primary objective

**Google Merchant Center approval.** Every decision is judged against whether it helps or
harms that. Approval is Google's decision and is never guaranteed; the objective is to
remove every controllable obstacle.

## 3. Confirmed platform architecture

WordPress + WooCommerce as the production commerce layer — products, URLs, cart, checkout,
payments, accounts, orders, inventory, shipping, tax, transactional email, structured data,
feed sync. HTTPS in place. Brick-and-mortar: single location, in-store pickup and returns
both offered. No Webflow layer required; the three reference sites inform design direction
only.

## 4. Information received

| Field | Value |
|---|---|
| Business name | omarscontainers |
| Domain | omarscontainers.de |
| Niche | Shipping containers, container pools, container homes, trailers |
| Market / currency | Germany / EUR |
| Physical address | Karnaper Str. 177 A, 45329 Essen |
| Opening hours | Mon–Sat, 08:00–18:30 |
| Support email | info@omarscontainers**.com** |
| Locations | Single |
| In-store pickup / returns | Yes / Yes |
| Shipping | Germany only, intermodal freight |
| Processing / delivery | 0–1 business days / 2–5 business days |
| Returns | 30 days, **company pays return shipping**, refund in 10 days |
| Payments wanted | Credit card, bank transfer |
| Products | 116 imported |
| Design references | cboxcontainers.de, selbstbaucontainer.de, kroftman.com/de-de |

## 5. Missing Information Register

| # | Item | Blocks | Status |
|---|---|---|---|
| MI-1 | **B2C or B2B?** | VAT config, price display, withdrawal right, 3 legal pages | **Missing — highest priority** |
| MI-2 | Legal entity name + Rechtsform | Impressum | Missing |
| MI-3 | Handelsregister number (HRB) | Impressum | Missing |
| MI-4 | USt-IdNr. | Impressum, VAT | Missing |
| MI-5 | Managing director name | Impressum (§5 DDG) | Missing |
| MI-6 | Telephone number | Impressum, trust, Merchant Center | Missing |
| MI-7 | Google Business Profile status | Local listings, verification lead time | Unconfirmed |
| MI-8 | Product source / supplier | Originality remediation, GTINs | Missing |
| MI-9 | GTIN/EAN availability | Feed identifiers | Missing |
| MI-10 | Product condition (new/used) | Feed `condition`, schema | Missing |
| MI-11 | Image rights ownership | Copyright risk | Missing |
| MI-12 | Logo, brand colours, fonts | Design system | Missing |
| MI-13 | Payment provider account status | Checkout | Missing |
| MI-14 | Freight pricing model | Shipping config | Partial |
| MI-15 | Warranty terms | Warranty page | Missing |
| MI-16 | Storefront photos available? | Visit Us page | Missing |

## 6. Assumptions register

| # | Assumption | Basis | Risk if wrong |
|---|---|---|---|
| A-1 | Selling currency EUR | Store config + DE market | Low |
| A-2 | Site language German | All content is German | Low |
| A-3 | B2C consumer sales | Retail-style storefront | **High** — changes VAT and legal pages |
| A-4 | Products are new, not used | No condition stated anywhere | Medium |
| A-5 | Business operates from the Essen address | Intake | Low |

## 7. Risk register

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| R-1 | **Copied product descriptions** — verified on 3 third-party sites | **High** | Rewrite all 116 originally |
| R-2 | Inherited false claims in copied text (e.g. "aus unserem Werk") | **High** | Remove during rewrite |
| R-3 | No legal pages — German statutory breach, not just Google | **High** | Write Impressum, Datenschutz, Widerruf, AGB |
| R-4 | Checkout impossible (no gateway) | **Blocker** | Enable payments |
| R-5 | VAT claimed in text but disabled in config | High | Resolve MI-1, configure tax |
| R-6 | Store country set to Hamburg, address is Essen | Medium | Correct to DE-NW |
| R-7 | Support email on .com, site on .de | Medium | Align or confirm both owned |
| R-8 | Branded resale (Daikin, Cheval Liberté) without authorisation | Medium | Confirm supplier authorisation |
| R-9 | Missing GTINs on branded goods | Medium | Obtain from supplier; never invent |
| R-10 | Catalogue breadth vs "containers" brand | Low | Address in IA and About |
| R-11 | GBP verification lead time (weeks) | Medium | **Start immediately** |

## 8. Merchant Center risk screening (Agent 2)

**Restricted products:** none. Containers, trailers, pools and HVAC are unrestricted.
Trailers are road vehicles — if sold road-ready, TÜV/registration claims must be accurate.

**Account-level blockers today:** no functioning checkout; no business identity on site;
no legal pages. All three are common misrepresentation triggers and all are fixable.

**Elevated-scrutiny factors:** new domain with no trust history; high average order value
(median €3,100, max €15,800); copied descriptions matching other merchants; branded goods
resold without visible authorisation.

**Favourable factors:** real physical premises with hours; in-store pickup and returns;
generous return terms (30 days, merchant pays return shipping); strong product imagery
(8.9 self-hosted images per product); no fake reviews, badges, scarcity or rating markup.

## 9. Proposed sitemap

```
/                        Homepage
/shop/                   All products
  /kategorie/…           Lagercontainer · Wohncontainer · Sanitärcontainer ·
                         Bürocontainer · Werkstattcontainer · Poolcontainer ·
                         Anhänger · Pferdeanhänger · Bootsanhänger ·
                         Klimaanlagen · Poolroboter
/produkt/…               116 product pages
/warenkorb/ /kasse/ /mein-konto/
/standort/               Visit Us — address, hours, map, directions (brick-and-mortar)
/ueber-uns/              About
/kontakt/                Contact
/faq/
/versand-und-lieferung/  Shipping incl. freight explanation
/zahlungsarten/          Payment methods
/widerrufsrecht/         Withdrawal right (statutory)
/rueckgabe-erstattung/   Returns & refunds
/agb/                    Terms
/datenschutz/            Privacy (GDPR)
/impressum/              Legal notice (statutory)
/versandkosten/          Shipping costs (PAngV)
/ratgeber/…              Buying guides
404
```

## 10. Agent execution order

Agents 1–2 complete (this document). Next: 3 (research — design direction from the three
reference sites), 4 (product data), 5 (IA), 6–7 (design), 8–9 (build), 10–11 (design QC),
12–13 (Merchant Center audit/remediation), 14–15 (SEO), 16–18 (security, accessibility,
checkout), 19 (live QA), 20 (feed + submission), 21 (diagnostics), 22 (final supervisory).

## 11. Product-data plan

1. Delete the 12 duplicates (6 SKUs × 2) — trash, reversible.
2. Extract brand factually from product names (Daikin, Cheval Liberté, Remko, Stahlworks).
   No brand invented where none is evidenced.
3. Add `condition` attribute once MI-10 is answered.
4. **Rewrite all 116 descriptions originally** — removes duplicate content, removes
   inherited false claims, improves SEO. Largest single work item.
5. Add weight and dimensions — for containers, dimensions are the primary spec.
6. GTIN/EAN only from supplier documentation; `identifier_exists: no` for custom builds.
7. Per-product classification: approved · warning · owner-info-required · excluded.

## 12. Website-development plan

Configuration first (fast, unblocks testing): store address, DE-NW, VAT per MI-1, payment
gateways, shipping zone Germany with freight rates. Then legal pages, then design system
and theme, then templates, then structured data (LocalBusiness + Product with
itemCondition), then feed.

## 13. Merchant Center compliance plan

Governed by `compliance/MISREPRESENTATION-COMPLIANCE.md`. NAP must match exactly across
site, schema, GBP and Merchant Center. Shipping and return settings in Merchant Center must
match the published policy text. Feed↔page parity monitored continuously, not once.
Re-audit with `compliance/audit-store.py` after each phase.

## 14. Immediate actions

**Started now (no site writes, no owner input needed):**
- Design direction analysis of the three reference sites
- Product-data classification of all 116
- Draft legal page content with `[BESTÄTIGEN: …]` markers where facts are missing
- Category and IA plan

**Ready on your go-ahead (site writes):**
- Delete 12 duplicates · set store address · correct region to DE-NW · brand extraction

**Owner-only, start today:**
- **Google Business Profile verification** — weeks of lead time, gates local listings
- Answer MI-1 (B2C/B2B) — unblocks tax, pricing and three legal pages
- Supply Impressum facts (MI-2 → MI-6)

## 15. Current project status

**STATUS: DEVELOPMENT IN PROGRESS**, with owner-dependent items outstanding.
Not ready for Merchant Center submission. No approval claim is made or implied.
