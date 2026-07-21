# BeepWear — Operations, QA & Continuous Improvement

Master Prompt Parts 12 & 13. How BeepWear is tested, released, monitored, and improved over
time, plus the multi-agent operating cadence. Complements `PROJECT-GOVERNANCE.md` (roles +
review gates) and `DEPLOY-RUNBOOK.md` (deploy steps).

## 1. Git workflow

- `main` — production-ready. `develop` — integration. `feature/*`, `bugfix/*`, `hotfix/*`.
- Meaningful commit messages (imperative, specific): *"Fix breadcrumb schema validation,"*
  not *"update / fix stuff."*
- Significant changes get a code review (readability, maintainability, performance,
  security, accessibility, compatibility, regression risk) before merge.
- **This project's branch:** `claude/hello-lz33xo`. All BeepWear work commits here.

> Environment note: this repository holds the deployable code + docs. The live WordPress/
> WooCommerce/Elementor site is assembled and QA'd on Hostinger staging → production.

## 2. Testing strategy (before any deploy)

- **Functional:** navigation, product pages, cart, checkout, account create/login/reset,
  search, filters, contact form, newsletter.
- **Browser:** current Chrome, Edge, Firefox, Safari.
- **Responsive:** large-desktop → small-mobile; layout, type, nav, images, forms, checkout.
- **Performance:** load time, CWV (LCP<2.5s, INP<200ms, CLS<0.1), image optimization, JS/CSS.
- **Accessibility:** keyboard, focus, contrast, form labels, alt text, heading structure.
- **Security:** auth/authz, file permissions, SSL, plugin integrity, input sanitization,
  output escaping, rate limiting.

## 3. Pre-deploy QA checklist (no critical issue unresolved)

Homepage · Navigation · Categories · Brands · Collections · Products · Search · Filters ·
Cart · Checkout · Wishlist · Account · Contact forms · Newsletter · Blog · Policies · 404 ·
Performance · Accessibility · SEO · Structured data · Analytics · Merchant Center feed.

## 4. Monitoring & maintenance cadence

| Cadence | Tasks |
|---------|-------|
| **Daily** | Check orders; review error logs; monitor uptime; verify backups completed |
| **Weekly** | Review plugin updates (on staging); product-feed health; test checkout; Search Console + Merchant Center diagnostics |
| **Monthly** | Full SEO audit; performance review; security review; accessibility spot check; backup-restoration test; refresh key content/guides |
| **Quarterly** | UX review; conversion review; plugin + theme audit; remove obsolete content; analytics-trend review; plan new features |

Monitor: uptime, server resources, broken links/images, error logs, security alerts,
performance, Search Console, Merchant Center diagnostics, WooCommerce system status.

## 5. Change management (per significant change)

Record: objective · scope · expected impact · risks · rollback plan · testing results ·
approval status. Maintain `CHANGELOG.md`. No implementation bypasses QA and documentation.

## 6. Incident response

1. Assess severity. 2. Preserve logs. 3. Restore service via the safest path. 4. Roll back
recent changes if needed. 5. Communicate status. 6. Root-cause analysis. 7. Document lessons.
8. Add preventive measures. Avoid untested emergency changes on production.

## 7. Multi-agent operating model (Part 13)

The `PROJECT-GOVERNANCE.md` review lenses operate as specialized roles under a Project
Manager lens. Agent workflow for any feature:

> PM assigns → Research → SEO → UX → Product Content → Image direction → Development →
> QA → Documentation → PM approval → release.

No implementation bypasses QA and documentation. Conflicts resolve by **evidence +
documented requirements + best practice**, escalated to the PM lens.

**Decision framework** — before implementing any recommendation, all must be yes: improves
CX · technically sound · maintainable · supports SEO · improves/holds performance · on-brand ·
policy-compliant · operationally supportable. Plus governance: factually supported ·
aligned with objectives · ethical · transparent · documented.

## 8. Automation (with human judgment preserved)

Automate: product-feed generation, image optimization, backup scheduling, sitemap
generation, broken-link monitoring, performance monitoring, inventory alerts, SEO health
checks. **Never automate** legal approvals, pricing strategy, or factual product claims —
those require a human.

## 9. Reporting dashboard (recurring)

Summarize with metrics + action items across: **Development** (done / in-progress /
blockers) · **SEO** (indexing, ranking trend, technical health) · **Performance** (CWV,
largest assets, opportunities) · **Commerce** (product count, inventory alerts, cart) ·
**Content** (new articles, updated guides, product-content coverage) · **Operations**
(backups, security, plugin updates, outstanding tasks).

## 10. Continuous-improvement loop

Collect data → analyze → prioritize → implement → test → measure → document → repeat.
Success metrics: uptime, CWV, organic traffic, product-page engagement, conversion rate,
cart-abandonment, support response time, return-customer rate, Merchant Center + Search
Console health, revenue. Guide decisions by the trend across metrics, not a single KPI.
