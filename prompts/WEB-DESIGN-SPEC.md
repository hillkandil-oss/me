# Master Prompt Update — Header, Homepage, About, Contact Form, Google Maps

**Status: mandatory.** These requirements take priority over any conflicting layout
instruction elsewhere in the master prompt.

Read together with **`WEB-DESIGN-AGENT.md`**, which covers *how* to work — verification
protocol, truthfulness constraints, measured contrast, motion rules. This document covers
*what* to build. Where they overlap, neither overrides the other: this file sets the
structure, that file sets the standard of evidence.

---

## 1. Contact information bar above the main header

A slim, professionally designed contact bar above the main header on all primary pages.

Must display:

- Verified business phone number
- Verified customer-service email address
- Verified physical business address

Values to be supplied per project:

```
Phone number:     [INSERT VERIFIED PHONE NUMBER]
Email address:    [INSERT VERIFIED EMAIL ADDRESS]
Physical address: [INSERT VERIFIED BUSINESS ADDRESS]
Google Maps URL:  [INSERT VERIFIED GOOGLE MAPS URL]
```

**Functional requirements**

1. Phone clickable via `tel:`.
2. Email clickable via `mailto:`.
3. Address clickable, linked to the verified Google Maps location.
4. Lightweight, visually consistent SVG icons for phone, email, location.
5. Compact and professional.
6. Sufficient colour contrast and readable typography.
7. Works on desktop, tablet, mobile.
8. Must not create horizontal scrolling.
9. On small screens: stack, scroll, or simplify — but keep all three details reachable.
10. No demo, placeholder, incomplete, or fabricated information on the live site.

The bar sits directly above the main header and navigation.

> **Implementation note — `tel:` formatting.** Use E.164 in the `href`
> (`tel:+492012760909`) and a readable form on screen (`+49 201 2760909`). A number
> written as `+0201…` is not dialable: `+` and the national trunk prefix `0` are mutually
> exclusive. Normalise the prefix; never alter the digits.

---

## 2. Main website header

Below the contact bar, using the existing theme's header system.

Must contain: business logo · Home · Shop · product categories · About Us · Contact Us ·
product search · customer account · shopping cart · responsive mobile menu.

Use a professional mega menu for main product categories where appropriate. A subtle sticky
effect is permitted provided the header stays compact and does not block content.

**Use the theme's existing header components. Do not replace the theme's header system
unnecessarily.**

> **Implementation note — cart and account icons.** WooCommerce renders the mini-cart glyph
> with a hard-coded `fill="#000000"` presentation attribute. On a dark header it is present
> in the DOM and invisible on screen. Fix with a CSS `fill` rule, which beats a presentation
> attribute in the cascade — do not re-author the block. Verify by computed style, not by
> looking for the class.

> **Implementation note — mobile menu.** Confirm the burger is visible against the header,
> and style the **open** overlay explicitly: background, link colour, submenu indent, close
> button, submenu arrows. Themes commonly force these to a light default with `!important`
> at a specificity that beats a naive override. Do not force `display` on the trigger — that
> overrides the framework's own breakpoint hiding and leaks the burger onto desktop.

---

## 3. Mandatory homepage structure

Build in exactly this order.

### Section 1 — Hero

Explain clearly: what the business sells · who the products are for · that customers can buy
online · that the business also operates a physical store · where that store is or the area
it serves.

Calls to action: Shop Now · Browse Products · Visit Our Store · Get Directions.

Use genuine product imagery or verified photographs of the physical business. **Do not use an
image that falsely represents the real store, team, warehouse, or products.** Subtle motion,
SVG elements and micro-interactions are welcome where they do not cost performance or
accessibility.

### Section 2 — Product categories

Professional category cards, each with: relevant category image · category name · short
description where appropriate · product count where useful · link to the category archive ·
subtle hover interaction · accessible focus state.

