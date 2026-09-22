---
name: mmom-bio-refresh
description: >
  Monthly refresh of Neil's short bio/profile copy across every channel —
  LinkedIn bio, Instagram bio, X bio, and the Lovable website's stats line
  — so the families/hours/countries numbers never go stale. Outputs
  ready-to-copy-paste text for each platform, it does not post or publish
  anything itself. Trigger on "refresh my bios", "update my bio stats",
  "monthly bio refresh", "/mmom-bio-refresh", or when the scheduled task by
  this name fires. Also trigger if Neil asks why his bio numbers look out
  of date.
---
<!-- v1.0 — 2026-09-22: Created alongside knowledge/offer/business-stats.md, the new single source of truth for families/hours/countries. This skill is the monthly consumer of that file — new-client keeps it updated, this skill turns it into copy-paste bio text. -->

# MMOM Bio Refresh

Neil's win count keeps climbing, and his bios across platforms quote a
families/hours/countries stat that goes stale the moment it's written. This
skill regenerates that copy every month from one source of truth so every
channel says the same true number.

## Before you start

1. Read `knowledge/offer/business-stats.md` — the current, correctly
   rounded families/hours/countries figures. Do not use a number from
   memory or from an old draft of this skill's output.
2. Read `README.md` for identity and voice, and skim
   `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` in full — bios are
   client-facing, so this is not optional even though the copy is short.
3. Note the date `business-stats.md` was last updated. If it's more than
   ~6 weeks old, flag that to Neil before writing anything — it likely
   means a new-client win didn't trigger the refresh, and the numbers may
   be behind what's in the tracker sheet.

## What to produce

One short draft per channel, in Neil's voice, each respecting that
platform's character limit and register. Pull the families/hours/countries
figures straight from `business-stats.md` — never invent, round differently,
or reuse a number from a previous run of this skill.

- **LinkedIn bio / headline line** — the "I help families feel closer in 12
  weeks..." positioning line used in `linkedin-post/SKILL.md`, with the
  current stat string swapped in. ~220 characters.
- **Instagram bio** — warmer, shorter, first-person. 150 character limit
  including line breaks and any emoji Neil already uses (check his current
  live bio for tone if accessible; otherwise keep it plain, no invented
  emoji).
- **X (Twitter) bio** — 160 character limit. Terser than LinkedIn/Instagram
  — X bios read more like a tagline than a pitch.
- **Lovable website stats line** — whatever short trust-stat strip
  currently exists on the site (e.g. "38 families · 11 countries · 390+
  hours"). If Neil hasn't shared the current live wording, ask rather than
  guessing at the site's existing copy and layout.

Every version must carry the *same* underlying numbers — only the phrasing
and length change per platform.

## Output format

Plain text, one platform per heading, ready to select and paste — no
surrounding commentary, no markdown bold/italics inside the bio text
itself (platforms don't render markdown). Example shape:

```
## LinkedIn
[bio text]

## Instagram
[bio text]

## X
[bio text]

## Lovable stats line
[stats line]
```

Deliver the work plus one line noting the source figures used (e.g. "Using
38 families · 11 countries · 390+ hours from business-stats.md, updated
2026-09-22") — nothing else. Neil copies each block by hand into the
platform; this skill never posts, publishes, or edits a live site or
profile.

## Notes on care

- If `business-stats.md` and the live tracker sheet disagree, trust
  `business-stats.md` but flag the mismatch — it means a new-client run
  skipped the refresh step and should be caught up.
- Never round differently per platform. The rounding rule (hours down to
  nearest 10; families and countries exact) is fixed in
  `knowledge/offer/business-stats.md` and applies everywhere.
- If nothing has changed since the last refresh (no new clients logged),
  say so plainly rather than manufacturing a diff — re-output the same
  correct copy.
