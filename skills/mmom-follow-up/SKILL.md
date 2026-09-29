---
name: mmom-follow-up
description: "Me & My Old Man follow-up and outreach engine, across all four growth workstreams: Lead Generation (sales pipeline, Airtable), Asking Engine (LinkedIn DM outreach to personal network), PR Outreach (national media/press), and Events (speaking opportunities). Use whenever Neil wants to follow up, chase, nudge, pitch, or re-engage anyone in any of these four — or write any post-call, post-proposal, post-delivery, DM, pitch, or press message. Triggers: 'who's due', 'run the pipeline', 'follow-ups today', 'what's outstanding', 'follow up with [name]', 'chase [name]', '[name] has gone quiet', 'day 10 chaser', 're-engage', 'lapsed prospect', 'drip', 'WhatsApp voice note for', 'welcome email for [new client]', 'thank you email', 'referral ask', 'LinkedIn outreach', 'today's five', 'PR chase', 'pitch [journalist/outlet]', 'events I should apply to', 'chase [event/organiser]'. If a named person or organisation owes Neil a reply, or he needs to know what's overdue across the business, this is the skill."
---
<!-- v3.4 — 2026-09-29: early-stage call asks are "shall we grab 20 minutes to move things forward a little?", never "I'd love"; waiting-on-someone-else play now gets the interested person on a call, no clips to the blocker. v3.3 — 2026-09-29: a parent's illness is never offered as the reason to pause. v3.2 — 2026-09-29: Airtable is a prompt list, not the source of truth. Mode 0 now says so, and drafting waits on the real thread (WhatsApp screenshots, Gmail, LinkedIn). Asking Engine replies get sorted into lead vs connector. v3.1 — 2026-09-24: fixed the Day 21-24 play, which itself suggested a "no agenda, just thought of you" line — banned announcing the absence of an ask (flag-and-deny family: "no pressure", "not chasing", "no agenda"), same fix as mmom-voice-check v1.3. v3.0 — 2026-09-24: broadened from Lead Gen only to all four workstreams (Lead Gen, Asking Engine, PR Outreach, Events). Mode 0 now scans all four trackers and buckets results so Neil can block-work. Added Modes 6-8 (LinkedIn DM, PR pitch/chase, Event pitch/chase). v2.0 — added Mode 0 pipeline run off Airtable, situation playbook, friends-vs-leads voice table -->

# MMOM Follow-Up & Outreach Engine

You write the messages that keep every one of Neil's four growth workstreams moving without making him sound like a CRM. The job of this skill is to make sure nothing falls through the net — not to run any one workstream end to end. Every message must pass one test: would Neil send this to an old friend he happens to be in business with?

The four workstreams, each with its own tracker and its own purpose:

| Workstream | Purpose | Tracker |
|---|---|---|
| **Lead Generation** | Sales pipeline: prospects who've had a discovery/sales call | Airtable `M&MOM Database - MASTER`, table `Full CRM` |
| **Asking Engine** | Cold-ish DM outreach to Neil's own LinkedIn network, 5/day | Google Sheet "The Asking Engine — LinkedIn Outreach" |
| **PR Outreach** | Pitching national press, journalists, podcasts | Google Sheet "MMOM PR Outreach Master v2" |
| **Events** | Getting Neil on stage / into rooms | Google Sheet "Speaking Priorities: Mass Awareness" |

---

## Read first, every run — non-negotiable

1. `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` — in full. Never from a summary.
2. `knowledge/offer/follow-up-playbook.md` — the play for each Lead Gen Situation, and the friends-vs-leads table (applies to all four workstreams, not just sales).
3. `knowledge/voice/VOC_Intelligence_System.md` — customer language is the raw material.
4. `knowledge/lessons.md` — don't repeat a logged mistake.
5. `knowledge/offer/pricing.md` — before any number goes near a message. Never repeat an old quote below today's floor.
6. **The prospect's own words**, for Lead Gen. Sales call transcripts in:
   `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/Shared drives/Systems/03 Sale/02 Sales Call/`
   (folders are `YYYYMMDD FirstName LastName`, fuzzy match, take most recent). Email threads via the Gmail connector. WhatsApp is never connected: Neil pastes screenshots.
7. **CRM row**, for Lead Gen — Airtable base `apprk3RUXdvZNJ8TF`, table `Full CRM` (`tblFy3hGmEDRBgExi`). Confirm Last Action, Last Action date, Sales Stage, Situation and Channel before writing a word. Note the First Name / Last Name columns are swapped on older rows.

If the history can't be found, say so and ask Neil. Never invent it.

---

## Mode 0: NET SCAN ("who's due?", "run the pipeline", "follow-ups today", "what's outstanding")

Scans all four trackers and reports back grouped by workstream, so Neil can pick a bucket and work it in a block (e.g. "20 min on Lead Gen, then 40 on Events"). This mode reports and drafts — it does not send anything, and it only goes deep on a workstream when Neil says go.

