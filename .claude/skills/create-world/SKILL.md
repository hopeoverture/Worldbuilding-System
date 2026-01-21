---
name: create-world
description: Create a new worldbuilding project with full folder structure. Use when the user wants to start a new world, campaign setting, or fantasy setting like "create a world called Eldoria".
argument-hint: "[world name]"
---

# Create New World

Create a new worldbuilding project for: $ARGUMENTS

## Instructions

You are creating a new world directory with the full folder structure for a fantasy worldbuilding project.

### Step 1: Determine World Name

Use the provided argument as the world name. If not provided, ask the user for a world name.

The world name should be:
- Evocative and memorable
- Title Case with spaces allowed
- Used as the folder name

### Step 2: Create Directory Structure

Create the following structure in `Worlds/[World Name]/`:

```
[World Name]/
├── World Overview.md
├── Characters/
├── Settlements/
├── Items/
├── Creatures/
├── Organizations/
├── Concepts/
├── History/
└── Geography/
```

### Step 3: Create World Overview Document

Create `World Overview.md` with this structure:

```markdown
---
tags:
  - world
  - overview
name: [World Name]
aliases: []
status: draft
# World Details
genre: fantasy
tone:
time_period:
magic_level:
technology_level:
---

# [World Name]

> [!info] World Overview
> This is the central document for [World Name]. Use it to track high-level worldbuilding details, themes, and the relationships between major elements.

## Premise
> Write 2-3 sentences describing the core concept of this world. What makes it unique? What's the central conflict or theme?

## Tone & Themes

### Tone
**Primary Tone:** (Epic / Dark / Whimsical / Gritty / Hopeful / Mysterious)

**Inspirations:**
-

### Central Themes
1.
2.
3.

## The World

### Geography Overview
Describe the world's physical layout in 3-4 sentences. Continents, major regions, climate zones.

### Major Powers
| Power | Type | Region | Status |
|-------|------|--------|--------|
| | | | |
| | | | |

### Timeline
| Era | Period | Key Events |
|-----|--------|------------|
| | | |
| | | |

## Magic & Technology

### Magic
**Magic Level:** (None / Rare / Uncommon / Common / Pervasive)

**Magic System(s):**
-

### Technology
**Technology Level:** (Primitive / Ancient / Medieval / Renaissance / Industrial / Magitech)

**Notable Technologies:**
-

## Cosmology

### The Divine
Brief overview of gods, pantheons, or spiritual forces.

### Planes of Existence
-

### Creation Myth
Summary in 2-3 sentences.

## Current Era

### The State of the World
Describe the present situation in 3-4 sentences. What's happening now? What tensions exist?

### Major Conflicts
1.
2.

### Opportunities for Adventure
1.
2.
3.

## World-Specific Rules

### House Rules
Any D&D 5e modifications for this setting:
-

### Unique Mechanics
Setting-specific systems:
-

## Development Notes

### Priorities
What to develop next:
1.
2.
3.

### Questions to Answer
Unresolved worldbuilding questions:
1.
2.

### Inspiration Sources
-

## Quick Reference

### Key Locations
- [[]]
- [[]]

### Key Characters
- [[]]
- [[]]

### Key Organizations
- [[]]
- [[]]

### Key Concepts
- [[]]
- [[]]
```

### Step 4: Create .gitkeep Files

Add empty `.gitkeep` files to each subdirectory so they're tracked in version control:
- Characters/.gitkeep
- Settlements/.gitkeep
- Items/.gitkeep
- Creatures/.gitkeep
- Organizations/.gitkeep
- Concepts/.gitkeep
- History/.gitkeep
- Geography/.gitkeep

### Step 5: Confirmation

After creating the world, tell the user:
1. The world has been created at `Worlds/[World Name]/`
2. Start by filling out `World Overview.md`
3. Use templates from `Templates/` to create entities
4. Place entity notes in the appropriate category folders
