# World Bible Skill

## Overview
A comprehensive world-building management system for maintaining story consistency and image generation consistency across your WordPress blog. This skill manages characters, locations, style bible, reference images, and master prompt templates.

## File Locations
- **Main World Bible**: `/a0/usr/workdir/world-bible/world_bible.json`
- **Character Templates**: `/a0/usr/workdir/world-bible/templates/character_template.json`
- **Location Templates**: `/a0/usr/workdir/world-bible/templates/location_template.json`
- **Character Storage**: `/a0/usr/workdir/world-bible/characters/`
- **Location Storage**: `/a0/usr/workdir/world-bible/locations/`
- **Assets Storage**: `/a0/usr/workdir/world-bible/assets/`

## Usage

### Adding a New Character
Use the `add_character.py` script:
```bash
python /a0/usr/workdir/world-bible/scripts/add_character.py --name "Character Name" --role "protagonist" --description "Physical description"
```

Or manually edit the JSON file following the character template structure.

### Adding a New Location
Use the `add_location.py` script:
```bash
python /a0/usr/workdir/world-bible/scripts/add_location.py --name "Location Name" --type "city" --description "Description"
```

### Updating Style Bible
Edit the `style_bible` section in `world_bible.json` to define:
- Art direction (primary style, influences, mood, themes)
- Lighting preferences (time of day, shadow style, atmosphere)
- Color palette (primary, secondary, accent colors)
- Visual references (reference images, style keywords)

### Generating Image Prompts
Use the master prompt template to generate consistent image prompts:
```bash
python /a0/usr/workdir/world-bible/scripts/generate_prompt.py --type "character" --name "Character Name" --scene "Scene description"
```

### Syncing with Second Brain
Capture important world elements to Second Brain for persistent memory:
```bash
python /a0/usr/workdir/world-bible/scripts/sync_to_second_brain.py
```

## JSON Structure

### World Bible Root Structure
```json
{
  "meta": { "title", "version", "created", "last_updated", "description" },
  "style_bible": { "art_direction", "lighting", "color_palette", "visual_references" },
  "characters": [...],
  "locations": [...],
  "objects": [...],
  "lore": { "history", "rules", "terminology" },
  "master_prompt_template": { "image_generation", "story_generation" }
}
```

### Character Structure
```json
{
  "id": "unique-id",
  "name": "Character Name",
  "aliases": [],
  "role": "protagonist|antagonist|supporting|background",
  "physical_description": { "appearance", "distinctive_features", "clothing_style", "age", "height", "build" },
  "personality": { "traits", "motivations", "fears", "quirks" },
  "background": "Backstory",
  "relationships": [],
  "reference_images": [],
  "prompt_keywords": [],
  "notes": ""
}
```

### Location Structure
```json
{
  "id": "unique-id",
  "name": "Location Name",
  "type": "city|building|region|interior|exterior",
  "description": "Detailed description",
  "atmosphere": "Mood and feel",
  "key_features": [],
  "lighting_notes": "Lighting specifics",
  "color_notes": "Color palette for this location",
  "reference_images": [],
  "prompt_keywords": [],
  "connected_locations": [],
  "notes": ""
}
```

## Integration with Second Brain

The World Bible integrates with your Second Brain knowledge base:
- **Characters** are captured as "people" bucket entries
- **Locations** are captured as "ideas" bucket entries
- **Style Bible** is captured as "admin" bucket entry
- **Lore** is captured as "thoughts" bucket entries

Use the `second_brain.search` tool to find World Bible entries by meaning.

## Workflow

1. **Initial Setup**: Define your style bible first - this ensures consistency
2. **Add Characters**: Create character profiles with physical descriptions and personality traits
3. **Add Locations**: Define locations with atmosphere, lighting, and color notes
4. **Generate Prompts**: Use the master template to create consistent prompts
5. **Sync to Memory**: Regularly sync to Second Brain for persistent reference

## Best Practices

- Always include reference images for visual consistency
- Use consistent naming conventions for IDs (e.g., `char_firstname_lastname`, `loc_city_name`)
- Update the `last_updated` timestamp when making changes
- Keep prompt keywords consistent with your style bible
- Regularly backup your World Bible JSON file

## Example Usage

### Creating a Character Entry
```python
import json

# Load World Bible
with open("/a0/usr/workdir/world-bible/world_bible.json", "r") as f:
    bible = json.load(f)

# Add new character
new_character = {
    "id": "char_elena_marie",
    "name": "Elena Marie",
    "role": "protagonist",
    "physical_description": {
        "appearance": "Athletic build with sharp features",
        "distinctive_features": ["Scar on left cheek", "Silver locket"],
        "clothing_style": "Practical adventurer gear",
        "age": "28",
        "height": "5'7"",
        "build": "Athletic"
    },
    "prompt_keywords": ["athletic woman", "sharp features", "scar left cheek", "silver locket", "adventurer gear"]
}

bible["characters"].append(new_character)

# Save
with open("/a0/usr/workdir/world-bible/world_bible.json", "w") as f:
    json.dump(bible, f, indent=2)
```

### Generating an Image Prompt
```python
def generate_image_prompt(character_name, scene_description):
    with open("/a0/usr/workdir/world-bible/world_bible.json", "r") as f:
        bible = json.load(f)

    # Find character
    char = next((c for c in bible["characters"] if c["name"] == character_name), None)

    # Get style prefix
    style = bible["style_bible"]
    style_prefix = f"{style["art_direction"]["primary_style"]}, {style["lighting"]["primary_lighting"]}"

    # Build prompt
    prompt = f"{style_prefix}, {', '.join(char["prompt_keywords"])} {scene_description}"

    return prompt
```