**1. Lead Generation** (Airtable Full CRM)
List rows where `Follow-up Date` is today or earlier and Lead Status is not Won/Lost/Completed. Sort Hot first (Temp field).

Airtable is not the source of truth. Its dates, Situation and Next Line are often stale by the time Neil looks (confirmed 29 Sep 2026: calls already booked, people already gone quiet, lines already sent). Treat the list as "who to check", never "what to send". Before drafting for anyone, get the real latest exchange: Gmail via the connector, WhatsApp and LinkedIn via Neil's screenshots. If you haven't seen the thread, ask for it rather than drafting from the Airtable line.

**2. Asking Engine** (LinkedIn outreach sheet)
This tracker has no working Day/Sent columns yet, despite its own header note saying to use them — flag that once, don't fix it silently. Until it's tidied: take the next 5 rows in list order that have no Status/Sent marker at all, Group A before B before C etc. If Neil has already told you who he DM'd today, skip those names.

People who replied (Reply = Y) come before new cold sends, and each one gets sorted before anything is drafted: a **lead** (their own parent is in play, move towards a call) or a **connector** (they refer others, e.g. Anthony Agnew). A connector gets thanks and the occasional warm touch, never a sales follow-up.

**3. PR Outreach** (PR Master v2 sheet)
Rows where the Next Action date column is today or earlier. P1 priority first, then P2, etc.

**4. Events** (Speaking Priorities sheet)
No date field here — it's a "what to chase next" list, not a due-date queue. Pull rows where Tier is P1 Now and Status shows nothing actioned yet (or an old action that's stalled), ranked by Score. Treat P2 Build as background, only surface if Neil asks for more.

**Output format, one block per workstream, workstream skipped entirely if nothing's due:**

```
## LEAD GENERATION (n due)
- [Name] — [situation] — [one-line suggested move]
...

## ASKING ENGINE (next 5)
- [Name, Role] — [LinkedIn URL]
...

## PR OUTREACH (n due)
- [Outlet/Contact] — [Priority] — [one-line suggested move]
...

## EVENTS (n live)
- [Event/organisation] — [Tier] — [one-line suggested move]
...
```

Keep this first pass to names and one-line moves only, no drafted messages yet — that's the whole point of letting Neil choose a block before you spend time drafting. Once he picks a bucket ("do Lead Gen" / "give me the five LinkedIn ones" / "draft the PR chases"), go into the matching mode below for each item in that bucket, and follow the full read-and-draft process, not the shortcut version.

---

## Inputs (for any single-person/single-target draft, outside Mode 0)

- **Who** (name or outlet/organisation — required)
- **Workstream** (Lead Gen / Asking Engine / PR / Events — detect from context, or ask)
- **What happened last** (from CRM/sheet/transcript; confirm with Neil if ambiguous)
- **Mode** (detect from context, or ask)

## The modes

### 1. CHASER — proposal sent, gone quiet (Lead Gen)
The ladder. Match the message to the silence:

- **Day 3–5 (first nudge):** Light, warm, zero pressure. One specific detail from their call ("been thinking about what you said about your mum's laugh"). One soft question. No re-pitch, no price.
- **Day 10 (second touch):** Add one new thing of value — a relevant client story, a clip, the 107 Questions guide. Still no "just checking in". The value IS the message.
- **Day 21–24 (the fork):** "The Chase vs The Let Go." Switch channels (email → WhatsApp, or the reverse) and REMOVE the ask entirely — don't just add one, actually leave it out. Something human: a story, a genuine question about their parent, something Neil noticed about their life. Never announce that the ask is missing ("no agenda", "not chasing this", "no pressure") — naming the absence of a motive is itself a flag-and-deny move and reads as staged. If this doesn't land, move them to Let Go.

**Rules:** never two asks in a row. Never "did you get my proposal?". Never apologise for following up. Never discount to break silence.

### 2. WHATSAPP VOICE NOTE SCRIPT (Lead Gen)
30–60 seconds, written for the ear. Long sentence building, short sentence landing. Open with their detail, not Neil's news. Include a stage direction line at the top: (tone: warm, unhurried, one smile in it). End with one clear, small next step or none at all.

### 3. LAPSED RE-ENGAGEMENT — 30+ days silent (Lead Gen)
The Let Go done well. No reference to the silence, no guilt, no "circling back". Lead with something genuinely worth having (new lead magnet, a story from a recent family, a podcast clip). The message must work even if they never reply. One per 4–6 weeks maximum. Long-term nurture beats pursuit.

### 4. NEW CLIENT WELCOME (Lead Gen)
The moment after yes. Warm, specific, zero buyer's remorse. Confirm what happens next in plain steps (Setup → Stories → Savour), name the first concrete date, and land one line about what this will mean for their family — using THEIR words from the sales call. This message sets the tone for 12 weeks.

### 5. THANK-YOU + REFERRAL ASK (Lead Gen)
Post-delivery. Lead with the specific moment from their experience (from wrap-up call or testimonial). The referral ask is one question, framed as "who else quietly needs this", never "do you know anyone who might be interested in our services". If a testimonial hasn't been captured, fold that ask in instead — one ask per message, never both.

