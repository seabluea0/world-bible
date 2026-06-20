#!/usr/bin/env python3
"""List contents of World Bible."""

import json
import argparse

WORLD_BIBLE_PATH = "/a0/usr/workdir/world-bible/world_bible.json"

def load_bible():
    with open(WORLD_BIBLE_PATH, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List World Bible contents")
    parser.add_argument("--section", choices=["characters", "locations", "style", "lore", "all"], default="all", help="Section to list")

    args = parser.parse_args()
    bible = load_bible()

    if args.section in ["all", "style"]:
        print("
🎨 STYLE BIBLE")
        print("=" * 50)
        style = bible["style_bible"]
        print(f"Primary Style: {style['art_direction']['primary_style'] or 'Not set'}")
        print(f"Mood: {style['art_direction']['mood'] or 'Not set'}")
        print(f"Themes: {', '.join(style['art_direction']['themes']) or 'Not set'}")
        print(f"Lighting: {style['lighting']['primary_lighting'] or 'Not set'}")
        print(f"Primary Colors: {', '.join(style['color_palette']['primary_colors']) or 'Not set'}")
        print(f"Style Keywords: {', '.join(style['visual_references']['style_keywords']) or 'Not set'}")

    if args.section in ["all", "characters"]:
        print("
👥 CHARACTERS")
        print("=" * 50)
        for char in bible["characters"]:
            print(f"
  📌 {char['name']} ({char['role']})")
            print(f"     ID: {char['id']}")
            if char['physical_description']['appearance']:
                print(f"     Appearance: {char['physical_description']['appearance']}")
            if char['prompt_keywords']:
                print(f"     Keywords: {', '.join(char['prompt_keywords'])}")

    if args.section in ["all", "locations"]:
        print("
🗺️ LOCATIONS")
        print("=" * 50)
        for loc in bible["locations"]:
            print(f"
  📍 {loc['name']} ({loc['type']})")
            print(f"     ID: {loc['id']}")
            if loc['description']:
                print(f"     Description: {loc['description'][:100]}...")
            if loc['prompt_keywords']:
                print(f"     Keywords: {', '.join(loc['prompt_keywords'])}")

    if args.section in ["all", "lore"]:
        print("
📚 LORE")
        print("=" * 50)
        lore = bible["lore"]
        if lore['history']:
            print(f"History: {lore['history'][:200]}...")
        if lore['rules']:
            print(f"Rules: {', '.join(lore['rules'])}")

    print("
")
