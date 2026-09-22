---
name: mmom-podcast-pr
description: "Me & My Old Man podcast and PR engine. Use this skill whenever Neil is pitching himself to a podcast, journalist, or newsletter; preparing for a recorded appearance; or repurposing an appearance afterwards. Triggers: 'podcast outreach', 'pitch me to', 'guest brief', 'prep for [show/host]', 'I'm on [podcast] next week', 'PR email', 'journalist', 'press', 'two-pager', and after an appearance: 'turn this episode into posts', 'repurpose the podcast', 'clips from the interview', 'newsletter featuring the episode'. One skill for the whole loop: get booked → show up sharp → squeeze every drop afterwards."
---

# MMOM Podcast & PR Engine

Podcasts are Neil's highest-leverage channel: one hour of him talking naturally produces a month of content in his real voice. This skill runs the full loop in three modes. Detect the mode from context; ask if unclear.

---

## Read first, every run

1. `About Me/VOICE_PROFILE_Neil_Taylor.md` — in full.
2. `About Me/VOC_Intelligence_System.md` (or latest dated version in `Projects/Linkedin Strategy/`) — for audience language and proof points. Check the date on this file each time — pricing and offer names get updated, and a stale price quoted on air or in a brief is a real risk.
3. `Lessons/lessons.md` — don't repeat a logged mistake.
4. `Projects/Lead Magnets/` — know what lead magnets currently exist (titles + one-line description each) before proposing a new one. Don't propose a magnet that already exists under a different name.
5. For MODE 3 only: the downstream skills — `linkedin-post`, `newsletter`, `instagram` — each output must follow its channel's skill, not a generic summary format.

