# Worldbuilding System

An AI-powered worldbuilding toolkit for **D&D 5e (2024)** fantasy settings, built as an Obsidian vault with 91 structured templates, 13 AI-assisted skills, and comprehensive rules reference.

## Features

- **91 Reusable Templates** across 11 categories with structured YAML frontmatter, AI generation prompts, and image prompt fields
- **13 AI Skills (Slash Commands)** for world generation, entity creation, auditing, and session prep
- **Complete D&D 5e 2024 Rules Reference** - 65 files covering core rules, classes, spells, equipment, and monsters
- **Bidirectional Wikilinks** - Obsidian-native `[[Entity Name]]` cross-references with validation
- **Image Prompt Integration** - Built-in prompts for AI image generation (OpenAI gpt-image-1)
- **MCP Server Integration** - Obsidian, Memory, and Fetch servers for enhanced AI capabilities

## Quick Start

### Prerequisites

- [Obsidian](https://obsidian.md/) (recommended for viewing/editing)
- [Claude Code](https://claude.ai/code) or compatible AI assistant for skill commands
- Node.js (for MCP servers)
- Python 3.8+ (optional, for batch scripts)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/worldbuilding-system.git
   ```

2. Open the folder as an Obsidian vault:
   - Launch Obsidian
   - Click "Open folder as vault"
   - Select the cloned directory

3. (Optional) Install MCP dependencies for AI integration:
   ```bash
   npm install -g obsidian-mcp @modelcontextprotocol/server-memory @modelcontextprotocol/server-fetch
   ```

## Project Structure

```
Worldbuilding System/
├── Templates/                    # 91 reusable templates
│   ├── Characters/               # Protagonist, Antagonist, Support, Background, Familiar, Divine Servant
│   ├── Character Options/        # Background, Class, Subclass
│   ├── Settlements/              # Village, Town, City, Stronghold, Tavern, Shop, Temple, Library
│   ├── Items/                    # Weapon, Armor, Artifact, Wondrous Item, Potion, Food, etc.
│   ├── Creatures/                # Monster, Animal, Insect, Plant, Species
│   ├── Organizations/            # Guild, Government, Military, Cult, Academy, Business, etc.
│   ├── Concepts/                 # Deity, Pantheon, Magic System, Calendar, Currency, Language, etc.
│   ├── History/                  # Age, Event, War, Battle, Dynasty, Adventure, Tragedy, Treaty
│   ├── Geography/                # Continent, Region, Mountain Range, Forest, Dungeon, Cave, etc.
│   ├── Encounters/               # Combat, Social, Exploration, Trap
│   ├── Maps/                     # World, Continent, Region, Settlement
│   └── Reference/                # Naming conventions, validation guides, connection matrix
│
├── Worlds/                       # Your worldbuilding projects
│   └── [World Name]/
│       ├── World Overview.md     # Central world document
│       ├── Characters/           # NPCs and PCs
│       ├── Settlements/          # Cities, towns, villages
│       ├── Organizations/        # Factions, guilds, governments
│       ├── Geography/            # Regions, landmarks
│       ├── History/              # Timeline events
│       ├── Concepts/             # Magic, religion, culture
│       ├── Items/                # Notable objects
│       └── Encounters/           # Prepared encounters
│
├── D&D 5e 2024 Rules/            # Complete rules reference
│   ├── Core Rules/               # Ability Scores, Combat, Conditions, Actions
│   ├── Character Creation/       # Species, Backgrounds
│   ├── Classes/                  # All 12 classes with features
│   ├── Feats/                    # Origin, General, Fighting Style, Epic Boon
│   ├── Equipment/                # Weapons, Armor, Adventuring Gear, Tools
│   ├── Spells/                   # Cantrips through 9th level
│   ├── Monsters/                 # CR and XP reference
│   └── Appendices/               # Creature Types, Damage Types, Abbreviations
│
├── scripts/                      # Utility scripts
│   └── linkify_world.py          # Batch wikilink generator
│
├── .claude/                      # Claude Code configuration
│   ├── settings.json             # Permissions and attribution
│   └── skills/                   # 13 slash command definitions
│
├── CLAUDE.md                     # AI assistant instructions
├── GEMINI.md                     # Gemini-specific instructions
└── .mcp.json                     # MCP server configuration
```

## Skills (Slash Commands)

Use these commands with Claude Code or compatible AI assistants:

### World Creation
| Command | Description |
|---------|-------------|
| `/create-world [name]` | Create a new world with full folder structure |
| `/generate-world [name]` | Auto-generate 80-120 interconnected entities across 13 phases |
| `/worldbuild [name]` | Interactive guided worldbuilding with Q&A workflow |

### Entity Management
| Command | Description |
|---------|-------------|
| `/create-entity [description]` | Generate entity from template (e.g., "dwarven city called Ironhold for Eldoria") |
| `/create-template [type]` | Create a new template type |
| `/expand-entity [entity]` | Add detail, create sub-entities, deepen connections |
| `/populate-entity [entity]` | Scan for mentions, create linked entities, add wikilinks |

### Linking & Validation
| Command | Description |
|---------|-------------|
| `/link-entities [entity1] [entity2]` | Create bidirectional wikilinks between entities |
| `/linkify [entity]` | Auto-add `[[wikilinks]]` to all entity mentions in a file |
| `/audit-world [name] [--fix]` | Audit for broken links, D&D 5e stat errors, orphaned entities |

### Game Prep
| Command | Description |
|---------|-------------|
| `/random-encounter [location] [level]` | Generate combat, social, or exploration encounters |
| `/session-prep [world] [focus]` | Create DM session notes, NPC cheat sheets, location briefs |
| `/generate-image [entity]` | Generate AI image using OpenAI gpt-image-1 |

## Template Format

All templates follow a consistent structure:

```markdown
---
tags: [template-type]
name: "{{title}}"
aliases: []
status: draft
image: ""
# ... entity-specific fields
---

# {{title}}

> [!info] Generation Instructions
> AI guidance for content creation...

## Section Name
Content with directive language ("Write 2-3 sentences...", "List 3-4...")

## Connections
- [[Related Entity 1]]
- [[Related Entity 2]]

## Image Prompts
**Art Style:** Description of visual style

### Scene 1
**Prompt:** [AI will fill this with entity-specific image prompt]
```

### Key Conventions

- **Wikilinks:** Always use `[[Entity Name]]` for cross-references
- **Status field:** `draft` → `in-progress` → `complete`
- **Image field:** `"[[Entity Name.png]]"` after image generation
- **Naming:** Title Case with spaces for files (e.g., `Mountain Range.md`)
- **Bidirectional links:** If A links to B, B must link back to A

## D&D 5e 2024 Integration

### Stat Block Modes

| Mode | When to Use | Fill | Leave Blank |
|------|-------------|------|-------------|
| **Level-based** | PC-style with class features | `level:` | `challenge_rating:` |
| **CR-based** | NPC/monster style | `challenge_rating:` | `level:` |

### Validation Formulas

```
Ability modifier     = floor((score - 10) / 2)
Proficiency (level)  = +2 (1-4), +3 (5-8), +4 (9-12), +5 (13-16), +6 (17-20)
Proficiency (CR)     = +2 (0-4), +3 (5-8), +4 (9-12), +5 (13-16), +6 (17-20), +7 (21-24), +8 (25-28), +9 (29-30)
Attack bonus         = proficiency + ability modifier
Spell Save DC        = 8 + proficiency + spellcasting ability modifier
HP (PC)              = hit_die_max + CON_mod + ((level - 1) × (hit_die_avg + CON_mod))
```

## Example World: Eldermyr

The repository includes **Eldermyr**, a complete example world with 54+ interconnected entities:

- **Setting:** Post-war succession crisis in a medieval fantasy realm
- **Tone:** Low/High Fantasy + Political Fantasy (inspired by Game of Thrones, LOTR, Octopath Traveler)
- **Content:** 16 characters, 12 settlements, 7 organizations, 6 geographic regions, 5 items, and more

Explore `Worlds/Eldermyr/` to see how templates are filled and entities interconnect.

## Scripts

### linkify_world.py

Batch add `[[wikilinks]]` to all entity files in a world:

```bash
python scripts/linkify_world.py Eldermyr           # Apply changes
python scripts/linkify_world.py Eldermyr --dry-run # Preview changes
python scripts/linkify_world.py Eldermyr --verbose # Detailed output
```

## MCP Integration

This vault includes Model Context Protocol (MCP) server configuration for enhanced AI capabilities:

| Server | Purpose |
|--------|---------|
| `obsidian-mcp` | Read/write vault files, search, manage notes |
| `server-memory` | Persistent knowledge graph for context retention |
| `server-fetch` | Web fetching for external references |

Configure in `.mcp.json`:

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "obsidian-mcp", "/path/to/vault"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

## Contributing

1. **Templates:** Follow the existing format in `Templates/`. Include YAML frontmatter, generation instructions, and image prompts.
2. **Skills:** Add new `.md` files to `.claude/skills/` following the skill definition format.
3. **Rules Reference:** Maintain accuracy with official D&D 5e 2024 materials.

## Template Categories

| Category | Templates | Examples |
|----------|-----------|----------|
| Characters | 6 | Protagonist, Antagonist, Support Character, Familiar |
| Character Options | 3 | Background, Class, Subclass |
| Settlements | 8 | Village, Town, City, Stronghold, Tavern, Shop |
| Items | 11 | Weapon, Armor, Artifact, Potion, Book, Vehicle |
| Creatures | 5 | Monster, Animal, Insect, Plant, Species |
| Organizations | 9 | Guild, Government, Military, Cult, Academy |
| Concepts | 10 | Deity, Pantheon, Magic System, Calendar, Currency |
| History | 9 | Age, Event, War, Battle, Dynasty, Adventure |
| Geography | 18 | Continent, Region, Mountain Range, Forest, Dungeon |
| Encounters | 4 | Combat, Social, Exploration, Trap |
| Maps | 4 | World, Continent, Region, Settlement |
| Reference | 4 | Naming conventions, validation, connection matrix |

## License

This project is intended for personal use with tabletop roleplaying games. D&D 5e rules reference is derived from the 2024 System Reference Document (SRD) under the Creative Commons license.

---

*Built for dungeon masters, worldbuilders, and storytellers who want AI-assisted creative tools with the precision of structured data.*
