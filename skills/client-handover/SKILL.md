---
name: client-handover
description: Runs the handover moment at Me & My Old Man — the 30-minute Calendly call ("The Handover 30mins") booked at project start and held once every chapter is edited and all assets (audio documentary, album artwork, "It's a Wrap" ebook) are ready. Prepares the family's consent & referral tracker doc before the call, gives Neil the call agenda and exact referral script, and after the call hands off into the referral-page skill for any family who consented and gave names. Trigger when Neil says "handover for [family]", "prep the handover call", "handover agenda", or is about to run or has just run a family's Handover 30mins call.
---

<!-- v1.0 — 2026-09-25: built from the Griffiths handover call. -->

## What this call is

The last live touchpoint on a project. Everything is delivered — audio documentary, album artwork, "It's a Wrap" ebook. This 30 minutes does three jobs: hand the work over, lock consent so testimonials/clips are usable, and ask for referrals while the family is at peak goodwill.

Biggest failure mode this skill exists to prevent: a family that's extremely engaged during the project goes quiet the moment it's delivered, and Neil can never get consent or a referral out of them again (the Bortner family, logged 2026-09-25). Everything below is built to close that gap live, on the call, not chase it afterwards.

## Before the call — prep

1. Find or create the family's **Consent & Referral Tracker** doc, saved in their Drive project folder. HTML build (per root CLAUDE.md — never plain-text markdown upload), one column per family member, one row per consent line:

   1. Video of them talking on camera — reflection or family story
   2. Audio of them talking — reflection or family story
   3. Video testimonial of the service
   4. Audio testimonial of the service
   5. Text testimonial
   6. LinkedIn post (offer to draft it for them)
   7. Instagram post
   8. LinkedIn recommendation (send the step-by-step guide there and then)
   9. Know any journalists?

   Plus a Referral section (names mentioned, live) and a Follow-up section (15-min check-in date). See the Griffiths tracker as the reference build.

2. **Read `knowledge/offer/pricing.md` before the call for the current Snapshot figure.** The referral incentive is a free Snapshot session — as of 22 Sep 2026 it sells at £300 and anchors at £750. Say the anchor (£750) as the "normally" figure, never the sell price — that's the value being given away. Check this every time; it is not to be remembered from a past call.

3. The 48-hour reminder email goes out automatically (`handover-reminder-watcher` scheduled task, runs daily 8am, drafts into Gmail, never sends) once the call is within ~48 hours. Neil reviews and sends it himself. If a call is imminent and no draft exists yet, draft it directly using the template in that task's SKILL.md.

## The call agenda (30 min)

**1. The walkthrough (5 min)** — show them everything: audio documentary, artwork, ebook. Let them react first.

**2. Consent (10 min)** — go through the 9-line list above out loud, mark the tracker doc live, one column per person. Get a yes/no on every line for every person before moving on. Nothing left as "I'll follow up."

**3. Referral (10 min)** — say close to verbatim:

> "Before we wrap up — I want to ask you something important. You know the free Snapshot session I mentioned? Worth [current anchor from pricing.md], normally. I give one of those to any family you refer.
>
> So genuinely — who's coming to mind right now? Doesn't have to be a firm yes from you today, just names.
>
> A few angles, in case it helps:
> - Your partner's side of the family — anyone there?
> - A close friend, someone you'd naturally tell about this anyway
> - Anyone you know going through a hard diagnosis, or an ageing parent — this tends to matter most exactly when time feels short
> - Any groups you're part of — a parents' group, a hobby club, a community or church group
>
> Who's the first name that comes to mind?"

Stop talking. Write every name down live, on the tracker doc, under Referral.

Once there's a name: "Here's exactly what I'll send them, so you know: '[name of your family], I'm Neil. I've just finished a project with [Family], capturing their parent's life story as an audio documentary. They loved it and thought of you. Here's more info.' I'll send it once, then one follow-up, then I'll leave it."

Then explain the `/refer-[family]` page: built from what they just consented to, personalised with their own story quotes, ready to send on.

**4. Close (2 min)** — confirm when the page goes live. Book the 15-minute check-in **now, live on the call**. This is the fix for the Bortner failure — the gap is between "call ends" and "someone next finds time to chase."

## Calendly

The event's own description (`thehandover-30min`, https://calendly.com/meandmyoldman/thehandover-30min) should mirror the current mechanic — currently the free Snapshot session at the pricing.md anchor, not any older discount/donation offer. If pricing.md's Snapshot figure changes, update the Calendly description in the same sitting (`event_types-update_event_type` on connector a0a8a416-4d7c-4f66-9323-904a97c35f78, uri https://api.calendly.com/event_types/44f9086d-8936-4340-bb90-bd1c9e628e2d) — don't let it drift like the last version did.

## After the call

- Update the tracker doc with every answer, live during the call, not from memory afterwards.
- Any consented testimonial/story/referral name goes to the **referral-page** skill to build or update that family's `/refer-[family]` page.
- Book the 15-min check-in as a real calendar event before the call ends, not a mental note.
- If Neil corrects anything about how this call went — a line that landed badly, a question he added, a consent level that needs splitting — log it in `knowledge/lessons.md` the same turn and fold the fix back into this SKILL.md, per the CLAUDE.md skill feedback loop.
