---
name: proposal
description: Generates a personalised Me & My Old Man sales proposal HTML file for a named prospective client. ALWAYS use this skill when Neil types /proposal followed by any client name, or asks to "create a proposal for", "write a proposal for", "build a deck for", or "generate a proposal for" any person. The skill reads the client's Fathom sales call transcript from Google Drive, the current offer ladder (options A to D, see knowledge/offer/pricing.md), and the latest testimonials, then produces a complete branded 6–12 slide HTML deck in the MMOM light design system. One command → finished proposal file, ready to open in browser and print to PDF.
---
<!-- v1.5 — 2026-07-23: Gold→Bronze→Silver anchor ordering; single-price separate-interview model replaces dual options; full standalone value table required for all three tiers, not just the recommended one; bonuses+guarantee merged into one dedicated closing slide; added one-week booking urgency discount. Lessons from Sam Tillett proposal V2→V3 rebuild. -->

<!-- v2.0 — 2026-09-22: removed the stale V8 tier prices, which the skill was instructing the model to treat as ground truth in client-facing decks. Replaced with the A to D ladder and a hard pointer to knowledge/offer/pricing.md. The three-tier slide/anchoring logic below is flagged as unrewritten and needs Neil. -->

# Me & My Old Man — Proposal Generator

You generate a bespoke 6–12 slide HTML sales proposal for Neil Taylor's family storytelling service. Each proposal must feel like it was written only for this one person — because it was.

---

## File paths (fixed — do not prompt Neil for these)

**Sales call transcripts root:**
```
/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/Shared drives/Systems/03 Sale/02 Sales Call/
```

**Three-tier offer:**
```
/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/FounderOS/02 Offer Optimization/Offer Optimization May-26/03 Neil's Latest Offer/
```

**Rule:** use the HIGHEST version number `MMOM_3-Tier-Offer_V*.md` in that folder (V7 beats V6). The offer changes — never assume V6 is current.

**Testimonials folder:**
```
/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/Shared drives/Systems/08 Delivery & Referrals/04 Testimonials/
```

**Cost model folder:**
```
/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/FounderOS/02 Offer Optimization/Offer Optimization May-26/03 Neil's Latest Offer/
```

---

## Step 1 — Find the client folder

List the Sales Call folders and fuzzy-match the client name argument (case-insensitive, partial match is fine):

```bash
ls "/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/Shared drives/Systems/03 Sale/02 Sales Call/"
```

Folders are named `YYYYMMDD FirstName LastName`. If multiple matches, take the most recent (highest date prefix). Note the folder date.

---

## Step 2 — Read source files (do all four in parallel)

1. **Transcript**: Find the `.md` file inside the matched folder (ignore `.gdoc` files). Read it in full.
2. **Three-tier offer**: Read the full offer doc from the path above.
3. **Testimonials**: Run `ls` on the testimonials folder, take the file with the highest date prefix, read it.
4. **Cost model**: See Step 2b — run simultaneously with the above three.

---

## Step 2b — Read the cost model for current pricing (MANDATORY)

The cost model is the single source of truth for all pricing. Always check it before drafting.

Find the latest `.xlsx` in the Cost model folder (highest version number) and read the `📊 Summary` sheet. If a `2-Parent Pricing` sheet exists, read it too (see Appendix C).

```bash
python3 -c "
import pandas as pd, os, glob
folder = '/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/FounderOS/02 Offer Optimization/Offer Optimization May-26/03 Neil'\''s Latest Offer/'
files = sorted(glob.glob(os.path.join(folder, '*.xlsx')))
path = files[-1]
print('Reading:', path)
df = pd.read_excel(path, sheet_name='📊 Summary', header=None)
for i, row in df.iterrows():
    if i > 20: break
    vals = [str(v) for v in row if str(v) != 'nan']
    if vals: print(i, vals)
"
```

> **STOP — THESE PRICES ARE WRONG. READ THIS BEFORE GENERATING ANYTHING.**
>
> The V8 tier figures that used to sit here (Bronze £1,750, Silver £3,800,
> Gold £8,000, and the 2P set) were superseded on 4 September 2026 and
> removed on 22 September 2026. They were roughly £650 under the current
> price for the nearest equivalent option. Do not reconstruct them from
> memory, from an old proposal, or from an archived copy of this skill.
>
> **Read `knowledge/offer/pricing.md` and take every figure from there.**
> It is the only current source. Margin-check any agreed price against
> Cost Model V10 (`1vN5YckOTYgne0yppRkfm2jYBjPp1ff6ug8gWntLeS8k`).

