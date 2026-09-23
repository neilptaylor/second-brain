---
name: matt-gray-youtube
description: >-
  Access to the distilled corpus of Matt Gray's YouTube teaching on personal
  brand, content systems, and stepping a founder out of operations — across
  both his channels (@realmattgray personal, @mattgraybusiness business),
  kept current by a weekly pipeline. Invoke when you need what Matt Gray
  teaches right now on brand-building, content systems, or founder
  delegation. Also the place to check before claiming he has or hasn't
  covered a topic.
allowed-tools: Read, Glob, Grep
disable-model-invocation: false
---

## What this is

`~/src/advisors/matt-gray-youtube` is Neil's local build of a distilled
archive of Matt Gray's YouTube teaching, modelled on Steve Wade's
`platformfix/alex-hormozi-youtube` design. It covers two channels —
`@realmattgray` (personal) and `@mattgraybusiness` (business) — tagged
per-video as `source_channel`.

Read the repo's own `CLAUDE.md` before answering from it. That file owns the
navigation protocol, the pipeline, and the segmentation rules — this skill
routes you there rather than restating them.

## What's different about this corpus

Matt chapters nearly every video, so distillation is chapter-anchored rather
than model-chosen: each point carries the chapter's own theme (specific,
per-video) plus any cross-cutting `taxonomy.md` terms (thematic, spans
videos). Scope is full backfill of both channels' long-form output (Shorts
excluded), not a bounded recent window.

**Check `INDEX.md` for how much has actually been distilled before relying
on this corpus for an answer.** Fetching and distilling are separate steps
here — the backlog clears incrementally, so the corpus can be fetched-but-
thin on a given topic even when the video exists.

## How to navigate

Read directly from the path above with Read, Glob, and Grep.

- **Topic-led** ("what does he say about content systems?") → `INDEX.md`,
  then `CONCEPTS.md` for the concept -> points lookup.
- **Video-led** (you already know which video) → `videos/<id>/`, holding
  `points.md` (distilled teaching), `transcript.md` (literal words), and
  `meta.json` (structure, `source_channel`).

`INDEX.md` and `CONCEPTS.md` are generated — never edit them, the next
pipeline run destroys the edit. The hand-curated file is `taxonomy.md`.

## When to invoke

- You need what Matt Gray teaches on personal brand, content systems,
  audience growth, or a founder stepping out of day-to-day operations.
- Someone asks whether Matt Gray has covered a topic. Check `CONCEPTS.md`
  rather than guessing.
- LinkedIn profile or content review work, where his perspective sits
  alongside Lara Acosta's and Chris Donnelly's.

## Provenance

Neil's independent build, modelled on Steve Wade's Hormozi pipeline design.
Weekly sync is the scheduled task `matt-gray-youtube-sync`.
