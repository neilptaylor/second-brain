---
name: chris-donnelly
description: >-
  Access to the distilled corpus of Chris Donnelly's public teaching on
  LinkedIn personal-brand growth, AI-search visibility (GEO / LLM SEO), and
  lead generation / outbound — YouTube (@chrisdonnellypodcast) auto-synced
  weekly, plus hand-collected written material. Invoke when you need his
  perspective on any of those three lanes. Also the place to check before
  claiming he has or hasn't covered a topic.
allowed-tools: Read, Glob, Grep
disable-model-invocation: false
---

## What this is

`~/src/advisors/chris-donnelly` is Neil's local build of a distilled advisor
corpus covering Chris Donnelly's public teaching. Chris built and sold the
luxury digital agency Verb, co-founded Lottie, runs the Creator Accelerator,
and founded Searchable.com (an AI-search visibility platform). Three lanes:
LinkedIn personal-brand growth, AI search visibility (GEO / LLM SEO), and
lead-generation / outbound. Two sources, one corpus:

- `youtube/` — his channel (@chrisdonnellypodcast, ~23 long-form videos,
  mostly interviews), auto-synced weekly.
- `docs/` — written material Neil collected (LinkedIn Bible, outbound
  templates, lead-gen blueprint), distilled once. See `docs/NOTE.md`.

Read the repo's own `CLAUDE.md` before answering from it — it owns the
navigation protocol and the three-lane taxonomy.

## Fidelity

The channel is mostly interviews. A transcript often contains Chris *and* a
guest — points are extracted as one corpus but a point that clearly comes
from a guest names the guest in its insight. Never attribute a guest's claim
to Chris.

## How to navigate

Read directly from the path above with Read, Glob, and Grep.

- **Topic-led** → `INDEX.md`, then `CONCEPTS.md` for the concept -> points
  lookup across both sources.
- **YouTube video-led** → `youtube/videos/<id>/`, holding `points.md`,
  `transcript.md`, `meta.json`.
- **Doc-led** → `docs/<slug>/`, holding `source.md` and `points.md`.

`INDEX.md` and `CONCEPTS.md` are generated — never edit them. `taxonomy.md`
is the hand-curated controlled vocabulary (3 lanes) both sources tag
against.

## Scope

The whole YouTube channel, not a bounded window — small enough (~23 videos)
that full backfill is practical, like Lara Acosta's corpus. The `docs/` side
only grows when Neil hand-adds material.

## When to invoke

- You need Chris Donnelly's take on LinkedIn growth, AI-search visibility,
  or outbound/lead-gen.
- Someone asks whether he has covered a topic — check `CONCEPTS.md` rather
  than guessing.
- LinkedIn profile or content review work, where his perspective sits
  alongside Matt Gray's and Lara Acosta's.

## Provenance

Neil's independent build, the third advisor of this design after Lara
Acosta and Matt Gray. Weekly sync is the scheduled task
`chris-donnelly-sync` (Sunday night); the `docs/` side is never touched by
that job.
