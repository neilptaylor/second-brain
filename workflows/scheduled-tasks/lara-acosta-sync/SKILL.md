---
name: lara-acosta-sync
description: Weekly sync + distillation of Lara Acosta's YouTube channel into Neil's Lara Acosta LinkedIn advisor corpus (LinkedIn side stays manual).
---

Run this exact sequence via the Bash tool, in order, from `~/src/advisors/lara-acosta`:

1. `python3 tools/ingest.py sync` — fetches any new videos from Lara Acosta's YouTube channel (@Laraacosta) via yt-dlp. Full-channel backfill, no cutoff date (channel is small, ~45 videos as of 2026-08).
2. `python3 tools/distil.py run --limit 15` — distils newly-fetched transcripts into tagged teaching points via headless `claude -p`, tagged against `taxonomy.md`. This step needs the local `claude` CLI to be logged in.
3. `python3 tools/index.py build` — rebuilds `INDEX.md` and `CONCEPTS.md` from both the YouTube side (`youtube/`) and any manually-added LinkedIn posts (`linkedin/posts/`, added separately when Neil pastes a post and says "add to lara advisor" — do NOT touch that folder in this scheduled run).

Reporting:
- If step 2 fails with a `claude` CLI authentication error (401 / "OAuth access token has expired"), say exactly that in one line and stop — do not retry, it needs Neil to run `claude login` in a terminal.
- Otherwise report only if something changed: how many new videos were fetched/distilled. If nothing new, a one-line "no new videos this week" is enough.