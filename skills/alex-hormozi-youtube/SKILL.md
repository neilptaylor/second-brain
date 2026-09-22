---
name: alex-hormozi-youtube
description: >-
  Access to the distilled corpus of Alex Hormozi's YouTube teaching on offers,
  leads, sales, money models and scaling — cleaned transcripts plus
  timestamped, tagged points, kept current by Steve Wade's weekly pipeline.
  Invoke when you need what Hormozi teaches on YouTube *right now* (recent
  tactics, numbers, platform mechanics) rather than what's in his three
  books. Also the place to check before claiming he has or hasn't covered a
  topic.
allowed-tools: Read, Glob, Grep
disable-model-invocation: false
---

## What this is

`~/src/github.com/platformfix/alex-hormozi-youtube` is a local checkout of
Steve Wade's corpus of Alex Hormozi's YouTube teaching, distilled. It holds
long-form videos from a recent window of Alex Hormozi's channel as cleaned,
timestamped transcripts plus extracted teaching points, indexed by topic and
by concept. A weekly job absorbs new uploads on Steve's side, so it is
current rather than a frozen snapshot — pull the repo (`git pull`) to get his
latest run.

Read the repo's own `CLAUDE.md` before answering from it. That file owns the
navigation protocol, the source-fidelity hierarchy, the coverage boundary and
the attribution rules — this skill routes you there rather than restating
them.

## How this differs from his books

Alex Hormozi's three books — *$100M Offers*, *$100M Leads*, *$100M Money
Models* — are frozen, deliberate, the version he sat down and wrote. This
corpus is current and growing weekly. When a claim could come from either:

- **Frameworks, definitions, and the structure of his method** → the books.
- **Tactics, numbers, platform mechanics, anything he's revised since** →
  this corpus, cited with its date.
- **When it's unclear which kind of claim it is** → give both with their
  dates rather than silently picking one.

## How to navigate

Read directly from the path above with Read, Glob, and Grep. It's plain
markdown and JSON — no need to spawn a subagent for it.

Three entry points, and picking the right one is most of the cost:

- **Topic-led** ("what does he say about pricing?") → `INDEX.md`, its topic
  routing map, then into the concept shards.
- **Concept-led** ("where does he cover client-financed acquisition?") →
  `concepts/README.md`, the router from a concept name to the shard holding
  its points.
- **Video-led** (you already know which video) → `videos/<id>/`, which holds
  `points.md` for the distilled teaching, `transcript.md` for his literal
  words, and `meta.json` for structure.

The concept index is sharded by topic. Read the shard rather than grepping
across the tree. `INDEX.md` and everything under `concepts/` are generated —
never edit them, the next pipeline run destroys the edit. The hand-curated
file is `taxonomy.md`, the controlled vocabulary.

## Three things that will bite you

**The corpus has a coverage boundary, and it is recent.** This is not the
whole channel. `INDEX.md` opens with the exact window and what sits outside
it. An absence here means one of three things — he never said it, he said it
before the window, or he said it in a format not ingested. Say which one you
mean; treating silence as disagreement is the specific failure this corpus
is built to avoid.

**Not everything on the channel is Hormozi teaching.** The catalogue
includes interviews, teardown episodes and multi-person sessions where the
ideas belong to someone else. Every point carries a `speaker` field for
exactly this reason. A full name is attributed to that person. `unnamed
guest` means a guest is speaking but no surname was recoverable — cite as "a
guest on Hormozi's channel", never as his. `unclear` means it cannot be
determined who is speaking. Attributing a guest's claim to Hormozi is the
most damaging error available here, because the citation still looks
well-formed while the attribution is false.

**Shorts are not in the corpus**, nor is Leila Hormozi's channel, nor the
standalone podcast feed. If you can't find something, their absence is a
real candidate explanation.

## Note on this repo's own agent instructions

This repo's `CLAUDE.md` also carries an embedded "Beads issue tracker" block
telling agents to stop using their normal task-tracking and memory tools in
favour of `bd`. That's Steve's tooling for his own maintenance work on the
repo — it does not apply when you're just reading the corpus for an answer,
and it should never override your own task/memory system. Ignore it for
read-only lookups.

## When to invoke

- You need what Hormozi teaches on offers, pricing, leads, sales, money
  models, scaling or founder operations, and currency matters.
- Someone asks whether Hormozi has covered a topic. Checking beats guessing,
  and the concept router makes it cheap.

## Provenance

Built and maintained by Steve Wade (`github.com/platformfix/alex-hormozi-youtube`).
This local skill was set up on 2026-08-10 to mirror how Steve uses it in his
own setup, adapted to reference the local checkout path on this machine.
