# Handover: finish the Drive skill merge

Written 22 September 2026. Pick this up in a fresh session.

## The job

Five skills still exist as two diverging copies, one in this repo and one in the Drive Cowork folder. Merge each into the repo, then freeze the Drive copy as a pointer. Sixteen have already been done this way.

Drive path: `~/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/Mega Claude Cowork/About Me/skills/`

## The five left

All small. Largest gap is 14 lines.

| Skill | Drive-only lines | Repo-only lines |
|---|---|---|
| mmom-podcast-pr | 14 | 58 |
| form-response-to-doc | 14 | 28 |
| weekly-action-plan | 10 | 16 |
| mmom-voice-check | 5 | 1 |
| newsletter | 4 | 2 |

`weekly-action-plan` in Drive is `mmom-weekly-action-plan` in the repo. Same skill, different folder name.

## The method that worked

1. `diff "$D/<skill>/SKILL.md" skills/<skill>/SKILL.md` both directions. Count `^<` and `^>`.
2. Read the version comments at the top of both. They are the fastest way to see what each lineage gained and when.
3. If one side is a strict superset, copy it wholesale. If both sides have unique content, take the larger or newer as the base and hand-merge the other's unique blocks.
4. Check the `references/` folder on both sides. Files live there that the diff on SKILL.md will not show.
5. Update the version comment, the frontmatter description if the capability changed, and any overview-of-steps list inside the skill.
6. Archive the Drive original to `Claude Outputs/Archive/Old-Instructions/skills-superseded-2026-09-22/<skill>/`, then overwrite its SKILL.md with the pointer stub. Copy the stub wording from any already-frozen skill, e.g. `proposal`.
7. Update `docs/drive-skill-sync-2026-09-22.md`: remove the row, decrement the count, add a short resolved note.
8. Log anything learned in `knowledge/lessons.md`.
9. Commit.

## Three traps, all hit already

- **Modified time is meaningless.** Every repo skill reads 22 Sep because that is when it was copied in. It tells you nothing about which side is newer. Use the version comments.
- **Version numbers do not resolve forks.** `editor-briefing` reached v1.5 on both sides with different content. Read what changed, never trust the higher number.
- **Do not freeze on an assumption.** Three skills nearly lost real rules that existed only in Drive. Diff first, always.

## Watch for stale tier language

The offer moved from Bronze / Silver / Gold to the A to D ladder. Any skill still keying logic off metal names is wrong, not just out of date. `new-client` had this and was retranslated. Grep the remaining five for `bronze|silver|gold` before finishing. Current ladder is in `knowledge/offer/pricing.md`. A is the only option with no Wrap Up.

## Context on what already happened

`docs/drive-skill-sync-2026-09-22.md` has the full record, including the resolved notes for `new-client` and `editor-briefing`. Read it first.

Also done today, no action needed: `CLAUDE.md` rewritten, `AGENTS.md` added as a pointer, 34 lessons imported from Drive into `knowledge/lessons.md`, and the Drive `CLAUDE.md` and `Lessons/lessons.md` frozen as pointers.
