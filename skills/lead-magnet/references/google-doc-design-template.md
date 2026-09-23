# Google Doc Design Template — MMOM Lead Magnets

Confirmed working method, locked in 23 Sep 2026 against "How Do I Actually Bring This Up?" and matched to the live Conversation Playbook design. Use this every time a lead magnet ships as a Google Doc, not the old "plain text, no design" instruction in `SKILL.md` Step 2A — that instruction is superseded for this format.

## Design system (from the Conversation Playbook)

- Headings: **Marcellus**, colour `#A85639` (terracotta), `font-weight: normal` (Marcellus has no true bold, don't fake one)
- Body: **Merriweather**, `#2B2420`
- Script/quote blocks: `#3E362F`, left border `2px solid #1F7A85` (teal), `padding-left: 16pt`
- Italic asides / subtitle: `#5A5048`
- Section dividers: `<hr>` styled `border-top: 1px solid #D8CFC2`
- Links and CTA accents: teal `#1F7A85`
- H1 (cover title): 28pt. H2 (section): 16-18pt.

## How to produce it

1. Write the content as clean semantic HTML — `<h1>`, `<h2>`, `<p>`, `<ul><li>`, `<b>` for script labels — with the colours and fonts above set as **inline `style` attributes on every element** (a `<style>` block or external CSS will not survive the conversion, inline only).
2. Wrap script/quote paragraphs in the teal-left-border treatment shown above so they read as distinct from body copy.
3. Upload with `mcp__<drive-server>__create_file`:
   - `contentMimeType: "text/html"`
   - `textContent`: the full HTML
   - `parentId`: the destination Drive folder
   - Leave `disableConversionToGoogleType` unset/false so Drive converts it to a native Google Doc
4. This reliably preserves fonts, colours, bold/italic, links, and structure. It does **not** reliably preserve custom `max-width`/layout CSS — don't rely on those, they're cosmetic only and Docs ignores them anyway.
5. After creating, tell Neil to open and eyeball it once. `read_file_content` on a Drive doc returns a plain-text/markdown rendering regardless of the actual styling, so it cannot be used to verify fonts or colour — a human check in the browser is the only real verification available from this session.

## Reusable skeleton

```html
<html>
<head><meta charset="utf-8"></head>
<body style="font-family: 'Merriweather', serif; color:#2B2420;">

<h1 style="font-family:'Marcellus', serif; color:#A85639; font-size:28pt; font-weight:normal; margin-bottom:4pt;">[TITLE]</h1>

<p style="font-family:'Merriweather', serif; font-style:italic; color:#5A5048; font-size:12pt;">[SUBTITLE]</p>

<p style="font-family:'Merriweather', serif; font-size:11pt;">Neil Taylor<br>CEO &amp; Founder | Me &amp; My Old Man<br><a href="https://www.meandmyoldman.co.uk" style="color:#1F7A85;">www.meandmyoldman.co.uk</a></p>

<hr style="border:none; border-top:1px solid #D8CFC2;">

<h2 style="font-family:'Marcellus', serif; color:#A85639; font-size:18pt; font-weight:normal;">[SECTION HEADING]</h2>

<p style="font-family:'Merriweather', serif; font-size:11pt; line-height:1.5;">[BODY COPY]</p>

<ul style="font-family:'Merriweather', serif; font-size:11pt; line-height:1.6;">
<li>[LIST ITEM]</li>
</ul>

<p style="font-family:'Merriweather', serif; font-size:11pt; line-height:1.5; color:#3E362F; padding-left:16pt; border-left:2px solid #1F7A85;">"[SCRIPT / QUOTE TEXT]"</p>

</body>
</html>
```

Copy the full template out of `scratch/20260923_how-to-tell-your-parents_v1.md`'s companion HTML build (see the "How Do I Actually Bring This Up?" doc, 23 Sep 2026) for a complete worked example with all section types.
