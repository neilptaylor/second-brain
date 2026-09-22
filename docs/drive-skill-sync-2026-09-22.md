# Drive skills: what was frozen and what still needs a decision

22 September 2026.

The skills in `Mega Claude Cowork/About Me/skills/` were duplicates of `skills/` in this repo. Comparing the two found 11 identical, 10 divergent, and 2 repo-only.

## Frozen, 14 skills

Their Drive `SKILL.md` is now a pointer to this repo. Originals archived at `Claude Outputs/Archive/Old-Instructions/skills-superseded-2026-09-22/`.

alex-hormozi-youtube, client-folder-setup, client-onboarding-complete, instagram, mmom-carousel, mmom-follow-up, mmom-onboarding, mmom-sales-strategist, mmom-visual, mmom-voice-profile-refresh, proposal, lead-magnet, linkedin-engagement, linkedin-post.

The last three were frozen only after merging Drive content the repo was missing:

- `lead-magnet` gained the Three-Tier Audience Rule, 23 lines. Write for die-hards, dry bias and drop-ins at once. Drop-ins first.
- `linkedin-engagement` gained the North Star v2 engagement allocation, 12 lines. The 30/30/30/10 split, plus owning your own comment section for 30 minutes.
- `linkedin-post` gained the carousel delivery spec, 10 lines. List posts always ship with a carousel, rendered to PNGs and a combined PDF, never left as a sidebar artifact.

## Not frozen, 0 skills remain

All 21 divergent skills are now resolved. `new-client` and `editor-briefing` were resolved on 22 September, see below; the last five (`mmom-podcast-pr`, `form-response-to-doc`, `weekly-action-plan`, `mmom-voice-check`, `newsletter`) were resolved later the same day, see "The last five, resolved 22 September" below.

## Repo-only, no Drive copy

`morning`, `onboarding-complete`. Nothing to do.

## new-client, resolved 22 September

All 15 repo-only lines turned out to be pre-edit originals of lines Drive had modified, so Drive was a clean superset. Taken wholesale, then retranslated from tiers to options. The repo gained three logging steps it never had: Airtable Editor Pipeline rows, the Production Tracker Sheet, and the Music Selection Tracker Sheet.

Tier to option translation, confirmed with Neil:

| Option | Children chapters | Wrap Up | Folders |
|---|---|---|---|
| A | none | no | 3 |
| B | 1, the buying child | yes | 5 |
| C | 1 shared, `Ch1. Us & [Old Man/Mum]` | yes | 5 |
| D | one per child | yes | 4 + one per child |

The old rule said "Bronze has no children chapters". That was wrong under the new ladder, because it covered both A and B, and B does interview the buying child. Option A is now the only option with no Wrap Up.

## editor-briefing, resolved 22 September

A true fork, not a stale copy. Both sides were actively edited after splitting around 24 August, and both independently reached a version numbered v1.5.

- Drive lineage, to v1.5 on 16 Sep: Step 3 propose chapter titles, `references/chapter-title-style-examples.md`, and the rule to log every selected track in the "family - selected tracks" tab.
- Repo lineage, to v1.6 on 18 Sep: Step 3a transcript reformat, Step 6 Gmail handoff, `references/editor-contacts.md`, hardened music lookup, Case B generalised to any parent session.

Repo taken as the base because it was newer and larger. The two Drive-only pieces were merged in as v1.7. The chapter-titles step became Step 3b, because the repo lineage creates the briefing doc at Step 2 rather than after the titles exist, so the titles now get written back into the placeholders rather than filled in at creation.

## The last five, resolved 22 September

- `mmom-voice-check` — Drive had a v1.1 banned-phrase addition ("stopped me in my tracks") and two checklist items (no em dashes, outreach length matching Neil's short templates) the repo lacked. Merged in, repo taken as base.
- `newsletter` — a real fork on the welcome-sequence paragraph. Repo's version proposed extending a single "'My Story'" email into a short Wave. Drive's version was a later, more accurate correction: the welcome sequence already exists as a 9-email "Drift" sequence with real performance data. Drive's correction replaced the repo's stale proposal.
- `form-response-to-doc` — repo was already a strict superset (parent-identification in doc titles, bold heading repeating which parent). Drive's lines were the pre-edit originals of content the repo had already improved. No merge needed.
- `mmom-podcast-pr` — same pattern: repo's Steps 1-4 are a full rewrite and expansion of Drive's shorter original. Every Drive-only line was superseded phrasing already covered, more thoroughly, on the repo side. No merge needed.
- `weekly-action-plan` (repo: `mmom-weekly-action-plan`) — Drive had forked at v1.4 with no unique content; the repo's v1.5 already contained everything Drive had. The real find was a bug: the repo copy had HTML entities (`&lt;`, `&gt;`, `&amp;`) littered through its code fences and headings, breaking the doc. Repaired and bumped to v1.6.

All five Drive originals archived to `Claude Outputs/Archive/Old-Instructions/skills-superseded-2026-09-22/`, Drive copies replaced with pointer stubs.

## Next

Nothing outstanding. All 23 divergent/duplicate skills identified on 22 September are now frozen or merged.
