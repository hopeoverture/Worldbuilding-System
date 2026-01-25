# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Obsidian vault containing 91 worldbuilding templates organized into 11 categories for D&D 5e (2024) fantasy settings. Templates are AI generation prompts with structured sections, YAML frontmatter, and image prompt templates.

## Project Structure

```
Templates/                    # 91 reusable templates organized by category
├── Characters/               # 6 templates (Protagonist, Antagonist, Support, Background, Familiar, Divine Servant)
├── Character Options/        # 3 templates (Character Background, Class, Subclass)
├── Settlements/              # 8 templates (Village, Town, City, Stronghold, Tavern, Shop, Temple, Library)
├── Items/                    # 11 templates (Weapon, Armor, Artifact, Wondrous Item, Potion, Food, etc.)
├── Creatures/                # 5 templates (Monster, Animal, Insect, Species, Plant)
├── Organizations/            # 9 templates (Guild, Government, Military, Cult, Academy, Business, etc.)
├── Concepts/                 # 10 templates (Deity, Pantheon, Magic System, Calendar, Currency, Language, etc.)
├── History/                  # 9 templates (Age, Event, War, Battle, Dynasty, Adventure, Tragedy, Treaty)
├── Geography/                # 18 templates (Continent, Region, Mountain Range, Forest, Dungeon, Cave, etc.)
├── Encounters/               # 4 templates (Combat, Social, Exploration, Trap)
├── Maps/                     # 4 templates (World, Continent, Region, Settlement)
└── Reference/                # Naming conventions and validation guides (4 files)

Worlds/                       # Actual worldbuilding projects
└── [World Name]/
    ├── World Overview.md     # Central world document
    ├── .worldbuild-state.json # Generation state tracking (for /generate-world)
    └── [Category folders]/   # Entities created from templates

D&D 5e 2024 Rules/            # Complete D&D 5e 2024 reference (65 files)
├── Core Rules/               # Ability Scores, Combat, Conditions, Actions
├── Character Creation/       # Species, Backgrounds
├── Classes/                  # All 12 classes with features
├── Feats/                    # Origin, General, Fighting Style, Epic Boon
├── Equipment/                # Weapons, Armor, Adventuring Gear, Tools
├── Spells/                   # Cantrips through 9th level by spell level
├── Monsters/                 # CR and XP reference
└── Appendices/               # Creature Types, Damage Types, Abbreviations

scripts/                      # Python utility scripts
└── linkify_world.py          # Batch wikilink generator for entire worlds

.claude/                      # Claude Code configuration
├── settings.json             # Permissions and attribution settings
└── skills/                   # 24 slash command definitions
```

## Skills (Slash Commands)

| Command | Description |
|---------|-------------|
| `/create-world [name]` | Create world with full folder structure |
| `/create-entity [description]` | Generate entity from template (e.g., "dwarven city called Ironhold for Eldoria") |
| `/create-template [type]` | Create new template type |
| `/generate-world [name]` | Auto-generate 80-120 interconnected entities (13 phases with checkpoints) |
| `/worldbuild [name]` | Interactive guided worldbuilding with Q&A (9 phases) |
| `/generate-image [entity path]` | Generate AI image using OpenAI gpt-image-1 |
| `/audit-world [name] [--fix]` | Audit for broken links, D&D 5e stat errors, orphans |
| `/expand-entity [entity]` | Add detail, create sub-entities, deepen connections for existing entities |
| `/link-entities [entity1] [entity2]` | Create bidirectional wikilinks; use "auto [world]" to scan for missing links |
| `/random-encounter [location] [level]` | Generate combat, social, or exploration encounters using world entities |
| `/session-prep [world] [focus]` | Create DM session notes, NPC cheat sheets, location briefs |
| `/populate-entity [entity]` | Scan entity for mentions, create linked entities, and add wikilinks |
| `/linkify [entity]` | Auto-add [[wikilinks]] to all mentions of existing entities within a file; supports `--world` for bulk |
| `/validate-template [path]` | Validate a template or entity has required sections and YAML fields |
| `/campaign-arc [world]` | Track multi-session story arcs, plot threads, and campaign progression |
| `/expand-settlement [settlement]` | Deep-dive into settlements: generate NPCs, shops, taverns, districts, rumors |
| `/expand-faction [org]` | Build out organizations: hierarchy, internal politics, plots, rivals |
| `/expand-region [region]` | Fill regions with villages, landmarks, encounters, legends, hazards |
| `/generate-culture [people]` | Create cultural depth: festivals, customs, taboos, cuisine, ceremonies |
| `/map-relationships [entity]` | Visualize/expand relationship networks, power dynamics, secrets |
| `/expand-history [era/event]` | Detail historical periods: timelines, key figures, artifacts, witnesses |
| `/generate-economy [world]` | Create trade routes, resource nodes, merchant guilds, black markets |
| `/generate-politics [world]` | Map alliances, conflicts, treaties, succession crises, power brokers |
| `/generate-quests [scope]` | Generate adventure hooks: bounties, mysteries, faction missions, dungeons |

