# Handover: push the Drift sequence fixes into Kit

Written 28 Sep 2026. First job next session. Neil has approved every change, including the two flagged lines, so do the push without asking again.

## What

Apply the approved before/after edits to the live Kit sequence **The Drift | Feb-26** (sequence id `2666400`, 10 emails, Tuesdays).

- Approved changes doc: https://docs.google.com/document/d/1--aeEkfQWDTeF_oOv253-YqnONAipWhVXoOR0nvBfD0
- Local copy of the same pairs: `scratch/drift_after.py` (dict `A`, keys 1 to 63, After text) and `scratch/drift_fixes.html` (Before and After).

## The three fixes

1. **Em dashes.** 63 lines, each with an agreed rewrite (not a straight swap). Use the "After" text exactly.
2. **"Audiobook" becomes "audio documentary"** in email 4 (id `10156887`). Line 30 is a client quote; Neil approved the swap.
3. **Email 5 (id `9555967`), "Someone has to go first".** The button changes from the 30min Calendly link to `https://calendly.com/meandmyoldman/20min-family-story-discovery-session`, and "no pitch, no pressure," is cut (line 37, approved).

Also line 55, email 9 (id `10156888`): fix the typo "working with for 9 months" to "working together for 9 months".

## Email ids (position: id)

0: 9542705 · 1: 9542709 · 2: 10156882 · 3: 10156887 · 4: 9555967 · 5: 9708323 · 6: 9708448 · 7: 9763146 · 8: 10156888 · 9: 10156902

## How

For each email:

1. `get_sequence_email` (sequence_id 2666400, id, include `content_tree`).
2. Find each "Before" sentence in the text leaves and replace it with the "After" text. Sentences can be split across leaves or links, so match within one paragraph block and rebuild only that block. Send every other block back unchanged.
3. `update_sequence_email` with the edited `content_tree` and `published: true`.
4. If Kit rejects the update with a content-loss conflict, do not set `allow_content_loss`. Stop and tell Neil which email.

Afterwards, grep every email's content for "—" and "audiobook" and confirm zero hits. Then tell Neil in one line, with the Kit link https://app.kit.com/sequences/2666400.

## Related, still open

- The North Star doc lists the other open actions: https://docs.google.com/document/d/1q-lm4Am46jFmsyqfpz3tRemEDWD9lnjIT09wguIdBOA
- Lapsed Drip 1 (id `2908750`): the timezone field showed blank in Neil's screenshot. Check that it's Europe/London.
