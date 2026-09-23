---
name: linkedin-post
description: "Write LinkedIn posts in Neil Taylor's voice for Me & My Old Man. Use this skill whenever Neil asks to write, draft, create, or brainstorm a LinkedIn post — or when he mentions LinkedIn content, hooks, engagement, or posting. Also trigger when he shares a topic, idea, story, or observation and wants it turned into social content, even if he doesn't say 'LinkedIn' explicitly. If he says 'write something about X' or 'turn this into a post' or 'I had this thought today', this is the skill to use."
---

# LinkedIn Post Skill — Neil Taylor / Me & My Old Man
## Version 3.2 — September 2026 (Conversation Playbook added to the ladder; opt-in pages are the only source of truth)
<!-- v3.4, 2026-09-23: lifted the ban on "snapshot". Snapshot is now a product name, so the word is fine to use. -->
<!-- v3.3 — 2026-09-22: Replaced hardcoded families/hours/countries figures with pointers to knowledge/offer/business-stats.md, the new single source of truth (updated by new-client each time a client is won). -->
<!-- v3.2 — 2026-09-17: caught in review — "The Weekly Run" [Sep 17] had CTA=Save on a Pain Points/Lead-gen post, with the Conversation Playbook's raw Google Doc link sitting in the funnel note instead of an opt-in page. Root cause: the Playbook wasn't in the lead-magnet ladder at all, so there was no live opt-in page to check it against. Fixed: added the Playbook to the ladder with its real opt-in page (https://meandmyoldman.co.uk/conversationplaybook, comment 'PLAYBOOK'), and made the ladder table the explicit single source of truth — a magnet not listed there with a URL is NOT LIVE regardless of what a Notion row's Notes field claims. Also ran a full audit of every planned post in Notion against the skill's hard rules (CTA-per-pillar, opt-in-page-only, Visual: line present, banned words, biographical facts) and corrected what was found — see the per-post notes for what changed. -->
## Version 3.1 — September 2026 (the Q&A scene rhythm, locked from Neil's hand-edit)
<!-- v3.1 — 2026-09-17: locked the Q&A scene rhythm from Neil's hand-edit on "The Weekly Run" — open with "I" when relaying someone else's moment, give every question its own blank-line-separated beat, stack multi-clause answer lines with no gaps, and sharpen insight lines to present tense instead of repeating the idea across two clauses. See "The Q&A scene rhythm" under "How to write as Neil on LinkedIn". -->
## Version 3.0 — September 2026 (the skill produces the visual, and writes it into the Notion Notes field)
<!-- v3.0 — 2026-09-03: (1) Every post's visual recommendation is a short "Visual:" line in the Notion row's NOTES property (not just the body) — Neil reads Notes. (2) The skill PRODUCES the asset, doesn't just brief it: invoke mmom-visual (cards) or mmom-carousel (Pain Points) and save to 03 Linkedin Assets 2026; brief-only + flag if Paper isn't running. (3) THREE visual sources, pick don't default: a real photo from the Image Bank (often best for Drift/Transformation), a hand-lettered/typographic card, or a carousel/infographic. Carousel + infographic TEMPLATES ARE STILL WIP WITH NEIL — brief them, flag "CAROUSEL BRIEF — templates still to finalise", don't auto-build. Cards and photos are safe to build now. -->
## Version 2.9 — September 2026 (lead-magnet fulfilment: DM the opt-in page, never the raw file)
<!-- v2.9 — 2026-09-03: nailed down the comment -> DM -> opt-in flow. The DM after a keyword comment links to the opt-in LANDING PAGE, never the Google Doc / PDF. Public reply first (with a nugget, not "check your DMs"), then DM with the page link + one question. Funnel/CTA notes must give the opt-in URL, never the Doc; if no page exists yet, say "TO BUILD". Full flow + scripts live in MMOM_LinkedIn-SOP_v1.md §4 Step 7. -->
## Version 2.8 — September 2026 (carousel + visual design picked up as part of a batch)
<!-- v2.8 — 2026-09-01: when posts are batched, the skill now also handles the visual. Pain Points posts with a carousel/infographic companion get a full slide brief written into the Notion row body (spec: Claude Outputs/LinkedIn System/MMOM_Carousel-Design-Brief_v1.md). Drift + The Now posts get 2-3 hand-lettered scroll-stopper line options for the mmom-visual skill. Drift/Transformation posts wanting a real photo get an image proposal from the Neil Image Bank index (or a "needs a photo" flag). ALL finished images/carousels save to the LinkedIn Assets folder (Shared drives/Systems/01 Awareness/Linkedin 2026/03 Linkedin Assets 2026), named to match the Notion post, so Neil can click straight to the image in Review mode. See "The visual" section below. -->
<!-- v2.7 — 2026-09-01: every finished post now creates its own row in the Notion "The Content" database via the Notion connector — Pillar, Job, CTA, Type, Status=Idea and Date pre-filled, not left as a manual step for Neil. Added the CTA Notion property (Repost + magnet comment / Save / Comment keyword / Link in comment / Book a call / None). See "Log the post to Notion" below. -->
<!-- v2.6 — 2026-09-01: Drift CTA is Repost only, never Save (photo + recognition posts travel by Repost). The Now pillar now carries two named contrarian takes — the memoir take and the AI take — use those, don't invent. Added the campaign countdown mechanic for Christmas / Mother's Day / Father's Day (a countdown number leads posts + email subjects as the date nears, ramping 1/wk -> 2/wk -> near-daily). -->
<!-- v2.5 — 2026-09-01: locked against North Star v3. Pillar 2 renamed The Questions -> PAIN POINTS (name the unspoken frustration precisely, then give one usable thing; framework rides along as a carousel/infographic, deeper version is the magnet — this is the pillar that adds demonstrated expertise). New mix: Drift 35 / Pain Points 30 / Transformation 20 / Now 15. Fixed posting days: Tue = Drift, Wed = Transformation/Now, Thu = Pain Points. External headline updated. Survivorship caveat added on the "personal posts are the engine" data. -->
<!-- v2.4 — 2026-08-31: rebuilt the strategy stack against North Star v2 and Chris Donnelly's Lead Generation Blueprint. One tag per post (Pillar sets a default Job); every post carries a real funnel CTA and at least one comment-trigger lead-gen post per week; lead-magnet ladder; added the repurpose checklist. Pillar + Job are now Notion select properties on "The Content" database. -->
<!-- v2.3 — 2026-08-04: folded in the one genuinely useful piece of Lara Acosta's Session 3 (email/lead magnets) framework — the 5 P's post structure (Problem/Pain/Possibility/Proof/Pitch) as the recommended shape for Lead Magnet posts (post type 7), and the hard rule that a lead magnet is never posted openly, always gated behind an email opt-in. Rejected the rest of her Session 3 material (urgency/FOMO launch-sequence language) as incompatible with Neil's hard rules — see newsletter skill v2.1 for the fuller writeup. -->
<!-- v2.2 — 2026-07-23: folded in the North Star model (SMPV → you're the engine → 5Ps → one job → 3/week). Corrected cadence from 5/week to 3/week and the content ratio from framework-led to personal-led, after the Jul 2025–Jul 2026 analytics showed personal "I" posts are the engine and frameworks underperform. Added the job layer (Trust/Reach/Convert/Lead-gen) and objection-mining. -->

---

## The strategy in one stack (read first)

Full version lives in `Claude Outputs/LinkedIn System/MAMO_LinkedIn-North-Star_v3.md` (LOCKED). The short version:

1. **Why Neil posts:** LinkedIn is the top of the Asking Engine funnel. Target by Aug 2027 — 5 discovery calls a month sourced from LinkedIn. LinkedIn gives no DM-open data: the metric is calls booked with "LinkedIn" as source, plus keyword comments and `LinkedIn`-tagged email sign-ups. Never follower count.
2. **Internal positioning (never posted as-is):** Neil helps adult children in the sandwich-generation squeeze reconnect with their parents, through a 12-week guided story experience that becomes a private family audio documentary. Read `knowledge/offer/business-stats.md` for the current hours/families/countries figures — never hardcode or reuse an old number.
   **External headline:** *I help families feel closer in 12 weeks than they have in 12 years — by recording a parent's life story in their own voice | [families] families · [countries] countries · [hours]+ hrs* (fill from `business-stats.md`)
3. **Personal "I" posts have carried every result so far — but that's partly survivorship** (they're the only type Neil posted at volume). Keep writing Neil, but v3 deliberately builds Pain Points and Transformation as lead drivers; re-check the Notion Pillar/Job data in ~Dec 2026.
4. **The 5Ps build the post** (Problem → Promise → Proof → Personality → Perspective). Problem → Proof → Perspective is the spine.
5. **Three posts a week — fixed days:** Tue, Wed, Thu.

### One tag per post — the Pillar sets the Job

Every post is exactly **one Pillar**. The Pillar carries a **default Job** — pick the Pillar and the Job follows. Override the Job only with a clear reason. Both are Notion select properties on "The Content" database — set them when the post is created.

| Pillar (topic) | Default Job | Built with | Visual | CTA | Monthly share |
|---|---|---|---|---|---|
| **The Drift** | **Trust** (the engine) | Personal "I" post, behind-the-scenes of Neil's own life, the contradiction | Real photo, never a graphic | Repost + pin a lead-magnet comment (NOT Save — a photo post travels by "this is my family too"; Save belongs to Pain Points) | **35%** |
| **Pain Points** | **Lead-gen** | Name the unspoken frustration of the grown-up child of an ageing parent so precisely they feel understood, then give ONE usable thing (a question, a reframe, a script). Neil's voice in the text. | **A carousel or infographic** carrying the framework — not a photo | Comment [WORD] for the full guide / Save | **30%** |
| **The Transformation** | **Convert** | Client proof, anonymised — lead with the result, hide the name | Real photo or pull-quote card | Repost / Save | **20%** |
| **The Now** | **Reach** | Contrarian take, an objection mined from a real sales call, or a gentle time-is-finite nudge | Real photo or single-stat card | Follow / Comment | **15%** |

**Pain Points is the pillar that adds demonstrated expertise** — the fix for "it's all stories, no proof I know how to help".

**Two hard rules from Chris Donnelly's Lead Generation Blueprint:**
1. **Every post ends on a real action** — Save / Repost / Comment [WORD] / Follow. Never a woolly question. (See the CTA Audit below.)
2. **At least one comment-trigger lead-gen post per week** (the Thursday Pain Points post). The magnet is never posted openly — always behind comment → DM → email opt-in.

**The funnel every magnet runs:** comment-trigger post → DM the link → email opt-in → tagged by magnet → nurture sequence → discovery call.

**The lead-magnet ladder** (light → expert): 1. 107 Questions (live, broad/light) · 2. The 10 Questions + objection-handling + scripts (exists, needs a name + landing page — more expert) · 3. The 2-Hour Starter (Transformation — to build) · 4. The Drift Diagnostic (Drift scorecard — to build).

**Objection-mining:** to feed Reach, pull a real objection from a sales-call transcript and flip it into a contrarian post. Real material, not invented.

**Repurpose checklist** — run every post that performs well through: → Stories That Matter newsletter section → Instagram carousel or Reel → cheat-sheet graphic for the Featured section → a talk anecdote. One idea, many surfaces (Donnelly: "one idea, eight ways").

**Campaign countdown posts (Christmas / Mother's Day 7 Mar / Father's Day 20 Jun only).** As the date nears, a countdown number leads the post and the email subject: *"18 days until Father's Day. Here's what still gets recorded in time."* Ramp: 6–4 weeks out = 1/week, number a soft mention; 3–2 weeks out = 2/week, number prominent, "there's still time" (never "you're running out"); final 7 days = near-daily, number leads, name the last date to start before the day. The number is a layer on a normal post — it still belongs to a pillar (usually The Now or The Transformation). These three campaigns grow year on year; log results each year so the next build starts from data.

---

## Before you write a single word

1. **Read the voice profile.** Open `About Me/VOICE_PROFILE_Neil_Taylor.md` and internalise it. Not as a checklist — as a sensibility. You're writing as a poet who learned business mechanics, not a marketer who learned to be emotional.

2. **Read the templates.** Open everything in `Templates/` and study the structures. These are Neil's proven posts with real performance data. Use them as blueprints for structure — never copy their content.

3. **Read the project brief** (if one exists). Check `Projects/` for anything relevant to the topic. If Neil has a brief, strategy doc, or content pillars document, read it before writing.

---

## The Four Content Pillars (the topic layer)

Every post belongs to one of these four pillars — but the pillar is the *subject*, not the job. Pair it with a job (Trust / Reach / Convert / Lead-gen) from the stack above. Know both before you write a word.

### Pillar 1: THE DRIFT
**What it's about:** The natural pull-apart of families. The dishwasher conversation. The 12-minute call about logistics. The way you can love someone and still be a stranger to them. No blame — just truth.
**Neil's signature line:** "Nobody stopped loving each other. Life just got in the way."
**Why the ICP stops:** Recognition. Sarah reads it and thinks: *That's us. That's literally my family.*
**Post types that live here:** Story posts, Problem posts, Contrarian posts, Poetic posts
**CTA direction:** Repost if this is your family / Tag someone who needs to read it. (Not Save — Drift posts are photo + recognition, they travel by Repost.)
**Lead magnet that connects:** The Drift Diagnostic (quiz), The 107 Questions guide

### Pillar 2: PAIN POINTS  *(Job: Lead-gen — replaces the old "The Questions")*
**What it's about:** The specific, unspoken frustration of being the grown-up child of an ageing parent — named so precisely the reader feels *understood* — then ONE usable thing to try: a question, a reframe, a small script.
**What Neil is doing:** Recognition first (I get you), then help (I know how to fix this). The post text is Neil's voice — pain + understanding + one visible tip. The framework/tool is delivered as a **carousel or infographic image, never a photo**. The deeper version is the lead magnet.
**Core belief:** People on LinkedIn want to feel understood and then get something usable. This is where Neil proves expertise, not just feeling.
**Why the ICP stops:** "That's exactly my problem — and he's just told me something I can actually do."
**What the content says:** "You call every Sunday. It lasts eleven minutes. You hang up knowing nothing new. Here's the one question that changes that call."
**Post types that live here:** Problem posts (with a carousel), Framework posts, Cheat Sheet / Infographic posts
**CTA direction:** Comment [WORD] for the full guide / Save the carousel
**Lead magnet that connects:** 107 Questions (light), The 10 Questions + objection-handling + scripts (more expert)

### Pillar 3: THE TRANSFORMATION
**What it's about:** Real family moments from real sessions — what actually changes when families do this. Not the audiobook. The relationship. The brother who cried. The stories nobody knew existed. The parent who finally felt heard.
**Core belief:** The experience is the product. The audiobook is just proof it happened.
**Why the ICP stops:** Proof. Sarah thinks: *If they felt that, I want that for my family.*
**Post types that live here:** Client Story posts, Proof posts, Before/After posts, Testimonial-led posts
**CTA direction:** Repost if you want this for your family / Save this / Comment your story
**Lead magnet that connects:** The Recording Roadmap (how to start capturing stories yourself)

### Pillar 4: THE NOW  *(Job: Reach)*
**What it's about:** Two things at once. The gentle nudge that time is finite and our people are changing (never alarm). AND the home for a strong contrarian opinion — always with a positive alternative, never provocation for its own sake.
**The running contrarian takes (use these, don't invent new ones):**
- **The memoir take.** When someone says they'll write their parent's memoir (or get the parent to write one) — stop. Long, arduous, solo, won't sound like them, almost no one reads it. Far more people will listen to an hour of them actually talking and come away with their essence.
- **The AI take.** Of everything we'd want to keep off-limits to AI, our closest relationships are top of the list. Don't hand your parent to a chatbot to "capture their story". Give them what a machine can't: being properly listened to by a curious human who holds their energy, draws out the humour, guides them through it.
- Standing ones: "Families don't need to talk more. They need to talk differently." / "You'll spend 75% of the time you'll ever have with your kids by the time they're twelve."
**Why the ICP stops:** A default they've never questioned, questioned. Or: *This is exactly where I am, and I need to do something.*
**Post types that live here:** Contrarian posts, Insight / Reflection posts, Observation posts, Commentary posts
**Visual:** real photo, or a single-line statement card.
**CTA direction:** Follow for more / Comment [your take]
**Lead magnet that connects:** The Drift Diagnostic, the Last-Summers one-pager

---

## The 3-Posts-Per-Week Rhythm

Consistency over volume, and depth is Neil's differentiator. Three posts a week, on the days he can also comment (the 48-hour-gap rule is a myth — ignore it). This replaces the old 5/week guidance.

The fixed week (North Star v3):

| Day | Pillar | Job | Format |
|------|--------|-----|--------|
| **Tuesday** | THE DRIFT | Trust | Personal "I" post, insight/reflection, behind-the-scenes, or the contradiction |
| **Wednesday** | THE TRANSFORMATION *(alt. THE NOW)* | Convert / Reach | Client proof (anonymised) — or a contrarian/objection-mined take |
| **Thursday** | PAIN POINTS | Lead-gen | Pain + one tip in the text; carousel/infographic carries the framework; comment mechanic → email |

Rotate Wednesday between Transformation and The Now across the month. Quiet-pipeline week → replace Thursday with a second Drift post; the engine never goes dark. Campaign weeks can add Monday (Drift) or Friday (The Now).

**Monthly mix (North Star v3 — personal-led, built to generate leads):**
- **The Drift / Trust — personal "I" posts: ~35%.** The trust engine. Each one pins a lead-magnet comment.
- **Pain Points / Lead-gen: ~30%** (~4 a month — comment-trigger → email, carousel every time).
- **The Transformation / Convert — anonymised client proof: ~20%.**
- **The Now / Reach — contrarian, objection-mined, or gentle nudge: ~15%.**

---

## The CTA Audit — Non-Negotiable

**The old problem:** Posts ended with a woolly question no one answered. "What do you think?" "Have you ever felt this?" Dead ends.

**The new rule:** Every single post must close with ONE of these four actions. Not a question. An action.

| Action | When to use it | Example |
|--------|---------------|---------|
| **SAVE** | Framework / Carousel / Cheat Sheet — anything with reference value | "Save this for your next family call." |
| **REPOST** | Story / Proof / Emotional post that someone else's network needs to see | "Repost if this is your family." |
| **COMMENT [WORD]** | Lead Magnet post — drive engagement AND email signups | "Comment 'QUESTIONS' and I'll send you the 107-question guide." |
| **FOLLOW** | High-reach post / when at end of a story that builds identity | "Follow for one post a week about family connection." |

**The rule:** Pick ONE. State it clearly. One line. No "would love to hear your thoughts" as a backup hedge.

Woolly questions are permitted ONLY inside the body of the post as rhetorical devices — never as the closing CTA.

---

## What you're actually doing

You're writing a LinkedIn post that sounds like Neil Taylor standing on stage doing spoken word — rhythmic, intimate, purposeful — adapted for LinkedIn's format. The post should make someone stop scrolling because it names something they feel but haven't said yet.

Neil's LinkedIn voice is his sharpest voice. One idea per post. Hook-driven opening. One-line paragraphs. But underneath the LinkedIn formatting, his spoken word instinct must still breathe — long sentences building pressure, then a short blunt line that drops the floor out.

---

## The brief

Before writing, you need to know:

- **What job is this?** (Trust / Reach / Convert / Lead-gen — decide first; it sets the format)
- **What pillar is this?** (The Drift / Pain Points / The Transformation / The Now — the topic)
- **What's the seed?** A personal moment, a client story, a reflection, a book idea, a reaction to news? Neil's best posts start from something specific and real that happened.
- **What format is this?** (See post types and format guides below)
- **What's the one insight?** Every post has exactly one thing it's trying to make the reader feel or realise. If you can't name it in one sentence, the post isn't ready.
- **What's the CTA?** Save / Repost / Comment [WORD] / Follow. Decided before you write, not after.

If Neil hasn't given you enough to work with, ask. Don't fill gaps with generic filler — that's the opposite of his voice. Specificity IS the hook.

---

## Post types and format guides

Neil rotates between these structures. Each one has a different job.

### 1. Client Story Insight
**Pillar:** 3 (The Transformation)
**Job:** Show what the experience does through a real family's moment.
**Structure:** Scene from an interview → what happened → what it meant → what the reader can take from it.
**Key rule:** Every story is real, one family, exactly as it happened. Never composite. Never fictionalise. Always anonymise unless Neil says otherwise.
**Default CTA:** Repost / Save
**Example pattern:** "I had to stop writing this post on Friday..." / "My dad never once told me he was at peace..."

### 2. List Post
**Pillar:** 1 or 2 (The Drift / Pain Points)
**Job:** Make the reader see their own life reflected back in a structured, scrollable format.
**Structure:** Personal hook → numbered points (each one specific and domestic, not generic) → emotional landing → action CTA.
**Key rule:** Each list item should feel like a gut-punch of recognition, not a tip. "Your parents feel outside your pod" hits harder than "Communication becomes harder."
**Default CTA:** Save / Repost
**Example pattern:** "I moved 1,000 miles away from home. Here's what nobody tells you..."
**Hard rule — always ships with a carousel.** Neil doesn't do List posts often, and every time he does, it gets a slide-by-slide carousel companion — not optional, not pillar-dependent (unlike the "Pain Points only, WIP" carousel guidance elsewhere in this doc). Build it in MMOM's actual website design system, not the generic cream/navy Paper design-brief palette: pull the current fonts, colours, and layout language from the live site (`meandmyoldman.co.uk`) or the latest copy deck / launch-plan artifact (see [[project_mmom_website_relaunch]] in memory for locations) before building. One slide per list item, hook slide first, CTA slide last.

**Delivery — never leave it as a sidebar-only canvas artifact.** A Design-canvas Artifact opens in the side panel with no fast "save all 8 and upload" path — Neil can't action it in two clicks, so it is not a finished deliverable on its own. The finished deliverable is files he can save straight from chat and drop into LinkedIn:
1. Build the design once (canvas artifact, or `mmom-carousel` when Paper is running) to lock the copy and layout per slide.
2. Re-express each slide as a standalone flat HTML file (plain `<div>` sized exactly to the target canvas, e.g. 1080×1350, real Google Fonts `<link>`, inline styles — no artifact runtime dependency) and render each to a PNG at that exact pixel size with headless Chrome:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --hide-scrollbars --window-size=1080,1350 --screenshot="slide-N.png" "file:///abs/path/N.html"`
   (verify with `sips -g pixelWidth -g pixelHeight` — must match exactly, no letterboxing).
3. Combine the PNGs into one PDF, page order = slide order (e.g. `Pillow`/PIL `Image.save(..., save_all=True, append_images=[...])`, or any equivalent) — LinkedIn's document-post carousel takes a single PDF upload and turns each page into a swipeable slide, which is the fastest path (one file, order guaranteed, no manual re-ordering of 8 separate images).
4. Deliver via `SendUserFile`: the individual PNGs (for Instagram or manual reordering) AND the combined PDF (for the one-click LinkedIn document-post upload) — both in one message, `display: "attach"`.
5. Also save the finished PNGs to `03 Linkedin Assets 2026/` and put the filename on the Notion row's `Visual:` line, same as any other visual — the local delivery to Neil does not replace logging the asset.

### 3. Poetic Post
**Pillar:** 1 (The Drift)
**Job:** Create an emotional moment. Pure spoken word on the page.
**Structure:** Anaphora (repeated opening phrase) → building emotional pressure through repetition → a quiet, powerful landing.
**Key rule:** This is Neil at his most lyrical. Stanza thinking, not paragraph thinking. Two lines, five lines, one word on a line. No hooks, no tricks — just honesty and rhythm.
**Default CTA:** Repost if this is your family / Follow
**Example pattern:** "If you still have a parent in your life... I'm here."

### 4. Insight / Reflection Post
**Pillar:** 1 or 4 (The Drift / The Now)
**Job:** Take a small personal moment and reveal the bigger truth underneath.
**Structure:** Specific domestic detail (the ice cream, the hair, the 90 seconds) → the reveal → the insight → action CTA.
**Key rule:** The mundane detail IS the hook. Don't dress it up. "My son sitting on my lap. Eating an ice cream. Me staring at his fluffy tufts of hair." That specificity earns everything that follows.
**Default CTA:** Save / Repost
**Example pattern:** "The best moment of my weekend lasted about 90 seconds..."

### 5. Framework / Carousel Post
**Pillar:** 2 (Pain Points)
**Job:** Break down a process, system, or insight into clear, numbered, shareable steps.
**Structure:** Bold claim or problem hook → numbered framework (5-8 steps or items) → brief explanation of each → power CTA (Save this / Comment for the full guide).
**Key rule:** Frameworks signal expertise. They also get saved and revisited. Name the framework — "The 3-Room Conversation Method" or "The 5 Questions That Unlock Your Parent's Story" — a named framework has more authority than a list.
**Default CTA:** Save this / Comment [WORD] for the full guide
**Carousel note:** Write the post text as the caption. In a separate brief block at the bottom, outline the carousel slides (Slide 1: Hook image / Slide 2-8: one point per slide / Slide 9: CTA).

### 6. Cheat Sheet / Infographic Post
**Pillar:** 2 (Pain Points)
**Job:** Deliver dense, reference-worthy information in a visually shareable format. The image does the work; the caption earns the share.
**Structure:** Short caption (3-5 lines max) that frames the value → the image / cheat sheet → CTA to save or repost.
**Key rule:** The caption is not where the education happens — the graphic is. The caption's only job is to make someone want to read the graphic AND share it. Keep it tight.
**Default CTA:** Save this / Repost to share with someone who needs it
**Design brief note:** After the post caption, include a one-paragraph design brief: what should appear on the graphic, how many sections, what the headline should be.

### 7. Lead Magnet Post
**Pillar:** 4 (The Now) — every Thursday
**Job:** Convert reach into email subscribers. Promote a specific resource the ICP genuinely wants.
**Structure — the announcement arc (5 beats, not the 5Ps from the strategy stack — see note below):** Problem → Pain → Possibility → Proof → Pitch.
  1. **Problem:** Name the specific thing the resource solves. One sentence, concrete.
  2. **Pain:** Make it felt, not stated. The domestic detail — the dropped story, the closed-off parent, the notebook that got two pages in. Specificity over abstraction, same as everywhere else.
  3. **Possibility:** What it looks like solved. One family's version of "and then we knew."
  4. **Proof:** Something that shows this is real and gettable — a real line from a client or prospect, a number (hours/families from `knowledge/offer/business-stats.md`), never invented.
  5. **Pitch:** The resource itself, named plainly, with the comment mechanic.
**Key rule:** The comment mechanic ("Comment 'QUESTIONS' and I'll DM you the guide") drives both engagement AND reach. The algorithm sees comments as high-value signals. Never just put a link in the post.
**Hard rule — never post the magnet itself, and never DM the raw file link.** The magnet is never in the post body, never an attachment, and the DM that follows a keyword comment links to the **opt-in landing page**, never the Google Doc / PDF. The chain: keyword comment → public reply with a nugget (not "check your DMs") → DM the opt-in page + one question to open a conversation → email opt-in → Kit tag `magnet-<name>` → nurture → call. DMing the raw file = zero emails, no nurture, no attribution, wasted asset. Full flow + scripts: SOP §4 Step 7 (`MMOM_LinkedIn-SOP_v1.md`).
**Default CTA:** Comment [WORD] — always. No exceptions on this post type.
**In the CTA / funnel note, always give the opt-in page URL, never the Doc.** If the page isn't built yet, write "opt-in page: TO BUILD (`/slug`)" — never fall back to the Doc link.
**The lead-magnet ladder** (light → expert — Thursday's Pain Points post rotates through it). **This table is the only source of truth for which magnets have a live opt-in page — if a magnet isn't listed here with a URL, treat it as NOT LIVE, whatever a Notion row's Notes field says.**
  1. **107 Questions to Get Your Parent's Stories** — Pillar: Pain Points / Drift — comment 'STORIES' — opt-in page: *live* (URL TBD — confirm with Neil if not already recorded here)
  2. **The Conversation Playbook** — Pillar: Pain Points — comment 'PLAYBOOK' — opt-in page: **https://meandmyoldman.co.uk/conversationplaybook** — *live, added 17 Sep 2026*. This is the "how do I actually make it work" magnet — the fit for posts about getting started, not just what to ask.
  3. **The 10 Questions + Objection-Handling + Scripts** — Pillar: Pain Points — needs a proper name + landing page — *exists but buried; the more-expert rung, NOT LIVE*
  4. **The 2-Hour Starter** — record your first conversation yourself — Pillar: The Transformation — comment 'START' — *to build, NOT LIVE*
  5. **The Drift Diagnostic** — 2-min scorecard, how far has your family drifted? — Pillar: The Drift — comment 'DIAGNOSTIC' — *to build, NOT LIVE*
  - "97 Conversation Prompts" — comment 'PROMPTS' (legacy, still usable) — opt-in page status unconfirmed, verify before using
  - Father's Day Conversation Guide — comment 'GUIDE' (seasonal only) — opt-in page status unconfirmed, verify before using
  Every magnet: comment → DM link → email opt-in → nurture sequence → discovery call. Never post the file itself. **Never write a magnet's raw Google Doc/PDF link into a Notion row's Notes or funnel note — only ever the opt-in page URL from this list, or "TO BUILD" if it's not here.**
**Example pattern:** "Most families talk every week. And talk about nothing that matters. I've spent [hours from business-stats.md] hours interviewing families. Here are the 107 questions that actually unlock the stories..."

**Note on the two "5" frameworks in this doc:** the 5Ps in the strategy stack above (Problem → Promise → Proof → Personality → Perspective) shape *any* post. The 5 P's here (Problem → Pain → Possibility → Proof → Pitch) are specific to Lead Magnet announcement posts only — borrowed from Lara Acosta's Session 3 framework, translated into Neil's voice. Don't conflate the two; use the strategy-stack 5Ps for everything, and this 5 P's arc only when building post type 7.

### 8. Problem Post
**Pillar:** 1 (The Drift)
**Job:** Describe the exact pain the ICP is living right now. Stop them mid-scroll with recognition.
**Structure:** Hyper-specific pain description (not vague — name the exact moment, the exact conversation) → why it keeps happening → what's actually possible → CTA.
**Key rule:** Be specific enough that it hurts. "Posting 3x a week for 6 months and still no inbound" is the LinkedIn Bible's example. Neil's version: "You call every Sunday. The call lasts 11 minutes. You talk about the weather, the kids, the news. You hang up and think: I don't really know them at all."
**Default CTA:** Repost / Save

### 9. Contrarian Post
**Pillar:** 1 or 2
**Job:** Challenge a piece of advice or assumption the audience has heard 100 times. Create conversation.
**Structure:** The conventional wisdom (stated quickly) → "But here's what I actually think..." → the better alternative → CTA.
**Key rule:** Neil doesn't do provocation for its own sake. His contrarian takes come from a place of genuine belief. "Families don't need to talk more. They need to talk differently." That's a contrarian take with a positive alternative.
**Default CTA:** Repost if you agree / Follow for more

### 10. Personal Brand Post
**Pillar:** 1 or 4
**Job:** Tell Neil's origin story or share a vulnerable moment that earns trust.
**Structure:** Vulnerability up front → the backstory → what he does now because of it → invitation.
**Key rule:** Grief is the doorway, never the destination. Always walk the reader back to the light. Pain paired with possibility.
**Default CTA:** Follow / Repost

### 11. Commentary Post
**Pillar:** 4 (The Now)
**Job:** React to something in culture, news, or a moment through Neil's lens of family connection.
**Structure:** The thing that happened → why it matters → how it connects to Neil's world → what the reader can do.
**Key rule:** Neil doesn't do provocation — he does connection. He takes someone else's moment and shows why it resonates with what he believes.
**Default CTA:** Repost / Follow

---

## How to write as Neil on LinkedIn

### The hook (first 1-2 lines)
This is what shows above the "...see more" fold. On LinkedIn, the fold hits after roughly 2-3 lines (around 140 characters on mobile). The hook AND the tension must land before that cutoff.

The tension is the key. Something that creates a gap — a contrast, a question, an "except." "My sisters and mum got together for Easter Sunday" is a scene. "Except I wasn't in it" is the tension. Both need to land above the fold.

- **Lead with a quote or a moment.** One of Neil's strongest moves is opening with someone else's words — a family member, a client — without quote marks. Creates intimacy before the reader realises it's not Neil speaking. Then reveal whose words they are a few lines later.
- Start with something specific that happened. Not a setup, not a framing device — the thing itself.
- Often starts with "I" — but vary this. A quote, a statistic, a one-line scene — mix it up.
- Never use clickbait mechanics. Neil's whole message is "slow down, be present, stop optimising." Clickbait undermines that.

**Good hooks from Neil's actual posts:**
- "I had to stop writing this post on Friday. It was bringing up a lot. Still is."
- "The best moment of my weekend lasted about 90 seconds."
- "My dad never once told me he was at peace with his life."
- "Her daughter had never heard her mum talk about her own childhood."

### The body

**THE CORE FORMATTING RULE — read this carefully:**

LinkedIn posts use three distinct formatting modes. Knowing when to switch between them is what makes the visual rhythm work.

**Mode 1: Flowing prose line**
A single complete sentence with a blank line above and below. Used for context-setting, transitions, and longer thoughts.

*Example:*
So when we sat down for the interviews, and her mum started talking about..

**Mode 2: Tight list block (NO blank lines between items)**
When content gets listy — short phrases, stacked details, sensory specifics — each phrase goes on its own line with NO blank line between them. They read as one fast block. This is the stanza move. It builds momentum and pace.

*Example:*
the jobs she worked,
the people she loved,
the things that broke her heart and put her back together
— her daughter heard something she'd missed her whole life.

The em-dash at the end of a block is a legitimate device — it pulls the stanza to a landing rather than leaving it hanging.

**Mode 3: Standalone impact line (blank line above AND below)**
A single short sentence given its own breathing room. This is the big point. The culmination. The line that lands after the build. Reserve these for the emotional peak of a section — the sentence you want the reader to pause on.

*Example:*
Not just the stories.

[blank line]

The way her mum tells them.
The laugh.
The pauses.
The "well, you see..." before something true.

[blank line]

Her daughter said, weeks later: "I'll have that forever now. I'll know her laugh forever."

**The rhythm in practice:**
- Prose line sets the scene
- List block accelerates and stacks
- Blank line + standalone impact line = the floor drops out
- Back into prose or another block

Do NOT put blank lines between each item in a list block. That kills the momentum and makes the post look like a bad PowerPoint. The block must run together, fast, no air between the lines. The air comes BEFORE and AFTER the block — not inside it.

**The stacked-sentence rule (Neil's explicit preference):** When a single thought contains multiple short phrases that build on each other, break them onto separate lines with NO blank lines between — even if they could sit on one line. This is the spoken word stanza move. Each line lands separately, like beats.

*Wrong (collapsed onto one line):*
Behind it: who he was at 25. The places he went when he needed to think. The version of himself before life got full and complicated.

*Right (each phrase its own line, no gaps):*
Behind it: who he was at 25.
The places he went when he needed to think.
The version of himself before life got full and complicated.

*Wrong:*
And his dad would have felt it. The impatience. The gentle redirection. The sense that his motorbike was taking up too much space.

*Right:*
And his dad would have felt it.
The impatience.
The gentle redirection.
The sense that his motorbike was taking up too much space.

Apply this whenever a sentence contains three or more short clauses that each carry their own weight. If you'd pause after each one when speaking it aloud, it goes on its own line.

- **Vary the rhythm.** Long sentences build tension. Short ones release it. "Different feelings mind." Without the long, the short has nothing to push against.
- **Lead with specific, domestic, recognisable detail.** The dishwasher. The twelve-minute phone call. The fluffy tufts of hair. The tax conversation.
- **Use "we" not accusatory "you."** Neil is in the same sandwich generation, the same drift.
- **Register shifts.** Move between reflective/literary and grounded/domestic within the same post.
- **Parenthetical asides.** Neil uses these naturally — thinking-out-loud moments.
- **British vernacular.** "Brilliant nick." "Cuppa." "Pint." "Telly." Natural texture, not performed.
- **Humour as release valve.** Observational, self-deprecating, dry. Never standalone — always inside a serious point.
- **Important: LinkedIn has no text formatting.** No bold, no italic, no underline. Never use asterisks, underscores, or any markdown in the post text.

### The close — the CTA, not the question
The old habit was ending with a woolly question. That's gone. Every post ends with ONE of the four actions:

- **Save:** "Save this for your next family call."
- **Repost:** "Repost if this is your family." / "Tag someone who needs to read this."
- **Comment [WORD]:** "Comment 'STORIES' and I'll send you the 107-question guide."
- **Follow:** "Follow for one post a week about family connection."

One line. One action. State it clearly. Done.

Rhetorical questions can still live in the body of the post — they pull the reader in. But they never close the post.

### The Q&A scene rhythm (locked, 17 Sep 2026 — Neil's hand-edit on "The Weekly Run")

When a post's scene is built from a real back-and-forth — Neil asking, someone answering — Neil's revision showed the exact spacing and phrasing this structure wants. Compare:

*Draft (AI, before):*
```
A client told me this week she's been running with her dad every Sunday since she was seven years old. Still does it. Both of them, every week, whatever the weather.
I asked what she thought she got out of it.
She said she thought it started as him trying to keep her fit. Then she stopped and said actually, no, she doesn't think it was ever about the running.
I asked what she thought he got from it.
She didn't have an answer straight away. Which was its own kind of answer.
That's the thing about the one-on-one things our parents did with us. We rarely ask why they kept doing them. We just did them, then grew up, then stopped asking.
```

*Neil's revision:*
```
I was struck by this reflection from a daughter last week.

She said she'd been running with her dad every Sunday since she was seven years old.
She still does it.
Every week, whatever the weather.

I asked what she thought she got out of it.

She said she thought it started as him trying to keep her fit.
Then she stopped and said actually, no, she doesn't think it was ever about the running.

I asked what she thought he got from it.

She didn't have an answer straight away.
Which was its own kind of answer.

That's the thing about the one-on-one things our parents did with us.

We rarely ask why they do them.
We just did them, then grew up, then stopped asking.
```

**What changed, and apply it every time this scene shape comes up:**

1. **Open with "I" when the post is Neil relaying someone else's moment.** "I was struck by this reflection from a daughter last week" beats leading with the other person's action ("A client told me..."). Neil as the observer/narrator opens the frame; the scene follows once he's placed himself in it.
2. **Every beat gets its own blank-line-separated stanza — even short ones.** The old draft ran "I asked what she thought she got out of it." straight into the next line with no space. Neil's version puts a blank line before AND after each question line ("I asked what she thought he got from it.") so it functions as its own beat, not a connector. This is the Q&A scene variant of Mode 3 (standalone impact line) — treat each question as its own standalone beat, not part of the surrounding block.
3. **Break multi-clause answer lines into their own lines, no blank line between them.** "Still does it. Both of them, every week, whatever the weather." (collapsed) becomes "She still does it." / "Every week, whatever the weather." (stacked, tight, no gaps) — the stacked-sentence rule applied inside a beat.
4. **Sharpen insight lines to present tense and cut the redundant clause.** "We rarely ask why they kept doing them. We just did them, then grew up, then stopped asking." (kept doing / did — repeats the past-tense idea twice) becomes "We rarely ask why they do them." (present tense — it's still happening, that's the point) followed by its own beat: "We just did them, then grew up, then stopped asking." Look for this pattern generally: if an insight line repeats itself across two clauses, cut to the sharper single clause and let the second clause carry a genuinely new idea.

Apply this rhythm to any Insight/Reflection or Client Story post built around a real question-and-answer exchange — it is a locked-set rule, not a one-off.

---

### Emotional architecture
Every post follows this underlying movement:
1. **Surface** — a mundane, domestic, specific detail
2. **Underneath** — what's actually happening beneath the surface
3. **Light** — always walk back from darkness to possibility

Pain is the doorway, never the destination. If a post ends in grief without hope, it's not Neil.

### Shareability test — Write for Three Audiences at Once

Before delivering, ask: "Would someone repost this?" A shareable post usually does one of these things:
- Names a feeling the reader has but hasn't articulated
- Tells a story that reminds them of their own family
- Offers a perspective shift they want to pass on
- Contains a framework or list they'll want to reference again

**CRITICAL insight — Why most content underperforms:**

Most content is written only for the smallest slice of the audience — the die-hards who already know Neil and love him. The post assumes familiarity the 95% don't have.

Every post must work for **THREE tiers simultaneously:**

1. **Die-Hards (1–5%)** — Know you, love you, already trust you. For them, a single sentence can carry the whole weight of shared understanding.

2. **Dry Bias (the "in and out" middle)** — Semi-familiar, scrolling past sometimes, might click "see more" if the hook lands. They need the specific scene, the concrete moment. They don't have context for shortcuts.

3. **Drop-Ins (strangers)** — Total strangers who landed on the post by algorithmic accident. Zero context, zero trust, no idea if you're worth listening to. They need the hook to work in three seconds, the scene to be crystal clear, and no assumptions about who you are.

**The practical test:** Does this post make sense to someone who has never heard of Neil before, in the first three seconds? Can a complete stranger read the first line and understand what's happening without needing to know your origin story, your dad's death, or your business?

If the answer is no, rewrite. The post is too inside. The die-hards will get it regardless — they always do. But you've lost the drop-ins, and that's where the exponential growth lives.

**In practice:** This changes what gets specificity.
- **Die-hards:** can handle a reference to your dad, to MMOM, to Patrick
- **Dry bias:** need context. If you say "after my dad died," you need to land it in one sentence. You can't assume they know your story.
- **Drop-ins:** need the scene so clear they can visualise it without knowing anything about you. The dishwasher. The twelve-minute call. The fluffy tufts of hair. These work for strangers because they're universal.

**A strong post opens with drop-in clarity** (the specific detail), **builds with dry-bias recognition** (the emotional truth), and **deepens for die-hards** (the knowing reference). All three layers, one post.

If the post is too personal to Neil's specific situation without a universal hook, it won't travel.

---

## Hard rules — never break these

### Banned words and phrases
Never use: preserve, legacy (mostly), heirloom, keepsake, treasure, for posterity, process (say "experience"), "stopped me cold", "stopped me in my tracks", "gold" (as exclamation), "sit with" (therapy vibes), achieved (corporate), "let's get connected!" (motivational coach), "hold space for", withholding (say "holding back")

Never end a post with hashtags. No #Family #Legacy #Storytelling. It cheapens everything that came before it.

### Banned moves
- Never use fear/regret as a standalone hook — always pair with transformation
- Never composite or fictionalise family stories — every story is real, one family, as it happened
- Never use urgency/alarm language — use observation instead: "I feel it changing" not "running out of time"
- Never point fingers at the reader — always "we", never accusatory "you"
- Never lead with the product — the audiobook is the byproduct; the reconnection is the real product
- Never use American-style hard-sell cadence
- Never sound like a motivational coach or a marketing tagline
- Never write anything that sounds like AI trying to create artificial suspense
- **Never close a post with a woolly question as the CTA.** Save / Repost / Comment [WORD] / Follow — those are the only four closes.
- **Never ask someone to repost a comment.** Comments are conversations, not promotion. No CTA that asks for amplification. (See revised Q100 on comments below.)
- **Avoid British colloquialisms that are context-specific.** "In brilliant nick" works because it appeared naturally in real comms about a specific moment — it's not a go-to phrase to sprinkle into other writing. Generic British texture: "cuppa," "pint," "telly," "yadda yadda." One-off observations: let them emerge naturally, don't force them.

### AI tells to watch for
Neil spots AI writing instantly. If there's no dishwasher, no twelve minutes, no fluffy tufts of hair — it's probably not Neil yet. Also watch for:
- **Cliché metaphors and similes** — "as natural as breathing," "hit me like a ton of bricks." Delete and say the thing plainly.
- Phrases designed to manipulate rather than connect
- Too-smooth transitions (Neil's real writing has asides, self-corrections, register shifts)
- Generic emotional language where there should be a concrete scene
- Over-complicated vocabulary when a simpler word works

### Biographical facts — get these right
- Neil's dad (Patrick) passed away in 2021. His son was born six days later. His son's middle name is Patrick.
- Neil's son is 5 years old. Don't write him as a teenager or older child.
- Neil's mum is alive. She's 75, lives in the UK, recently moved. She's in "brilliant nick" but slowing down.
- Neil lives near Barcelona. His audience is UK-based.
- He's done [hours]+ hours of interviews across [families] families — read `knowledge/offer/business-stats.md` for the current figures, never a remembered or old number.
- The business is called Me & My Old Man. The experience costs £4,800.
- Never reference both parents as deceased. Never imply his mum has passed.

---

## Writing LinkedIn Comments (not posts)

Comments are conversations, not broadcasts. They have a different rhythm and energy from posts.

### Rules for comments

**Conversational entry:** Start with agreement or a genuine question — "Agreed" or "This landed for me because..." You're joining a thought, not pronouncing from above.

**Proof points, not credentials:** If you mention your work, keep it soft. "I speak with a lot of 60-70 year olds" is a proof point that's curious and humble. "After 350+ hours of interviews across 32 families" (pull the real current figures from `knowledge/offer/business-stats.md`) is a sell that makes the reader suspicious. Soft proof lets the conversation deepen; hard proof interrupts it. If they want to know more, they'll click your profile.

**Specificity and rhythm:** Comments are thinking-out-loud. Build arguments across sentences. Use your natural speaking rhythm — dashes, parenthetical asides, "yeah?" at the end of a thought. Less formatted, more alive.

**No CTA.** Comments don't have a call to action — no "Save this," no "Repost this," no closing mechanic. Comments are extensions of the conversation, not conversion funnels. The goal is to deepen the thread and be genuinely useful.

**Darkness into light:** If you're addressing a challenging idea, acknowledge it, then flip to what's possible. Pain is the doorway, never the destination.

**Never self-promote.** The moment a comment becomes about you or your offer, it stops being a comment and becomes a sales pitch in disguise. Stay in service of the original idea.

### The one-level-deeper rule (proven June 2026)

The comments that travel — that get served by the algorithm to people who never saw the original post — are the ones that answer the question the post didn't ask.

Jake Humphrey posted about Golden Time: "When did you last have thirty minutes that were only yours?"

Neil's comment: 44k impressions, 37 likes, 5 comments.

The comment didn't answer Jake's question. It went one layer deeper: not when did we lose Golden Time, but *why* — and landed on "We didn't lose the time. We lost permission." That reframe is the move.

**The formula:**
- The post asks Q1 (the surface question)
- The best comment asks Q2 (the question underneath Q1)
- State it compressed and blunt, with specific details building to it
- No pivot to your work. Let the insight stand alone.

This is also Neil's core writing move — surface then underneath — applied to commenting. The comment is a micro version of his best posts.

**What this means for comment strategy:** High-reach posts (100k+ impressions, creators like Jake Humphrey, Emily Maitlis, etc.) are worth investing in. A well-placed comment on a viral post can get more reach than a standalone post. The same quality thinking, a fraction of the content. Prioritise comments on posts where:
- The topic connects to family, time, presence, drift, or permission
- The creator has a large but not niche-identical audience
- Neil can genuinely add a layer, not just agree

---

## Formatting rhythm — blocks vs standalone lines (v2.1, locked-set rules)

These rules come from Neil's hand-edits to the locked 10-post ICP set (May 2026). They are not optional.

**BLOCKS** — related lines grouped tight, no blank lines between them. Use for:
- Listy sequences (the five directions pulling you apart)
- Poetic runs (stacked sensory details: "The laugh. The pauses. The 'well, you see...' before something true.")
- Questions that build momentum (doubts stacked together)
- Thematic clusters that need energy

**STANDALONE LINES** — one line with white space either side. Reserve ONLY for:
- Emotional peaks or thesis statements ("It's not a metaphor. It's physics.")
- Turning points
- Lines the reader should pause on

**The interplay is the rhythm:** a block builds energy; a standalone line lands it. If every line is standalone, nothing hits (exhausting). If everything is blocked, nothing breathes (overwhelming). Map the block/standalone structure before writing the body — think in stanzas.

**Other locked-set rules:**
- **Real names, real details.** Judy, the doughnut routine, the Englishman/Scotsman/Irishman joke. If you don't have the specific detail, don't write the post — ask Neil for the real story. Generic details are AI tells.
- **Fear + hope, never fear alone.** The "memory vs. ghost" pattern: name the loss, acknowledge the finality, then show that some families do capture it. Recognition + permission, never "you'll regret this."
- **Close questions flip perspective.** End on THEIR transformation ("What's the story you'd most regret losing?"), never on the product.
- **CTAs live in the comment or P.S.,** never in the post body. Lead magnet anchor, repost invitation, or soft follow — invitations, not demands.
- **The P.S. is a strategic beat**, not an afterthought. It's where the most vulnerable line goes — the quiet thing said after stepping back from the mic.

---

## Output format

Deliver one polished post, ready to copy-paste into LinkedIn. Format it as:

```
[The post text, formatted with one-line paragraphs as it would appear on LinkedIn]

---
Pillar: [The Drift / Pain Points / The Transformation / The Now]
Job: [Trust / Convert / Reach / Lead-gen] — the pillar's default unless there's a reason to override
Post type: [which type from above]
Hook strategy: [one sentence on why this hook works]
CTA: [exactly what appears at the end and why — must be Save / Repost / Comment [WORD] / Follow, never a question]
Funnel note: [which lead magnet this feeds, and whether it's a pinned comment or the main CTA]
Visual: [one short line — the chosen card line / carousel concept / photo brief — per pillar, see "The visual" section. This exact line ALSO goes into the Notion row's Notes property, and gets the saved filename appended once the asset is built.]
Format companion: [if this is a Carousel or Cheat Sheet, the full slide-by-slide brief goes in the Notion row body]
Suggested edits for Neil: [2-3 specific places where Neil should swap in his own detail — a real name, a real moment, a real number. The soul comes from him; efficiency from AI.]
```

The "suggested edits" section matters. Neil's workflow is: AI provides structure and a strong V1. Neil swaps generic details for specific, real ones. Never produce something so polished there's nothing left for Neil to make his own. Leave room for him.

---

## Log the post to Notion — do this every time, without being asked

After delivering the post, create a row in the Notion **"The Content"** database so the post is already allocated a Pillar and CTA — never leave this as a manual step for Neil.

- Database: `https://app.notion.com/p/c1b22210a703839083d70102f3c58ccd` — data source `collection://0df22210-a703-82d0-a417-873a066b9b5c`
- Use the Notion connector (`notion-create-pages` against that data source). If the connector isn't available in this environment, say so in one line and paste the field values for Neil to add by hand — don't skip silently.

Set these properties:

| Property | Value |
|---|---|
| Name (title) | a short handle for the post (e.g. "Motorbike dad — Drift") |
| Pillar | the Pillar decided above — The Drift / Pain Points / The Transformation / The Now |
| Job | the Pillar's default Job unless overridden — Trust / Convert / Reach / Lead-gen |
| CTA | the closing mechanic mapped to the property options: Repost + magnet comment / Save / Comment keyword / Link in comment / Book a call / None |
| Type | Post, or Reel / Video / Short Video / Stories if the companion format is that |
| Status | Idea |
| Date | the target post date — the next free fixed slot for this Pillar (Tue = Drift, Wed = Transformation/Now, Thu = Pain Points). Ask Neil for the date only if the week is ambiguous. |
| Notes | a short human-readable block: `Pillar / Job / Hook / CTA / Source`, then a **`Visual:` line** — the chosen card line or carousel concept in one sentence, plus the saved asset filename once built (or `BRIEF ONLY — Paper not running`). This is the field Neil actually reads, so the visual plan lives here, not only in the body. |

Put the full post text in the page body. For a carousel, the full slide-by-slide brief also goes in the body. Report the created row's URL on the last line of your reply.

**Then produce the asset (next section) before you finish.**

---

## The visual — every post gets one, and the skill BUILDS it

Not optional, not "a brief for later". Every post leaves this skill with either a finished image saved to the assets folder, or (only if Paper isn't running) a complete brief plus a clear flag.

The design spec is `Claude Outputs/LinkedIn System/MMOM_Carousel-Design-Brief_v1.md` (canvas 1080×1350, cream/navy/one-peach palette, Marcellus + Inter + Biro Script, premium and pared back). Reference it, don't restate it.

**The build step (run it, don't describe it):**
1. Pick the visual by pillar (below) and settle the exact copy — the card line, or the full carousel slide list.
2. Invoke the production skill: **`mmom-visual`** for a hand-lettered card (Drift / The Now / a pull-quote), **`mmom-carousel`** for a Pain Points carousel or infographic. Pass it the copy + the design-brief tokens.
3. Move the exported file from `~/Downloads` to `03 Linkedin Assets 2026/` named `MMOM_LI_<post-slug>_v1.png` / `.pdf`.
4. Put that filename on the Notion row's `Visual:` line (in Notes) so Neil can click straight to it in Review mode.
5. If the Paper.design MCP is unavailable (Paper Desktop not open): write the full brief into the row body, set the Notes `Visual:` line to `BRIEF ONLY — Paper not running: <one-line concept>`, and tell Neil in one line so he can open Paper and ask for the batch.

**Not every post is a Paper card.** There are three visual sources — pick the one that fits the post, don't default:

1. **A real photo from the Image Bank.** Often the best choice for The Drift and The Transformation — "this is my family too" travels further than a designed card. Index: `Shared drives/Systems/01 Awareness/Linkedin 2026/03 Linkedin Assets 2026/00 Image Bank Index - LinkedIn Assets 2026` (a Google Sheet) and, if built, `Neil Image Bank/_INDEX.md`. Propose 1–2 images + a one-line caption in Neil's voice. Nothing suitable → `Visual: needs a photo — [what it should show]`.
2. **A hand-lettered / typographic card** (`mmom-visual`, Paper). For The Drift, The Now, and pull-quotes. Propose 2–3 short lines in Neil's voice, pick one, build it. Signed `— Neil` for the wistful ones.
3. **A carousel or infographic** (`mmom-carousel`, Paper). The default for Pain Points — the framework rides along as slides. **WIP: the carousel/infographic templates are not fully worked out with Neil yet.** Until they are, write the full slide brief into the row body and flag `Visual: CAROUSEL BRIEF — templates still to finalise with Neil` on the Notes line; don't auto-build a carousel he hasn't signed off the look of. Cards (source 2) and photos (source 1) are safe to build now.

By pillar, as a starting point (override when the post says otherwise):
- **The Drift** → a real photo, or a hand-lettered card. Offer both.
- **Pain Points** → a carousel/infographic (brief now, build once templates are agreed).
- **The Transformation** → a real photo, or a single pull-quote card. Carousel only if there's a genuine framework.
- **The Now** → a hand-lettered statement card, or a single-stat card.

The `Visual:` line goes in three places, identical: the Output format block in your reply, the Notion row's **Notes** property, and (for carousels) expanded to a full slide brief in the row body. Neil reads Notes — if the visual plan isn't there, it doesn't exist as far as he's concerned.

**Where images are saved.** Every finished image, card or carousel PDF is saved to:
`/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/../Shared drives/Systems/01 Awareness/Linkedin 2026/03 Linkedin Assets 2026/`
(Drive: https://drive.google.com/drive/folders/1knMSHsrKPhThLaLecy7OQOROvkoq-yZc). Name each file to match its Notion post so Neil can pair them at a glance: `MMOM_LI_<post-name-slug>_v1.png` (or `.pdf` for a carousel). Put that filename on the Notion row's `Visual:` line too. This is the folder Neil opens in Review mode: he reads the post in Notion, edits, then clicks through to this folder for the image and feeds tweaks back into Claude before posting. The `mmom-visual` / `mmom-carousel` skills export to `~/Downloads` first — move the file here as the final step.

**Writing the `Visual:` line into Notion — go through Chrome, not the MCP.** The Notion MCP tools (`notion-fetch`, `notion-update-page`, `insert_content`, etc.) are frequently *not* injected into a Claude Code session even though the connector shows Connected, and there is no desktop app to fall back to. Don't stall on it — drive Notion in the browser: use the `claude-in-chrome` tools (Neil's real Chrome, already logged into Notion). Open `https://www.notion.so/<page-id>`, click at the end of the target line/block, press `cmd+ArrowRight` then `Return`, and type. Two spaces after a pasted URL stop Notion swallowing the following text into the link.

**When a card is built after the post shipped** (Paper was down at the time, or `mmom-visual` / `mmom-carousel` runs later): go back to each post's Notion page and append one line directly under its existing image/visual note —

```
Final asset: <filename> — <Drive view link>
```

— and update the `Visual:` line in Notes from `BRIEF ONLY …` to the real filename. If the built artwork's wording ended up different from the brief (e.g. a banned word like "films" / "videos" / "movies" got swapped for "perspectives" — MMOM makes audio documentaries), note the change on that same line and fix the matching word in the post body copy.

---

## The litmus test

Before delivering, ask yourself:

> "Does this sound like something Neil would actually write — or does it sound like an AI trying very hard to imitate him?"

If it feels forced, pull back. Less imitation, more inhabitation.

Specifically: if there are no specific, domestic, recognisable details in the piece, it's probably not Neil yet. And if the reader could feel blamed for the drift — if there's even a whiff of finger-pointing — it stops being Neil.

And if the post ends without a clear action — save, repost, comment, follow — it's not done yet.

Remember: his single most important belief about writing is that the specific detail IS the emotional hook. Show the scene. Trust the reader to feel it.
