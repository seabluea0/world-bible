#!/usr/bin/env python3
"""Generate image or story prompts from World Bible."""

import json
import argparse

WORLD_BIBLE_PATH = "/a0/usr/workdir/world-bible/world_bible.json"

def load_bible():
    with open(WORLD_BIBLE_PATH, "r") as f:
        return json.load(f)

def generate_image_prompt(bible, character_name=None, location_name=None, scene_description=""):
    """Generate an image prompt using the style bible and character/location data."""

    style = bible["style_bible"]
    template = bible["master_prompt_template"]["image_generation"]

    # Build style prefix
    style_parts = []
    if style["art_direction"]["primary_style"]:
        style_parts.append(style["art_direction"]["primary_style"])
    if style["lighting"]["primary_lighting"]:
        style_parts.append(style["lighting"]["primary_lighting"])
    if style["art_direction"]["mood"]:
        style_parts.append(style["art_direction"]["mood"])

    # Add style keywords
    style_parts.extend(style["visual_references"]["style_keywords"])

    prompt_parts = [", ".join(style_parts)]

    # Add character keywords
    if character_name:
        char = next((c for c in bible["characters"] if c["name"].lower() == character_name.lower()), None)
        if char:
            prompt_parts.append(", ".join(char["prompt_keywords"]))
            # Add physical description elements
            pd = char["physical_description"]
            if pd["appearance"]:
                prompt_parts.append(pd["appearance"])
            if pd["distinctive_features"]:
                prompt_parts.append(", ".join(pd["distinctive_features"]))

    # Add location keywords
    if location_name:
        loc = next((l for l in bible["locations"] if l["name"].lower() == location_name.lower()), None)
        if loc:
            prompt_parts.append(", ".join(loc["prompt_keywords"]))
            prompt_parts.append(loc["atmosphere"])
            if loc["lighting_notes"]:
                prompt_parts.append(loc["lighting_notes"])

    # Add scene description
    if scene_description:
        prompt_parts.append(scene_description)

    # Add quality tags
    if template["quality_tags"]:
        prompt_parts.append(template["quality_tags"])

    prompt = ", ".join([p for p in prompt_parts if p])

    return prompt

def generate_story_prompt(bible, character_name=None, location_name=None, plot_seed=""):
    """Generate a story prompt using the World Bible data."""

    template = bible["master_prompt_template"]["story_generation"]

    context_parts = []

    # Add character context
    if character_name:
        char = next((c for c in bible["characters"] if c["name"].lower() == character_name.lower()), None)
        if char:
            context_parts.append(f"Main character: {char['name']}")
            context_parts.append(f"Role: {char['role']}")
            context_parts.append(f"Personality: {', '.join(char['personality']['traits'])}")
            context_parts.append(f"Background: {char['background']}")

    # Add location context
    if location_name:
        loc = next((l for l in bible["locations"] if l["name"].lower() == location_name.lower()), None)
        if loc:
            context_parts.append(f"Setting: {loc['name']} ({loc['type']})")
            context_parts.append(f"Atmosphere: {loc['atmosphere']}")
            context_parts.append(f"Key features: {', '.join(loc['key_features'])}")

    # Add lore
    if bible["lore"]["history"]:
        context_parts.append(f"World context: {bible['lore']['history']}")

    # Build final prompt
    prompt = f"""{template['base_template']}

Context:
{chr(10).join(context_parts)}

Plot seed: {plot_seed}

Narrative voice: {template['narrative_voice']}
Pacing: {template['pacing_guidelines']}"""

    return prompt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate prompts from World Bible")
    parser.add_argument("--type", choices=["image", "story"], required=True, help="Prompt type")
    parser.add_argument("--character", help="Character name")
    parser.add_argument("--location", help="Location name")
    parser.add_argument("--scene", help="Scene description (for image) or plot seed (for story)")

    args = parser.parse_args()
    bible = load_bible()

    if args.type == "image":
        prompt = generate_image_prompt(bible, args.character, args.location, args.scene)
        print("
🎨 Generated Image Prompt:")
        print("-" * 50)
        print(prompt)
    else:
        prompt = generate_story_prompt(bible, args.character, args.location, args.scene)
        print("
📖 Generated Story Prompt:")
        print("-" * 50)
        print(prompt)
