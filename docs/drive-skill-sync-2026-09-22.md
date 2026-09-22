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

## Not frozen, 5 skills, diverged both ways

Each of these has content in Drive the repo lacks AND content in the repo that Drive lacks. They need a human call, not a merge script.

`new-client` and `editor-briefing` were resolved on 22 September, see below. Five remain.

| Skill | Drive-only lines | Repo-only lines | Note |
|---|---|---|---|
| mmom-podcast-pr | 14 | 58 | Repo mostly ahead. |
| form-response-to-doc | 14 | 28 | Repo mostly ahead. |
| weekly-action-plan | 10 | 16 | Named `mmom-weekly-action-plan` in the repo. |
| mmom-voice-check | 5 | 1 | Small. |
| newsletter | 4 | 2 | Small. |

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

## Next

Five remain, all small: mmom-podcast-pr, form-response-to-doc, weekly-action-plan, mmom-voice-check, newsletter. Largest gap is 14 Drive-only lines.