Only genuine categories containing active products. **Do not display** empty categories, demo
categories, unrelated theme-imported categories, categories of placeholder products, duplicate
categories, or categories without working archives.

Responsive and easy to browse on mobile.

### Section 3 — Filtered products

Let visitors switch between relevant product groups without leaving the homepage.

Possible filters: All Products · Featured · New Arrivals · Available In Store · Recommended ·
Sale Products *(only where genuine sale pricing exists)* · Best Sellers *(only where supported
by genuine sales data)* · categories · brands · types · collections · niche attributes.

Use only filters useful for the actual catalogue. **No filter may return empty results.**

Each product card shows: image · title · current price · genuine sale price where applicable ·
availability · category · genuine review rating if available · Add to Cart or View Product ·
accessible hover and focus states.

**Filter requirements**

1. Use the theme's existing product grid and filtering where possible.
2. AJAX filtering where the theme or an installed plugin supports it.
3. No unnecessary full-page reloads.
4. Clear loading indicator while updating.
5. Clear active state for the selected filter.
6. All controls keyboard operable.
7. Works on mobile.
8. A filter appears only if its group contains products.
9. Prices match the individual product pages.
10. Availability matches the product pages and inventory.
11. No fake stock information.
12. No fake ratings or reviews.
13. No permanent or fabricated discounts.
14. Nothing labelled trending, popular, best-selling or featured without a reasonable basis.
15. Filtering scripts must not interfere with product schema, analytics, or accessibility.

If the theme has no reliable filtering component, use one lightweight, actively maintained,
compatible plugin. **Do not install two plugins that do the same job.**

> **Implementation note — sale pricing.** A higher `regular_price` in the database is not
> evidence a discount is genuine. Under PAngV §11 (EU 98/6/EC Art. 6a) an advertised
> reduction must state the lowest price applied in the preceding 30 days. If nobody can
> confirm that history, **do not display the reduction and do not emit `sale_price` in the
> feed** — publish the price the customer actually pays. A permanent open-ended sale with no
> start date is a recognised disapproval trigger.

### Section 4 — Shopping benefits

Concise, lightweight SVG icons. **Only benefits the business genuinely offers.**

Candidates: shop online or in store · secure payment · helpful support · transparent returns ·
reliable delivery · store pickup *(only if operational)* · product advice in store · verified
physical location.

**Do not advertise** free shipping, same-day delivery, store pickup, extended warranties, free
returns, or around-the-clock support unless each is genuinely provided. Benefits must match
the site's own policy pages.

### Section 5 — Short About Us

Explain: what the business sells · that it has a physical retail location · who it serves ·
how products are selected or sourced · its commitment to customer service · where the store is.

Include a heading, two or three concise paragraphs, a real product/store/team photograph where
available, a **Learn More About Us** button, and a **Visit Our Store** or **Get Directions**
button.

**Do not invent** company history, founding date, founders, employees, achievements, awards,
certifications, years of experience, customer numbers, partnerships, store photographs, or
manufacturing capabilities. Any historical or company-specific claim must be verified by the
owner before publication.

### Section 6 — Homepage contact form

**The contact form is the final major content section on the homepage.** It comes after the
hero, categories, filtered products, benefits, short About Us, and any other approved content.
**The footer follows immediately.** No further product, promotional, testimonial,
informational, newsletter, FAQ, gallery, or content section may appear beneath it.

Content: heading · short customer-friendly introduction · phone · email · address · opening
hours where provided · Get Directions link · the form.

Headings: Contact Our Store · Have a Question? · Speak With Our Team · Contact Us · Get in Touch.

Fields: full name · email · phone · subject · reason for enquiry · order number (optional) ·
message · privacy-consent checkbox · submit.

Reason-for-enquiry options: product question · product availability · visiting the store ·
existing order · delivery question · store pickup · return or refund · general enquiry.

**Form requirements**

