# Homepage tiers: match the live offer (plan, nothing sent to Lovable)

9 October 2026. Sources read: Lovable `TierCards.tsx` and `index.tsx` (project M&MOM), Henry Sturgess proposals (9 Oct short deck, 11 Sep full deck), Gem Catlin call script (15 Sep deck terms), `knowledge/offer/pricing.md`, Cost Model V10.12 (Proposal Picker, Delivery Costs, Change Log). The Google Doc you linked is the V10 "How to read it" guide. It stops at V10.5 and is superseded on chapters and prices by pricing.md, so I used pricing.md and the live sheet.

## What is wrong on the homepage now

| Where | Live now | Offer says |
|---|---|---|
| Tier names | "Family Audio Documentary", "Multi-generational Family Biopic" | Family Documentary, Full Chorus |
| Silver and Gold shape | Silver: "individual Child Reflection sessions". Gold: same plus 4 parent sessions | Silver (C) is ONE shared 90-minute children's session. Gold (D) is a private hour for each child. Both are 3 parent sessions |
| Hero Story | "Child Inputs, offline capture" | B: your own recorded hour plus a family wrap-up. Wrap-up is missing from every card |
| Clips on Silver and Gold | "Range of shareable audio and video clips" | Not in any option. Mementos (3 audio clips plus 1 video memento) is a £350 add-on at 72.9% margin. Clips are still uncosted in V10 |
| Gold extras | 4th session, grandchildren, prologue, in-home recording, award winning montage, Interactive Family Storybook | 4th session is a £750 add-on, grandchildren £200. Prologue, in-home recording, Storybook are in no deck and not in the cost model |
| Durations | 4, 12, 16 weeks. "12-week concierge" | No tier duration in pricing.md. Henry's decks say twelve weeks start to finish for Hero Story |
| "Most families choose this" badge on Silver, and "Most families choose Silver" in step 2 | Fixed default | The proposal skill dropped the fixed default in v3.0. Recommendation follows family shape. Metal also leads here, brand name should lead |
| Guarantee (section 9) | "after your first session" | Full refund after the kickoff call and before the first recorded session |
| Section 15 | "You'll get audio highlights, video mementos you can share" | Reads as included. Mementos is paid |

## Proposed cards

Brand name leads, metal stays as the small sub-heading. Everything below is in the live decks, per parent. No prices on the page, as now.

**Hero Story** (bronze)
- Reflection guides, a life chart and audio for your parent, so nobody walks in cold
- 3 x 2-hour recorded sessions with your mum or dad
- Your own 1-hour session, so you are in the record too
- A family wrap-up once you've listened
- Fully edited, with music and album artwork

**Family Documentary** (silver)
- Everything in Hero Story, except your hour becomes one 90-minute session with all the children together
- Briefing and reflection guides for every sibling
- 3 x 2-hour sessions with your mum or dad
- A family wrap-up with everyone, once you've listened
- Fully edited, with music and album artwork

**Full Chorus** (gold)
- Everything in Family Documentary, except every child gets their own private hour with me
- Nobody shapes what they say around a sibling
- 3 x 2-hour sessions with your mum or dad
- A family wrap-up with everyone, once you've listened
- Fully edited, with music and album artwork

**Strip under the cards, no prices:** "Add to any option: grandchildren's voices played to your parent live, Mementos (three audio clips and a video memento), an extra 2-hour session."

## Decisions I need from you before it goes to Lovable

1. **Hero Story shape.** Homepage Hero Story = option B (your own hour, as Henry's deck). Your note to Alison described the lighter "offline brief, then I record with Mum" version, which is option A. I recommend B on the page and A stays a call-only fallback. OK?
2. **Durations.** I have nothing settled to put on the cards. Drop the line, or give me the numbers.
3. **The Silver badge and step 2.** I recommend removing the badge and rewriting step 2 to "three ways to do this, the right one depends on who's in your family". Or keep Silver as the "most chosen" if the 37 families really lean that way. Your call, I can't check the count.
4. **Gold extras (prologue, in-home recording, Storybook, award winning montage).** Real and delivered, or retire? If real, they need a price and a place in the sheet before they go back on the page.
5. **Family count.** Homepage says 37, the proposals say 35. Not part of this job, but they should agree.

## Margin check against V10.12

- A to D at LIST sit at 60% to 66% on full cost, against the 50% floor. That holds only for what is in the decks: sessions, edit, music, artwork, wrap-up. Every extra I am removing (clips, prologue, Storybook, 4th session, grandchildren) was either an uncosted promise or a paid bolt-on given away on a public page.
- Mementos at £350 (72.9%), grandchildren £200 (68.8%) and the extra 2-hour session £750 (62.3%) are the add-ons the strip names.
- Chapters, if a card wants them (one parent): Hero Story 8, Family Documentary 8, Full Chorus 9 to 11. I left them off the cards. Say if you want them.

## Build steps once you've answered

1. In Lovable, search the whole project for "Biopic", "Family Audio Documentary", "silver", "12-week" and "first session" before editing. The `/refer-[family]` pages and FAQ may carry copies.
2. Brief to Lovable, plan mode first, touching only: the `TIERS` array in `src/components/mmom/TierCards.tsx`, the "Most families choose this" badge, homepage step 2 copy in `src/routes/index.tsx`, the guarantee sentence in section 9, and the "video mementos" sentence in section 15. Name every label around each slot in the brief (lesson of 9 Oct).
3. Check the preview at desktop and phone width before publishing. Nothing goes live until you've seen it.
4. Log it in `knowledge/lessons.md` and note the date in `pricing.md` if any decision above changes the offer.
