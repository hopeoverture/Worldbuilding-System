---
tags:
  - reference
  - yaml
  - frontmatter
  - validation
status: complete
---

# YAML Frontmatter Reference

This reference defines all YAML frontmatter fields used across entity templates in the worldbuilding system. Use this guide to ensure consistent metadata across all entities.

## Universal Fields (All Templates)

These fields appear in **every** entity template:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `tags` | array | Yes | Category and type tags | `[character, protagonist]` |
| `name` | string | Yes | Entity display name | `"Lord Aldric Karath"` |
| `aliases` | array | Yes | Alternative names/titles | `["The Iron Duke", "Aldric"]` |
| `status` | string | Yes | Completion state | `draft`, `in-progress`, `complete` |
| `image` | string | Yes | Image filename or empty | `"[[Lord Aldric.png]]"` or `""` |

### Status Values

| Value | Description |
|-------|-------------|
| `draft` | Initial creation, minimal content |
| `in-progress` | Actively being developed |
| `complete` | Fully fleshed out, ready for use |

---

## Character Templates

### All Character Types
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `species` | string | Yes | D&D 5e 2024 species | `"Human"`, `"Elf"`, `"Dwarf"` |
| `gender` | string | Yes | Character gender | `"Male"`, `"Female"`, `"Non-binary"` |
| `age` | string | Yes | Age or age descriptor | `"45"` or `"Middle-aged"` |
| `alignment` | string | Yes | D&D alignment | `"Lawful Good"`, `"Chaotic Neutral"` |
| `occupation` | string | Yes | Primary role/job | `"Knight Commander"` |
| `location` | string | Yes | Current location | `"[[Thornhaven]]"` |

### Stat Block Fields (Protagonist, Antagonist, Support)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `level` | number | Conditional | Character level (PC-style) |
| `challenge_rating` | string | Conditional | CR (NPC/monster-style) |
| `class` | string | Conditional | D&D class (if level-based) |
| `hit_points` | number | Yes | Total HP |
| `armor_class` | number | Yes | AC value |
| `speed` | string | Yes | Movement speeds | `"30 ft."` |
| `strength` | number | Yes | STR score (1-30) |
| `dexterity` | number | Yes | DEX score (1-30) |
| `constitution` | number | Yes | CON score (1-30) |
| `intelligence` | number | Yes | INT score (1-30) |
| `wisdom` | number | Yes | WIS score (1-30) |
| `charisma` | number | Yes | CHA score (1-30) |
| `saving_throws` | string | No | Proficient saves | `"CON +5, WIS +3"` |
| `skills` | string | No | Skill proficiencies | `"Perception +5, Stealth +4"` |
| `damage_resistances` | string | No | Damage resistances |
| `damage_immunities` | string | No | Damage immunities |
| `condition_immunities` | string | No | Condition immunities |
| `senses` | string | No | Special senses | `"Darkvision 60 ft."` |
| `languages` | string | Yes | Known languages | `"Common, Elvish"` |

> [!important] Level vs CR
> Use **level** for PC-style characters with class features.
> Use **challenge_rating** for NPC/monster-style stat blocks.
> Never fill both fields.

### Familiar Template
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `creature_type` | string | Yes | D&D creature type | `"Fey"`, `"Fiend"`, `"Celestial"` |
| `size` | string | Yes | Creature size | `"Tiny"`, `"Small"` |
| `bonded_to` | string | Yes | Master entity link | `"[[Wizard Name]]"` |

### Divine Servant Template
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `creature_type` | string | Yes | Usually `"Celestial"` or `"Fiend"` |
| `divine_patron` | string | Yes | Deity link | `"[[Pelor]]"` |
| `divine_rank` | string | Yes | Servant hierarchy | `"Herald"`, `"Exarch"` |

---

## Settlement Templates

### Common Settlement Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `population` | string | Yes | Population range | `"5,000-10,000"` |
| `government` | string | Yes | Government type | `"Monarchy"`, `"Council"` |
| `ruler` | string | No | Ruler entity link | `"[[Duke Harlan]]"` |
| `region` | string | Yes | Parent geography | `"[[Thornwood Region]]"` |
| `economy` | string | No | Primary industries | `"Trade, Mining"` |
| `defenses` | string | No | Defensive features | `"Stone walls, militia"` |

### Village/Town/City
| Field | Type | Description |
|-------|------|-------------|
| `size` | string | `"Village"`, `"Town"`, `"City"` |
| `wealth` | string | Economic status: `"Poor"`, `"Modest"`, `"Wealthy"`, `"Prosperous"` |

