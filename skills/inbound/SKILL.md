---
name: inbound
description: "Weekly scan of Neil's Gmail for inbound leads he has not spotted: someone he does not know, or knows only as a Kit subscriber, who has written in showing interest. Reads the content, not the sender list, decides who is a prospect, makes sure they are in Airtable, drafts the three-touch drip as Gmail drafts, sets a Trello card with a deadline for each touch, and sets the fork and the Lapsed decision. Use when Neil says 'inbound', 'scan my email for leads', 'any new enquiries', 'did anyone reply to the guide', 'add [name] as a prospect', or on the Thursday morning routine. Dated lead-magnet and Kit replies, LinkedIn-post enquiries, 'how much' emails, referrals and cold interest all count. mmom-sales-hustle owns every chase after the first drip, mmom-follow-up holds the voice rules."
---
<!-- v1.0 — 2026-10-15: built from the Sapna Nundloll miss (replied to the 107 Questions guide on 8 Oct about rebuilding things with her parents and sisters; Kit had made an Airtable row, Neil's reply carried no ask, nothing was ever scheduled). Best of the small-business lead-triage skill folded in: rank by signal, say plainly when the signal is flat, drafts never sent, nothing changed without a yes. -->

# Inbound

A lead is anyone who writes in, or replies, and shows interest in what Neil does. The test is reading what they said. Not whether they are in a CRM, not the subject line.

## Read first, every run

1. `knowledge/offer/follow-up-playbook.md` (the ladder).
2. `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` in full, and `knowledge/lessons.md`. Load `mmom-voice-check` before drafting a word.
3. `knowledge/offer/pricing.md` only if they asked "how much". Then the range rule in the playbook applies.

## 1. Scan

Gmail, last 7 days (8 on the Thursday run, so nothing falls between weeks), both directions. Search inbox excluding promotions, social and updates, then check the Kit "Your guide" replies and any thread with a Kit or Calendly sender separately. Also look at threads Neil has sent a reply to that carry no question or next step. That is the Sapna shape: he answered, she was never asked anything.

Skip without comment: current clients and their families, editors, suppliers, the UK Audio Network list, calendar acceptances, newsletters, anyone already on the live ladder with a dated next step.

## 2. Decide: prospect or not

Read each candidate thread and sort into one of four buckets.

- **Prospect.** A person Neil does not already work with who has said something about their own situation or asked a question about the service, the price, the process or a call. Strong signals, in order: asked for a call or a price; named a parent, sibling or family situation in their own words; replied to a lead magnet or newsletter with anything personal; thanked Neil and said it sounds like what they need. Weak signals: "great idea", a one-line thank-you, an out-of-office.
- **Warm, not yet a lead.** Friendly, no family situation, no ask. One human reply with a real question (see the DM rules in `mmom-sales-hustle`), no ladder.
- **Not a lead.** Press, vendors, peers, spam. List by name in one line.
- **Already handled.** In Airtable with a dated next step. One line, nothing to do.

Rank the prospects by signal strength, strongest first. If every prospect has the same weak signal and there is nothing to separate them, say so plainly and order by date received. Never present a ranking that the evidence does not support.

## 3. For each prospect, same turn

1. **Airtable** (base `apprk3RUXdvZNJ8TF`, table `tblFy3hGmEDRBgExi`). Search by email and by surname first. If the row exists, update it. If not, create it, and ask Neil for Lead Source in one line, never pick one. Kit rows arrive with Lead Status New and no history: set Engaged, Stage Pre-Sales, Channel, Knows Me, Type Lead, Follow-up Date, Last Action with the real date, and paste the lead's own words and phone number into the notes field. Never create a duplicate.
2. **Temperature line before any draft.** Moving or stalled, who they are to Neil, what they said in their words, the real next step. Show it in the output.
3. **Drip as three Gmail drafts**, replies in the existing thread where there is one. Voice and rung briefs are in `mmom-sales-hustle`. Touch 1 within 1 to 2 days (answer what they said, one ask, a 20-minute chat with two real times from Google Calendar in their timezone plus the Calendly link as backup). Touch 2 three to four days later (one new thing, never a re-send). Touch 3, the fork, four to five days after that, ending on the diary link. Never invent a family story or reuse a client's without consent.
4. **Trello Inbox cards, one per touch**, due 9am UK on the day, named "<Lead>: touch N via <channel>". Description carries the deadline, a line of context, the Gmail draft link and the Airtable record id. Touches 2 and 3 say "only if no reply".
5. **The decision.** When the fork has gone and there is no booking after about two weeks, the row goes to Temp Lapsed and into the no-ask drip. A reply or a booking at any point cancels the remaining touches: Neil tells Claude, Claude archives the cards, deletes the unsent drafts and moves the row to the right stage.

A lead who asks "how much" gets the per-parent range in the message, exact figure on the call. A lead whose email suggests a difficult family situation (estrangement, illness, bereavement) gets a softening aside from Neil before the question, and no lead magnet.

## 4. Output

One table, nothing before it: Lead | How they came in | What they said (their words) | Signal | Airtable | Drafts and cards. Below it, prospects ranked with one line of talking point each. Then "Not leads" and "Already handled" as single lines. Then the touch 1 draft text for each new prospect and two alternative opening lines. If there is nothing new, say "No new inbound this week" and list what was checked.

## Gates

- Claude never sends. Drafts and cards only.
- Never change a lead's stage to Won or Lost, and never mark Lapsed, without Neil's yes (the fork-then-two-weeks rule is the exception, and still only proposed).
- Never create a calendar event for a lead without a yes.
- If the Gmail connector or Airtable is not authorised in the session, say so and stop, do not guess.
- Log any correction in `knowledge/lessons.md` the same turn and edit this file, bump the version comment.
