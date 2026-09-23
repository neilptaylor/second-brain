# Me & My Old Man: working instructions

This repo is Neil Taylor's second brain for Me & My Old Man. It is the single source of truth for how the business thinks, writes, sells and delivers. Neil is the only user. Assume every task is business work, not software work.

## Read before you act

1. `README.md` — who Neil is, the business, core beliefs, voice. Read for anything client-facing.
2. `INDEX.md` — what lives where, and what is still outside the brain.
3. `knowledge/lessons.md` — do not repeat a logged mistake.
4. The one knowledge file your task depends on (see the table below). Do not work from memory of this business.

Read the voice profile in full. Never work from a summary of it. Summarised copies are how the old Drive instruction files drifted out of date.

## Non-negotiables

Style, applies everywhere including plain chat replies:

- No em dashes. Use a full stop, a comma, or restructure the sentence.
- Double quotes for speech and quoted text, never single.
- "Audio documentaries", never films, videos or movies.
- British English, British spelling, pounds sterling.
- No "nothing salesy" style disclaimers. The disclaimer is itself salesy.
- Never name sales gurus or frameworks in client-facing drafts. Use the thinking, drop the label.
- Google Docs are built as HTML (`<h1>`/`<h2>` for Title/Heading, `<b>` for bold, `<ul><li>` for lists), never as markdown text uploaded as plain text. Drive's plain-text upload renders `#` and `**` as literal characters on the page instead of formatting.

Facts:

- Never quote a price without reading `knowledge/offer/pricing.md` first. The pricing in `README.md` is out of date, and so is every tier figure in the old Drive CLAUDE.md.
- Never write in Neil's voice without reading `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` first.
- The A to D option labels are internal. Families see Hero Story, Family Documentary, Full Chorus.
- Never invent, composite or embellish a family story. Every story used is real.
- Never invent a client name, a date, a number or a testimonial. If a fact is missing, ask.
- Never fill an unclear brief with generic content. Ask Neil instead.

## The two corrections Neil makes most, pre-empt them

**Still sounds AI.** Passing the banned-words list is not enough. If a paragraph has no concrete object or moment in it (a dishwasher, a twelve-minute phone call, a name), rewrite it before showing him. Test every sentence: would Neil say this out loud to his best mate?

**Too much output.** Deliver the work plus one or two lines, nothing else. No preamble, no postamble, no recap of what you did, no unrequested bullets or structure.

## Deliverable defaults

- Content: one strong draft, saved as `.md`, with two alternative opening hooks at the bottom. Neil swaps hooks far more often than he asks for a rewrite.
- Just do it, no plan needed: any single piece of routine content, a post, an email, a proposal run through its skill.
- Plan and wait for a yes: multi-deliverable projects, client-facing work going out the same day, or anything with no skill or template to follow.

## Where to look, by job

| Job | Read first |
|---|---|
| Anything in Neil's voice | `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` |
| Customer language, objections, pain | `knowledge/voice/VOC_Intelligence_System.md` |
| Quoting, proposals, packaging | `knowledge/offer/pricing.md` |
| Sales calls and objection handling | `knowledge/offer/sales-call-scripts.md` |
| Identity, beliefs, positioning | `README.md` |
| Which tools connect to what | `knowledge/systems-map.md` |
| Past corrections | `knowledge/lessons.md` |
| What exists and what does not | `INDEX.md`, `docs/handover-*.md` |

## Skills do the work

`skills/` holds the repeatable jobs. Before writing anything from scratch, check whether a skill already covers it: content (linkedin-post, linkedin-engagement, instagram, newsletter, lead-magnet, mmom-carousel, mmom-visual), sales (mmom-sales-strategist, mmom-voice-check, proposal, mmom-follow-up, mmom-podcast-pr), delivery (new-client, client-folder-setup, onboarding-complete, client-onboarding-complete, mmom-onboarding, editor-briefing), ops (morning, mmom-weekly-action-plan, mmom-voice-profile-refresh, form-response-to-doc).

For any sales or prospect task, load `mmom-voice-check` before `mmom-sales-strategist`.

`skills/` is symlinked into `~/.claude/skills/`, so edits here are live in Claude Code. The Claude.ai web app runs its own copies and will drift until re-uploaded by hand.

## The skill feedback loop

Trigger: Neil says "add to skill: ...", or he rewrites or corrects output that came from a skill-driven task (a hook, a proposal structure, an email opening).

Every time, same turn:

1. Name the skill that produced it, or decide the lesson is cross-cutting.
2. Log it in `knowledge/lessons.md` either way. That file is the permanent record.
3. If it belongs to one skill, edit that skill's `SKILL.md` here in the repo. Put the rule in the section it belongs to, written as an instruction the skill will follow next time. Bump the version comment under the frontmatter. Because the skills are symlinked, the edit is live, no reinstall needed for Claude Code. Tell Neil if the Claude.ai copy needs re-uploading too.
4. If it is cross-cutting, log it and tell Neil whether this `CLAUDE.md` should change and what the edit would be. Do not edit `CLAUDE.md` unprompted.
5. Report back in one or two lines. Which skill changed, or "logged only, cross-cutting". No recap of the reasoning.

## Systems outside this repo

The brain describes these, it does not contain them. See `knowledge/systems-map.md`.

- Airtable CRM, base `apprk3RUXdvZNJ8TF` — live client and pipeline data.
- Google Drive `Mega Claude Cowork/` — client folders, proposals, templates, transcripts. Read-only unless Neil says otherwise. Anything new Claude writes there goes in `Claude Outputs/`.
- Cost Model V10 sheet `1vN5YckOTYgne0yppRkfm2jYBjPp1ff6ug8gWntLeS8k` — margin-check every agreed price against it.
- Fathom, Gmail, Calendly, Riverside — call recordings, mail, bookings, audio.

If a connector for one of these is not authorised in the session, say so rather than guessing at the data.

## Layout

- `README.md` — identity doc
- `INDEX.md` — map of the brain
- `knowledge/` — durable facts: voice, voice of customer, offer and pricing, systems, lessons
- `skills/` — the reusable skills that do the work
- `workflows/scheduled-tasks/` — the automations that run on a schedule
- `prompts/` — one-off prompt templates
- `docs/` — notes and handovers about the brain itself
- `scratch/` — working files, never a source of truth

## Working rules

- Durable facts go in `knowledge/`. Anything half-formed goes in `scratch/`. Never let `scratch/` be cited as truth.
- One topic per file. Short. Markdown. Clear headings.
- When a fact changes, update the file that owns it and note the date. Do not leave two versions in two places.
- Commit in small, described chunks. Do not push unless asked.
- Drafts for clients are drafts. Never send an email, post or message without Neil saying yes to that exact text.