### Stronghold
| Field | Type | Description |
|-------|------|-------------|
| `fortification_type` | string | `"Castle"`, `"Keep"`, `"Fortress"`, `"Citadel"` |
| `garrison_size` | string | Military presence |
| `strategic_value` | string | Why it matters |

### Tavern/Shop/Temple/Library
| Field | Type | Description |
|-------|------|-------------|
| `establishment_type` | string | Specific type |
| `owner` | string | Owner entity link |
| `parent_settlement` | string | Location link |
| `specialty` | string | What it's known for |

### Bastion (D&D 5e 2024)
| Field | Type | Description |
|-------|------|-------------|
| `bastion_level` | number | 1-20 |
| `bastion_points_total` | number | Total BP accumulated |
| `bastion_points_spent` | number | BP spent on facilities |
| `facilities` | array | List of facility objects |
| `hirelings` | array | List of hireling objects |
| `hireling_morale` | string | `"Loyal"`, `"Content"`, `"Disgruntled"` |

---

## Organization Templates

### Common Organization Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `organization_type` | string | Yes | Category | `"Guild"`, `"Government"`, etc. |
| `headquarters` | string | Yes | Location link | `"[[Guildhouse]]"` |
| `leader` | string | No | Leader entity link |
| `founded` | string | No | Founding date/era |
| `membership_size` | string | No | Member count | `"500+"` |
| `alignment` | string | No | Organizational alignment |
| `symbol` | string | No | Emblem description |
| `motto` | string | No | Organization motto |

### Government
| Field | Type | Description |
|-------|------|-------------|
| `government_type` | string | `"Monarchy"`, `"Republic"`, `"Theocracy"` |
| `territory` | string | Controlled regions |
| `capital` | string | Capital settlement link |

### Military
| Field | Type | Description |
|-------|------|-------------|
| `military_branch` | string | `"Army"`, `"Navy"`, `"Guard"` |
| `strength` | string | Force size |
| `commander` | string | Commander link |
| `parent_government` | string | Governing entity |

### Cult
| Field | Type | Description |
|-------|------|-------------|
| `deity` | string | Worshipped entity link |
| `secrecy_level` | string | `"Open"`, `"Hidden"`, `"Secret"` |
| `goals` | string | Cult objectives |

---

## Geography Templates

### Common Geography Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `geography_type` | string | Yes | `"Continent"`, `"Region"`, `"Forest"`, etc. |
| `climate` | string | Yes | `"Temperate"`, `"Tropical"`, `"Arctic"` |
| `terrain` | string | Yes | Primary terrain features |
| `parent_geography` | string | Conditional | Parent region link |
| `notable_features` | string | No | Key landmarks |

### Region-Specific
| Field | Type | Description |
|-------|------|-------------|
| `area` | string | Size description |
| `resources` | string | Natural resources |
| `hazards` | string | Environmental dangers |
| `settlements` | string | Major settlements |

### Dungeon
| Field | Type | Description |
|-------|------|-------------|
| `dungeon_type` | string | `"Tomb"`, `"Lair"`, `"Ruins"`, `"Natural"` |
| `levels` | number | Number of levels |
| `challenge_tier` | string | `"Tier 1"` (1-4), `"Tier 2"` (5-10), etc. |
| `current_occupants` | string | Who/what lives there |
| `original_purpose` | string | Why it was built |

---

## Item Templates

### Common Item Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `item_type` | string | Yes | `"Weapon"`, `"Armor"`, `"Wondrous"`, etc. |
| `rarity` | string | Yes | `"Common"`, `"Uncommon"`, `"Rare"`, `"Very Rare"`, `"Legendary"`, `"Artifact"` |
| `attunement` | boolean | Yes | Requires attunement? |
| `attunement_requirements` | string | No | Who can attune | `"spellcaster"`, `"paladin"` |
| `value` | string | No | GP value |

### Weapon
| Field | Type | Description |
|-------|------|-------------|
| `weapon_type` | string | `"Martial Melee"`, `"Simple Ranged"`, etc. |
| `damage` | string | `"1d8 slashing"` |
| `properties` | string | `"Versatile (1d10)"`, `"Finesse"` |
| `bonus` | string | `"+1"`, `"+2"`, `"+3"` |

### Armor
| Field | Type | Description |
|-------|------|-------------|
| `armor_type` | string | `"Light"`, `"Medium"`, `"Heavy"`, `"Shield"` |
| `base_ac` | number | Base AC value |
| `bonus` | string | Enhancement bonus |
| `stealth_disadvantage` | boolean | Causes stealth disadvantage? |

