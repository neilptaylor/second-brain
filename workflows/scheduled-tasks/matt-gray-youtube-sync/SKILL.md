---
name: matt-gray-youtube-sync
description: Weekly sync of Matt Gray's two YouTube channels (personal + business) plus incremental chapter-anchored distillation, clearing the initial backlog over successive weeks.
---

Run this exact sequence via the Bash tool, in order, from `~/src/advisors/matt-gray-youtube`:

1. `python3 tools/ingest.py sync` — fetches any new long-form uploads from both @realmattgray and @mattgraybusiness via yt-dlp. Full backfill scope (not a bounded window), so this also continues catching any videos the initial pull missed.
2. `python3 tools/distil.py run --limit 20` — distils the 20 newest fetched-but-undistilled videos via headless `claude -p`, using chapter-anchored segmentation (Matt chapters nearly every video; each chapter is distilled as its own unit, tagged with its own title plus any `taxonomy.md` cross-cutting terms). This step needs the local `claude` CLI to be logged in. Because the initial ingest covers ~274 videos across both channels and distillation is real wall-clock cost, this will take several weeks of runs to clear the full backlog — that's expected, not a bug. `python3 tools/ingest.py status` shows current per-channel counts if useful context.
3. `python3 tools/index.py build` — rebuilds `INDEX.md` and `CONCEPTS.md`.

Context: this repo is Neil's own build of the same design Steve Wade's `platformfix/matt-gray-youtube` uses (per Steve — not yet shared/accessible). If Steve ever shares that repo, this local build may get replaced or merged with it; until then this is the live source.

Reporting:
- If step 2 fails with a `claude` CLI authentication error (401 / "OAuth access token has expired"), say exactly that in one line and stop — do not retry, it needs Neil to run `claude login` in a terminal.
- Otherwise report only if something changed: how many new videos were fetched, how many were distilled this run, and the running total distilled vs. total fetched (the backlog-clearing progress). Keep it to 2-3 lines — do not dump INDEX.md or CONCEPTS.md.