# trenchsafety.org — Remediation Work Order (for a Claude Code session with WordPress access)

**Goal:** Take the store from "instant Merchant Center suspension" to a coherent, finished,
policy-compliant WooCommerce store. Based on the audit in
`trenchsafety-org-MERCHANT-CENTER-AUDIT.md`.

**Platform:** WordPress + WooCommerce 10.9.1, Elementor + "Industrie" theme, AIOSEO, Hostinger.

---

## ⛔ RULE FOR THE AGENT — read first

This is a **Google Merchant Center compliance** job. The entire reason this store is at
risk is *misrepresentation*. Therefore you must **NEVER invent business facts** to fill a
gap. Do **not** fabricate an address, phone, email, company name, product price, weight,
brand, or origin. If a required real fact is missing from the "Owner inputs" section below,
**stop and ask the owner** — a plausible-sounding invention is worse than a blank, because
it's the thing Google bans stores for. Everything in Phase 1–7 is safe to execute *only*
after the Owner inputs are provided.

---

## 🔑 ACCESS THE AGENT NEEDS (owner provides)

- WordPress admin URL + login, **or** a WordPress **Application Password** for an admin user.
- WooCommerce **REST API** key (Read/Write) for bulk product edits
  (WooCommerce → Settings → Advanced → REST API).
- Confirmation the agent may edit live (or a staging copy to work on first — preferred).
- **Back up the site first** (Hostinger backup or a WordPress backup plugin) before any change.

---

## 📋 OWNER INPUTS REQUIRED (fill these before the agent starts)

The agent cannot proceed on these without your real answers:

1. **One business identity.** The real (legal or trading) business name to use everywhere.
   - Is "TrenchSafety" the brand you want, even though you sell containers/trailers/propane?
     If yes, the site must clearly explain the brand + what it sells. If no, say the real name.
   - Legal entity + DBA relationship, if any (for footer/terms and to match the payment processor).
2. **Real contact info** (must be genuine and monitored):
   - Business email on your own domain (e.g. `sales@trenchsafety.org`) — **not** `info@gmail.com`.
   - One real phone number.
   - One real street address (not a Google Plus Code).
   - Business hours.
3. **Product price list** — every product with its real price. Fill the table in Appendix A
   (price required; brand/condition/GTIN/weight where they exist — never invented).
4. **Category eligibility** — confirm you can legally sell/ship **propane tanks** (pressurized
   fuel vessels) and how they ship (freight/LTL, lead times, any restrictions).
5. **Payment processor** legal name + the checkout/bank **statement descriptor** (should read
   as your business, e.g. "TRENCHSAFETY").
6. **Social links** — real, active profiles only (or "none").

---

## 🧹 PHASE 1 — Purge ALL theme-demo content (highest priority)

The demo content appears site-wide via the theme header/footer and demo pages. Nothing
placeholder may remain on any public page.

**1a. Replace global header/footer** (Elementor → Templates → Theme Builder, and/or
Appearance → Widgets / Customizer). Remove and replace with the real business NAP:
- Delete tagline *"…personally meeting their insurance needs."*
- Delete brand *"Yellow Construction Company."*
- Replace demo phone **`(+880)155-69566`** → real phone.
- Replace demo address **`374 William S Canning Blvd, Fall River MA`** and the Plus-Code
  address **`VVV4+3G7, Watertown, SD 57201`** → the one real address.
- Replace demo emails `info@gmail.com` and `support.industrie@gmail.com` → real email.

**1b. Site identity** (Settings → General): set Site Title, Tagline, and Admin Email to the
real business. (WooCommerce → Settings → General: set the store address.)

**1c. WooCommerce emails** (WooCommerce → Settings → Emails): set "from" name/address to the
real business.

**1d. Contact Form 7** recipient: point the form to the real business email.

## 🗑 PHASE 2 — Delete demo pages & rebuild the menu

**Delete these demo pages** (Pages → Trash; then empty trash). They are theme filler:
- `/home` (duplicate — keep the real homepage only), `/about-us` **or** `/about` (keep one),
  `/contact-2` (keep `/contact`), `/coming-soon`.
- All construction-service demos: `/services`, `/services/oil-gas-energy`,
  `/services/project-management`, `/services/civil-engineering`, `/services/demolition-services`,
  `/services/general-contracting`, `/services/pre-construction`, `/services/roofing-services`.
- `/projects`, `/portfolios/manufacture`, `/team`, `/teams/joshua-sendu`, `/pricing-plans`,
  `/appointment`.