1. Submissions go to the verified business email.
2. Clear, permanently visible field labels.
3. Required and optional fields clearly marked.
4. Accessible validation messages.
5. Clear success message.
6. Clear submission-error message.
7. Suitable spam protection.
8. Responsive.
9. Tested on desktop and mobile.
10. Privacy-consent checkbox.
11. Consent wording linked to the Privacy Policy.
12. Confirmation email where appropriate.
13. No unnecessary personal information requested.
14. Receiving address never exposed in insecure code.
15. **Confirm form emails are actually delivered before launch.**
16. Configure authenticated delivery or SMTP where necessary.
17. Record any email-delivery issue in the final report.

---

## 4. Contact Us page

Build in exactly this order.

### Section 1 — Introduction
Heading · short introduction · how to contact the business · how to visit the store · verified
response time if available. **Do not promise an unsupported response time.**

### Section 2 — Business contact information
Business name · phone · email · complete address · opening hours · Get Directions button.
Professional SVG icons for phone, email, address, opening hours.

This information must match what appears above the header, in the footer, on About Us, in the
policies, in WooCommerce, in LocalBusiness structured data, in Merchant Center, and in the
Google Business Profile.

### Section 3 — Contact form
Same fields and same accessibility, privacy, validation, spam-protection, SMTP, responsiveness,
confirmation and testing requirements as the homepage form.

### Section 4 — Store visit information
Where verified: opening days · opening hours · holiday-hours disclaimer · parking · public
transport · accessibility · nearby landmark · store-pickup instructions · advice to call ahead.

**Do not invent** parking, transport routes, accessibility facilities, landmarks, pickup
services, appointment requirements, or holiday hours.

Where store inventory is not synchronised with online inventory, display:

> "Online and in-store availability may differ. Please contact the store before visiting to
> confirm that a product is available."

### Section 5 — Contact FAQ
May answer: where the store is · opening hours · buying directly in store · confirming
availability · store pickup · delivery · returns · email response time · appointments.
**Only publish answers verified by the owner.**

### Section 6 — Google Maps, as the final content section

**The map is the last major section. The footer follows immediately. Nothing goes beneath it.**

Use a reliable, actively maintained plugin compatible with the WordPress version, the theme,
Flux, WooCommerce, the builder, desktop/tablet/mobile, the cookie-consent system, and the
caching configuration.

Before installing anything:

1. Check whether a suitable map plugin is already installed.
2. Reuse it if secure, maintained, compatible and working.
3. No duplicate mapping plugins.
4. No plugin carrying unrelated functionality.
5. Confirm no known compatibility or security problems.
6. Back up the site before installing or replacing a map plugin.

**Content:** heading such as "Find Our Store" · complete verified address · responsive embed ·
correct marker · Get Directions button · store phone · optional verified landmark.

**Requirements**

1. Points to the genuine physical store.
2. Uses the exact verified address or coordinates.
3. Marker correctly placed.
4. Fully responsive.
5. Tested on desktop, tablet, mobile.
6. Accessible map title.
7. Direct Google Maps link as fallback.
8. Get Directions opens the correct location.
9. No horizontal scrolling.
10. No unnecessary layout shift.
11. Lazy-load, or load after user interaction, where appropriate.
12. Complies with the cookie-consent configuration.
13. No non-essential Google Maps cookies before consent where consent is required.
14. API key stored securely.
15. API key never in visible page content.
16. API key restricted by domain and API where possible.
17. Tested after caching and performance optimisation.
18. Does not interfere with the contact form.
19. Does not significantly reduce performance.
20. Address and directions link present **even if the map fails to load**.

**Never use** a generic city map · an approximate location · an unrelated address · a fake
marker · a virtual office shown as a retail store · a warehouse shown as customer-facing
unless customers may genuinely visit · a residential address without authorisation · an
address differing from the rest of the site · a map copied from another business ·
unverified coordinates.

