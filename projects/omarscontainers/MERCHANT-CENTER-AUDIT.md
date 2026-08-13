# Merchant Center Compliance Audit — omarscontainers.de

**Audited:** 2026-08-04 · **Catalogue:** 108 products · **Feed:** 108 items

> **This is not an approval.** Approval is Google's decision, made after it crawls the site
> and reviews a submitted feed. This report records what was tested, what passed, what was
> fixed during the audit, and what remains.

---

## Result

| | |
|---|---|
| **Blocking findings** | **0** |
| HIGH | 2 — one correct as-is, one a robustness gap |
| MEDIUM | 0 |
| Fixed during this audit | 6 products |

---

## 1. Misrepresentation policy

The policy area that disapproves the most accounts. Tested against every product and page.

| Check | Result |
|---|---|
| Fake reviews, ratings, `AggregateRating` | **0** — none present, none ever added |
| Trust badges, awards, certifications | **0** |
| Scarcity messaging, countdowns, "only N left" | **0** |
| Superlatives ("weltweit erste", "Marktführer") | **0** — 3 removed in an earlier cycle |
| Unsupported comparatives ("zuverlässiger als…") | **0** — 1 removed |
| Promotional text in titles (SALE, GRATIS, JETZT KAUFEN) | **0** |
| Gimmicky punctuation, ALL-CAPS titles, URLs in titles | **0** |
| Competitor advertised in own listing | **0** — 1 removed earlier |
| **Unsubstantiated guarantee claims** | **4 found → 4 removed.** See §7. |
| Placeholder / demo text visible to customers | **0** — 14 removed, verified across 13 pages |

**Business identity consistency** — Merchant Center cross-checks the site against the account.
Six surfaces tested programmatically for five facts each:

```
surface                    phone  email  street  city   hours
/                            Y      Y      Y      Y      Y
/kontakt/                    Y      Y      Y      Y      Y
/impressum/                  Y      Y      Y      Y      Y
/standort/                   Y      Y      Y      Y      Y
/datenschutz/                Y      Y      Y      Y      Y
/versand-und-lieferung/      Y      Y      Y      Y      Y
```

`Store` JSON-LD matches all of them. `geo` is **deliberately absent** — coordinates were never
verified, and an approximate coordinate is a fabricated one.

## 2. Feed specification

All 108 items carry `id`, `title`, `description`, `link`, `image_link`, `availability`,
`price`, `condition`, `product_type`, `google_product_category`, `shipping`.

| Check | Result |
|---|---|
| Titles over 150 chars | 0 |
| Descriptions over 5,000 chars | 0 |
| Malformed prices | 0 |
| Invalid `availability` or `condition` values | 0 |
| Missing `google_product_category` | 0 |
| Non-HTTPS `link` or `image_link` | 0 |
| **Duplicate titles** | **2 found → 0.** See §7. |
| Fabricated GTIN/MPN | **0** — all 108 correctly declare `identifier_exists: no` |

## 3. Landing pages

**108 of 108 fetched as Googlebot.**

| Check | Result |
|---|---|
| Non-200 responses | **0** |
| `noindex` on a product page | 0 |
| Missing or mismatched canonical | 0 |
| Mixed content | 0 |
| Missing `Product` structured data | 0 |
| Feed price not findable on the page | 0 |
| Feed says in-stock, page says unavailable | 0 |

*(25-product random sample for parity checks; all 108 for status codes.)*

## 4. Images

**750 image URLs fetched and decoded.**

| Check | Result |
|---|---|
| Non-200 | 0 |
| Not served with an `image/*` content type | **9 found → 0.** See §7. |
| Below Merchant Center's 100×100 minimum | 0 |
| Below 250×250 | 0 |
| Unsupported format (AVIF) | **10 found → 0.** See §7. |
| Formats now in use | JPEG 62 · WebP 41 · PNG 6 |

## 5. Checkout and payment

Exercised end to end against the public Store API, not read from settings.

