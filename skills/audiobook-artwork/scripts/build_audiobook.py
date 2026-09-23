#!/usr/bin/env python3
"""
Import a folder of chapter MP3s into Music.app with per-chapter metadata
and artwork, driven by the "ChNN [name]" naming convention.

Usage:
    python3 build_audiobook.py \
        --folder "/path/to/audiobook folder" \
        --client "Judy Dickson" \
        [--album "Judy Dickson's Life Story"] \
        [--year 2026] \
        [--dry-run]

Folder expectations:
    - MP3s named "ChNN [chapter name].mp3", e.g. "Ch01 Steph & Mum.mp3"
    - One image per chapter starting with the SAME "ChNN" number, e.g.
      "Ch01 [anything].jpg" (.jpg/.jpeg/.png, case-insensitive) — the
      rest of the filename doesn't need to match the mp3 exactly, only
      the chapter number does
    - Chapter number (NN) drives track order, track count and pairing

The script does not touch Music.app in --dry-run mode — it only reports
the pairing it found, so you can check the match-up before committing.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

CHAPTER_RE = re.compile(r"^Ch\s*0*(\d+)\b", re.IGNORECASE)
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}

SCRIPT_DIR = Path(__file__).resolve().parent
APPLESCRIPT_PATH = SCRIPT_DIR / "import_track.applescript"


def _chapter_num(path: Path):
    match = CHAPTER_RE.match(path.stem)
    return int(match.group(1)) if match else None


def find_chapters(folder: Path):
    mp3s = sorted(folder.glob("*.mp3"))
    if not mp3s:
        sys.exit(f"No .mp3 files found in {folder}")

    images = [p for p in folder.iterdir() if p.suffix.lower() in IMAGE_EXTS]

    # Pair by chapter number, not exact filename — the chapter name in the
    # image filename doesn't always match the mp3 exactly (e.g. "Geoff" vs
    # "Geoffrey"), so matching on the leading "ChNN" is more reliable.
    images_by_num = {}
    problems = []
    for img in images:
        num = _chapter_num(img)
        if num is None:
            problems.append(f"Image skipped (no 'ChNN' prefix): {img.name}")
            continue
        if num in images_by_num:
            problems.append(
                f"Two images match Ch{num}: {images_by_num[num].name} and {img.name} — keeping the first, fix the folder"
            )
            continue
        images_by_num[num] = img

    chapters = []
    for mp3 in mp3s:
        num = _chapter_num(mp3)
        if num is None:
            problems.append(f"Skipped (no 'ChNN' prefix): {mp3.name}")
            continue

        image = images_by_num.get(num)
        if image is None:
            problems.append(f"No matching image for Ch{num}: {mp3.name}")
            continue

        chapters.append({
            "num": num,
            "title": mp3.stem,
            "mp3": mp3,
            "image": image,
        })

    chapters.sort(key=lambda c: c["num"])
    return chapters, problems


def run_track(chapter, artist, album, genre, year, track_count):
    args = [
        "osascript",
        str(APPLESCRIPT_PATH),
        str(chapter["mp3"]),
        str(chapter["image"]),
        chapter["title"],
        artist,
        album,
        genre,
        str(year),
        str(chapter["num"]),
        str(track_count),
    ]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0 or "OK" not in result.stdout:
        raise RuntimeError(
            f"AppleScript failed for {chapter['mp3'].name}:\n{result.stderr.strip()}"
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--folder", required=True, help="Folder containing the chapter MP3s and images")
    parser.add_argument("--client", required=True, help="Client's full name, used as the Artist tag")
    parser.add_argument("--album", help="Album title. Defaults to \"[Client]'s Life Story\"")
    parser.add_argument("--genre", default="Audiobook", help="Genre tag (default: Audiobook)")
    parser.add_argument("--year", type=int, help="Year tag. Defaults to the current year")
    parser.add_argument("--dry-run", action="store_true", help="Only report the chapter/image pairing, don't touch Music.app")
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        sys.exit(f"Not a folder: {folder}")

    album = args.album or f"{args.client}'s Life Story"
    year = args.year or __import__("datetime").date.today().year

    chapters, problems = find_chapters(folder)

    print(f"Folder: {folder}")
    print(f"Artist: {args.client}")
    print(f"Album:  {album}")
    print(f"Genre:  {args.genre}")
    print(f"Year:   {year}")
    print(f"Chapters found: {len(chapters)}")
    print()

    for c in chapters:
        print(f"  Ch{c['num']:02d}  {c['mp3'].name}  <->  {c['image'].name}")

    if problems:
        print("\nProblems (these files will be skipped):")
        for p in problems:
            print(f"  - {p}")

    if not chapters:
        sys.exit("\nNothing to import — fix the pairing above and re-run.")

    if args.dry_run:
        print("\nDry run only — nothing was sent to Music.app.")
        return

    if problems:
        answer = input("\nSome files have problems and will be skipped. Continue? [y/N] ")
        if answer.strip().lower() != "y":
            sys.exit("Aborted.")

    track_count = len(chapters)
    print(f"\nImporting {track_count} chapters into Music.app...")
    for c in chapters:
        print(f"  Importing Ch{c['num']:02d} - {c['title']}...", end=" ", flush=True)
        run_track(c, args.client, album, args.genre, year, track_count)
        print("done.")

    print("\nAll chapters imported with metadata and artwork.")
    print("Next: check them in Music.app, then continue with the export/zip steps.")


if __name__ == "__main__":
    main()
