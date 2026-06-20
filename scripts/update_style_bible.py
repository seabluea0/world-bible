#!/usr/bin/env python3
"""Update the Style Bible section of World Bible."""

import json
import argparse
from datetime import datetime

WORLD_BIBLE_PATH = "/a0/usr/workdir/world-bible/world_bible.json"

def load_bible():
    with open(WORLD_BIBLE_PATH, "r") as f:
        return json.load(f)

def save_bible(bible):
    bible["meta"]["last_updated"] = datetime.now().isoformat()
    with open(WORLD_BIBLE_PATH, "w") as f:
        json.dump(bible, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update Style Bible")
    parser.add_argument("--primary-style", help="Primary art style")
    parser.add_argument("--mood", help="Overall mood")
    parser.add_argument("--themes", help="Comma-separated themes")
    parser.add_argument("--lighting", help="Primary lighting style")
    parser.add_argument("--atmosphere", help="Atmosphere description")
    parser.add_argument("--primary-colors", help="Comma-separated primary colors")
    parser.add_argument("--secondary-colors", help="Comma-separated secondary colors")
    parser.add_argument("--accent-colors", help="Comma-separated accent colors")
    parser.add_argument("--style-keywords", help="Comma-separated style keywords for prompts")
    parser.add_argument("--negative-keywords", help="Comma-separated negative keywords")

    args = parser.parse_args()
    bible = load_bible()

    if args.primary_style:
        bible["style_bible"]["art_direction"]["primary_style"] = args.primary_style
    if args.mood:
        bible["style_bible"]["art_direction"]["mood"] = args.mood
    if args.themes:
        bible["style_bible"]["art_direction"]["themes"] = [t.strip() for t in args.themes.split(",")]
    if args.lighting:
        bible["style_bible"]["lighting"]["primary_lighting"] = args.lighting
    if args.atmosphere:
        bible["style_bible"]["lighting"]["atmosphere"] = args.atmosphere
    if args.primary_colors:
        bible["style_bible"]["color_palette"]["primary_colors"] = [c.strip() for c in args.primary_colors.split(",")]
    if args.secondary_colors:
        bible["style_bible"]["color_palette"]["secondary_colors"] = [c.strip() for c in args.secondary_colors.split(",")]
    if args.accent_colors:
        bible["style_bible"]["color_palette"]["accent_colors"] = [c.strip() for c in args.accent_colors.split(",")]
    if args.style_keywords:
        bible["style_bible"]["visual_references"]["style_keywords"] = [k.strip() for k in args.style_keywords.split(",")]
    if args.negative_keywords:
        bible["style_bible"]["visual_references"]["negative_keywords"] = [k.strip() for k in args.negative_keywords.split(",")]

    save_bible(bible)
    print("✅ Style Bible updated successfully!")
