# BeepWear — Luxury Watch E-commerce (WordPress + WooCommerce + Elementor Pro)

Production build assets for **BeepWear**, an international luxury watch retailer.
Stack: **WordPress** (CMS) · **WooCommerce** (commerce, source of truth) ·
**Elementor Pro** (page building) · **Hostinger** (hosting).

This repository holds everything that lives in version control: the child theme,
the design system, original content, structured-data/SEO code, the Merchant Center
feed, and the deploy runbook. The live store is assembled on Hostinger by importing
these assets — see `docs/DEPLOY-RUNBOOK.md`.

## What's here

```
beepwear/
├─ theme/beepwear/          BeepWear child theme (base: Hello Elementor)
│  ├─ style.css             Theme header + full luxury design system (CSS)
│  ├─ functions.php         Enqueue, WooCommerce support, JSON-LD, SEO, feed hooks
│  └─ assets/               Fonts, images, icons
├─ docs/
│  ├─ BRAND.md              Visual identity: palette, type, spacing, voice
│  ├─ ELEMENTOR-BUILD-GUIDE.md   Page-by-page build instructions for Elementor Pro
│  └─ DEPLOY-RUNBOOK.md     Hostinger + WooCommerce + Merchant Center setup
├─ content/                 Original copy: homepage, policies, about, FAQ, guides
└─ preview/                 Rendered static HTML references (design proofs), e.g. homepage
```

> `preview/homepage.html` is a self-contained visual reference of the approved homepage
> design (real fonts embedded). It is a design proof for the Elementor build — not the
> production page, which is assembled in WordPress/Elementor per `docs/ELEMENTOR-BUILD-GUIDE.md`.

**Top-level status & acceptance:** see **`docs/MASTER-BLUEPRINT.md`** — the phase→milestone
map with live status, acceptance criteria, launch gate, and business-provided items that
gate publication.

## How this project is run

BeepWear follows the operating model in **`docs/PROJECT-GOVERNANCE.md`**: a 15-milestone
plan, six review gates (Design, SEO, Accessibility, Performance, Merchant Center, QA)
that every deliverable must clear, and a milestone sign-off log in **`docs/REVIEW-LOG.md`**.
The next milestone doesn't begin until the previous one is signed off.

## Milestones

| # | Milestone | Status |
|---|-----------|--------|
| 1 | Project Planning | ✅ complete |
| 2 | Brand Identity | ✅ complete (logo concepts pending) |
| 3 | Architecture | ✅ complete |
| 4 | Homepage | ✅ complete |
| 5 | Navigation (header, mega menu, footer) | ✅ complete |
| 6 | Collections | ✅ complete |
| 7 | Product Pages | ✅ complete |
| 8 | Checkout | ✅ complete |
| 9 | Policies | ⬜ planned |
| 10 | Customer Account | ⬜ planned |
| 11 | SEO | ⬜ planned |
| 12 | Merchant Center Audit | ⬜ planned |
| 13 | Testing | ⬜ planned |
| 14 | Deployment | ⬜ planned |
| 15 | Launch | ⬜ planned |

## Environment note

These assets are authored to be installed on a live WordPress/WooCommerce instance
on Hostinger. They cannot be rendered from this repository alone — WordPress (PHP +
MySQL) and Elementor Pro are required at runtime. The design system CSS and PHP are
written to be standards-compliant and drop-in installable.
