# Handover: what else to feed the second brain

Written 22 September 2026. A companion to the SOP and Agent Build Plan. That plan says what to build. This says what the brain still needs to know.

## The principle

Do not bulk-import. A brain full of raw transcripts is worse than an empty one, because the useful thing is buried and every future session pays to read past it.

Everything here follows the same shape: **read the source, extract the durable thing, write that into the repo, leave the source where it is.** A 300-page folder becomes a two-page distillation. The link back stays in case anyone needs the original.

## Answering the Cowork question directly

You suggested opening Cowork in Chrome to harvest old chats. **Not necessary.** They are already on this Mac, in plain files.

340 conversation transcripts, April to September 2026, at:
`~/Library/Application Support/Claude/local-agent-mode-sessions/43a624ef-e50a-451a-b645-1fca6bb5b691/4ee3cd9d-67b3-442b-bf7b-deec9396bd08/`

That is 275MB of your own thinking. Browsing it through Chrome would be slow, expensive and lossy. Reading the files directly is none of those things.

**What I have already taken from Cowork:** only the skills, from the Drive "About Me/skills" folder. Nothing from the conversations. That is the gap.

**What to do with them:** not import. Mine them. Run a pass that pulls out decisions made and never written down, prices and policies stated in passing, objections real prospects raised, phrases you reached for repeatedly, and things you said you would do and did not. Write those into the repo as short notes. Delete nothing.

Worth doing as its own session, because 275MB needs a careful, targeted read rather than a general trawl.

## Everything else, in priority order

### 1. The SOPs in Shared drives/Systems

Covered as Step 1 of the build plan. The single biggest gap. The brain holds skills, which are how Claude does a job, but almost no procedures, which are how the business does a job.

### 2. Sales call transcripts

`Systems/Fathom Transcripts` and the per-client Sales Call folders. This is the richest voice-of-customer source you own and the brain currently holds a VoC *system* without much recent VoC *evidence*.

Extract: objections in the words prospects used, what makes someone say yes on the call, what makes them go quiet afterwards, which parts of the offer they ask about and which they ignore.

### 3. Testimonials and wrap-up transcripts

`08 Delivery & Referrals/04 Testimonials` and the wrap-up sessions. What families say changed for them, in their words. Feeds proposals, the website and every piece of content.

Note: `mmom-voice-profile-refresh` already exists to do part of this. Check what it covers before duplicating it.

### 4. The Airtable CRM schema

Base `apprk3RUXdvZNJ8TF`. The data stays in Airtable, but the brain should hold a note of what tables and fields exist and what each stage name means. Without it, every session that touches the CRM rediscovers the structure from scratch.

### 5. The numbers

The cost model is now summarised in `knowledge/offer/pricing.md`. Still missing: actual conversion rates, what a family is worth, where leads come from, and the five numbers on your wall. Facts, not files, and they change, so date them.

### 6. The advisor corpora

`~/src/advisors` holds distilled Hormozi, Chris Donnelly, Lara Acosta and Matt Gray material, kept current by four weekly tasks. These are reference libraries rather than your own thinking, so **leave them where they are**. Just add a line in `INDEX.md` saying they exist and what each is for, so future sessions know to look.

### 7. Website and email copy

The live site copy and the best-performing Kit emails. What has actually worked on real audiences, rather than what you think should work.

### 8. The decision log you do not have

Not a source, a habit worth starting. Every significant call with the reason behind it: why Gold was deleted, why per-parent pricing, why Cowork was retired. Reasons decay fastest of all and no system captures them today.

## What not to feed it

- **Raw transcripts in bulk.** Distillations only.
- **Anything already live somewhere authoritative.** Airtable records, Kit subscribers, Drive client files. Note where they are, do not copy them.
- **Old versions.** The repo keeps its own history, so superseded drafts just add noise.
- **The HyperFrames and generic file skills.** General tooling, not business knowledge.
- **Anything with client personal data.** This repo is on GitHub. Nothing identifying goes in.

## Suggested order

Step 1 of the build plan (the SOPs) first, because everything else assumes it. Then the Cowork mine, because it is the biggest untouched store and the only one at any risk of being lost. Then sales calls and testimonials together, since they feed the same skills. The rest can follow as needed.
