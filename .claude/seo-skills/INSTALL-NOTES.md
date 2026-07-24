# SEO Skills — install notes

Source: https://github.com/seranking/seo-skills (MIT, SE Ranking) — plugin `seo-skills` v2.10.4.

## What was installed

- **32 skills** vendored into `.claude/skills/` (each `<name>/SKILL.md`), matching this repo's
  existing skill convention. They are auto-discovered by Claude Code and triggerable by slash
  command (e.g. `/seo-content-brief`, `/seo-geo`, `/seo-technical-audit`) or by natural-language
  description.
- **Support bundle** in `.claude/seo-skills/`:
  - `scripts/` — Python helpers for the Google-APIs skills (GSC, PSI, CrUX, Indexing, GA4, YouTube, NLP).
  - `extensions/` — installers for the optional Firecrawl and Google extensions.
  - `schemas/`, `plugin.json`, `mcp.json`, `LICENSE`.
- The upstream `examples/` folder (1.3 MB of sample outputs) was intentionally omitted to keep the
  repo lean. The "Example output" links at the top of each `SKILL.md` therefore 404 — cosmetic only;
  skills work without them.

## Required: connect the SE Ranking MCP (live data)

Most skills read live keyword/backlink/ranking/AI-search data from the SE Ranking MCP server.
Without it they can still structure work, but can't pull real numbers. Connect it once per client:

```
/mcp
```

Sign in via OAuth (no API token to manage). If `/mcp` doesn't list `se-ranking`, register it:

```
claude mcp add --transport http se-ranking https://api.seranking.com/mcp
```

To make it a persistent, per-project MCP instead, add this block to the repo's root `.mcp.json`
under `mcpServers` (OAuth still happens on first connect):

```json
"se-ranking": { "type": "http", "url": "https://api.seranking.com/mcp" }
```

## Optional: Firecrawl extension (raw HTML / JSON-LD / JS rendering)

Used by ~11 skills + the `seo-firecrawl` orchestrator. Wires `firecrawl-mcp` into Claude Code.
Requires Node 20+ (this env has v22) and a `FIRECRAWL_API_KEY`.

```
FIRECRAWL_API_KEY=fc-... bash .claude/seo-skills/extensions/firecrawl/install.sh
```

Note: the installer merges into `~/.claude/settings.json`, which is per-container (ephemeral on
Claude Code web). Re-run it in each fresh environment, or add the firecrawl MCP to the repo
`.mcp.json` for persistence.

## Optional: Google extension (`seo-google` skill)

Adds Google API client libraries + config at `~/.config/seo-skills/`. Requires Python 3.10+
(this env has 3.11) and Google API credentials.

```
bash .claude/seo-skills/extensions/google/install.sh
# then fill in credentials:
#   ~/.config/seo-skills/google-api.json
# verify:
python3 .claude/seo-skills/scripts/google_auth.py --check --json
```

## Script base path

The Google-APIs skills document their helpers as `python3 scripts/<name>.py` (relative to the
upstream plugin root). In this repo they live at `.claude/seo-skills/scripts/`, so run them as:

```
python3 .claude/seo-skills/scripts/gsc_query.py ...
```