```
product        15,800.00  (13,277.31 net + 2,522.69 VAT)
shipping          300.00  (   252.10 net +    47.90 VAT)
TOTAL          16,100.00 EUR
```

Feed, landing page and checkout agree exactly. HTTPS throughout, `upgrade-insecure-requests`
set, cart and checkout reachable.

**Pricing compliance:** 9 discounted products each display the PAngV §11 30-day-lowest-price
line beside the price. `sale_price` is emitted only because the owner confirmed the reference
prices were genuinely charged; the generator withholds it by default.

## 6. Policy pages and crawlability

All eight required pages exist and are linked from every page: returns/refund, shipping,
terms, privacy, imprint, contact, payment, warranty.

`robots.txt` blocks nothing that matters — product pages, `/shop/` and `/wp-content/uploads`
are all crawlable. Sitemap present, 108 products listed, no `noindex` URLs submitted.

## 7. Fixed during this audit

| # | Finding | Action |
|---|---|---|
| 1 | **"10 Jahre Garantie" on 4 trailers** with no guarantor, duration, scope or claim procedure — § 479 BGB requires all four, and an unsubstantiated guarantee is a misrepresentation | Claim removed from 3411, 3435, 3447 and from the **product title** of 3483, which fed straight into `title`. Every numeric specification asserted preserved. |
| 2 | **2 duplicate product pairs** — same titles, identical prices, sequential SKUs, the same photos uploaded twice, created seconds apart | 3631 and 3638 moved to **trash** (recoverable). 3602 and 3613 kept — the fuller, correctly-ordered galleries. Duplicate titles 2 → 0. |
| 3 | **A silver product led with the white model's photo** — the image the feed sends as `image_link` | Relead with the genuine silver photograph; verified all four SKUs' image colour matches their title |
| 4 | **An entire gallery in AVIF**, served as `text/plain` — AVIF is not a supported Merchant Center format | 9 images converted to WebP, re-uploaded with German alt text, all now `image/webp` |
| 5 | **Unreplaced theme placeholders live in the footer** — `trans-socials`, and `mailto:trans-encoded_email` as a clickable contact link | Entire placeholder footer removed |
| 6 | **14 `[BESTÄTIGEN]` markers visible to customers** across 10 pages | All removed, with 3 headings left empty behind them |

## 8. Remaining

**HIGH — 52 products have no brand.** *Correct as-is.* These are unbranded containers and
pools. They declare `identifier_exists: no`, which is the honest handling. Inventing a brand
would be the violation.

**HIGH — `Product` schema omits `itemCondition`.** A robustness gap, not a policy breach: the
feed declares `condition: new` for every item and every item is new, so there is no
feed↔page contradiction. Closing it needs a PHP filter on
`woocommerce_structured_data_product`, reachable only by installing a snippets plugin —
i.e. arbitrary PHP execution on a live store. **Owner decision, not taken.**

## 9. Outside the website, and blocking submission

1. **Site language is `en_US`.** The buy button reads *"Add to cart"* on a German store, and
   `og:locale: en_US` / `inLanguage: en-US` sit in the structured data Google reads.
   *Einstellungen → Allgemein → Deutsch (Sie) → Speichern.* Not settable over REST —
   exhaustively established across 128 abilities and 30 REST namespaces.
2. **E-mail delivery is unverified and now load-bearing.** Bank details are sent manually by
   e-mail, so the payment path depends on one message arriving. The store sends via PHP
   `mail()` with no SMTP plugin, which Gmail, Outlook and GMX routinely reject or spam-file.
   Place one real test order; configure authenticated SMTP.
3. **No Merchant Center account.** Nothing has been submitted, so there is nothing to approve.
   Requires domain verification, claiming, and Search Console.
4. **AGB and Widerrufsbelehrung have not had legal review**, including whether custom-built
   containers fall under the § 312g Abs. 2 Nr. 1 BGB exemption.
5. **Google Business Profile is unverified.** Weeks of lead time; gates free local listings.
