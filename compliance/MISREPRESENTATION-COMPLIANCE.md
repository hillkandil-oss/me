# Misrepresentation Compliance — Google's Five Best Practices

Standing requirements for every project. Sourced from the Merchant Center Misrepresentation
policy guidance. These are **not** optional polish: Misrepresentation is the policy most
likely to produce an account-level suspension rather than a per-product disapproval, and it
is enforced partly by **automated checks**, so it can fire before any human looks at the site.

Owner: Agent 12 (Merchant Center Audit) audits these; Agent 13 (Merchant Center Remediation)
fixes them; Agent 22 (Final Supervisory) verifies before submission.

---

## 1. Transparency about business identity, business model, policies, and customer interaction

**Required on site:**
- Legal/trading name visible, consistent everywhere (site, schema, GBP, Merchant Center).
- Physical address and phone in the footer or header, not buried on one page.
- Opening hours published (brick-and-mortar: mandatory).
- A real About page that states who operates the business and how it operates —
  where stock comes from, whether items are new/used, whether you hold inventory.
- Every policy on its own crawlable URL, linked from the footer: shipping, returns/refunds,
  cancellation, privacy, terms, payment, warranty, cookies.
- Contact methods that actually work — tested, not just present.

**Business model transparency is the part most sites fail.** If you dropship, resell,
consign, or sell pre-owned goods, say so plainly. Concealing the model is itself the
misrepresentation, and it is what automated checks and manual reviewers both look for.

**Acceptance evidence:** NAP-consistency matrix across all four surfaces; HTTP 200 on every
policy URL; contact-form and phone test records.

---

## 2. Online reputation — reviews, badges, seals

**Read this one carefully. It is a trap as often as an opportunity.**

Google is saying: *surface the reputation you genuinely have.* It is **not** an instruction to
add review widgets or trust seals to satisfy a checklist. Fabricated reviews, purchased
badges, invented seals, and unearned certifications are themselves Misrepresentation
violations — so "fixing" this bullet dishonestly is a direct route to the suspension it was
meant to prevent.

**Legitimate sources, in order of preference for a brick-and-mortar:**
1. **Google Business Profile reviews.** A physical store's strongest asset here. Real,
   independently verifiable, tied to the verified location, and they feed seller ratings.
   This is the single best fit for a brick-and-mortar business.
2. **Google Customer Reviews** — opt-in post-purchase survey programme; genuine and free.
3. **A reputable third-party review platform** with verified-purchase collection.
4. **Genuine payment/security marks you actually hold** (e.g. the real payment gateway's
   badge, an SSL indicator that reflects a real certificate).

**Never:** written-in testimonials, stock "5 stars" graphics, "As featured in" without the
feature, award badges you did not win, membership seals you do not hold, or star ratings in
structured data that no real review backs.

**If there is no reputation yet** — a new store — the honest answer is to ship with none and
build it. An empty review section is not a policy violation. A fake one is.

**Acceptance evidence:** for every review or badge on the site, a link to its verifiable
source. No source, no badge.

---

## 3. Professional design + SSL

**Required:**
- Valid HTTPS across the whole site, no mixed content, no certificate warnings.
- HTTPS enforced on cart, checkout, and account pages specifically.
- A design that reads as a finished, operating business: no placeholder text, no lorem
  ipsum, no broken images, no empty sections, no dead buttons, no unstyled defaults.
- Working mobile layout — a broken mobile experience reads as unfinished.

"Appears unfinished" is an explicit automatic failure condition in this project's own rules,
and it overlaps precisely with what automated checks can detect cheaply.

**Acceptance evidence:** SSL verification result; full-site link scan with zero 404/500;
placeholder-content scan returning clean; mobile screenshots at three viewports.

---

## 4. Business information settings inside Merchant Center

**Owner action — I cannot do this without account access.** Merchant Center's own business
information must be complete *and must match the website exactly*:
- Business name, address, phone, customer service contact.
- Business address verification where requested.
- Shipping settings that match the published shipping policy.
- Return settings that match the published returns policy.
- Tax settings where applicable.

**A mismatch between Merchant Center settings and the website is a Misrepresentation
trigger in its own right** — even when both are individually truthful. This is one of the
most common causes of account issues and one of the easiest to avoid.

**Acceptance evidence:** side-by-side comparison table, Merchant Center setting vs. live
site text, every row matching.

---

## 5. SEO guidelines, seller-ratings eligibility, and product-data parity

**Required:**
- Site crawlable and indexable: robots.txt not blocking commercial pages, valid XML
  sitemap, correct canonicals, no redirect chains or loops on product URLs.
- Product structured data present and **matching visible content** — price, availability,
  condition, brand.
- Feed ↔ landing-page parity on every attribute: title, price, sale price, availability,
  currency, condition, brand, image, URL.
- Landing pages reachable by Google's crawler without interstitials, geo-redirects, or
  cookie walls blocking access.

Parity is the highest-frequency failure of the five. Price and availability drift between
feed and page as stock moves, so this needs monitoring after launch, not just a one-time
check before submission.

**Acceptance evidence:** structured-data validation output; automated feed-vs-page diff
across the full catalogue with zero mismatches; crawl test on a sample of product URLs.

---

## Commonly reported automated-check triggers

Google does not publish its detection logic, so treat this as a risk checklist derived from
widely reported cases rather than confirmed mechanics — useful for prioritising, not a
guarantee of what fires:

- Missing or inconsistent business contact information
- No physical address on a store presenting itself as an established business
- Policy pages missing, thin, or containing unmodified template boilerplate
- Feed data not matching landing pages
- New domain with no trust signals and no reputation history
- Checkout that cannot be completed, or requires contact to complete
- Products that cannot actually be bought
- Concealed business model (dropshipping, reselling, pre-owned presented as new)
- Copied content or copied business identity from another store
- Star ratings in structured data with no real reviews behind them

---

## Remediation discipline

If a Misrepresentation notice is already active on an account, the rules from Agent 21 apply
and they are absolute:

- Find the **root cause** before requesting review. Automated flags are usually specific even
  when the notice text is generic.
- Fix substantively, then verify the fix on the rendered live page.
- **Never** create duplicate accounts or domains to bypass enforcement, submit false
  documentation, add policies temporarily for review then remove them, or request review
  repeatedly without changing anything. Each of these escalates enforcement.
- One well-prepared review request beats five hopeful ones.

Approval is Google's decision. This document maximises the chance of it; it cannot promise it,
and any claim of guaranteed approval would itself be a misrepresentation.