**Neil's canonical talking points** (the spine of every pitch and brief):
- Lost his dad in 2021 after three years of dementia; son born six days after. Tried and failed to capture his dad's story in time.
- 30+ families, 350+ hours of interviews. The experience is the product; the audiobook (say "audio documentary" if it comes up) is proof it happened.
- "Nobody stopped loving each other. Life just got in the way." / "The drift is natural." / "Stories, not skeletons." / "Stories that matter, with people you love."
- The sandwich generation squeeze — he lives it too. Running a business about presence that pulls him away from his own family. (This contradiction is allowed on air. It's the most trustworthy thing he can say.)

---

## MODE 1: OUTREACH — get booked

**Input:** show/journalist name (+ link if Neil has one).

1. **Research first.** Search the web for the show: host name, format, episode length, audience, 2–3 recent episode titles. Find the one recent episode closest to Neil's territory (family, midlife, meaning, mortality, fatherhood). If nothing checks out, tell Neil the fit is weak — don't force a pitch.
2. **Write the pitch email.** Structure:
   - Subject: specific and human, never "Guest suggestion" ("The 12-minute phone call most families mistake for connection")
   - One line proving Neil actually listened (name the specific episode and the moment).
   - Two lines of who Neil is, led by the story not the business.
   - Three bulleted angles HE can bring — framed as audience value, each one specific ("why every family thinks they have more time — and the maths of why they don't").
   - One-line close, zero pressure: "If it's a fit, I'd love to come on. If not, keeping listening either way."
3. **Output:** `Claude Outputs/Podcast/MMOM_Outreach_[ShowName]_v1.md` — email plus a 2-line LinkedIn DM version of the same pitch.

## MODE 2: GUEST BRIEF — show up sharp

**Input:** show name + recording date (and any show URLs Neil supplies — always use them as the starting point rather than searching cold).

### Step 1 — Research the show across its platforms, not just one page

A single homepage fetch is not enough — home pages are often thin on tone and back-catalogue signal. Work through as many of these as are findable, in this order, and stop early only once you have host name, tone, audience, and 3+ recent/relevant episode titles with real confidence:

1. **The show's own website** — homepage/about page AND a dedicated episodes/archive page if one exists (archive pages surface far more episode titles than the homepage).
2. **Any topic/category archive pages** on the site (e.g. a "family," "caregiving," "relationships," or "sandwich generation" category) — these are gold for finding the closest thematic cousin episode and confirming audience fit at a glance.
3. **YouTube channel**, if the show has one — check the channel description and recent video titles. Video titles sometimes reveal a more current or different episode slate than the website if the site hasn't been updated recently.
4. **Podcast platform listing** (Apple Podcasts / Spotify) — the show description here is often the most concise, current "what this show is" statement, and lists recent episodes with dates.
5. **A targeted web search for the host's name + the show name** — surfaces interviews, bios, or press the host has done elsewhere, useful for the "prove you did your homework" line.
6. **A search for listener reviews or testimonials** (host name + "review" or "testimonial") — reviews reveal tone in the audience's own words ("like hanging out at a coffee shop," "goofing off," etc.), which is more reliable than guessing tone from the host's own copy.

Cross-check dates: prioritise the most recent episodes over old back-catalogue hits, but note if the show has a distinct thematic category (e.g. Rock Your Retirement's "Sandwich Generation" archive) even if those specific episodes are older — categories reveal standing audience interest, not just recency.

If research surfaces conflicting signals (e.g. site says one tone, reviews say another), trust the reviews and recent episodes over the site's own marketing copy.

### Step 2 — Assess audience fit and calibrate brief length

Not every show deserves equal-length treatment. Before writing, judge fit:

- **Strong direct fit** (host's own territory overlaps Neil's — therapists, relationship coaches, family/midlife-focused shows): full-length brief, all five talking points fleshed out with context.
- **Adjacent fit** (broader lifestyle/retirement/midlife show where family connection is one thread among many): full-length brief is still warranted if the audience-fit case is genuinely strong (e.g. a whole back-catalogue category on the topic) — don't shorten just because the show is broader, shorten only when there's less genuinely new ground to cover.
- **When producing brief 2+ in the same request** (e.g. Neil is prepping for several shows back to back and one has already had a full brief written elsewhere, or the fit is clearly narrower): a condensed TLDR format is appropriate — host one-liner, audience one-liner, five points compressed to a phrase each, three questions, the plug, traps. Always state clearly that it's a condensed version and point to the full brief if one exists.

Use judgement, not a fixed rule — a weak-fit show with a genuinely novel angle can still earn a full brief; a strong-fit show Neil already knows well might only need a TLDR refresh.

### Step 3 — Build the brief

- **The host:** who they are, what they care about, one thing to mention that proves Neil did his homework (the "homework line").
- **The audience:** who's listening and which MMOM pain point/persona is theirs. If the show's audience naturally splits into two roles relevant to Neil's work (e.g. some listeners are the adult child, others are the parent generation), name both explicitly — don't default to only the adult-child framing.
- **Five talking points**, each mapped to a content pillar (Drift / Questions / Transformation / Now), each anchored to one REAL story from the VOC system or testimonials — named family, specific detail. Never composite.
- **Three questions Neil should ask the host** (conversation, not performance) — genuinely tailored to what the research surfaced about the host's own interests or catalogue, not generic.
- **The one plug**, planned: usually the 107 Questions guide, occasionally the discovery call. One plug per episode, delivered as a gift not a pitch. Script the single sentence.
- **Traps:** banned words reminder (preserve, legacy, process...), plus any topics or tonal missteps to sidestep for this specific audience (e.g. an older or bereavement-adjacent audience needs mortality language handled more carefully than a younger one).

### Step 4 — Propose a show-specific lead magnet and landing page (when it earns its place)

For any show with a genuinely distinct audience segment — not just a generic listener overlap — consider proposing a lead magnet built specifically for that audience, rather than defaulting to the general 107 Questions guide. Signals this is worth doing:
- The audience clearly splits into a role the existing lead magnets don't address well (e.g. a retirement show where a chunk of listeners are the parent generation, not the adult child).
- The show has enough scale or fit to justify custom asset-building time.

If proposing one, include:
- **A working title and 1–2 alternates**, following the voice profile's banned-word list and framing rules.
- **A short content shape** (format, length, 4–6 key sections/prompts) — grounded in real client language from the VOC system, not invented.
- **A proposed landing page**: suggested URL slug (using the show name where it aids trackability and recognisability, e.g. `meandmyoldman.co.uk/[showname]`), a short content outline, and a suggested plug line that references the page and acknowledges the show's specific audience split if relevant.
- **A build checklist** — note this is a proposal, not a build; flag it as a separate task for the `lead-magnet` skill if Neil wants to proceed.

Don't force this step — a show with no distinct audience angle doesn't need a bespoke asset; the general 107 Questions guide plug is enough.

### Output

`Claude Outputs/Podcast/MMOM_GuestBrief_[ShowName]_v1.md` — brief(s) for all shows covered in the request. If a lead magnet/landing page was proposed, either include it in the same file under its own heading or as a companion file `Claude Outputs/Podcast/MMOM_LeadMagnet-Proposal_[ShowName]_v1.md` — use the companion file when the proposal is substantial enough to stand alone.

## MODE 3: REPURPOSE — squeeze the episode

**Input:** episode link, transcript, or Fathom/recording reference. Read or fetch the actual content — never work from memory of what Neil "probably said".

1. **Mine the transcript.** Pull 6–10 verbatim Neil moments: the lines where he said something true and specific, off the cuff. Off-script Neil beats scripted Neil. Note timestamps.
2. **Produce the asset set:**
   - **3 LinkedIn posts** (via `linkedin-post` skill) — each built on one verbatim moment, not a summary of the episode. One may be an appearance announcement; two must stand alone.
   - **1 newsletter feature** (via `newsletter` skill) — the episode as go-deeper link, not the subject of the email.
   - **Clip list for Reels** (via `instagram` skill for captions) — 3–5 moments with timestamps, the hook line for each, and why it stops the scroll.
   - **1 landing page blurb** — two sentences + listen link for the podcast page on the site.
3. **Output:** one folder `Claude Outputs/Podcast/[ShowName]/` containing each asset as its own file, named per convention. Plus `_EpisodeMoments.md` — the verbatim quote bank with timestamps (Neil reuses these for months).

---

## Voice rules (enforced)

- No em dashes. Banned words list applies to pitches and briefs, not just public copy.
- Every claim checkable: episode names, host details, family stories — real or absent.
- Neil pitches as a peer with a story, never as "a founder disrupting the memoir space".
- One ask per message. One plug per episode.
- Always sense-check any pricing or offer figures against the most recently dated VOC/offer doc before including them in a brief — don't carry forward a figure from an older brief without checking.
