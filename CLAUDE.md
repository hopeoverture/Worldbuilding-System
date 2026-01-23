# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Obsidian vault containing 87 worldbuilding templates organized into 11 categories for D&D 5e (2024) fantasy settings. Templates are AI generation prompts with structured sections, YAML frontmatter, and image prompt templates.

## Project Structure

```
Templates/                    # 87 reusable templates organized by category
├── Characters/               # 6 templates (Protagonist, Antagonist, Support, Background, Familiar, Divine Servant)
├── Character Options/        # 3 templates (Character Background, Class, Subclass)
├── Settlements/              # 8 templates (Village, Town, City, Stronghold, Tavern, Shop, Temple, Library)
├── Items/                    # 11 templates (Weapon, Armor, Artifact, Potion, Book, Vehicle, etc.)
├── Creatures/                # 5 templates (Monster, Animal, Insect, Species, Plant)
├── Organizations/            # 9 templates (Guild, Government, Military, Cult, Academy, etc.)
├── Concepts/                 # 10 templates (Deity, Pantheon, Magic System, Calendar, Currency, etc.)
├── History/                  # 9 templates (Age, Event, War, Battle, Dynasty, Adventure, etc.)
├── Geography/                # 18 templates (Continent, Region, Mountain Range, Forest, Dungeon, etc.)
├── Encounters/               # 4 templates (Combat, Social, Exploration, Trap)
├── Maps/                     # 4 templates (World, Continent, Region, Settlement)
└── Reference/                # Naming conventions and validation guides

Worlds/                       # Actual worldbuilding projects
└── [World Name]/
    ├── World Overview.md     # Central world document
    └── [Category folders]/   # Entities created from templates

D&D 5e 2024 Rules/            # Complete D&D 5e 2024 reference
├── Core Rules/               # Ability Scores, Combat, Conditions, Actions
├── Character Creation/       # Species, Backgrounds
├── Classes/                  # All 12 classes
├── Feats/                    # Origin, General, Fighting Style, Epic Boon
├── Equipment/                # Weapons, Armor, Adventuring Gear, Tools
├── Spells/                   # Cantrips through 9th level by spell level
├── Monsters/                 # CR and XP reference
└── Appendices/               # Creature Types, Damage Types, Abbreviations

.claude/skills/               # Claude Code slash commands
```

## Skills (Slash Commands)

| Command | Description |
|---------|-------------|
| `/create-world [name]` | Create world with full folder structure |
| `/create-entity [description]` | Generate entity from template (e.g., "dwarven city called Ironhold for Eldoria") |
| `/create-template [type]` | Create new template type |
| `/generate-world [name]` | Auto-generate 80-120 interconnected entities (13 phases with checkpoints) |
| `/worldbuild [name]` | Interactive guided worldbuilding with Q&A (7 phases) |
| `/generate-image [entity path]` | Generate AI image using OpenAI gpt-image-1.5 |
| `/audit-world [name] [--fix]` | Audit for broken links, D&D 5e stat errors, orphans |
| `/expand-entity [entity]` | Add detail, create sub-entities, deepen connections for existing entities |
| `/link-entities [entity1] [entity2]` | Create bidirectional wikilinks; use "auto [world]" to scan for missing links |
| `/random-encounter [location] [level]` | Generate combat, social, or exploration encounters using world entities |
| `/session-prep [world] [focus]` | Create DM session notes, NPC cheat sheets, location briefs |
| `/populate-entity [entity]` | Scan entity for mentions, create linked entities, and add wikilinks |

## Template Format

All templates follow this structure:
1. **YAML Frontmatter** - Required fields: `tags`, `name`, `aliases`, `status`, `image`, plus entity-specific metadata
2. **Title** - Uses `{{title}}` Obsidian Templates variable
3. **Generation Instructions** - `> [!info]` callout with AI guidance
4. **Hierarchical Sections** - Content areas with directive language ("Write 2-3 sentences...", "List 3-4...")
5. **Image Prompts** - Art style + two scene templates with `**Prompt:**` fields to fill
6. **Connections** - `[[Entity Name]]` wikilinks to related entities

### Key Conventions

- **Wikilinks:** Always use `[[Entity Name]]` for cross-references
- **Status field:** `draft` → `in-progress` → `complete`
- **Image field:** `"[[Entity Name.png]]"` after image generation
- **Naming:** Title Case with spaces for files (e.g., "Mountain Range.md")
- **Connections must be bidirectional:** If A links to B, B should link back to A

## D&D 5e 2024 Integration

### Stat Block Modes (Characters)
| Mode | When to Use | Fill | Leave Blank |
|------|-------------|------|-------------|
| **Level-based** | PC-style with class features | `level:` | `challenge_rating:` |
| **CR-based** | NPC/monster style | `challenge_rating:` | `level:` |

### Validation Formulas
- **Ability modifier:** `floor((score - 10) / 2)`
- **Proficiency by level:** +2 (1-4), +3 (5-8), +4 (9-12), +5 (13-16), +6 (17-20)
- **Proficiency by CR:** +2 (0-4), +3 (5-8), +4 (9-12), +5 (13-16), +6 (17-20), +7 (21-24), +8 (25-28), +9 (29-30)
- **Attack bonus:** proficiency + ability modifier
- **Spell Save DC:** 8 + proficiency + spellcasting ability modifier
- **HP (PC):** hit_die_max + CON_mod + ((level - 1) × (hit_die_avg + CON_mod))

### Reference Files
- `D&D 5e 2024 Rules/Monsters/CR and XP.md` - CR to XP conversion table
- `Templates/Reference/D&D Species Naming Conventions.md` - Species-appropriate naming patterns
- `Templates/Reference/Tolkien Naming Conventions.md` - High fantasy linguistic patterns
- `Templates/Reference/Connection Matrix.md` - Bidirectional linking rules and patterns

## Important Files

- `Templates/Reference/D&D 5e Stat Block Validation.md` - Full validation checklist
- `Templates/Reference/Connection Matrix.md` - Bidirectional linking rules
- `Worlds/README.md` - Guide for world directory structure
- `.claude/settings.json` - Permission configuration and attribution settings

## Content Generation Guidelines

1. Fill all template sections with specific names, numbers, and details
2. Create internal consistency across entities
3. Reference other entities using `[[Entity Name]]` syntax
4. Fill image prompt sections with entity-specific details
5. Ensure bidirectional connections (use `/audit-world` to verify)
6. For creatures CR 5+, consider Legendary Resistance and Legendary Actions
