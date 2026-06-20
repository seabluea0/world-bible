#!/usr/bin/env python3
"""Add a new character to the World Bible."""

import json
import argparse
from datetime import datetime
import uuid

WORLD_BIBLE_PATH = "/a0/usr/workdir/world-bible/world_bible.json"

def load_bible():
    with open(WORLD_BIBLE_PATH, "r") as f:
        return json.load(f)

def save_bible(bible):
    bible["meta"]["last_updated"] = datetime.now().isoformat()
    with open(WORLD_BIBLE_PATH, "w") as f:
        json.dump(bible, f, indent=2)

def add_character(args):
    bible = load_bible()

    char_id = f"char_{args.name.lower().replace(' ', '_')}_{uuid.uuid4().hex[:8]}"

    new_char = {
        "id": char_id,
        "name": args.name,
        "aliases": args.aliases.split(",") if args.aliases else [],
        "role": args.role or "supporting",
        "physical_description": {
            "appearance": args.appearance or "",
            "distinctive_features": args.features.split(",") if args.features else [],
            "clothing_style": args.clothing or "",
            "age": args.age or "",
            "height": args.height or "",
            "build": args.build or ""
        },
        "personality": {
            "traits": args.traits.split(",") if args.traits else [],
            "motivations": args.motivations or "",
            "fears": args.fears or "",
            "quirks": args.quirks.split(",") if args.quirks else []
        },
        "background": args.background or "",
        "relationships": [],
        "reference_images": [],
        "prompt_keywords": args.keywords.split(",") if args.keywords else [],
        "notes": args.notes or ""
    }

    bible["characters"].append(new_char)
    save_bible(bible)

    print(f"✅ Character '{args.name}' added successfully!")
    print(f"   ID: {char_id}")
    return char_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a character to World Bible")
    parser.add_argument("--name", required=True, help="Character name")
    parser.add_argument("--role", choices=["protagonist", "antagonist", "supporting", "background"], help="Character role")
    parser.add_argument("--aliases", help="Comma-separated aliases")
    parser.add_argument("--appearance", help="Physical appearance description")
    parser.add_argument("--features", help="Comma-separated distinctive features")
    parser.add_argument("--clothing", help="Clothing style")
    parser.add_argument("--age", help="Character age")
    parser.add_argument("--height", help="Character height")
    parser.add_argument("--build", help="Character build")
    parser.add_argument("--traits", help="Comma-separated personality traits")
    parser.add_argument("--motivations", help="Character motivations")
    parser.add_argument("--fears", help="Character fears")
    parser.add_argument("--quirks", help="Comma-separated quirks")
    parser.add_argument("--background", help="Background story")
    parser.add_argument("--keywords", help="Comma-separated prompt keywords")
    parser.add_argument("--notes", help="Additional notes")

    args = parser.parse_args()
    add_character(args)
