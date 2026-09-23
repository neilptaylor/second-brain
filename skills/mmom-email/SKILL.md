---
name: mmom-email
description: Universal email-writing gate for Me & My Old Man. Use this whenever Neil asks to write, draft, reply to, or send any email — a Gmail draft, a reply to a fan/prospect, a catch-up with a friend, an editor briefing/handoff, or a press/PR pitch. Loads EMAIL_VOICE_Neil_Taylor.md, identifies which of the four email sub-tones applies, and drafts in Gmail. Distinct from mmom-follow-up (which is specifically for chasing/re-engaging sales prospects) — this is the entry point for ANY email, sales-related or not.
---
<!-- v1.0 — 2026-09-23: created. First skill to own knowledge/voice/EMAIL_VOICE_Neil_Taylor.md, built same day from three fan-reply drafts plus a scan of the prior week's sent mail. -->

# MMOM Email Skill

Every email Neil asks for, or asks Claude to draft/reply to, routes through here first.

## Step 1: Read the voice doc

Always read `knowledge/voice/EMAIL_VOICE_Neil_Taylor.md` in full before drafting. Do not work from memory of it, it gets extended over time and a stale summary will miss the latest correction.

## Step 2: Identify the sub-tone

The doc defines four registers. Pick one before writing a word:

1. **Incoming reply** — strangers, fans, podcast listeners, curious non-buying prospects who emailed first.
2. **Friend / personal** — people Neil actually knows outside MMOM ops (old colleagues, TERN alumni, school friends).
3. **Editor / ops** — Vuk, Abhi, Jodie (editor), or any production collaborator. Task-and-deliverable, brisk.
4. **Pitch / outreach** — journalists, PR, press, cold or semi-warm gatekeepers (Saga, the Independent, Telegraph, etc.).

If the recipient relationship is ambiguous, ask Neil which register applies rather than guessing. Getting this wrong (e.g. editor-brisk tone to a grieving fan, or breezy-friend tone to a journalist) is worse than pausing to check.

If the email is a sales follow-up/chase to a lapsed or active prospect specifically, hand off to `mmom-follow-up` instead, that skill owns the sales-chase cadence and objection-handling logic. This skill (`mmom-email`) is for everything else, plus the general "write me an email" case.

## Step 3: Draft in Gmail, never send

Create the draft via the Gmail connector. Never send on Neil's behalf, per the standing rule that drafts for clients (and everyone else) are drafts until Neil says yes to the exact text.

## Step 4: The mechanical last step, every single time

Before handing the draft back:
- Em-dash sweep. Zero em dashes, anywhere, no exceptions. Replace with a comma, a full stop, or a restructure.
- Check against the banned-word list in the core VOICE_PROFILE_Neil_Taylor.md (preserve, legacy, heirloom, keepsake, process, "stopped me cold" family, "gold," "sit with," etc.) — these apply in every sub-tone, including pitches.
- Confirm the sub-tone's specific patterns were followed (see the table and examples in EMAIL_VOICE_Neil_Taylor.md).

## The feedback loop

Whenever Neil rewrites or corrects an email this skill produced, that's signal for the same-turn logging rule in root CLAUDE.md:
1. Log it in `knowledge/lessons.md` immediately.
2. If the correction reveals a new pattern in one of the four sub-tones, add it to `knowledge/voice/EMAIL_VOICE_Neil_Taylor.md` in the relevant section, with the verbatim before/after where useful. Small, incremental additions are the whole point of this doc, it should keep getting more accurate.
3. Bump this file's version comment.
4. Report back in one line: which sub-tone, what changed.
