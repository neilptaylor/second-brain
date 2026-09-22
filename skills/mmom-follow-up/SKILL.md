---
name: mmom-follow-up
description: "Me & My Old Man sales follow-up engine. Use this skill whenever Neil wants to follow up, chase, nudge, or re-engage a prospect or client — or write any post-call, post-proposal, or post-delivery message. Triggers: 'follow up with [name]', 'chase [name]', '[name] has gone quiet', 'day 10 chaser', 're-engage', 'lapsed prospect', 'drip', 'WhatsApp voice note for', 'welcome email for [new client]', 'thank you email', 'referral ask'. If a named person owes Neil a reply or has just said yes, this is the skill."
---

# MMOM Follow-Up Engine

You write the messages that keep Neil's pipeline moving without making him sound like a CRM. Every message must pass one test: would Neil send this to an old friend he happens to be in business with?

---

## Read first, every run — non-negotiable

1. `About Me/VOICE_PROFILE_Neil_Taylor.md` — in full. Never from a summary.
2. `About Me/VOC_Intelligence_System.md` — customer language is the raw material.
3. `Lessons/lessons.md` — don't repeat a logged mistake.
4. `About Me/skills/mmom-sales-strategist/references/sales-process.md` — follow-up frameworks and pricing logic.
5. **The prospect's own words.** Find their folder in:
   `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/Shared drives/Systems/03 Sale/02 Sales Call/`
   (folders are `YYYYMMDD FirstName LastName` — fuzzy match, take most recent). Read the transcript. Their exact phrases about their parent are the hook of every follow-up.
6. **CRM row** — search Google Drive for "Full CRM-SALES TRACKER". Confirm last action, last date, and stage before writing a word. Never guess where a prospect is in the pipeline.

If the transcript or CRM row can't be found, say so and ask Neil — never invent the history.

---

## Inputs

- **Who** (name — required)
- **What happened last** (from CRM/transcript; confirm with Neil if ambiguous)
- **Mode** (detect from context, or ask):

## The five modes

### 1. CHASER — proposal sent, gone quiet
The ladder. Match the message to the silence:

- **Day 3–5 (first nudge):** Light, warm, zero pressure. One specific detail from their call ("been thinking about what you said about your mum's laugh"). One soft question. No re-pitch, no price.
- **Day 10 (second touch):** Add one new thing of value — a relevant client story, a clip, the 107 Questions guide. Still no "just checking in". The value IS the message.
- **Day 21–24 (the fork):** "The Chase vs The Let Go." Switch channels (email → WhatsApp, or the reverse) and REMOVE the ask entirely. Something human: a story, a genuine question about their parent, a "no agenda, just thought of you". If this doesn't land, move them to Let Go.

**Rules:** never two asks in a row. Never "did you get my proposal?". Never apologise for following up. Never discount to break silence.

### 2. WHATSAPP VOICE NOTE SCRIPT
30–60 seconds, written for the ear. Long sentence building, short sentence landing. Open with their detail, not Neil's news. Include a stage direction line at the top: (tone: warm, unhurried, one smile in it). End with one clear, small next step or none at all.

### 3. LAPSED RE-ENGAGEMENT — 30+ days silent
The Let Go done well. No reference to the silence, no guilt, no "circling back". Lead with something genuinely worth having (new lead magnet, a story from a recent family, a podcast clip). The message must work even if they never reply. One per 4–6 weeks maximum. Long-term nurture beats pursuit.

### 4. NEW CLIENT WELCOME
The moment after yes. Warm, specific, zero buyer's remorse. Confirm what happens next in plain steps (Setup → Stories → Savour), name the first concrete date, and land one line about what this will mean for their family — using THEIR words from the sales call. This message sets the tone for 12 weeks.

### 5. THANK-YOU + REFERRAL ASK
Post-delivery. Lead with the specific moment from their experience (from wrap-up call or testimonial). The referral ask is one question, framed as "who else quietly needs this", never "do you know anyone who might be interested in our services". If a testimonial hasn't been captured, fold that ask in instead — one ask per message, never both.

---

## Output — every run

Save to `Claude Outputs/Sales Follow-Ups/MMOM_FollowUp_[FirstName]_[mode]_v1.md` (increment version, never overwrite):

```
CHANNEL: [email / WhatsApp text / WhatsApp voice note]
TIMING: [when to send and why, one line]

[The message, ready to send. Subject line if email.]

---
Why this works: [one line — the psychology, not a lecture]
Alternative opener 1: [different first line]
Alternative opener 2: [different first line]
Watch for: [what a reply / continued silence means for the next step]
```

Neil swaps openers more than he rewrites. Always give him the two alternatives.

---

## Voice rules (enforced)

- No em dashes anywhere. Full stop, comma, or restructure.
- Banned: preserve, legacy, heirloom, keepsake, treasure, process (say "experience"), "just checking in", "circling back", "touching base", "hope this finds you well", "gentle reminder".
- British, warm, specific. If there's no concrete detail from THEIR life in the message, it isn't ready.
- "We" not "you" — Neil's in the sandwich generation too.
- Factual accuracy is non-negotiable: triple-check names, parents' names, dates, and what was actually said on the call before it goes in a message.
- Pain paired with possibility, always. A follow-up is a door left open, not a hand on the shoulder.
