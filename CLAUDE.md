# Worldbuilding Vault

## Overview
Obsidian vault containing worldbuilding templates for a fantasy setting. Templates are designed as AI generation prompts with structured sections, YAML frontmatter, and image prompt templates.

## Project Structure
```
Templates/                    # Reusable templates for entity creation
├── Characters/               # Protagonists, Antagonists, Support Characters, Background Characters,
                              # Divine Servants, Familiars
├── Settlements/              # Villages, Towns, Cities, Strongholds, Taverns, Shops, Temples, Libraries
├── Items/                    # Weapons, Armor, Wondrous Magic Items, Potions, Gear, Food, Drink,
                              # Containers, Artifacts, Vehicles, Books
├── Creatures/                # Monsters, Animals, Insects, Species, Plants
├── Organizations/            # Guilds, Governments, Religious Orders, Cults, Military, Criminal,
                              # Business, General, Academies
├── Concepts/                 # Religions, Pantheons, Deities, Magic Systems, Technologies, Languages,
                              # Prophecies, Planes of Existence, Currencies, Calendars
├── History/                  # Events, Wars, Battles, Treaties, Trade Agreements, Tragedies,
                              # Dynasties, Ages
└── Geography/                # Continents, Regions, Mountains, Forests, Rivers, Roads, Deserts,
                              # Tundras, Plains, Hills, Steppes, Oceans, Lakes, Coasts, Passes,
                              # Islands, Caves, Dungeons

Worlds/                       # Actual worldbuilding projects
└── [World Name]/
    ├── World Overview.md     # Central world document
    ├── Characters/
    ├── Settlements/
    ├── Items/
    ├── Creatures/
    ├── Organizations/
    ├── Concepts/
    ├── History/
    └── Geography/
```

## Template Format

### Structure
All templates follow this pattern:
1. **YAML Frontmatter** - Entity-specific metadata for filtering and organization
2. **Title** - Uses `{{title}}` Obsidian Templates plugin variable
3. **Generation Instructions** - `> [!info]` callout block with AI guidance
4. **Hierarchical Sections** - Organized content areas with directive language
5. **Image Prompts** - Dual format with art style and two scene templates
6. **Notes** - Space for additional details
7. **Connections** - `[[Entity Name]]` wikilinks to related entities

### Writing Style
- **Directive language**: "Write 2-3 sentences...", "List 3-4...", "Describe in 2-3 sentences..."
- **Specific output requirements**: Clear expectations for content length and format
- **Classification options**: Parenthetical choices like "(Type A / Type B / Type C)"
- **Tables**: For structured data with clear column headers

### Image Prompt Format
```markdown
### Art Style
**Hyper-realistic digital art, photorealistic rendering, cinematic lighting, rich textures, intricate detail on [relevant elements], dramatic atmosphere, depth of field, volumetric lighting, 8K quality, masterful composition.**

### [Scene Type 1]
**Template:**
> [Detailed scene description with placeholders in brackets]. [Art style suffix].

**Prompt:**

### [Scene Type 2]
**Template:**
> [Second scene description]. [Art style suffix].

**Prompt:**
```

### Connections Section
Use `[[Entity Name]]` wikilink syntax for cross-referencing:
```markdown
## Connections
Link to related entities using `[[Entity Name]]` syntax.

### Category
- **Relationship:** [[]], [[]]
```

## Conventions

### YAML Frontmatter
- Always include `tags`, `name`, `aliases`, and `status` fields
- Add entity-specific metadata fields (e.g., `location`, `affiliation`, `challenge_rating`)
- Use `status: draft` for new entries

### D&D 5e (2024) Integration
- Include mechanical fields where applicable (Challenge Rating, ability scores, domains)
- Reference 5e creature types, weapon properties, armor categories
- Cleric domains for deities

### Naming
- Template files use Title Case with spaces (e.g., "Mountain Range.md")
- Use descriptive, evocative names for generated content

## Important Files
- `Templates/` - All worldbuilding templates organized by category
- `Worlds/` - Actual worldbuilding projects with entities created from templates
- `Worlds/README.md` - Guide for using the Worlds directory

## Claude Code Skills
Skills are located in `.claude/skills/` and provide slash commands:

| Skill | Usage | Description |
|-------|-------|-------------|
| `/create-template` | `/create-template [type]` | Create a new template (e.g., "tavern", "spell") |
| `/create-world` | `/create-world [name]` | Create a new world with full folder structure |
| `/create-entity` | `/create-entity [description]` | Generate a populated entity from a template |

**Examples:**
```
/create-world Eldoria
/create-entity dwarven city called Ironhold for Eldoria
/create-template dungeon
```

## Guidelines

### When Creating New Templates
1. Follow the established format pattern
2. Include YAML frontmatter with relevant metadata
3. Add `> [!info] Generation Instructions` callout
4. Use directive language throughout
5. Include dual image prompts
6. Add Connections section with appropriate relationship categories

### When Generating Content
1. Fill all sections with coherent, interconnected details
2. Use specific numbers and names, not vague descriptions
3. Create plot hooks that tie to the broader world
4. Ensure image prompts are filled with entity-specific details
5. Link to other entities using `[[Entity Name]]` syntax

### Template Categories (75 total)
| Folder | Templates |
|--------|-----------|
| Characters | 6 (Protagonist, Antagonist, Support Character, Background Character, Divine Servant, Familiar) |
| Settlements | 8 (Village, Town, City, Stronghold, Tavern, Shop, Temple, Library) |
| Items | 11 (Weapon, Armor, Wondrous Magic Item, Potion, Gear, Food, Drink, Container, Artifact, Vehicle, Book) |
| Creatures | 5 (Monster, Animal, Insect, Species, Plant) |
| Organizations | 9 (Guild, Government, Religious Order, Cult, Military, Criminal Organization, Business, Organization General, Academy) |
| Concepts | 10 (Religion, Pantheon, Deity, Magic System, Technology, Language, Prophecy, Plane of Existence, Currency, Calendar) |
| History | 8 (Event, War, Battle, Treaty, Trade Agreement, Tragedy, Dynasty, Age) |
| Geography | 18 (Continent, Region, Mountain Range, Forest, River, Road, Desert, Tundra, Plains, Hills, Steppes, Ocean, Lake, Coast, Pass, Island, Cave, Dungeon) |
