---
name: chris-donnelly-sync
description: Weekly sync + distillation of Chris Donnelly's YouTube channel into Neil's Chris Donnelly LinkedIn/AI-search advisor corpus (docs/ side stays manual).
---

Run this exact sequence via the Bash tool, in order, from `~/src/advisors/chris-donnelly`:

1. `python3 tools/ingest.py sync` — fetches any new videos from Chris Donnelly's YouTube channel (@chrisdonnellypodcast) via yt-dlp. Full-channel backfill, no cutoff date (channel is small, ~23 long-form videos as of 2026-08 — mostly long interviews).
2. `python3 tools/distil.py run --limit 15` — distils newly-fetched transcripts into tagged teaching points via headless `claude -p`, tagged against `taxonomy.md` (three lanes: LinkedIn personal brand & growth; AI search / GEO / LLM visibility; lead generation & outbound). This step needs the local `claude` CLI to be logged in. There is an initial backlog of ~20 videos still undistilled from the 2026-08-31 build, so the first several weekly runs will each clear ~15 and that is expected, not a bug — `python3 tools/ingest.py status` shows current counts.
3. `python3 tools/index.py build` — rebuilds `INDEX.md` and `CONCEPTS.md` from both the YouTube side (`youtube/`) and any manually-added docs (`docs/`, added separately when Neil says "add to the Chris Donnelly advisor" — do NOT touch that folder in this scheduled run).
4. `git add -A && git -c user.name="Neil Taylor" -c user.email="neil@meandmyoldman.co.uk" commit -m "weekly sync"` — commit the week's changes (skip if nothing changed).

Reporting:
- If step 2 fails with a `claude` CLI authentication error (401 / "OAuth access token has expired"), say exactly that in one line and stop — do not retry, it needs Neil to run `claude login` in a terminal.
- Otherwise report only if something changed: how many new videos were fetched, how many distilled this run, and the running total distilled vs fetched (backlog progress). Keep it to 2-3 lines — do not dump INDEX.md or CONCEPTS.md.