---
name: client-first-batch-email
description: Draft the "first batch of chapters is ready to listen" email a Me & My Old Man family gets partway through editing, once the first tranche of their audio documentary chapters is ready. Trigger on "draft the listening email for [family]", "first batch email for [family]", "chapters are ready, email the family", or when Neil shares a chapter/duration list (like a Riverside or editing tracker screenshot) and asks for the family email. Distinct from editor-briefing (internal, to the editor) and client-handover (end of project, consent/referral) — this is the mid-project "go and listen" email to the family itself.
---
<!-- v1.0 — created 2026-09-28 -->

## When to use

The family has had one or more chapters of their audio documentary edited and approved, and Neil wants to send them the batch to listen to. There will usually be more chapters still to come. Trigger even on terse asks ("send the Griffiths their next chapters") — the shape of the email is fixed, only the specifics change.

## Before drafting anything

1. **Identify the family unambiguously.** Do not rely on a Fathom recap snippet, a search-result match, or a surname that sounds like another client's (e.g. Best/Beard are two different real families — do not confuse them). Confirm the family and their actual email addresses from one of:
   - Their onboarding email ("The everything you need to know" email, sent to all family members at project start)
   - Their folder under Google Drive Shared Drive > Families > [Surname] > checking who the parent/children on the project are
   - Airtable CRM record for the family
2. **Find their "04 Stories" folder.** Every family folder in Shared Drive > Families > [Surname] has a `04 Stories` subfolder — this is what "On this link" points to. Find it by searching Drive for the family surname folder, then locating the `04 Stories` child folder inside it. Never guess or reuse another family's folder link.
3. **Get the exact chapter titles and durations** from what Neil gives you (a screenshot of the editing tracker/Riverside export, or a message). Never invent, composite, or borrow a chapter title or duration from another family's project.
4. **Get the Wrap Up date** from what Neil tells you — don't guess it.
5. Read `README.md` and this file only — this is short, mechanical client comms, not a case for pulling the full voice profile, but keep British spelling and the site's usual warmth.

## Duration format

Round each chapter duration to the **nearest whole minute**, drop the seconds and the colon, and write it as `59"` (not `59:01`, not `1:01:45`, not `59 mins`). Round 30+ seconds up, under 30 seconds down. For durations over an hour, convert fully to minutes (e.g. `1:01:56` → `62"`, though check Neil's own figure if he's given you the number directly — his stated duration always wins over your own recalculation).

## Template

Subject: **It's time to start listening**

```
Hello family,

It is with great pleasure that I now share with you the first batch of treats - hot out of the oven!!

On this link, you will find the following chapters of Dad's Life Story (as detailed below), or rather, your family's stories.
The final [N] chapters will come before the weekend.

Chapters
Ch1. [Title] ([mins]")
Ch2. [Title] ([mins]")
...

3 Recommendations for listening

1. Download to your device (phone) to avoid interruptions from incoming calls or Wi-Fi, which could cause you to lose your place
2. Use headphones for the full immersive experience
3. Check the chapter's duration before starting and tell your partner you're going to be out-of-action. Then take a long walk, get out in the garden, or brew a nice cuppa

Our Family Wrap Up & Reflections Session
We have this booked in for [date]. Ahead of that session, I will be asking you to share with me some reflections on:

- What delighted or surprised you?
- What do you want to know or share more about?

Next Step
Please acknowledge receipt.
I hope to share the final [N] chapters before the weekend.

Thanks,
Neil
```

- "On this link" hyperlinks to the family's `04 Stories` Drive folder.
- "Dad's Life Story" — swap for "Mum's Life Story" or the correct framing if the parent being interviewed is not "Dad".
- Only include the "Additional points" asks (photo uploads, favourite-photo requests) seen in some past examples (e.g. Griffiths) if Neil explicitly asks for them for this family — they are not part of the standard template and must never be copied over from another family's email.
- Build as HTML (`<b>`, `<ul><li>`) when creating as a Gmail draft, not markdown.

## Delivery

Create as a Gmail draft (never send outright — Neil always sends client-facing drafts himself after reviewing). Report back in one or two lines: which family, which chapters, and the draft link. No recap of the reasoning.
