# Snapshot recording workflow: sharpened prompt (v2, 2026-10-16)

Status: scratch. Ready for skill search once the OPEN items are answered.

## Inputs Neil supplies at briefing

1. Riverside recording link
2. Interviewee name (must match their sub-folder in 03 Clients)
3. Album artwork title card (Neil supplies, ask if missing, never invent)
4. Recording month and year (default: month of recording)
5. Any extra notes

Already in the interviewee's folder, not re-supplied: the photo of the year, and the intro/outro music track.

## Prompt

I have recorded a Snapshot interview. Using the Riverside link, work through Chrome (or MCP if available). Neil is on the Riverside Pro plan, so do the editing inside Riverside (editor, Magic Clips, Magic Audio, multitrack, media library). If a step genuinely cannot be done in Riverside, say which and stop before falling back to anything else.

Save everything into `03 Clients/[Interviewee name]/` in Drive (folder: https://drive.google.com/drive/folders/1Jk3Udf0ojnKAY3j-htCXF1qL9cYoeES5). Create the sub-folder if it does not exist. Anything written there is a new file, never an overwrite.

**Hard rule across every deliverable:** Neil's face and voice appear nowhere, at any moment. Check each deliverable against the speaker labels and report "checked, clean" or the exact timestamp of any bleed.

### 1. Transcript, and voice of customer
Download the Riverside transcript. Save as a Google Doc (built as HTML, per house rule) and as `.md`. Speaker labels kept, filler preserved, no rewriting.

Then feed it into the voice of customer (`knowledge/voice/VOC_Intelligence_System.md`). This is a different customer: a Snapshot interviewee, not a life-story client. Tag it as such. They embody the ICP's way of thinking: nostalgic, reflective, caught in the messy middle, aware life is moving fast, caring about family, connection and people. Pull verbatim phrases only, never paraphrase, never invent.

### 2. Magic clips (4 to 6, vertical 9:16)
Riverside already generates Magic Clips. First judge them: are they on point, do they stand alone, are they the strongest moments in the transcript? Report that judgement in two lines.
- If they are excellent: download them and make sure Neil's voice and video are not in them at all (interviewee-only layout, or cut to their track). If a clip cannot be made Neil-free, drop it and pick another.
- If they are weak: say so, and choose the clips from the transcript instead.
- Every clip gets a title card (the question, or the story they are responding to) and an end card. Both fade in and out, and the end card matches the title card.
- Name files `[Interviewee] - Clip 01 - [short slug].mp4`.

### 3. Photo-of-the-year clip (vertical 9:16)
Find the response where the interviewee describes what feelings their photo of the year brings up. This is one of the clips. Their photo (from their folder) is on screen the whole time, the voiceover fades in over 2 seconds, and they describe the photo and their feelings. That's it: photo plus voiceover. No face footage.

### 4. Full audio edit (~1 hour), start to finish, no involvement from Neil
Claude manages the whole process and delivers a finished, excellent file. Neil does not appear in any way, shape or form: track removed, not just muted.
- Follow the audio house style spec exactly: https://docs.google.com/document/d/14rxJZ3nJIZ7n7Ip_E3kB2wCbpUOeDAqy/edit
- Cut so each response starts clean (no breath-in, no clipped first word).
- Riverside Magic Audio (touch-up, 0 to 100% slider) set to 50%.
- Music: the single track in the interviewee's folder, used for both intro and outro, per the spec. Intro fades in over 2 seconds, plays about 15 to 25 seconds, crossfades to the voice. Outro fades in over 2 to 5 seconds very lightly under the final answer, never clashing, crescendo 2 to 3 seconds after their last words, 30 to 60 seconds or to the end of the track, slow fade to zero, 5 seconds of silence at the end.
- Stings from https://drive.google.com/drive/folders/1SXEJTkwVZkpNEjMUMDEIAh7OdlYeK3DJ between responses. Soft and gentle, 2 to 3 second fade in and out, never dropped in at level. Smooth, smooth, smooth.
- Export the final mp3 into the interviewee's folder.

### 5. Album artwork
Neil supplies the title card and the final audio file. Use the album-artwork skill and Neil's fonts as set there. Photo from the interviewee's folder, title, and "Recorded [Month Year]" as a subheading. One chapter, one track, album name "Snapshot", artist the interviewee. Built to grow: each new Snapshot client adds a track to the same album.

### 6. Final deliverable: transcript of the final audio edit
After the edit is done, produce a transcript of the final audio file itself (not the raw recording), as a Google Doc and `.md`, in the interviewee's folder. It should match what a listener hears, with no Neil lines.

## Deliverables checklist (what lands in the folder)

- Raw transcript (Google Doc and `.md`), plus VOC entry
- 4 to 6 vertical clips with title and end cards, including the photo-of-the-year clip
- Final audio edit (mp3)
- Album cover
- Transcript of the final audio edit (Google Doc and `.md`)

## Dropped for now

- Audio plus waveform clip (cut, revisit later)

## OPEN

1. Album artwork and audio: your brief says Neil supplies the title card and "the audio file". Does that mean the approved final mp3 from step 4 (so artwork follows approval), or a separate file?
2. Review gate: should Claude stop for a yes before the final export, or run start to finish with no stops and Neil reviews in Riverside afterwards? I have assumed no stops.
