---
name: lara-acosta
description: >-
  Access to the distilled corpus of Lara Acosta's public teaching on LinkedIn
  personal-brand writing and growth — YouTube (@Laraacosta) auto-synced
  weekly, plus manually-added LinkedIn posts. Invoke when you need her
  perspective on LinkedIn writing, hooks, or personal-brand growth. Also the
  place to check before claiming she has or hasn't covered a topic.
allowed-tools: Read, Glob, Grep
disable-model-invocation: false
---

## What this is

`~/src/advisors/lara-acosta` is Neil's local build of a distilled advisor
corpus on LinkedIn personal-brand writing, built from Lara Acosta's public
teaching. Two sources, one corpus:

- `youtube/` — her channel (@Laraacosta, ~45 long-form videos), auto-synced
  weekly.
- `linkedin/` — her actual LinkedIn posts, added manually (LinkedIn has no
  public feed to scrape without violating their ToS). See
  `linkedin/NOTE.md` for how a post gets added.

Read the repo's own `CLAUDE.md` before answering from it — it owns the
navigation protocol and the manual-add workflow.

## How to navigate

Read directly from the path above with Read, Glob, and Grep.

- **Topic-led** → `INDEX.md`, then `CONCEPTS.md` for the concept -> points
  lookup across both sources.
- **YouTube video-led** → `youtube/videos/<id>/`, holding `points.md`,
  `transcript.md`, `meta.json`.
- **LinkedIn post-led** → `linkedin/posts/<slug>/`, holding `post.md` and
  `points.md`.

`INDEX.md` and `CONCEPTS.md` are generated — never edit them. `taxonomy.md`
is the hand-curated controlled vocabulary both sources tag against.

## Scope

The whole YouTube channel, not a bounded window — small enough (~45 videos)
that full backfill is practical. The LinkedIn side only grows when Neil
forwards a post.

## When to invoke

- You need Lara Acosta's take on LinkedIn writing, hooks, or personal-brand
  growth.
- Someone asks whether she has covered a topic — check `CONCEPTS.md` rather
  than guessing.
- LinkedIn profile or content review work, where her perspective sits
  alongside Matt Gray's and Chris Donnelly's.

## Provenance

Neil's independent build, modelled on Steve Wade's Hormozi pipeline design.