### Skill Comparison: /generate-world vs /worldbuild

| Aspect | `/generate-world` | `/worldbuild` |
|--------|-------------------|---------------|
| **Approach** | Automatic batch generation | Interactive Q&A collaboration |
| **Output** | 80-120 entities in one session | Entities created one at a time |
| **User Input** | Initial concept, then checkpoints | Every decision requires approval |
| **Phases** | 13 phases with checkpoints | 9 phases with deep questions |
| **Best For** | Quick world scaffolding | Thoughtful, custom worlds |
| **Control** | Medium (approve at checkpoints) | High (approve each entity) |
| **Session Length** | 30-60 minutes continuous | Multiple sessions, pauseable |

### Skill Prerequisites & Recommended Order

Some skills work best when run in a specific sequence:

| Goal | Skill Sequence |
|------|----------------|
| **New world from scratch** | `/create-world` → `/generate-world` OR `/worldbuild` |
| **Add entity to world** | `/create-entity` → `/linkify` → `/audit-world --check links` |
| **Flesh out existing entity** | `/expand-entity` → `/populate-entity` → `/linkify` |
| **Quality check** | `/audit-world` → `/link-entities auto` → `/audit-world --fix` |
| **Session preparation** | `/random-encounter` → `/session-prep` |
| **Complete enhancement cycle** | `/populate-entity` → `/linkify` → `/audit-world` → `/link-entities auto` |

**Dependency Notes:**
- Always run `/audit-world` AFTER `/populate-entity` (entities must exist before auditing)
- Run `/linkify` BEFORE `/audit-world` to reduce broken link warnings
- `/generate-image` requires filled image prompt sections (created by `/create-entity`)

### Expansion Skills (Deep-Dive Commands)

These commands add depth to areas that `/worldbuild` creates in breadth:

| Skill | Expands | Creates | Best After |
|-------|---------|---------|------------|
| `/expand-settlement` | Cities, Towns, Villages | 10-25 NPCs, shops, taverns, districts | `/worldbuild` or `/create-entity` |
| `/expand-faction` | Organizations | Hierarchy, members, plots, rivals | Organization exists |
| `/expand-region` | Geographic Regions | Villages, landmarks, routes, legends | Region exists |
| `/generate-culture` | Peoples/Nations | Customs, festivals, ceremonies, cuisine | Government/Species exists |
| `/map-relationships` | Characters/Orgs | Relationship webs, power dynamics | Multiple entities exist |
| `/expand-history` | Ages, Events, Wars | Timelines, figures, artifacts, witnesses | History entity exists |
| `/generate-economy` | Entire World | Trade routes, resources, guilds, markets | Settlements/regions exist |
| `/generate-politics` | Entire World | Alliances, conflicts, treaties, succession | Governments exist |
| `/generate-quests` | Any Scope | Bounties, mysteries, faction missions | World has content |

### Expansion Workflows