- All builder "Elements" demos: `/icon-box-elements`, `/services-box-elements`,
  `/services-tab-elements`, `/advance-tab-elements`, `/work-process-elements`,
  `/projects-elements`, `/team-elements`, `/testimonials-elements`, `/partner-logo-elements`,
  `/pricing-elements`, `/counter-elements`, `/blog-elements`, `/gsap-elements`.

**Keep & clean:** homepage, `/shop`, product categories (`containers`, `dump-trailers`,
`propane-tanks`, `utility-trailers`), one `/about`, `/buyers-guide`, `/blog` + posts,
one `/contact`, all products, and the policy pages (Phase 5).

**Rebuild the primary menu** (Appearance → Menus) to real pages only:
`Home · Shop · Containers · Dump Trailers · Propane Tanks · Utility Trailers · About ·
Buyers Guide · Blog · Contact`. Put policies in the footer menu.

## 🔌 PHASE 3 — Disable "coming soon"

Deactivate the **Ultimate Coming Soon** plugin (Plugins). Confirm no page/region serves an
under-construction wall to visitors or crawlers.

## 📝 PHASE 4 — Rewrite About + homepage identity (owner facts only)

- Rewrite `/about` using the owner's real story/identity — no theme demo, no invented people.
  State plainly what the business is and that it's a reseller of the listed equipment.
- Ensure the homepage hero and "Our History" section describe one coherent business that
  matches the domain/brand decision from Owner input #1.

## 💲 PHASE 5 — Products: prices + data (via WooCommerce REST API)

For **every** product (start with the propane tanks, containers, trailers already in the shop):
- Set the **real price** (from Appendix A). No product may be published without a price.
- Set **stock/availability** accurately.
- Set **condition** (new/used) to match reality; add **brand** and **GTIN/MPN** where they
  genuinely exist (else leave blank / identifier-exists = no — never invent).
- Set **weight/dimensions/shipping class** for freight items so shipping is real at checkout.
- Ensure each product image is the actual item, ≥ 500×500 px, no overlays/watermarks.
- Confirm each product page is **purchasable** (add-to-cart → checkout works).

## 📄 PHASE 6 — Verify & fix policy pages

Read each and make it real, specific, original, and internally consistent with product pages:
`/shipping-policy` (freight costs + lead times), `/refund_returns` (window, who pays return
freight, restocking, refund timeframe in real days), `/product-condition`, `/sales-tax-policy`,
`/payment-policy`, `/terms-and-condition` (governing-law state), `/privacy-policy-2` (data +
analytics). Remove any demo text; ensure the real business name/contact appears.

## 🔎 PHASE 7 — Final QA sweep (must pass before Merchant Center)

Crawl every public URL and confirm **none** of these demo strings remain anywhere:
```
insurance needs | Yellow Construction | +880 | 155-69566 | Fall River | William S Canning
| Watertown, SD 57201 | VVV4+3G7 | info@gmail.com | support.industrie@gmail.com
| Industrie | Lorem | coming soon | joshua sendu
```
Also verify: every product has a price; contact info identical across site/policies; HTTPS on
every page incl. checkout; sitemap regenerated (AIOSEO); menu contains only real pages.

**Then, and only then:** connect Google for WooCommerce on the verified `trenchsafety.org`
domain, set business info to match the site + payment processor, and request review **once**.
Approval is never guaranteed (propane/heavy equipment gets manual review).

---

## Appendix A — Product price list (owner fills; agent applies)

| Product (URL slug) | Real price (USD) | Condition | Brand | GTIN/MPN (if real) | Ship weight / freight class |
|---|---|---|---|---|---|
| 500-gallon-above-below-ground-steel-asme-propane-tank | | | | | |
| 1000-gallon-above-below-ground-propane-tank | | | | | |
| 1000-gallon-below-ground-propane-tank-with-riser | | | | | |
| 250-gallon-above-ground-steel-new-propane-tank | | | | | |
| 320-gallon-steel-above-ground-propane-tank | | | | | |
| 200-pound-propane-tank-for-small-spaces | | | | | |
| 20-gallon-steel-below-ground-propane-tank | | | | | |
| asme-420-steel-120-gallon-small-propane-tank-cylinder | | | | | |
| 20′-iso-tank-container-chemical | | | | | |
| …(add every remaining product from /shop) | | | | | |

---

## Appendix B — Quick verification commands (for the agent)

```bash
# after changes, sweep the live site for leftover demo strings:
for url in / /about /contact /shop /refund_returns /shipping-policy /terms-and-condition; do
  curl -s "https://trenchsafety.org$url" | grep -Eio \
   "insurance needs|yellow construction|\+880|fall river|william s canning|vvv4\+3g7|info@gmail\.com|support\.industrie|industrie|lorem|coming soon|joshua sendu" \
   | sort -u | sed "s|^|$url: |"
done
# expect: no output = clean
```
