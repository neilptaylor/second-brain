import subprocess, os
from PIL import Image, ImageDraw, ImageFont

ROOT = "/Users/neiltayloradmin/my second brain"
SRC = f"{ROOT}/scratch/mmom-reels-source"
OUT = f"{ROOT}/scratch/mmom-reels-output"
os.makedirs(OUT, exist_ok=True)

FONT = "/System/Library/Fonts/Supplemental/Georgia.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
ACCENT = (191, 87, 0)  # craft accent, matches earlier cut
CANVAS_W, CANVAS_H = 1080, 1920

CLIPS = {
    "nobody-stopped-loving": {
        "raw": f"{SRC}/nobody-stopped-loving_raw.mp4",
        "captions": [
            (1.0, 7.5, ["Nobody's fallen out.", "Nobody's stopped loving anyone."]),
            (47.0, 53.5, ["It just recentred us", "as a family."]),
            (96.0, 102.5, ["Nobody stopped loving one another.", "Life just got in the way."]),
        ],
        "end_cta": ["Full episode linked in comments", "meandmyoldman.co.uk"],
    },
    "scared-of": {
        "raw": f"{SRC}/scared-of_raw.mp4",
        "captions": [
            (2.5, 7.5, ["What are you scared of?"]),
            (9.2, 13.5, ["And what's the alternative?"]),
            (19.5, 25.5, ["I'd rather have", "the awkward ten minutes."]),
        ],
        "end_cta": ["Follow for more", "meandmyoldman.co.uk"],
    },
    "someday-dangerous": {
        "raw": f"{SRC}/someday-dangerous_raw.mp4",
        "captions": [
            (1.0, 6.5, ["Someday is one of the most", "dangerous words in a family."]),
            (27.5, 33.5, ["Memory preserves events.", "Story preserves meaning."]),
        ],
        "end_cta": ["Comment “STORIES” for the free", "107-question guide", "meandmyoldman.co.uk/liveinspired"],
    },
}


def render_caption_png(lines, path, fontsize=54):
    font = ImageFont.truetype(FONT_BOLD, fontsize)
    pad_x, line_gap = 60, 18
    dummy = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(dummy)
    sizes = [d.textbbox((0, 0), l, font=font) for l in lines]
    w = max(b[2] - b[0] for b in sizes) + pad_x * 2
    line_h = max(b[3] - b[1] for b in sizes)
    h = int(len(lines) * (line_h + line_gap) + line_gap)
    img = Image.new("RGBA", (CANVAS_W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = line_gap
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (CANVAS_W - tw) / 2
        # soft shadow for legibility over video, no boxed panel
        for ox, oy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, 3)]:
            d.text((x + ox, y + oy), line, font=font, fill=(0, 0, 0, 160))
        d.text((x, y), line, font=font, fill=(255, 255, 255, 255))
        y += line_h + line_gap
    img.save(path)
    return h


def render_endcard_png(lines, path):
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), (246, 239, 225))
    d = ImageDraw.Draw(img)
    word_font = ImageFont.truetype(FONT_BOLD, 68)
    body_font = ImageFont.truetype(FONT, 42)
    wm = "Me & My Old Man"
    bbox = d.textbbox((0, 0), wm, font=word_font)
    d.text(((CANVAS_W - (bbox[2] - bbox[0])) / 2, CANVAS_H / 2 - 130), wm, font=word_font, fill=ACCENT)
    y = CANVAS_H / 2 - 10
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=body_font)
        tw = bbox[2] - bbox[0]
        d.text(((CANVAS_W - tw) / 2, y), line, font=body_font, fill=(45, 45, 45))
        y += 58
    img.save(path)


def build(name, cfg):
    raw = cfg["raw"]
    work = f"{OUT}/{name}"
    os.makedirs(work, exist_ok=True)
    body_mp4 = f"{work}/body.mp4"
    end_mp4 = f"{work}/end.mp4"
    final_mp4 = f"{OUT}/{name}_final.mp4"

    overlay_inputs = []
    overlay_chain_parts = []
    filter_complex = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,gblur=sigma=25,eq=brightness=-0.08[bg];"
        "[0:v]scale=1080:-2[fg];"
        "[bg][fg]overlay=(W-w)/2:(H-h)/2[base]"
    )
    prev = "[base]"
    for i, (start, end, lines) in enumerate(cfg["captions"]):
        png = f"{work}/cap-{i}.png"
        h = render_caption_png(lines, png)
        y = int(CANVAS_H * 0.72 - h / 2)
        overlay_inputs += ["-i", png]
        label = f"[c{i}]"
        nxt = f"[v{i}]" if i < len(cfg["captions"]) - 1 else "[v]"
        filter_complex += (
            f";{prev}[{i+1}:v]overlay=x=(W-w)/2:y={y}:"
            f"enable='between(t,{start},{end})'{nxt}"
        )
        prev = nxt

    subprocess.run([
        "ffmpeg", "-y", "-i", raw, *overlay_inputs,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "0:a",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "24",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
        body_mp4,
    ], check=True)

    end_png = f"{work}/end.png"
    render_endcard_png(cfg["end_cta"], end_png)
    subprocess.run([
        "ffmpeg", "-y",
        "-loop", "1", "-i", end_png,
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
        "-t", "2.5",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "24", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-shortest",
        end_mp4,
    ], check=True)

    concat_list = f"{work}/concat.txt"
    with open(concat_list, "w") as f:
        f.write(f"file '{body_mp4}'\nfile '{end_mp4}'\n")

    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "27",
        "-vf", "scale=1080:1920", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
        final_mp4,
    ], check=True)

    size_mb = os.path.getsize(final_mp4) / 1e6
    print(f"{name}: {final_mp4} ({size_mb:.1f} MB)")


for name, cfg in CLIPS.items():
    build(name, cfg)
