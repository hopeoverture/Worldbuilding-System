# Getting Started with Worldbuilding System

Welcome! This guide will help you start building your first world in minutes.

## Quick Start (5 Minutes)

### 1. Open in Obsidian

1. Download and install [Obsidian](https://obsidian.md/) if you haven't already
2. Open Obsidian and click "Open folder as vault"
3. Select this repository's folder
4. Trust the vault when prompted

### 2. Explore the Example World

Before creating your own world, explore **Eldermyr** to see how everything fits together:

1. Navigate to `Worlds/Eldermyr/`
2. Open `World Overview.md` - this is the central hub
3. Click any `[[wikilink]]` to explore connected entities
4. Notice how characters link to settlements, which link to organizations, etc.

### 3. Create Your First World

Using Claude Code or a compatible AI assistant:

```
/create-world MyWorld
```

This creates a complete folder structure with a World Overview ready for you to fill in.

---

## Two Paths to Worldbuilding

### Path A: Quick Generation (30-60 minutes)

Use `/generate-world` to automatically create 80-120 interconnected entities:

```
/generate-world MyWorld
```

You'll provide a concept, then the AI generates entities across 13 phases with checkpoints where you can guide the direction.

**Best for:** Quick prototypes, getting unstuck, exploring possibilities

### Path B: Guided Collaboration (Multiple Sessions)

Use `/worldbuild` for interactive, thoughtful world creation:

```
/worldbuild MyWorld
```

The AI asks questions about your world and creates entities one at a time based on your answers.

**Best for:** Personal campaigns, specific visions, detailed control

---

## Your First Entity

Once you have a world, create your first custom entity:

```
/create-entity a dwarven blacksmith named Thorin Ironforge for MyWorld
```

The AI will:
1. Choose the appropriate template (Support Character)
2. Fill in the sections with your specifications
3. Create connections to existing entities
4. Add image prompt templates

---

## Understanding Templates

Every entity starts from a template in the `Templates/` folder. Templates have:

### YAML Frontmatter
```yaml
---
tags: [character, support]
name: "Thorin Ironforge"
status: draft
species: "Dwarf"
location: "[[Ironhold]]"
---
```

### Structured Sections
Headings with guidance like "Write 2-3 sentences about..."

### Image Prompts
Ready-to-use prompts for AI image generation

### Connections
Wikilinks to related entities: `[[Ironhold]]`, `[[Blacksmith's Guild]]`

---

## Essential Concepts

### Wikilinks
Everything connects via `[[Entity Name]]` syntax. Click any link to navigate. These connections:
- Enable vault navigation
- Show in Obsidian's graph view
- Get validated by audit tools

### Bidirectional Linking
If Character A mentions Settlement B, Settlement B should mention Character A. The `/audit-world` command checks this.

### Status Tracking
Every entity has a status:
- `draft` - Just created, minimal content
- `in-progress` - Being developed
- `complete` - Fully detailed, ready for use

---

## Next Steps After Your First World

### Add More Entities
```
/create-entity an ancient forest called the Whispering Woods for MyWorld
```

### Connect Everything
```
/linkify --world MyWorld
```
Automatically adds wikilinks where entity names are mentioned.

### Check Your Work
```
/audit-world MyWorld
```
Finds broken links, orphaned entities, and D&D stat errors.

### Prepare for Sessions
```
/session-prep MyWorld "the party visits Ironhold"
```
Generates DM notes, NPC cheat sheets, and location briefs.

---

## Recommended Workflow

### Building a New World

1. **Start:** `/create-world` or `/generate-world`
2. **Expand:** `/create-entity` for specific additions
3. **Connect:** `/linkify --world` to add wikilinks
4. **Validate:** `/audit-world` to check quality
5. **Deepen:** `/expand-settlement`, `/expand-faction`, etc.

### Before Each Session

1. **Review:** Read relevant entities
2. **Prep:** `/session-prep` for focused notes
3. **Generate:** `/random-encounter` for backup encounters
4. **Create:** `/generate-image` for key NPCs or locations

### After Each Session

1. **Update:** Edit entities based on what happened
2. **Create:** New entities for introduced elements
3. **Connect:** `/link-entities` for new relationships
4. **Track:** `/campaign-arc` for ongoing plots

---

## Useful Skills by Task

| I want to... | Use this skill |
|--------------|----------------|
| Create a new world | `/create-world` |
| Auto-generate a world | `/generate-world` |
| Build world interactively | `/worldbuild` |
| Add a specific entity | `/create-entity` |
| Add wikilinks | `/linkify` |
| Check for problems | `/audit-world` |
| Prepare for a session | `/session-prep` |
| Create a random encounter | `/random-encounter` |
| Generate AI art | `/generate-image` |
| Flesh out a city | `/expand-settlement` |
| Develop an organization | `/expand-faction` |
| Add NPCs and shops | `/populate-entity` |

---

## File Locations

| What | Where |
|------|-------|
| Your worlds | `Worlds/[WorldName]/` |
| Templates | `Templates/` |
| D&D 5e rules | `D&D 5e 2024 Rules/` |
| Utility scripts | `scripts/` |
| Example world | `Worlds/Eldermyr/` |
| Reference guides | `Templates/Reference/` |

---

## Getting Help

- **Skill list:** Run `/help` or see `CLAUDE.md`
- **Template format:** See `Templates/Reference/YAML Frontmatter Reference.md`
- **Naming conventions:** See `Templates/Reference/` folder
- **D&D rules:** Browse `D&D 5e 2024 Rules/`
- **Issues:** Report at https://github.com/anthropics/claude-code/issues

---

## Tips for Success

### Start Small
Don't try to build everything at once. Start with one region, a few NPCs, and expand as needed for your campaign.

### Let Connections Guide You
When creating an entity, the Connections section suggests what to create next. A blacksmith needs a shop, a guild, a settlement...

### Use the Graph View
In Obsidian, open the Graph View (Ctrl/Cmd+G) to visualize how your world connects. Orphaned nodes need more links!

### Embrace Imperfection
`draft` status exists for a reason. Create quick entities during sessions and flesh them out later.

### Iterate Often
Run `/audit-world` regularly. It's easier to fix a few broken links than hundreds.

---

Ready to start? Open your terminal and run:
```
/create-world [YourWorldName]
```

Happy worldbuilding!
