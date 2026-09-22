# Me & My Old Man: working instructions

This repo is Neil Taylor's second brain for Me & My Old Man. It is the single source of truth for how the business thinks, writes, sells and delivers. Neil is the only user. Assume every task is business work, not software work.

## Read before you act

1. `README.md` — who Neil is, the business, core beliefs, voice. Read for anything client-facing.
2. `INDEX.md` — what lives where, and what is still outside the brain.
3. The one knowledge file your task depends on (see the table below). Do not work from memory of this business.

## Non-negotiables

Style, applies everywhere including plain chat replies:

- No em dashes. Use commas, full stops or brackets.
- Double quotes for speech and quoted text, never single.
- "Audio documentaries", never films, videos or movies.
- British English, British spelling, pounds sterling.
- No "nothing salesy" style disclaimers. The disclaimer is itself salesy.
- Never name sales gurus or frameworks in client-facing drafts. Use the thinking, drop the label.

Facts:

- Never quote a price without reading `knowledge/offer/pricing.md` first. The pricing in `README.md` is out of date.
- Never write in Neil's voice without reading `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` first.
- The A to D option labels are internal. Families see Hero Story, Family Documentary, Full Chorus.
- Never invent a client name, a date, a number or a testimonial. If a fact is missing, ask.

## Where to look, by job

| Job | Read first |
|---|---|
| Anything in Neil's voice | `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` |
| Customer language, objections, pain | `knowledge/voice/VOC_Intelligence_System.md` |
| Quoting, proposals, packaging | `knowledge/offer/pricing.md` |
| Identity, beliefs, positioning | `README.md` |
| What exists and what does not | `INDEX.md`, `docs/handover-*.md` |

## Skills do the work

`skills/` holds the repeatable jobs. Before writing anything from scratch, check whether a skill already covers it: content (linkedin-post, linkedin-engagement, instagram, newsletter, lead-magnet, mmom-carousel, mmom-visual), sales (mmom-sales-strategist, mmom-voice-check, proposal, mmom-follow-up, mmom-podcast-pr), delivery (new-client, client-folder-setup, onboarding-complete, client-onboarding-complete, mmom-onboarding, editor-briefing), ops (morning, mmom-weekly-action-plan, mmom-voice-profile-refresh, form-response-to-doc).

For any sales or prospect task, load `mmom-voice-check` before `mmom-sales-strategist`.

`skills/` is symlinked into `~/.claude/skills/`, so edits here are live in Claude Code. The Claude.ai web app runs its own copies and will drift until re-uploaded by hand.

## Systems outside this repo

The brain describes these, it does not contain them.

- Airtable CRM, base `apprk3RUXdvZNJ8TF` — live client and pipeline data.
- Google Drive `Mega Claude Cowork/` — client folders, proposals, templates, transcripts.
- Cost Model V10 sheet `1vN5YckOTYgne0yppRkfm2jYBjPp1ff6ug8gWntLeS8k` — margin-check every agreed price against it.
- Fathom, Gmail, Calendly, Riverside — call recordings, mail, bookings, audio.

If a connector for one of these is not authorised in the session, say so rather than guessing at the data.

## Layout

- `README.md` — identity doc
- `INDEX.md` — map of the brain
- `knowledge/` — durable facts: voice, voice of customer, offer and pricing
- `skills/` — the reusable skills that do the work
- `workflows/scheduled-tasks/` — the automations that run on a schedule
- `prompts/` — one-off prompt templates
- `docs/` — notes and handovers about the brain itself
- `scratch/` — working files, never a source of truth

## Working rules

- Durable facts go in `knowledge/`. Anything half-formed goes in `scratch/`. Never let `scratch/` be cited as truth.
- One topic per file, short, markdown, clear headings.
- When a fact changes, update the file that owns it and note the date. Do not leave two versions in two places.
- Commit in small, described chunks. Do not push unless asked.
- Drafts for clients are drafts. Never send an email, post or message without Neil saying yes to that exact text.