> **Implementation note — the no-plugin route usually wins.** Requirements 11–16 are all
> satisfied at once by a **two-click (Zwei-Klick) loader with a keyless embed**, and it needs
> no plugin at all:
>
> - Ship a styled placeholder with the address and a "Load map" button. Build the `<iframe>`
>   only on click. Nothing reaches Google before the visitor agrees, which satisfies 12 and 13
>   without a consent-manager integration.
> - `https://www.google.com/maps?q=<urlencoded address>&output=embed` needs **no API key**,
>   so 14, 15 and 16 become non-issues.
> - Plain `maps/search/?api=1&query=…` and `maps/dir/?api=1&destination=…` links alongside
>   satisfy 7, 8 and 20, and work with JavaScript disabled.
>
> Verify by counting network requests: **zero to Google on page load, exactly one after the
> click.** Fetch the embed URL once before shipping to confirm it resolves to the real address
> rather than a blank tile. Draw the placeholder in CSS — a stock aerial photograph there
> reads as a picture of the yard and is a misrepresentation.

---

## 5. LocalBusiness structured data

Use the same verified information as the contact bar and the map.

Where applicable: business name · website URL · logo · phone · email · complete address ·
geographic coordinates · opening hours · Google Maps URL · business category · accepted
payment methods · social profiles · customer-service information.

**Coordinates in structured data must match the location the map displays.**

**Do not fabricate** ratings, review totals, awards, coordinates, opening hours, service areas,
branch locations, business descriptions, or price ranges.

Validate before launch.

> **Implementation note.** `Store` is a valid LocalBusiness subtype and is the more precise
> choice for a retail business. Emit `image` and `logo` — both are commonly omitted and the
> logo is an acceptable `image` where no storefront photograph exists. If coordinates have
> not been verified, **omit `geo` entirely** rather than deriving it from the address: an
> approximate coordinate is a fabricated one.

---

## 6. Final quality assurance

Confirm before declaring the site complete.

**Contact bar and header**
- [ ] Phone, email and address all displayed above the main header
- [ ] `tel:` link correct · `mailto:` link correct · address opens the right Maps location
- [ ] Bar is responsive · no demo contact information remains
- [ ] Main navigation works on desktop and mobile

**Homepage**
- [ ] Professional hero · Product Categories section · every category has active products
- [ ] Filtered Products section · every filter works · none returns an unintended empty result
- [ ] Filters work on mobile · prices match product pages · availability accurate
- [ ] Short About Us · no fabricated company information
- [ ] Contact form is the final major section · footer immediately follows
- [ ] Form submits, reaches the correct inbox, success and error messages work
- [ ] Form accessible and mobile responsive

**Contact Us page**
- [ ] Contact information accurate and consistent · form submits successfully
- [ ] Store visit information factual · FAQ answers verified
- [ ] Google Maps is the final major section · footer immediately follows
- [ ] Marker points to the genuine store · visible address matches the map
- [ ] Get Directions opens the correct location · map works on all devices
- [ ] Accessible map title · fallback link works · no horizontal scrolling
- [ ] Complies with cookie consent · no serious performance impact
- [ ] No approximate, fabricated or unrelated map location

**Business consistency** — the same business name, phone, email, address, opening hours and
Maps location across: top contact bar · main header · footer · homepage · Contact Us · About
Us · policy pages · checkout · WooCommerce settings · transactional emails · LocalBusiness
structured data · Google Business Profile · Merchant Center · product feed · social profiles.

Document and correct every inconsistency before submitting for Merchant Center review.

> **Implementation note — how to actually check consistency.** Do not eyeball it. Fetch each
> surface and diff the strings programmatically. Two failures found this way on a real
> project: a phone number whose area code belonged to a different city from the address, and
> three different spellings of the business name across the site, the Impressum and the
> domain. Both are exactly what Merchant Center's business-information check and Google
> Business Profile's NAP matching look for.