**The current ladder, one parent (LIST, per parent):**

| Option | What they're buying | LIST | Standalone value |
|---|---|---|---|
| A | Solo, no child interview | £2,400 | £7,000 |
| B | Solo, buyer interviewed | £3,150 | £8,500 |
| C | Children batched, one session | £3,350 | £11,000 |
| D | Children individually, 2 children baseline | £4,000 | £13,000 |

Option D adds £300 per child above the baseline of 2, value uplift £1,000 per
extra child. Two-parent LIST is 2.5% off double the one-parent LIST, rounded
up to the nearest £100 — confirm the exact figure in `pricing.md` rather than
calculating it here.

**Families never see A to D.** They see Hero Story (A and B), Family
Documentary (C), Full Chorus (D), with the metal name only ever as a
sub-heading. The brand name always leads.

> **Also stale, not yet rewritten:** everything below this point that assumes
> three tiers — the Gold → Bronze → Silver slide order and its anchoring
> logic, the per-tier value stacks, the bonus structure, the "Silver is
> always the default" rule, the Silver+ 2P scenario, and the per-tier
> inclusion lists. The pricing is now four options, not three. Ask Neil how
> he wants the tier comparison slides to work under A to D before generating
> a deck that depends on them. Flag this to him rather than improvising a
> mapping.

**Hard override rule:** If Neil's prompt explicitly states a price or option, use that. In all other cases `knowledge/offer/pricing.md` is ground truth — never this file, and never a figure remembered from a previous proposal.

---

## Step 3 — Transcript Analysis Protocol

Run all ten steps before writing a word of the proposal. Then output the pre-flight note (Step 3c).

### 3.1 — Buyer type

Identify which type this buyer is. It determines the emotional framing for the entire proposal.

| Type | Signal | Framing emphasis |
|---|---|---|
| **Biography Buyer** | Adult child (often daughter). Initiates because the parent never will. Emotionally responsible for the family. | Fear of regret. Pre-emptive action. "You don't need anyone else's agreement." |
| **Gift Buyer** | Buying for a spouse/partner whose parent is elderly or unwell. | Gift frame. Second-person throughout ("she'll hear her mother's voice"). |
| **Health-Scare Buyer** | Diagnosis or prognosis has made the window feel suddenly real. Urgency is already live — don't manufacture it. | The window. What's at stake in six months. |
| **Regret-Avoider** | Lost a parent already. Buying this for the remaining one. Knows exactly what the alternative costs. | "You already know what the alternative feels like." |
| **Milestone Buyer** | Birthday, anniversary, or reunion as the anchor. Time pressure is a date, not a health concern. | "She turns 80 in [month]. This is the gift." |

### 3.2 — Trigger event

What brought them to Neil? Quote the exact line from the transcript where this is clearest.

Look for: a diagnosis or health scare · a recent bereavement · a milestone event · a referral · a persistent sense that time is running out.

This quote goes on Slide 3.

### 3.3 — Dream state

