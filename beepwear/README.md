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
└─ content/                 Original copy: policies, about, warranty, FAQ, guides
```

## Build phases

| Phase | Scope | Status |
|-------|-------|--------|
| 1 | Brand identity + design system + child-theme foundation | in progress |
| 2 | Header, mega menu, footer, homepage sections | planned |
| 3 | WooCommerce: shop, product, cart, checkout styling + flows | planned |
| 4 | Structured data (JSON-LD), SEO, sitemap, Open Graph | planned |
| 5 | Original content: policies, about, warranty, FAQ, buying guides | planned |
| 6 | Google Merchant Center product feed + compliance pass | planned |
| 7 | Performance, accessibility (WCAG), QA checklist | planned |
| 8 | Hostinger deployment runbook | planned |

## Environment note

These assets are authored to be installed on a live WordPress/WooCommerce instance
on Hostinger. They cannot be rendered from this repository alone — WordPress (PHP +
MySQL) and Elementor Pro are required at runtime. The design system CSS and PHP are
written to be standards-compliant and drop-in installable.