| Goal | Recommended Sequence |
|------|---------------------|
| **Make a city playable** | `/expand-settlement` → `/map-relationships` (key NPCs) → `/generate-quests` |
| **Develop a faction** | `/expand-faction` → `/map-relationships` → `/generate-quests` (faction missions) |
| **Flesh out a region** | `/expand-region` → `/expand-settlement` (villages) → `/generate-quests` |
| **Add world depth** | `/generate-economy` → `/generate-politics` → `/generate-quests` |
| **Cultural immersion** | `/generate-culture` → Update settlements with culture → `/session-prep` |
| **Historical campaign** | `/expand-history` → Create descendant NPCs → `/map-relationships` |

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

## MCP Integration

This vault uses Model Context Protocol servers for enhanced AI capabilities:

| Server | Package | Purpose |
|--------|---------|---------|
| `obsidian` | `obsidian-mcp` | Read/write vault files, search notes, manage tags |
| `memory` | `@modelcontextprotocol/server-memory` | Persistent knowledge graph for session context |
| `fetch` | `@modelcontextprotocol/server-fetch` | Web fetching for external references |

Configuration is in `.mcp.json`. Enable all servers in `.claude/settings.json`:
```json
"enableAllProjectMcpServers": true
```

## Example World: Eldermyr

The repository includes a complete example world in `Worlds/Eldermyr/` with 54+ entities:
- **Setting:** Post-war succession crisis, medieval fantasy
- **Tone:** Low/High Fantasy + Political Fantasy
- **Inspirations:** Game of Thrones, LOTR, Octopath Traveler

Use this as reference for how templates are filled and entities interconnect.

## Scripts

### linkify_world.py

Batch add `[[wikilinks]]` to all entity files in a world:

```bash
python scripts/linkify_world.py Eldermyr           # Apply changes
python scripts/linkify_world.py Eldermyr --dry-run # Preview changes
python scripts/linkify_world.py Eldermyr --verbose # Detailed output
```

Features:
- Reads aliases from YAML frontmatter
- Respects existing wikilinks, code blocks, and tables
- Handles partial name matches intelligently
- Tracks ambiguous references

## Important Files

- `Templates/Reference/D&D 5e Stat Block Validation.md` - Full validation checklist
- `Templates/Reference/Connection Matrix.md` - Bidirectional linking rules
- `Worlds/README.md` - Guide for world directory structure
- `.claude/settings.json` - Permission configuration and attribution settings

## Permissions

Configured in `.claude/settings.json`:

**Allowed operations:**
- Git commands
- Directory listing (`ls`, `dir`)
- File reading (`type`)
- Directory creation (`mkdir`)
- File copying and moving (`copy`, `move`)

**Denied operations:**
- Destructive deletion (`rm -rf`, `del /s`, `rmdir /s`)
- Reading secrets (`.env`, `.env.*`, `secrets/**`)

## Performance Guidelines

For optimal performance with large worlds:

| World Size | Entity Count | Expected Behavior |
|------------|--------------|-------------------|
| Small | < 50 entities | All operations instant |
| Medium | 50-150 entities | Linkify/audit may take 10-30 seconds |
| Large | 150-300 entities | Use `--category` flags to scope operations |
| Very Large | 300+ entities | Use batch scripts (`linkify_world.py`) for bulk ops |

**Tips for Large Worlds:**
- Use `/audit-world [world] --category Characters` to audit one category at a time
- Use `/linkify --world [world] --dry-run` to preview before bulk changes
- The Python script `scripts/linkify_world.py` is faster for 100+ entities
- Consider splitting very large worlds into sub-regions with their own folders

## Content Generation Guidelines

1. Fill all template sections with specific names, numbers, and details
2. Create internal consistency across entities
3. Reference other entities using `[[Entity Name]]` syntax
4. Fill image prompt sections with entity-specific details
5. Ensure bidirectional connections (use `/audit-world` to verify)
6. For creatures CR 5+, consider Legendary Resistance and Legendary Actions
7. For image prompts, always fill the `**Prompt:**` field with specific descriptive text

## Attribution

All AI-generated commits include:
```
🏰 Worldbuilding content generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
```
