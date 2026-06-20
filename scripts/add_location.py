#!/usr/bin/env python3
"""Add a new location to the World Bible."""

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

def add_location(args):
    bible = load_bible()

    loc_id = f"loc_{args.name.lower().replace(' ', '_')}_{uuid.uuid4().hex[:8]}"

    new_loc = {
        "id": loc_id,
        "name": args.name,
        "type": args.type or "region",
        "description": args.description or "",
        "atmosphere": args.atmosphere or "",
        "key_features": args.features.split(",") if args.features else [],
        "lighting_notes": args.lighting or "",
        "color_notes": args.colors or "",
        "reference_images": [],
        "prompt_keywords": args.keywords.split(",") if args.keywords else [],
        "connected_locations": args.connected.split(",") if args.connected else [],
        "notes": args.notes or ""
    }

    bible["locations"].append(new_loc)
    save_bible(bible)

    print(f"✅ Location '{args.name}' added successfully!")
    print(f"   ID: {loc_id}")
    return loc_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a location to World Bible")
    parser.add_argument("--name", required=True, help="Location name")
    parser.add_argument("--type", choices=["city", "building", "region", "interior", "exterior", "nature"], help="Location type")
    parser.add_argument("--description", help="Detailed description")
    parser.add_argument("--atmosphere", help="Mood and atmosphere")
    parser.add_argument("--features", help="Comma-separated key features")
    parser.add_argument("--lighting", help="Lighting notes")
    parser.add_argument("--colors", help="Color palette notes")
    parser.add_argument("--keywords", help="Comma-separated prompt keywords")
    parser.add_argument("--connected", help="Comma-separated connected location IDs")
    parser.add_argument("--notes", help="Additional notes")

    args = parser.parse_args()
    add_location(args)
