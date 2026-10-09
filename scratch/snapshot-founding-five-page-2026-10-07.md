# Snapshot: Founding Five page, copy deck v1 (7 Oct 2026)

A copy of `/snapshot` on an unlisted URL: `/snapshot-f5k`. Hero, VSL, the "What you get" list, the talk list, what it isn't and who I am all stay. Two things change: a new block straight under the VSL, and the waitlist form becomes a "confirm your place" form. Nothing links to it. Only the people you send it to will see it.

Terms are from `knowledge/offer/pricing.md` (Founding five, set 2 Oct): £99 with video included, a 30-minute feedback call, the form and the session done within two weeks of saying yes, and the offer closes Friday 16 October.

---

## UNDER THE VSL (replaces the waitlist form)

**Eyebrow:** The Founding Five

**H2:** Five places. £99. Video included.

**What it is**
An hour and a half with me, online, about your life as it is right now. Within 7 days you get it back as the story of your year: about an hour, fully produced, in audio and video.

**What you get**
- A short reflection form before we start, about 30 minutes, so you arrive with more than "erm, work's been busy"
- An hour and a half recorded together, online, from wherever you can get some quiet
- About an hour of finished audio, plus the video, within 7 days

**About the video**
It's just you, talking to camera. I'm there asking the questions, but I'm cut out, so it's you telling your story. Before we start, I'll brief you on how to make that easy: where to sit, the light, how to forget the camera is there.

**What I ask back**
You're the first five, so you're helping me build this. After you've listened, we have a 30-minute call. You record a two-minute video about what it was like, and then you tell me honestly what worked and what was clunky.

**What happens next**
1. You confirm below.
2. I send you a payment link.
3. You pay, and I send the reflection form and a link to book your session.
4. We record within two weeks. Your Snapshot lands within 7 days of that.

**Form:** [ First name ] [ Email ] [ **Confirm my place** ]

Small print under the button: Five places. Closes Friday 16 October, or sooner if they go.

**After they submit:** Thanks, [first name]. Your payment link is on its way from me.

---

## FIXES TO THE REST OF THE PAGE (this version only)

- "What you get", row 3: "One week later" becomes **"Within 7 days"**. pricing.md says never "a week".
- "What you get", row 4: drop "A handful of short video clips" and put **"To keep: the video. Just you, talking to camera. Yours to watch back, to share with your partner, for your kids one day."** The handful of clips is no longer promised.
- Closing dark section: replace the second waitlist form with the same "Confirm my place" form. Remove the "full video documentaries in 2027" tick box from this page.

The live `/snapshot` page has the same "one week" and "handful of clips" wording. Worth fixing there too.

---

## LOVABLE BRIEF (paste once you've signed off the copy)

> Create a new route `/snapshot-f5k`, a copy of `/snapshot` with the same design system. Set it `noindex` and leave it out of the sitemap and nav. Changes:
> 1. Under the VSL, replace the waitlist form with a Founding Five block: eyebrow, H2, three short sections ("What it is", "What you get", "What I ask back") and a numbered four-step "What happens next" list, using the copy in this deck.
> 2. The form takes first name and email only. Button: "Confirm my place". No video tick box. On submit, add the subscriber in Kit and tag them `snapshot-founding-five`, not `snapshot-waitlist`. Success message: "Thanks, {firstName}. Your payment link is on its way from me."
> 3. Apply the "What you get" fixes above.
> 4. Use the same Confirm form in the closing dark section.

Before it ships, the Kit tag `snapshot-founding-five` needs to exist. The server function looks tags up by name and throws an error if it can't find one.

---

## Alternative H2s (under the VSL)

1. You're one of five. Here's how it works.
2. The first five Snapshots. £99, and I'll ask for your honest feedback.