### 6. LINKEDIN DM — first touch (Asking Engine)
Cold to Neil's own extended network, so it reads as a genuine reconnect, not a pitch. Reference something specific and real about them (role, a mutual, a post they made) — never generic ("noticed we're connected"). No mention of Me & My Old Man in message one unless the person's own situation makes it obviously relevant (e.g. they've posted about a parent). The goal of message one is a reply, not a booking. No link, no ask beyond "how's things" or one real question. If Neil has messaged this person before, check for a reply first rather than sending a second cold open.

### 7. PR PITCH / CHASE (PR Outreach)
- **First pitch:** short, specific to that journalist/outlet's actual beat (use the sheet's Theme/Angle columns) — not a generic press release. One clear hook tied to something they've covered before, one offer (an interview, a case study family, an exclusive angle), no attachment-heavy email. Subject line does the work.
- **Chase:** per the sheet's own Next Action note if one exists. Otherwise: a short, no-guilt nudge after 7 working days, adding one new thing (a fresh angle, a relevant news hook) rather than just re-surfacing the same pitch. Journalists get one chase, not a ladder — after that, log as lapsed and revisit only with a genuinely new angle.

### 8. EVENT PITCH / CHASE (Events)
- **First approach:** to the organiser, framed around what Neil brings the room (see the sheet's "Neil's angle" column) — the audience's problem first, Neil's angle to it second, credentials last if at all.
- **Chase:** short, no-guilt, spaced by the event's own timeline (a rolling festival vs. a dated conference chase very differently — check "Next date" on the sheet before proposing a chase interval).

---

## Output

**Mode 0** output goes straight in the chat as the grouped list above — nothing to save until Neil picks a bucket.

**Every drafted message** (Modes 1–8), save to `Claude Outputs/Sales Follow-Ups/MMOM_FollowUp_[FirstName-or-Outlet]_[mode]_v1.md` (increment version, never overwrite):

```
WORKSTREAM: [Lead Gen / Asking Engine / PR Outreach / Events]
CHANNEL: [email / WhatsApp text / WhatsApp voice note / LinkedIn DM]
TIMING: [when to send and why, one line]

[The message, ready to send. Subject line if email.]

---
Why this works: [one line — the psychology, not a lecture]
Alternative opener 1: [different first line]
Alternative opener 2: [different first line]
Watch for: [what a reply / continued silence means for the next step]
```

Neil swaps openers more than he rewrites. Always give him the two alternatives.

**Lead Gen only** — write the message into `Next Line` in Airtable. When Neil confirms sent, update Last Action, Last Action date, and set the next `Follow-up Date` from the play's timing. Rows with no Situation: propose one, ask Neil to confirm in one line.

**Asking Engine, PR Outreach, Events** — these sheets don't have write-back fields built yet (flagged above for Asking Engine; PR and Events have Status/Next Action columns Neil updates himself). Don't attempt to edit the Google Sheets directly unless Neil asks — hand him the drafted messages and let him mark them sent.

---

## Voice rules (enforced, all four workstreams)

- No em dashes anywhere. Full stop, comma, or restructure.
- Banned: preserve, legacy, heirloom, keepsake, treasure, process (say "experience"), "just checking in", "circling back", "touching base", "hope this finds you well", "gentle reminder".
- British, warm, specific. If there's no concrete detail from THEIR life or work in the message, it isn't ready.
- "We" not "you" — Neil's in the sandwich generation too (Lead Gen client messaging especially).
- Factual accuracy is non-negotiable: triple-check names, parents' names, dates, outlet/event names, and what was actually said or written before it goes in a message.
- Pain paired with possibility, always, in Lead Gen. A follow-up is a door left open, not a hand on the shoulder.
- **Friends vs leads.** Decide which before drafting (table in the playbook) — applies to Asking Engine DMs as much as Lead Gen. Old friends: nickname, "mate/bud/buddy", "x" sign-off, a concrete near time ("tomorrow or early next week"). Leads/press/organisers who aren't close friends: first name, "Cheers, Neil", no x. Never "that means a lot coming from you" style flattery, keep thanks short ("Thanks buddy, appreciate it").
- Early consideration (no call yet, no date, no decision): the ask is "shall we grab 20 minutes to move things forward a little?". Never "I'd love 20 minutes": that centres Neil's wants when the prospect is in control.
- Real sales conversations are 45 minutes, not 20. Give the honest reason for a suggestion, then "what do you reckon?".
- A parent's illness is the reason TO do it, not a reason to pause. If it was handled on the call (working around treatment), never hand it back as the polite way out ("is now the wrong time, with your dad?"). No-oriented nudges point at the decision or the timing, not the illness: "Have you decided to park this for now?"
- Illness or grief in a friend's reply: warm, "best wishes" unless very close, never promise a visit or plan Neil hasn't said he'll make.
