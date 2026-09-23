---
name: claude-advisor
description: >-
  Access to a filtered corpus of Ruben Hassid's and Charlie Hills's Substack
  posts, scored against a solo-operator fit rubric into Adopt Now / Watch /
  Skip verdicts. Invoke before adopting any new AI tool or tactic, or when
  Neil asks whether a piece of AI-tooling hype is worth his time. Built to
  stop shiny-object chasing, not to catalogue everything AI.
allowed-tools: Read, Glob, Grep
disable-model-invocation: false
---

## What this is

`~/src/advisors/claude-advisor` is a filtered corpus built for one purpose:
stop Neil (solo founder, Me & My Old Man) from chasing shiny AI tooling that
won't move his one-person business. Every extracted point from Ruben
Hassid's and Charlie Hills's Substack posts is scored against
`filter-rubric.md` — shiny-object test, material business impact,
time-to-value, 30-day sales line, solo-operator fit — and lands in Adopt
Now, Watch, or Skip.

Read the repo's own `CLAUDE.md` before answering from it — it owns the
fidelity rules and the verdict logic.

## How to navigate

Read directly from the path above with Read, Glob, and Grep.

- Start at `INDEX.md` for the current Adopt Now / Watch / Skip lists,
  newest first.
- Drill into `posts/<slug>/points.md` for the reasoning behind a verdict, or
  `posts/<slug>/post.md` for the source text.

`INDEX.md` is generated — never edit it. `filter-rubric.md` is the actual
quality lever; if verdicts start looking wrong, sharpen the rubric there.

## Fidelity rules

- Every point is grounded in the actual post text — commentary and
  predictions that don't describe a concrete mechanism get skipped, not
  scored.
- The verdict is computed from the five scored fields, not vibes. A verdict
  that contradicts its own scores is a pipeline bug, not a judgment call.
- Skip is not deleted — rejected ideas stay in `INDEX.md` so the corpus is
  honest about what was considered.

## Scope

Substack's RSS feed only carries the most recent ~10-15 posts per
publication with full content, so this tracks what Charlie and Ruben are
saying *now*, not a full backlog.

## When to invoke

- Before recommending Neil adopt a new AI tool, workflow, or tactic.
- When Neil asks whether something he's seen hyped is actually worth his
  time as a solo operator.

## Provenance

Modelled on the Hormozi/Matt Gray YouTube corpora design, adapted for
Substack. Weekly sync is the scheduled task `claude-advisor-sync`.