What do they actually want to feel or have when this is done? Listen for:
- "I just want to know..." (curiosity about a parent's inner life)
- "I wish I'd asked..." (pre-emptive regret)
- "My kids would..." (next-generation thinking)
- "We've always been close but..." (desire to go deeper)
- "He never talks about..." (frustration with surface-level access)

Quote the clearest expression. This informs Slide 5.

### 3.4 — Pain points and fears

Extract 2–3 specific fear expressions verbatim. Common patterns:
- Parent is ageing or health is changing
- The stories will be lost
- Already lost one parent and knows the regret
- Sibling relationship is strained — this feels like a way to fix it
- The parent is a "closed book" — tells anecdotes but never goes beneath the surface

**CRITICAL UPDATE #3:** Do NOT show these pain points as a separate blockers slide early in the proposal. Save them for Slide 9 (cost of delay). The narrative flow is: pain point → dream state → show offer as solution → *then* address blockers and fears.

### 3.5 — Objections

| Objection type | Transcript signal | Diagnosis |
|---|---|---|
| Price | "That's a lot", "need to think", sibling cost-splitting mentioned | Logistics problem or genuine constraint? |
| Timing | "After Christmas", "when things settle down" | Real or avoidance? Name the cost of delay specifically. |
| Parent resistance | "He won't want to", "she's quite private" | Solvable. Parents almost always come round. Use Steve Millard testimonial. |
| Sibling alignment | "Need to check with my brother/sister" | Who is the actual decision-maker? Bronze removes this blocker entirely. |
| Overwhelm | Too many options, unclear next step | Simplify the path in Slide 3. |

A price objection is almost never purely about money. Identify the real fear underneath it.

### 3.6 — Family dynamics

Map the family:
- How many adult children? Names if given.
- Who is the emotional driver (will make this happen)?
- Who is the potential blocker (sceptical sibling, reluctant parent)?
- Are both parents alive? Which is the priority?
- Are grandchildren in the picture? Ages?
- Any estrangements, sensitivities, or topics to handle carefully?

**CRITICAL UPDATE #1:** Refer to people's parents as **Mum (FirstName)** and **Dad (FirstName)** throughout all analysis and proposal copy.

Example: "Mum (Linda)" or "Dad (James)" — not "Linda" or "your mum" alone.

**Two-parent flag:** If both parents are mentioned as subjects (not just alive), flag this in Step 3c and follow Appendix C before generating.

### 3.7 — Buying signals

Strong signals (close to yes):
- "I can picture exactly how it would be"
- Asking detailed questions about process, timeline, delivery
- Mentioning a specific date or occasion
- Asking "what happens next"

Weak signals (note but don't over-weight):
- General enthusiasm without specificity
- "I'll talk to my..." without a timeline

### 3.8 — Verbatim gold

Extract every quote that should appear in the proposal verbatim. Aim for 5–8. Tag each with where it lands:
- Single best quote → Slide 2 (emotional anchor)
- Trigger event quote → Slide 3
- Fear/pain quote → Slide 9
- Close quote → Slide 12

### 3.9 — Tier recommendation

State: recommended tier and why · alternative if relevant · pricing flexibility notes · sensitive topics.

**Silver (£[see pricing.md] · 12 weeks) is always the default** unless one of these hard overrides applies:
- Client explicitly stated they cannot spend more than £1,800
- Fixed deadline that physically cannot fit 12 weeks
- Solo buyer confirmed, no siblings, no grandchildren, no family dimension — and they explicitly need speed over depth

Bronze (£[see pricing.md]) is never the "cheap option." It is a complete, standalone experience. The only thing it doesn't include is siblings.

**Gold (£[see pricing.md] · 16 weeks):** Recommend when grandchildren are young and the window for capturing their voices alongside a grandparent is genuinely live. Gold always appears in the tier comparison as a price anchor.

**Silver seeds — mandatory:** When selecting facts for Slide 2, deliberately choose the details that build the case for Silver — siblings mentioned, multiple children, family stories that belong to more than one person, grandchildren. By the time the prospect reaches the tier slide, they already feel why Silver is right.

**Single price, not dual options — CRITICAL UPDATE #11:** When siblings are involved, default to ONE price with separate (not joint) sibling interviews as standard — never present a joint-session option and a separate-session option side by side ("Option A / Option B"). Two priced options force the prospect to do maths and second-guess themselves; one option with the best structure already built in removes that friction entirely. Explain the separate-interview benefit directly: sitting down alone, before recording, to really think about what you want to know about a parent is part of the value, not just prep for it. Kept separate, no one is shaping what they say around a sibling — no groupthink. Each person prepares, reflects, shares, and listens back to their own reflections and each other's afterwards. Siblings very often name this as one of the biggest transformations of the whole experience. Only offer a joint session as the default if the prospect explicitly said on the call that they want to be interviewed together.

### 3.10 — Testimonial selector

Match 2–3 testimonials to this prospect's situation (see Appendix A for full matching table). One per slide. Pull exact wording from the testimonials file — never paraphrase.

---

## Step 3b — Three Hormozi elements (non-negotiable)

**1. Reason Why (closing summary slide — see below)**
Show why the price is lower than the standalone value. One sentence. Direct. No false modesty. Example: "I take on four Silver families per month. That's not a marketing line — it's how I can promise you that every session gets my full attention, from kickoff to delivery. The price reflects that model."

**2. Bonus expiry + booking discount (closing summary slide — see below)**
Calculate today + 7 days. Format: "Bonuses included if confirmed by [DATE]." Styled callout directly below the value stack rows — same visual level as the price, not a footnote.

**CRITICAL UPDATE #7:** If Neil explicitly mentioned a bonus on the call (e.g., "if you sign within a week, I'll include Audio Story Reels"), include that bonus in the callout. Make the one-week expiry explicit and specific.

**CRITICAL UPDATE #12 — urgency discount:** Alongside (or instead of) bonus items, offer a 5% discount on the recommended tier's price if the prospect books within one week of the call/proposal date. State the discounted price only in the private note to Neil (see Step 5) — do not print the discounted number in the client-facing HTML unless Neil has explicitly said to include it there. Default assumption: show the full price in the deck, keep the discount maths in the private note so Neil can offer it verbally or by follow-up if useful, not have it undercut the anchor price on the page itself.

**3. Cost of delay + guarantee (closing summary slide — see below)**
Don't assert urgency — argue it. One honest, precise statement about what waiting actually costs. Adapt to their specific situation — if health is a factor, name it. If memory concerns were mentioned, reference them. Use their own words. The Angus Watts line ("You always assume there will be more time. Now is the time.") is the strongest closer when it fits.

**Closing summary slide — CRITICAL UPDATE #13:** Bonuses, urgency deadline, and guarantee belong together on ONE dedicated slide near the end of the deck (immediately before the final "say yes" slide), not scattered across separate slides or folded quietly into the value stack table. Structure it as: what everything is worth standalone → what the bonuses are worth and when they expire → the investment price → the guarantee. This is the "here's what it should cost, here's what it does cost, here's what you get, here's the bonus, here's the guarantee" slide — it's the last piece of resistance-removal before the close, so give it its own full slide rather than compressing it.

**Guarantee copy — always use this framing unless Neil gives a different one for this client:** "If after your kickoff call — and before [Parent]'s first recorded session — this doesn't feel right for any reason, a full refund is issued immediately. No questions asked." Pair it with the positive-spin proof stat, pulled fresh from the latest count (do not hardcode a number that will go stale): "[N] families · [N] countries · 0 guarantees invoked." Frame as 100% progressed / 0% invoked — never phrase the guarantee defensively.

---

## Step 3c — Pre-flight output

Output this before generating the HTML:

```
PROPOSAL PRE-FLIGHT — [Client Name]
──────────────────────────────────────────
Buyer type:       [type from 3.1]
Tier:             [Bronze / Silver / Gold] — [one sentence why]
Emotional anchor: "[exact quote from 3.8]"
Trigger event:    [from 3.2]
Key objection:    [from 3.5]
Slide 3 mode:     [Re-engagement / First-time]
Testimonials:     [which ones, which slides]
Watch-outs:       [two-parent flag / sensitive topic / sibling blocker / anything unusual]
──────────────────────────────────────────
Generating proposal now.
```

**Two-parent rule:** If there is a two-parent flag, STOP after the pre-flight note and ask Neil: "Two parents were mentioned — which option, and one parent or both?" Take the two-parent figure from `pricing.md`. Wait for the answer before generating.

For all other situations: output the pre-flight note and immediately proceed to generate. No waiting.

---

## Step 4 — Generate the proposal HTML

Read `references/slide-structure.md` for the exact HTML pattern for each slide. Use 6–12 slides — include only the slides that add genuine value for this prospect's situation; omit slides where you have nothing specific to say.

Build a single self-contained HTML file:
- Inline `assets/proposal-light.css` inside a `<style>` tag in `<head>`
- Inline `assets/deck-stage.js` at the bottom of `<body>`
- Load Google Fonts via CDN: `Inter` (300,400,500,600,700), `Marcellus`, `Cormorant+Garamond` (ital,wght@0,300;0,400;0,500;1,300;1,400;1,500)

**Personalisation is not optional.** Every placeholder must be replaced with real content from the transcript.

**CRITICAL UPDATE #2:** When addressing the prospect, always write to them directly as "you." Never use their first name in body copy. The prospect is reading this—addressing them by name mid-document feels unnatural and formal. The only places their name appears are: the cover title tag ("For [Name]") and the HTML `<title>` tag.

**Slide-by-slide rules:**

- **Slide 1 cover** — context tag from: INTRODUCTION (first proposal after a call) · RE-ENGAGEMENT (lapsed prospect) · GIFT (buying for someone else) · MILESTONE (birthday/anniversary anchor). Add one line naming the occasion.

- **Slide 2 quote** — their exact words from the call, verbatim. Silver seeds: select beats that build the case for Silver — siblings, multiple children, grandchildren, family stories that belong to more than one person.

- **Slide 3 mode:**
  - **First-time:** Name their trigger event exactly as it happened ("Your Mum (Linda)'s diagnosis in March", never "a health event"). State what the window is. What changes if they wait. Close with their own words.
  - **Re-engagement:** Name the old quote. Name the specific blocker that stopped them. Show THEN vs NOW. Name what they can say yes to today.

- **Slide 4 Bronze identity line** — mandatory. In the `compare-note` section (or immediately below the table): *"Bronze is for people ready to act now, for their parent, alone. It is not an entry-level product — it is a complete, standalone experience. The only thing it doesn't include is siblings."* Never present Bronze apologetically.

- **Slides 5–7 Tier details** — CRITICAL UPDATE #4: Explain each tier in detail BEFORE showing the summary table.

  **Order — CRITICAL UPDATE #10 (price anchoring):** Show Gold first, then Bronze, then Silver last. This is deliberate Hormozi price anchoring: Gold sets the ceiling (makes the real offer feel reasonable by comparison), Bronze shows the floor (proves the model isn't only expensive), Silver lands last as the obvious, already-desired middle. Never default to Bronze→Silver→Gold — that order buries the anchor and makes Silver look like an upsell rather than the landing choice.
  - Slide 5: Gold — full standalone value table (every line item priced, not summarised) + investment price + "who this is for" / "not the shape of what you've described" framing if Silver is the recommendation. This is a genuine full slide, not a compressed "for context" strip.
  - Slide 6: Bronze — full standalone value table + investment price + Bronze identity line (see below). Also a genuine full slide, matching Gold's treatment.
  - Slide 7: Silver — the recommended tier. Full standalone value table + investment price + the specific benefit/differentiator for this family + one matched testimonial folded into this slide (do not give the testimonial its own slide).
  - Slide 8: Summary comparison table only if it adds something the three full slides didn't already show — often it's redundant once Gold/Bronze/Silver each have their own complete slide. Default to omitting it unless Neil asks for a side-by-side.

  **Every tier gets its own full value-stack table.** Do not show a detailed table for the recommended tier only and a compressed price-only mention for the other two — Gold and Bronze each need their standalone value total and price shown with the same weight as Silver. Pull exact line items and figures from the current offer doc / cost model, never estimate.

- **Tier naming — CRITICAL UPDATE #6:** Always show tier names next to prices.
  - ✅ "Bronze: Hero Story Capture — £[see pricing.md]"
  - ✅ "Silver: Family Stories Across Generations — £[see pricing.md]"
  - ✅ "Gold: Multi-Generational Heirloom — £[see pricing.md]"
  - ❌ Do NOT write "Bronze — £[see pricing.md]" without the name.

- **CRITICAL UPDATE #5:** Verify tier inclusions against the Latest Offer Document before writing Slides 5–7.
  - **Bronze NEVER includes:** child interviews, personalised era soundtrack, Audio Story Reels (unless explicitly listed as current bonus), any extended family voices.
  - **Bronze ALWAYS includes:** one parent, hero story capture, deep-dive interviews, audio file output.
  - **Silver MUST mention:** sibling inclusion (group session with all children), both parents' full stories (if two-parent), grandchildren voice collection (if mentioned).

- **Closing summary slide (bonuses + guarantee)** — use figures from Step 2b for the recommended tier. Include: standalone value total, bonus items with combined value and expiry callout (explicit date), investment price, Reason Why paragraph, and the guarantee block (see Step 3b). **Payment plan line:** include only for first-contact proposals (context tag: INTRODUCTION or MILESTONE). Do NOT include for re-engagement proposals (context tag: RE-ENGAGEMENT) — lapsed prospects who walked away on price should not see a payment plan offered upfront; it signals desperation. If they ask, address it in follow-up.

- **Slide 9 cost of delay** — argued not asserted. Specific to their parent's situation. Never vague. This is where pain points from 3.4 belong — NOT shown earlier.

- **Slide 9–10 CTA buttons** — CRITICAL UPDATE #9: All CTAs are payment-focused, never "book a call."
  - Under each tier price, add a button: "Start [Tier Name]" or "Get [Tier Name]"
  - Example: Bronze button = "Hero Story Capture — £[see pricing.md] / Start Now"
  - Link to payment/booking system (Stripe, Calendly, or email reply to Neil)

- **Slide 12 close** — do NOT address the prospect by name anywhere in the body copy. They are reading this — it feels unnatural to be called by name mid-document. The cover title tag ("For [Name]") and the HTML `<title>` tag are the only places the name appears. Repeat the three tier buttons in a footer.

**CRITICAL UPDATE #8:** Never pre-empt sales tactics in copy. Remove any line that explains *why* a constraint exists.
- ❌ "That limit isn't there to create pressure—it's just how I manage my calendar."
- ✅ Omit. Just state the limit: "Available slots: 2 this month."
- ❌ "I'm offering a discount for this week only, not to rush you, but because..."
- ✅ Omit the disclaimer. Just: "Bonuses included if confirmed by [DATE]."

**Copy rules — see Appendix B for the full list. Key rules:**
- Never use: heirloom, keepsake, preserve, legacy (avoid), precious, priceless, heavy lifting, gift of voice, process (say "experience")
- No performed emotion ("truly special", "so meaningful")
- No over-qualification ("this might be...", "perhaps...")
- Never use the prospect's name in body copy — cover tag and HTML title only
- Present price without apology

---

## Step 5 — Save and output private note

**Save to:**
```
[matched_client_folder]/[YYYYMMDD] [FirstName LastName] Proposal.html
```
where YYYYMMDD = today's date.

**Output this private note in the conversation (not in the HTML):**

```
## ⚠ PRIVATE NOTE FOR NEIL — DO NOT SEND TO CLIENT

Situation read: [2–3 sentences on what's really going on with this buyer]
Pricing flexibility: [what to offer if they push back — never reduce scope]

VOC phrases used verbatim:
  - "[quote]" → Slide [X]
  - "[quote]" → Slide [X]

Sensitive topics for follow-up: [anything to tread carefully on]

One-week booking discount (5% off recommended tier, do not print in the deck unless Neil says to):
  Full price: £[X] → Discounted price if booked by [today + 7 days]: £[X × 0.95, rounded]

Fill in before sending:
  ☐ Bonus expiry date (closing summary slide): [today + 7 days, calculated]
  ☐ Availability slots (Slide 11): how many open this month
  ☐ Next available month (Slide 11): [month name]
  ☐ Booking link (Slide 12): Calendly or booking link
  ☐ Session start dates (if relevant): any specific weeks mentioned on the call
  ☐ Guarantee proof stat: confirm current family/country/invoked count before using — do not reuse a stale number
```

**Then tell Neil:**
1. Full path to the saved file
2. **To view**: double-click (opens in browser), arrow keys to navigate
3. **To send as PDF**: File → Print → Save as PDF
4. One sentence: tier recommended and why
5. One sentence: the personalisation hook you led with

---

## Appendix A — Testimonial matching

One per slide. Exact wording from testimonials file only — never paraphrase. Attribution: *"Quote."* — First name, Relationship.

| Situation | Use |
|---|---|
| Price objection / "is it worth it" | Chris Walton — *"It's not really a decision. Just go and do it."* |
| Closed-book dad | Steve Millard — *"I've cried. I've laughed uncontrollably."* |
| Siblings / family reconnection | Leah — *"It definitely brought the siblings closer together."* |
| Health scare / diagnosis | Edward Finley — *"Each episode has been its own dopamine hit of joy."* |
| Gift buyer | Chris Walton — *"they were both almost speechless"* |
| Parent as hero / milestone birthday | Frank Watts family — *"Five hours later, he was still sharing."* |
| Wanting more depth / parent never opens up | Angus Watts — *"You always assume there will be more time. Now is the time."* |
| Values the experience over the output | Axel — *"The audiobook is just a result. The whole change happened throughout."* |
| Legacy / grandchildren | Laura Frith — *"It is going to be even more important for my children."* |
| Dad reluctant, mum enthusiastic | Jennifer Millard — *"The best thing we have done in years."* |

**Best all-purpose:** Steve Millard and Chris Walton. **Health-scare contexts only:** Edward Finley. **Values experience over output:** Axel.

---

## Appendix B — Copy rules

### Never use these words
heirloom · keepsake · preserve · legacy (avoid, use sparingly if at all) · precious · priceless · heavy lifting · gift of voice · process (always say "experience")

### Never do these things
- Inspirational-quote tone
- Corporate language ("deliverables", "engagement", "touchpoints")
- Performed emotion: "this is so meaningful", "truly special", "what a journey"
- Mortality-forward messaging without hope
- Over-qualification: "this might be...", "perhaps...", "you could consider..."
- Apologise for the price or preamble before stating it
- Use the prospect's first name anywhere in the body copy — the prospect is reading this and being addressed by name mid-document feels unnatural. Name appears only in the cover tag ("For [Name]") and the HTML `<title>`.
- Explain why constraints or limits exist (no "That's not to create pressure, it's just...")

### Always do these things
- Write like Neil talks — warm, direct, plain English
- Lead with their situation, not with the offer
- State price confidently
- Use verbatim quotes in quotation marks and italics
- Match testimonials to the specific situation, not just the sentiment
- Close with their own words
- Refer to parents as Mum (FirstName) and Dad (FirstName)

---

## Appendix C — Two-parent protocol

Two-parent interest is the most common source of pricing confusion. Handle precisely.

**When the transcript indicates interest in capturing both parents:**
1. Flag it in the pre-flight note
2. Stop and ask Neil which pricing scenario applies before generating
3. Use V8 2P pricing — never invent a bundle price

**Official 2-parent prices (V8):**

| Tier | Price | When to use |
|---|---|---|
| Bronze 2P | £[see pricing.md] | Two parents, two complete stories, delivered as a paired collection |
| Silver 2P | £[see pricing.md] | Full family experience for both parents. Children's group session shared — no extra cost. |
| Silver+ 2P | £[see pricing.md] | Silver 2P with individual 1:1 child briefings instead of the group session. Use when sibling dynamics are complicated. |
| Gold 2P | £[see pricing.md] | Full multi-generational biopic for both parents. Every lever deployed. |

**Starting with one parent:** If the prospect wants to start with one parent only, generate the single-parent proposal. Flag in private note: "Two-parent interest identified. Two-parent LIST is in `pricing.md`. Mention only if they ask."

**Silver+ signal:** Listen for: siblings who don't get on · geographical distance · one child who seems less involved · "we wouldn't all say the same thing in front of each other." Don't pitch it — hear it. The conversation leads you there.

**Additional children in Gold:** Gold includes 3 children's 1:1 sessions. Extra children beyond 3: £200/child. Mention conversationally only if a family has 4+ children. Never put it in the proposal.

---

## THIRTEEN CRITICAL UPDATES — Summary

These changes reshape the proposal to be clearer, more direct, and prospect-focused:

1. **Parent naming (Mum/Dad FirstName)** — Section 3.6, Appendix B, all copy
2. **Write to prospect as "you"** — Never use their name in body copy; appears only in cover tag and HTML title
3. **No blockers on early slides** — Move pain points to the closing summary slide; flow is pain → dream → solution → objection handling
4. **Tier details before any summary table** — Slides 5–7 each fully explain one tier; a comparison table is optional and only added if it adds something new
5. **Verify Bronze/Silver inclusions** — Always check Latest Offer Document; Bronze never has child interviews or personalised era soundtrack
6. **Add tier names next to prices** — "Bronze: Hero Story Capture — £[see pricing.md]" not just "Bronze — £[see pricing.md]"
7. **One-week bonus expiry explicit** — If mentioned on call, include it as a dated callout on the closing summary slide
8. **Never pre-empt sales tactics** — Remove disclaimers that explain *why* a limit exists
9. **CTA is payment, not "book a call"** — Buttons link to payment/booking, not another call
10. **Gold → Bronze → Silver slide order** — Anchor high (Gold), show the floor (Bronze), land on the recommendation (Silver) last. Every tier gets a full standalone value table, not just the recommended one.
11. **Single price, not dual options** — When siblings are involved, default to one price with separate (not joint) interviews built in as standard. Never present "Option A / Option B" side by side.
12. **One-week booking discount (5%)** — Offer alongside bonuses; keep the discounted number in the private note, not printed in the client-facing deck, unless Neil says otherwise.
13. **Bonuses + guarantee share one closing slide** — Standalone value → bonuses + expiry → investment price → guarantee, all on one dedicated slide right before the final close, not scattered or buried in the value table.
