---
name: claude-advisor-sync
description: Weekly sync + rubric-scoring distillation of Ruben Hassid + Charlie Hills Substacks into Neil's Claude Advisor corpus.
---

Run this exact sequence via the Bash tool, in order, from `~/src/advisors/claude-advisor`:

1. `python3 tools/ingest.py sync` — fetches any new posts from Ruben Hassid's and Charlie Hills's Substacks (RSS-based, no auth needed).
2. `python3 tools/distil.py run --limit 20` — scores newly-fetched posts against `filter-rubric.md` (shiny-object / material-impact / time-to-value / 30-day-sales-line / solo-fit) via headless `claude -p`. This step needs the local `claude` CLI to be logged in.
3. `python3 tools/index.py build` — rebuilds `INDEX.md`.

Context: this corpus exists to stop Neil (solo founder, Me & My Old Man) from chasing shiny AI tooling that won't move his business. Every point gets a computed verdict: Adopt Now, Watch, or Skip.

Reporting:
- If step 2 fails with a `claude` CLI authentication error (401 / "OAuth access token has expired"), say exactly that in one line and stop — do not retry, do not attempt to fix it yourself, it needs Neil to run `claude login` in a terminal.
- Otherwise, report only if there's something worth surfacing: how many new posts were fetched, and — the main thing Neil actually wants to see — any new **Adopt Now** verdicts by name (from `INDEX.md`'s Adopt Now section). If nothing new landed in Adopt Now, a one-line "N posts synced, nothing cleared the bar this week" is enough. Do not dump the full INDEX.md.