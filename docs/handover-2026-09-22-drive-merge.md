# Handover: finish the Drive merge and the tier cleanup

Written 22 September 2026. Pick up in a fresh session. Do the tasks in order.

Drive path, used throughout. Export it first:

```
D=~/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/"My Drive"/"Mega Claude Cowork"/"About Me"/skills
A=~/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/"My Drive"/"Mega Claude Cowork"/"Claude Outputs"/Archive/Old-Instructions/skills-superseded-2026-09-22
```

## Background in three lines

Every skill existed twice, once here and once in Drive, and both copies were being edited. Sixteen have been merged into this repo and their Drive copies frozen as pointers. Five are left. Separately, the offer moved from Bronze/Silver/Gold to options A to D, and skills that still key logic off the metal names produce confidently wrong output.

## Task 1: merge the last five skills

| Skill | Drive-only lines | Repo-only lines |
|---|---|---|
| mmom-podcast-pr | 14 | 58 |
| form-response-to-doc | 14 | 28 |
| weekly-action-plan | 10 | 16 |
| mmom-voice-check | 5 | 1 |
| newsletter | 4 | 2 |

`weekly-action-plan` in Drive is `mmom-weekly-action-plan` here. Same skill, different folder name.

For each one:

1. `diff "$D/<skill>/SKILL.md" skills/<skill>/SKILL.md`. Look at both directions, `^<` is Drive-only and `^>` is repo-only.
2. Read the `<!-- v1.x -->` comments at the top of both files. Fastest way to see what each side gained and when.
3. `ls "$D/<skill>/references/"` and compare with `skills/<skill>/references/`. Files live there that a diff on SKILL.md will not show. Copy anything missing.
4. Merge. If one side is a strict superset, copy it wholesale. If both have unique blocks, take the larger or newer as the base and hand-merge the other's unique blocks in. Check the merged step order still makes sense, do not just paste a block at its old line number.
5. Update the version comment, the frontmatter `description` if the capability changed, and any "Overview of steps" list inside the skill.
6. Freeze the Drive copy: `cp -R "$D/<skill>" "$A/<skill>"`, then overwrite `"$D/<skill>/SKILL.md"` with a pointer stub. Copy the stub wording from `"$D/proposal/SKILL.md"`.
7. Update `docs/drive-skill-sync-2026-09-22.md`: delete the row, decrement the count in the heading, add a one-paragraph resolved note.
8. Commit.

Do not use `rm -rf` on the Drive folders. It gets blocked. Archive with `cp -R`, then overwrite the SKILL.md in place.

## Task 2: grep each merged skill for stale tiers

Before finishing each skill above, run:

```bash
grep -niE "bronze|silver|gold" skills/<skill>/SKILL.md
```

Hits on the banned word "gold" in a voice checklist are fine, leave them. Hits on tier names driving logic or prices are bugs. Current ladder is in `knowledge/offer/pricing.md`. Option A is the only one with no Wrap Up. Families never see A to D, they see Hero Story (A and B), Family Documentary (C), Full Chorus (D).

## Task 3: ask Neil about the proposal slide architecture

**The biggest open item in the repo.** Do not start this without asking him.

`skills/proposal/SKILL.md` had the old V8 prices stripped out on 22 Sep and now points at `pricing.md`, so the numbers are safe. The structure is not. The whole deck still assumes three tiers:

- the Gold → Bronze → Silver slide order and its price-anchoring logic
- a full value-stack table per tier
- the bonus structure per tier
- "Silver is always the default" and the "Silver seeds" rule
- the Silver+ 2P scenario

There are now four options, not three. Mapping three slides onto four options is a commercial decision about how Neil wants to anchor, not a find-and-replace. There is a flagged block in the file saying so. Ask him how he wants the comparison slides to work, then rewrite.

## Three traps, all hit already

- **Modified time is meaningless.** Every repo skill reads 22 Sep because that is when it was copied in. Use the version comments, not timestamps.
- **Version numbers do not resolve forks.** `editor-briefing` reached v1.5 on both sides with different content. Read what changed.
- **Never freeze on an assumption.** Three skills nearly lost rules that existed only in Drive. Diff first, every time.

## Smaller outstanding items

- **Eight commits unpushed.** Working tree clean. Push permission is already in `.claude/settings.json`. Ask Neil first.
- **The two Drive voice files are unprotected.** `About Me/VOICE_PROFILE_Neil_Taylor.md` and `VOC_Intelligence_System.md` are currently byte-identical to the repo copies, but nothing stops them drifting. Worth freezing the same way as the skills. Neil has not decided.
- **The claude.ai web app runs its own skill copies.** Claude Code reads this repo by symlink so it is current. The web app is not, and will keep running pre-merge versions until Neil re-uploads by hand. That is a third lineage and it is how this fork started. Only he can fix it, in the browser.
- **Drive SOPs outside `About Me/` still use tier language.** The Onboarding folder has Bronze/Silver/Gold SOPs. Not touched. Noted in `knowledge/systems-map.md`.

## Read these first

- `docs/drive-skill-sync-2026-09-22.md` — full record, including the resolved notes for `new-client` and `editor-briefing`.
- `knowledge/lessons.md` — five lessons were logged on 22 Sep from this work.

Done already, no action needed: `CLAUDE.md` rewritten, `AGENTS.md` added as a pointer, 34 lessons imported from Drive, Drive `CLAUDE.md` and `Lessons/lessons.md` frozen as pointers, `new-client` retranslated to A to D, `editor-briefing` fork merged, tier sweep run across all skills.
