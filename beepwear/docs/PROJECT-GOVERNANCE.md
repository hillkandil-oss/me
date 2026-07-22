# BeepWear — Project Governance & Operating Model

This document adopts the BeepWear "AI company" operating model (Master Prompt Part 2)
as the way this project is run. It is the plan of record: the milestone sequence, the
review gates every deliverable must clear, and the workflow each feature follows.

## How this actually runs (candor)

One agent executes every department role below. The "departments" are **review lenses**,
not separate personas — each milestone is checked against every lens with concrete
findings recorded in `REVIEW-LOG.md`. Sign-off means the lens was genuinely applied and
its blocking findings resolved, not that a second party approved it.

Two environment realities shape scope:

1. **No live runtime here.** WordPress (PHP/MySQL), WooCommerce, Elementor Pro, and
   Hostinger exist at deploy time, not in this repository. Deliverables are therefore
   *installable assets + build guides + runbooks*, authored to standards and PHP-linted,
   but rendered and QA'd on the live/staging Hostinger instance.
2. **Stack is classic WordPress, not headless.** Per the confirmed brief, the storefront
   is rendered by WordPress + WooCommerce, built visually in Elementor Pro, styled by the
   BeepWear child theme. Roles in Part 2 that assume a separate Next.js/WPGraphQL front
   end (Next.js Architect, headless API integration) are **not applicable** and are
   folded into the WordPress/WooCommerce/Elementor roles.

## Role → responsibility map (as applied here)

| Department (Part 2) | Applied responsibility in this project |
|---|---|
| Chief Executive / Project Manager | Milestone briefs, sequencing, sign-off, this doc + REVIEW-LOG |
| Business Analyst / Research | Personas, journeys, luxury-retail best practices → `docs/RESEARCH.md` |
| UI/UX + Brand Design | `docs/BRAND.md`, child-theme CSS, Elementor build guides |
| Engineering (WordPress + WooCommerce Architect) | Child theme PHP/CSS/JS, Woo config, data model, hooks |
| ~~Next.js Architect~~ | **N/A** — classic WordPress storefront |
| SEO / Google SEO | JSON-LD, metadata, sitemap, canonicals, headings, internal links |
| Content Writer | Original copy in `content/` (policies, about, guides, FAQ, PDP) |
| Google Merchant Center | Feed spec, policy compliance audit each milestone |
| Higgsfield AI Director | Editorial/hero image prompts + review (never product images) |
| Performance / Security / Accessibility | Review gates below, applied per milestone |
| DevOps | `docs/DEPLOY-RUNBOOK.md` (Hostinger, SSL, backups, cron) |
| QA / Documentation | REVIEW-LOG, checklists, this governance doc |

## Review gates (definition of done)

No milestone is "complete" until every gate passes. Blocking findings must be resolved;
non-blocking findings become tracked action items with an owner milestone.

1. **Design Review** — matches BRAND.md tokens; premium spacing/type; states designed
   (loading, empty, error, success).
2. **SEO Review** — one H1, correct heading order, title/meta, canonical, schema valid,
   internal links, image alt text.
3. **Accessibility Review (WCAG 2.2 AA target)** — keyboard path, visible focus,
   contrast ≥ 4.5:1 (text), ARIA where needed, form labels, reduced-motion honored.
4. **Performance Review** — Core Web Vitals budget: LCP < 2.5s, INP < 200ms, CLS < 0.1;
   images sized/lazy; fonts preloaded/subset; no layout shift.
5. **Merchant Center Review** — pricing, availability, shipping & returns visible,
   contact info, no misrepresentation, no fake trust signals, valid Product schema.
6. **QA Review** — responsive desktop/tablet/mobile; links; forms; cross-page consistency.

## Feature workflow

Research → Planning → Wireframe → UI Design → Content → Development →
SEO → Accessibility → Performance → Security → Merchant Center → QA →
Documentation → Approval → Deployment.

## Milestone plan of record

| # | Milestone | Status |
|---|-----------|--------|
| 1 | Project Planning (governance, plan, workflow) | ✅ complete |
| 2 | Brand Identity (`BRAND.md`, logo concepts) | ✅ complete (logo concepts pending) |
| 3 | Architecture (child theme, data model, plugin list) | ✅ complete |
| 4 | Homepage | ✅ complete |
| 5 | Navigation (header, mega menu, mobile, footer) | ✅ complete |
| 6 | Collections (shop + category pages) | ✅ complete |
| 7 | Product Pages (PDP) | ✅ complete |
| 8 | Checkout | ✅ complete |
| 9 | Policies & content | ✅ complete |
| 10 | Customer Account | ✅ complete |
| 11 | SEO | ✅ complete |
| 12 | Merchant Center Audit | ⬜ planned |
| 13 | Testing | ⬜ planned |
| 14 | Deployment | ⬜ planned |
| 15 | Launch | ⬜ planned |

The next milestone does not begin until the previous one is signed off in `REVIEW-LOG.md`.

## Project Manager milestone brief — template

Every milestone opens with a brief in this shape (see REVIEW-LOG for filled instances):

```
Objectives
Tasks
Dependencies
Risks
Deliverables
Acceptance Criteria
```