### Artifact
| Field | Type | Description |
|-------|------|-------------|
| `creator` | string | Creator entity link |
| `age` | string | When created |
| `destruction_conditions` | string | How to destroy it |

---

## Creature Templates

### Common Creature Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `creature_type` | string | Yes | D&D type | `"Beast"`, `"Monstrosity"`, `"Undead"` |
| `size` | string | Yes | `"Tiny"` through `"Gargantuan"` |
| `alignment` | string | Yes | Typical alignment |
| `challenge_rating` | string | Yes | CR value |
| `habitat` | string | Yes | Where found |

### Species (Playable)
| Field | Type | Description |
|-------|------|-------------|
| `species_type` | string | `"Humanoid"` usually |
| `size` | string | `"Small"`, `"Medium"` |
| `speed` | string | Base speed |
| `lifespan` | string | Average lifespan |
| `traits` | array | Racial traits |

---

## History Templates

### Common History Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date` | string | Yes | When it occurred |
| `era` | string | No | Parent age link |
| `location` | string | Yes | Where it happened |
| `participants` | string | No | Key figures involved |

### Age
| Field | Type | Description |
|-------|------|-------------|
| `start_date` | string | Beginning |
| `end_date` | string | Ending (or "present") |
| `defining_events` | string | Major events |

### War/Battle
| Field | Type | Description |
|-------|------|-------------|
| `combatants` | string | Opposing sides |
| `outcome` | string | Result |
| `casualties` | string | Loss summary |

---

## Concept Templates

### Deity
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domains` | array | Yes | D&D domains | `["Life", "Light"]` |
| `alignment` | string | Yes | Deity alignment |
| `symbol` | string | Yes | Holy symbol |
| `pantheon` | string | No | Parent pantheon link |
| `worshippers` | string | No | Typical followers |

### Magic System
| Field | Type | Description |
|-------|------|-------------|
| `magic_type` | string | Type of magic |
| `source` | string | Where power comes from |
| `limitations` | string | Restrictions |
| `practitioners` | string | Who uses it |

---

## Encounter Templates

### Combat/Social/Exploration
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `encounter_type` | string | Yes | `"Combat"`, `"Social"`, `"Exploration"` |
| `difficulty` | string | Yes | `"Easy"`, `"Medium"`, `"Hard"`, `"Deadly"` |
| `party_level` | string | Yes | Intended level range |
| `location` | string | Yes | Where it occurs |
| `creatures` | array | Conditional | Enemies (combat) |
| `npcs` | array | Conditional | NPCs (social) |
| `hazards` | array | Conditional | Hazards (exploration) |

### Trap
| Field | Type | Description |
|-------|------|-------------|
| `trap_type` | string | `"Mechanical"`, `"Magical"` |
| `trigger` | string | What activates it |
| `effect` | string | What happens |
| `detection_dc` | number | DC to spot |
| `disarm_dc` | number | DC to disable |
| `damage` | string | Damage dealt |

---

## Validation Rules

### Required Field Checks
1. All universal fields must be present
2. Type-specific required fields must be filled
3. `status` must be a valid value
4. Wikilinks must use correct `[[Entity Name]]` syntax

### Conditional Field Logic
| If Field | Then Required |
|----------|---------------|
| `level` filled | Leave `challenge_rating` blank |
| `challenge_rating` filled | Leave `level` blank |
| `attunement: true` | Consider `attunement_requirements` |
| `parent_geography` | Must link to valid geography entity |

### Numeric Ranges
| Field | Valid Range |
|-------|-------------|
| Ability scores | 1-30 |
| Level | 1-20 |
| CR | 0, 1/8, 1/4, 1/2, 1-30 |
| Armor Class | 5-30 |
| Bastion Level | 1-20 |

---

## YAML Syntax Reminders

### Arrays
```yaml
tags:
  - character
  - protagonist
aliases: ["The Iron Duke", "Lord Aldric"]
```

### Strings with Special Characters
```yaml
name: "Lord Aldric 'The Brave' Karath"  # Use quotes
motto: "Through fire, we forge"          # Colons need quotes
```

### Wikilinks in YAML
```yaml
location: "[[Thornhaven]]"    # Always quote wikilinks
ruler: "[[Duke Harlan]]"
```

### Empty Values
```yaml
image: ""           # Empty string for unfilled
aliases: []         # Empty array
damage_resistances: # Leave blank (null)
```

---

## Integration with Skills

This reference is used by:
- `/validate-template` - Checks required fields
- `/audit-world` - Validates YAML consistency
- `/create-entity` - Generates correct frontmatter
- `/populate-entity` - Ensures proper linking
