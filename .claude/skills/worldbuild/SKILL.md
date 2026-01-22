---
name: worldbuild
description: Interactive guided worldbuilding with questions, choices, and incremental creation. Creates worlds collaboratively through a question-and-answer workflow rather than automatic generation. Use when the user wants to thoughtfully build a world step-by-step.
argument-hint: "[world name] or 'resume'"
---

# Interactive Worldbuilding

Build a world collaboratively: $ARGUMENTS

## Overview

This skill guides users through worldbuilding via an interactive question-and-answer workflow. Unlike `/generate-world` which auto-generates 80-120 entities, this skill collaborates with the user at every step—asking questions, offering choices, and creating entities one at a time with approval.

**Philosophy:**
- Start small, expand gradually
- Establish tone and theme first—everything flows from core identity
- Ask the right questions at the right time
- Skip irrelevant sections based on user choices
- Show previews before creating; user approves each entity

**7 Interactive Phases:**
1. World Identity (tone, theme, inspirations)
2. Metaphysical Foundation (magic, gods, cosmology)
3. The Land (geography, terrain, scale)
4. Powers & People (nations, species, organizations)
5. History & Conflict (past events, current tensions)
6. Places of Interest (settlements, dungeons)
7. Characters & Details (NPCs, items, finishing touches)

---

## Instructions

### Getting Started

1. **Parse the argument:**
   - If `$ARGUMENTS` is a world name → start new worldbuilding session
   - If `$ARGUMENTS` is "resume" → check for existing sessions
   - If blank → ask user for world name or if they want to resume

2. **Check for existing session:**
   - Look for `Worlds/[World Name]/.worldbuild-state.json`
   - If found, offer to resume or start fresh

3. **Session state tracking:**
   Store decisions and progress in a state file at `Worlds/[World Name]/.worldbuild-state.json`:
   ```json
   {
     "version": "1.0",
     "world_name": "World Name",
     "current_phase": 1,
     "current_section": "tone",
     "completed_phases": [],
     "decisions": {},
     "entities_created": [],
     "skipped_sections": [],
     "last_updated": "ISO timestamp"
   }
   ```

4. **Commands available to user:**
   - `continue` - Proceed to next question
   - `back` - Go back one question
   - `skip` - Skip current section
   - `pause` - Save state and exit
   - `summary` - Show progress dashboard
   - `review [entity]` - View a created entity

---

## Phase 1: World Identity

**Goal:** Establish the core identity that everything else flows from.

### Step 1.1: World Name

Ask the user:
> "What would you like to name your world?"

If they're unsure, offer to suggest 3 names based on their tone preferences (ask tone first if needed).

### Step 1.2: Tone & Genre

Ask the user to choose or describe their tone:
> "What tone and genre are you going for? Choose one or describe your own:"
>
> 1. **Epic Fantasy** - Heroic adventures, good vs evil, grand scale (Lord of the Rings, Wheel of Time)
> 2. **Dark Fantasy** - Grim, morally gray, dangerous magic (Dark Souls, Warhammer, Witcher)
> 3. **Sword & Sorcery** - Personal stakes, adventure-focused, pulpy action (Conan, Fafhrd & Gray Mouser)
> 4. **Mythic Fantasy** - Gods walk among mortals, legendary heroes, fate and prophecy (Greek myths, Exalted)
> 5. **Low Fantasy** - Subtle magic, realistic politics, grounded world (Game of Thrones early seasons)
> 6. **Whimsical/Comedic** - Lighter tone, humor welcome, fantastical fun (Discworld, Princess Bride)
> 7. **Other** - Describe your vision

Store the answer in `decisions.tone`.

### Step 1.3: Inspirations

Ask:
> "What are 1-3 inspirations for this world? These could be books, games, TV shows, movies, historical periods, or even vibes/aesthetics."

Store in `decisions.inspirations` as an array.

### Step 1.4: Content Rating

Ask:
> "What content rating works for your world?"
>
> 1. **Family-friendly (PG)** - Suitable for all ages, violence is abstract, no mature themes
> 2. **Standard Fantasy (PG-13)** - Typical D&D fare, combat violence, mild dark themes
> 3. **Mature (R)** - Adult themes welcome, graphic content possible, darker elements explored

Store in `decisions.rating`.

### Step 1.5: Sensitive Topics (Optional)

Ask:
> "Are there any topics you'd like to avoid or handle carefully in this world? (This is optional but helps me create appropriate content.)"

Store in `decisions.avoid_topics` if provided.

### Step 1.6: The Hook

Ask:
> "In one sentence, what makes this world unique or interesting? What's the first thing you want players or readers to discover?"
>
> Examples:
> - "Magic is dying, and the last mages are hunted as heretics"
> - "Three empires vie for control of the only river in a vast desert"
> - "The gods went silent fifty years ago, and cults have risen in the void"

Store in `decisions.hook`.

### Step 1.7: Central Conflict

Ask:
> "What's the main problem, tension, or struggle in this world right now?"
>
> Examples:
> - War brewing between two kingdoms
> - An ancient evil awakening
> - Political intrigue as factions vie for a vacant throne
> - A plague with no cure spreading across the land
> - The barrier between worlds is weakening

Store in `decisions.central_conflict`.

### Step 1.8: Intended Feeling

Ask:
> "What do you want players/readers to feel when exploring this world?"
>
> Select 1-3:
> - Wonder and discovery
> - Dread and tension
> - Political intrigue
> - Heroic triumph
> - Mystery and secrets
> - Melancholy and loss
> - Adventure and excitement
> - Other (describe)

Store in `decisions.intended_feelings`.

### Step 1.9: Create World Overview

Based on all answers, create the World Overview document:

1. **Create directory structure:**
   ```
   Worlds/[World Name]/
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

2. **Generate World Overview.md** with YAML frontmatter and filled sections:
   - Use tone and inspirations to guide writing style
   - Fill Premise with the hook expanded to 2-3 sentences
   - Fill Tone & Themes from decisions
   - Fill Central Conflict
   - Leave placeholders for sections to be filled in later phases

3. **Show preview to user:**
   > "Here's your World Overview. Does this capture your vision? I can adjust anything before we save it."

4. **Save upon approval** to `Worlds/[World Name]/World Overview.md`

5. **Update state file** with Phase 1 complete.

### Step 1.10: Phase 1 Summary

Display progress dashboard:
```
=== WORLDBUILDING PROGRESS: [World Name] ===

Phase 1: World Identity      [COMPLETE]
Phase 2: Metaphysical        [NOT STARTED]
Phase 3: The Land            [NOT STARTED]
Phase 4: Powers & People     [NOT STARTED]
Phase 5: History & Conflict  [NOT STARTED]
Phase 6: Places of Interest  [NOT STARTED]
Phase 7: Characters & Details [NOT STARTED]

Entities Created: 1
- World Overview

Key Decisions:
- Tone: [tone]
- Rating: [rating]
- Hook: "[hook]"

Ready to continue to Phase 2: Metaphysical Foundation?
```

---

## Phase 2: Metaphysical Foundation

**Goal:** Establish magic, divinity, and the "rules" of reality.

### Section 2A: Magic

**Adaptive Skip:** If user indicated "no magic" or "low fantasy" in Phase 1, ask:
> "Your tone suggests a low-magic or no-magic world. Do you want to skip the magic section, or would you like to define what little magic exists?"

If skipping, add "magic" to `skipped_sections` and proceed to Section 2B.

#### Step 2A.1: Magic Prevalence

Ask:
> "How common is magic in this world?"
>
> 1. **None** - Magic doesn't exist (skip remaining magic questions)
> 2. **Extremely Rare** - One in 10,000 might have a spark; most never see real magic
> 3. **Rare** - Magic exists, but most people never personally encounter it
> 4. **Uncommon** - Known to exist, practitioners are notable figures
> 5. **Common** - Part of daily life for many; magical services available
> 6. **Pervasive** - Everything is touched by magic; it's woven into society

Store in `decisions.magic_level`. If "None", skip to Section 2B.

#### Step 2A.2: Magic Source

Ask:
> "Where does magical power come from?"
>
> 1. **Divine** - Granted by gods; tied to faith and worship
> 2. **Arcane** - Learned through study; academic and intellectual
> 3. **Primal** - From nature and elements; shamanic and druidic
> 4. **Innate** - Bloodlines and species; sorcerous and born with it
> 5. **External** - Drawn from planes, ley lines, or cosmic forces
> 6. **Multiple Sources** - Different types of magic from different sources

Store in `decisions.magic_source`.

#### Step 2A.3: Who Can Use Magic

Ask:
> "Who can use magic in this world?"
>
> 1. **Anyone with training** - Magic is a skill anyone can learn
> 2. **Only certain bloodlines** - Magical ability is inherited
> 3. **Only the chosen** - Gods, spirits, or fate select practitioners
> 4. **Varies by type** - Different magics have different requirements
> 5. **Natural talent required** - Must be born with potential, then train

Store in `decisions.magic_users`.

#### Step 2A.4: Costs and Risks

Ask:
> "What are the costs or risks of using magic? Select all that apply:"
>
> 1. **Physical exhaustion** - Magic drains the body; overuse can kill
> 2. **Mental strain** - Madness, corruption, or memory loss
> 3. **Attracts attention** - Using magic draws dangerous entities or authorities
> 4. **Environmental effects** - Magic warps the land, causes wild magic zones
> 5. **Social persecution** - Mages are feared, hunted, or controlled
> 6. **Material components** - Requires rare ingredients or sacrifices
> 7. **Minimal risk** - Magic is relatively safe when used properly

Store in `decisions.magic_costs` as array.

#### Step 2A.5: Society's View

Ask:
> "How does society view magic and its users?"
>
> 1. **Revered** - Mages are honored, sought after, hold high status
> 2. **Feared** - Magic is dangerous; users are treated with suspicion
> 3. **Regulated** - Magic is legal but controlled; guilds or governments oversee it
> 4. **Common/mundane** - Magic is normal, like any other profession
> 5. **Hunted** - Magic is outlawed; practitioners hide or flee

Store in `decisions.magic_society_view`.

#### Step 2A.6: Forbidden Magic

Ask:
> "Are there forbidden or dangerous forms of magic? Select any that exist:"
>
> 1. **Necromancy** - Death magic, raising the dead
> 2. **Blood magic** - Power from sacrifice and life force
> 3. **Mind control** - Dominating wills, memory manipulation
> 4. **Planar summoning** - Calling entities from other realms
> 5. **Time magic** - Manipulating the flow of time
> 6. **Soul magic** - Trapping, manipulating, or destroying souls
> 7. **None forbidden** - All magic is acceptable if used responsibly
> 8. **Other** - Describe

Store in `decisions.forbidden_magic` as array.

#### Step 2A.7: Magic Limitations

Ask:
> "What can magic NOT do in this world? This helps establish limits. Select any that apply:"
>
> 1. **Raise the truly dead** - Resurrection is impossible or extremely limited
> 2. **Time travel** - The past cannot be changed
> 3. **Create permanent life** - Golems fade, undead decay, true creation is impossible
> 4. **Read minds perfectly** - Thoughts can be hidden or protected
> 5. **Predict the future reliably** - Prophecy is vague or unreliable
> 6. **Teleport freely** - Long-distance travel still requires time
> 7. **Override free will permanently** - Domination always fades
> 8. **Other limitations** - Describe

Store in `decisions.magic_limitations` as array.

#### Step 2A.8: Magical Traditions

Ask:
> "Do you have any specific magical traditions, schools, or organizations in mind? (Optional - I can help develop these later)"

Store freeform in `decisions.magic_traditions` if provided.

#### Step 2A.9: Create Magic System Entity

Based on answers, generate a Magic System entity:

1. Read template: `Templates/Concepts/Magic System.md`
2. Fill all sections using decisions
3. Show preview to user:
   > "Here's the Magic System for [World Name]. Does this capture how magic works? I can adjust anything before saving."
4. Upon approval, save to `Worlds/[World Name]/Concepts/[Magic System Name].md`
5. Add to `entities_created` in state
6. Update World Overview with link to magic system

---

### Section 2B: The Divine

#### Step 2B.1: Do Gods Exist

Ask:
> "Do gods exist in this world?"
>
> 1. **Yes, definitely** - Gods are real and have power
> 2. **Unknown** - Something grants divine magic, but its nature is debated
> 3. **No** - Gods don't exist; "divine" magic is something else
> 4. **They existed** - Gods were real but are now dead, sleeping, or gone

Store in `decisions.gods_exist`.

If "No", ask if they want to skip divine sections and proceed to Section 2C.

#### Step 2B.2: Divine Interaction

Ask:
> "How do gods interact with mortals?"
>
> 1. **Absent/Unreachable** - Gods exist but don't answer; faith is blind
> 2. **Distant observers** - Gods watch but rarely intervene
> 3. **Subtle influence** - Gods work through signs, omens, dreams, and chosen agents
> 4. **Active through agents** - Gods empower clerics, send celestials, grant visions
> 5. **Directly meddlesome** - Gods walk the world, appear to mortals, take sides

Store in `decisions.divine_interaction`.

#### Step 2B.3: Divine Structure

Ask:
> "How are the gods organized?"
>
> 1. **Single deity** - One true god (monotheism)
> 2. **Dualistic pair** - Two opposing forces (light/dark, order/chaos)
> 3. **Small pantheon (5-8 gods)** - A tight circle of major deities
> 4. **Large pantheon (12+ gods)** - Many gods with varied domains
> 5. **Countless spirits** - Animistic; spirits in everything, no "major" gods
> 6. **Regional pantheons** - Different cultures worship different gods

Store in `decisions.divine_structure`.

#### Step 2B.4: Important Domains

If pantheon exists, ask:
> "What aspects of life do the most important gods represent? Select 4-6 primary domains:"
>
> - Life and Healing
> - Death and the Afterlife
> - Sun, Light, and Truth
> - Moon, Night, and Dreams
> - War, Battle, and Strength
> - Peace, Diplomacy, and Civilization
> - Nature, Animals, and the Wild
> - Storms, Sea, and Sky
> - Knowledge, Magic, and Secrets
> - Love, Beauty, and Art
> - Forge, Craft, and Creation
> - Trickery, Luck, and Thieves
> - Harvest, Fertility, and Plenty
> - Justice, Law, and Order

Store in `decisions.divine_domains` as array.

#### Step 2B.5: Divine Morality

Ask:
> "Do gods have alignments or clear morality, or are they beyond such concepts?"
>
> 1. **Clear alignments** - Good gods, evil gods, clear sides
> 2. **Complex morality** - Gods have virtues and flaws, not purely good or evil
> 3. **Beyond morality** - Gods represent forces of nature; morality doesn't apply
> 4. **Varies by god** - Some are clearly good/evil, others are ambiguous

Store in `decisions.divine_morality`.

#### Step 2B.6: Apotheosis

Ask:
> "Can mortals become gods? Has it happened?"
>
> 1. **Impossible** - The divine is unreachable by mortals
> 2. **Legendary** - It happened once in myth, none since
> 3. **Rare but possible** - A few mortals have achieved godhood through great deeds
> 4. **Achievable** - A path to godhood exists for those worthy

Store in `decisions.apotheosis`.

#### Step 2B.7: Divine Conflicts

Ask:
> "Are there conflicts among the gods?"
>
> 1. **Harmonious** - Gods cooperate or stay in their domains
> 2. **Rivalries** - Gods compete but rarely fight openly
> 3. **Active conflict** - Divine wars in heaven affect the mortal world
> 4. **Ancient wounds** - A past divine war left lasting scars
> 5. **No conflict** - Single deity or spirits don't compete

Store in `decisions.divine_conflicts`.

#### Step 2B.8: Specific Deities

Ask:
> "Do you have any specific deities already in mind? For each, tell me:
> - Name
> - Domain(s)
> - Personality or key trait
>
> (Optional - I can generate deities based on your domains if you prefer)"

Store in `decisions.planned_deities` if provided.

#### Step 2B.9: Create Pantheon Entity

If applicable, create a Pantheon entity:

1. Read template: `Templates/Concepts/Pantheon.md`
2. Fill based on decisions
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Concepts/[Pantheon Name].md`
5. Update state

#### Step 2B.10: Create Deity Entities

For each deity (planned or generated based on domains):

1. Read template: `Templates/Concepts/Deity.md`
2. Generate deity details using world tone and decisions
3. Show preview:
   > "Here's [Deity Name], god/goddess of [domains]. Does this work?"
4. Upon approval, save to `Worlds/[World Name]/Concepts/[Deity Name].md`
5. After each deity, ask: "Ready for the next deity, or would you like to adjust this one?"
6. Continue until all planned deities are created

---

### Section 2C: Cosmology (Optional)

#### Step 2C.1: Planes Matter?

Ask:
> "Do other planes of existence matter for your world? This includes things like the Feywild, Shadowfell, elemental planes, or divine realms."
>
> 1. **Not really** - The material world is what matters (skip this section)
> 2. **Background detail** - They exist but rarely come up
> 3. **Occasionally important** - Planar travel or influence happens sometimes
> 4. **Central to the setting** - Planes are a major part of the world

If "Not really", skip to Phase 2 Summary.

#### Step 2C.2: Which Planes Exist

Ask:
> "What planes exist in your cosmology? Select all that apply:"
>
> 1. **Material Plane** - The "normal" world (assumed to exist)
> 2. **Feywild/Faerie** - A wild, magical mirror realm of nature and emotion
> 3. **Shadowfell/Shadow Plane** - A dark, dreary echo realm of death and despair
> 4. **Elemental Planes** - Realms of pure fire, water, earth, air, etc.
> 5. **Divine Realms** - Heavens, paradises where gods dwell
> 6. **Infernal/Abyssal** - Hells, demon realms, places of evil
> 7. **Astral Plane** - The realm of thought, dreams, and travel between planes
> 8. **Ethereal Plane** - A ghostly overlap with the material world
> 9. **Other** - Describe unique planes

Store in `decisions.planes` as array.

#### Step 2C.3: Planar Interaction

Ask:
> "How do mortals interact with other planes?"
>
> 1. **They can't** - Other planes are unreachable
> 2. **Only through death** - Souls travel to afterlife planes
> 3. **Rare magic** - Powerful spells can breach the barriers
> 4. **Natural portals** - Some locations connect to other planes
> 5. **Regular travel** - Planar travel is known and sometimes common

Store in `decisions.planar_interaction`.

#### Step 2C.4: Afterlife

Ask:
> "What happens when people die?"
>
> 1. **Deity-specific afterlife** - Each god claims their followers
> 2. **Single destination** - All souls go to the same place
> 3. **Reincarnation** - Souls are reborn in new bodies
> 4. **Judgment** - Souls are judged and sorted by deeds
> 5. **Unknown** - What happens after death is a mystery
> 6. **Nothing** - Death is the end; no afterlife exists

Store in `decisions.afterlife`.

#### Step 2C.5: Create Plane Entities

For each important plane selected, offer to create entities:

> "Would you like me to detail [Plane Name] now, or save it for later?"

If yes:
1. Read template: `Templates/Concepts/Plane of Existence.md`
2. Generate based on decisions and tone
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Concepts/[Plane Name].md`

---

### Phase 2 Summary

Display progress:
```
=== WORLDBUILDING PROGRESS: [World Name] ===

Phase 1: World Identity      [COMPLETE]
Phase 2: Metaphysical        [COMPLETE]
Phase 3: The Land            [NOT STARTED]
...

Entities Created: X
- World Overview
- [Magic System Name] (Magic System)
- [Pantheon Name] (Pantheon)
- [Deity 1], [Deity 2], ... (Deities)
- [Plane Names] (Planes, if any)

Key Decisions:
- Magic: [level], [source]
- Gods: [structure], [interaction level]
- Planes: [list or "minimal"]

Ready to continue to Phase 3: The Land?
```

---

## Phase 3: The Land

**Goal:** Create the physical world geography.

### Section 3A: Scale & Focus

#### Step 3A.1: Detail Scope

Ask:
> "How much of the world do you want to detail now?"
>
> 1. **One city and surroundings** - A single urban hub and nearby areas
> 2. **One region/kingdom** - A focused area with several settlements
> 3. **One continent** - A full landmass with multiple regions
> 4. **Multiple continents** - Several major landmasses
> 5. **Entire world** - Comprehensive global geography

Store in `decisions.geographic_scale`.

**Adaptive Logic:**
- If "One city", skip continent/region questions, focus on city details in Phase 6
- If "One region", skip full continent, create one focused region

#### Step 3A.2: Adventure Location

Ask:
> "Where will most adventures take place?"
>
> 1. **Urban** - Primarily in a single large city
> 2. **Rural** - Countryside, wilderness, small villages
> 3. **Frontier** - Edge of civilization, unexplored lands
> 4. **Traveling** - Moving across many regions
> 5. **Underground** - Depths, Underdark, subterranean realms

Store in `decisions.adventure_focus`.

#### Step 3A.3: Exploration State

Ask:
> "Is the world fully explored or are there unknown regions?"
>
> 1. **Well-mapped** - Civilization knows what's out there
> 2. **Frontiers exist** - Known lands, but wilderness beyond
> 3. **Largely unexplored** - Most of the world is mysterious
> 4. **Mix** - Some areas known, others legendary or forbidden

Store in `decisions.exploration_state`.

#### Step 3A.4: Climate

Ask:
> "What's the general climate of the main region?"
>
> 1. **Temperate** - Four seasons, forests and farmland (European)
> 2. **Mediterranean** - Warm, dry summers; mild winters (Greek/Italian)
> 3. **Tropical** - Hot, humid, jungles and monsoons
> 4. **Arid/Desert** - Dry, hot days, cold nights, sparse water
> 5. **Arctic/Subarctic** - Cold, harsh winters, brief summers
> 6. **Varied** - Multiple climate zones in the main region

Store in `decisions.climate`.

#### Step 3A.5: Civilization Age

Ask:
> "How old is civilization in this world?"
>
> 1. **Ancient and crumbling** - Empires have risen and fallen many times
> 2. **Established empires** - Centuries-old nations, stable but evolving
> 3. **Young/frontier** - Civilization is new or recently expanded here
> 4. **Post-apocalyptic rebuilding** - A disaster destroyed the old world

Store in `decisions.civilization_age`.

#### Step 3A.6: Weird Geography

Ask:
> "Are there any unusual or magical geographic features? (Optional)"
>
> 1. **None** - Geography follows real-world logic
> 2. **Floating islands** - Landmasses in the sky
> 3. **Hollow world** - Interior lands beneath the surface
> 4. **Flat world** - The world is flat with edges
> 5. **Magical zones** - Areas where reality is warped
> 6. **Living geography** - Mountains move, forests migrate
> 7. **Other** - Describe

Store in `decisions.weird_geography` if any.

---

### Section 3B: Major Landmasses

**Skip if scale is "One city" or "One region" without broader context needed.**

#### Step 3B.1: Main Continent Name

Ask:
> "What's the main continent or landmass called where adventures take place?"

If user is unsure, offer 3 suggestions based on tone/inspirations.

#### Step 3B.2: Continent Size

Ask:
> "How large is [Continent Name]?"
>
> 1. **Island nation** - Small, isolated
> 2. **Small continent** - Like Australia
> 3. **Large continent** - Like Europe + North Africa
> 4. **Supercontinent** - Massive, like Pangaea

Store in `decisions.continent_size`.

#### Step 3B.3: Continent Character

Ask:
> "What's the general character of [Continent Name]? Describe it in a few words, or I can suggest something based on your tone."
>
> Examples:
> - "Temperate forests and rolling hills, dotted with ancient ruins"
> - "A harsh desert interior ringed by coastal city-states"
> - "Frozen wastes in the north, fertile south, mountains dividing them"

Store in `decisions.continent_character`.

#### Step 3B.4: Borders

Ask:
> "What borders [Continent Name]?"
>
> Select all that apply:
> 1. **Ocean(s)** - Name them if you like
> 2. **Other continents** - Connected by land bridges or nearby
> 3. **Impassable barriers** - Magical walls, endless storms, void
> 4. **Unknown** - What lies beyond is a mystery

Store in `decisions.continent_borders`.

#### Step 3B.5: Create Continent Entity

1. Read template: `Templates/Geography/Continent.md`
2. Generate based on all decisions
3. Show preview:
   > "Here's [Continent Name]. Does this geography work for your vision?"
4. Upon approval, save to `Worlds/[World Name]/Geography/[Continent Name].md`
5. Update state

#### Step 3B.6: Additional Continents

If scale is "Multiple continents" or "Entire world":
> "Do you want to create another continent now, or detail this one first and add more later?"

Repeat 3B.1-3B.5 for each additional continent.

---

### Section 3C: Regions & Terrain

#### Step 3C.1: Number of Regions

Ask:
> "How many distinct regions exist in [Continent/Area Name]?"
>
> For a focused game, 3-4 regions is usually enough. For a larger scope, 5-8 gives variety.

Store in `decisions.region_count`.

#### Step 3C.2: Define Each Region

For each region, ask:
> "Tell me about Region [X]:"
>
> 1. **Name:** What's this region called?
> 2. **Terrain:** What dominates? (Forests, mountains, plains, coast, desert, etc.)
> 3. **Control:** Who rules this region? (Can reference governments from Phase 4, or placeholder)
> 4. **Known for:** What is this region famous for? (Resources, culture, danger, history)
> 5. **Character:** In 1-2 sentences, what's the vibe?

Store each region in `decisions.regions` array.

#### Step 3C.3: Major Geographic Features

Ask:
> "What major geographic features define [Continent Name]? Select 3-5:"
>
> 1. **Mountain range** - Natural border, mining, dwarves, dragons
> 2. **Great river** - Trade artery, floods, river cultures
> 3. **Ancient forest** - Mysterious, elves, druids, dangers
> 4. **Vast desert** - Harsh, nomads, buried secrets
> 5. **Frozen wastes** - Northern/southern extremes, hardy folk
> 6. **Major coastline** - Maritime trade, pirates, sea monsters
> 7. **Island chain** - Scattered settlements, unique cultures
> 8. **Swamps/marshland** - Treacherous, hidden things, lizardfolk
> 9. **Rolling plains** - Agriculture, cavalry, horse lords
> 10. **Volcanic region** - Fire, destruction, rare minerals
> 11. **Underground realm** - Caves, Underdark, subterranean civilizations

Store in `decisions.geographic_features` as array.

#### Step 3C.4: Detail Each Feature

For each selected feature, ask:
> "Tell me about the [feature type]:"
>
> 1. **Name:** What's it called?
> 2. **Significance:** Why does it matter? (Strategic, sacred, dangerous, valuable)
> 3. **Dangers:** What threats exist here?
> 4. **Mysteries:** Any secrets or legends?
> 5. **Connection:** How does it relate to regions or the broader world?

#### Step 3C.5: Create Geographic Entities

For each region and feature, create entities:

1. Read appropriate template (e.g., `Templates/Geography/Region.md`, `Templates/Geography/Mountain Range.md`)
2. Generate content using decisions and maintaining consistency
3. Show preview for each:
   > "Here's [Feature Name]. Does this work?"
4. Upon approval, save to `Worlds/[World Name]/Geography/[Name].md`
5. Ensure wikilinks connect: Regions → Continent, Features → Regions

#### Step 3C.6: Travel and Resources

Ask:
> "A few quick questions about this land:"
>
> 1. **How do these features affect travel?** (Mountains block, rivers enable, etc.)
> 2. **Are there any cursed or magically altered regions?**
> 3. **What resources are valuable and where?** (Ore, timber, gems, magical materials)

Store answers for use in later entity creation.

---

### Phase 3 Summary

Display progress with map of created geography:
```
=== WORLDBUILDING PROGRESS: [World Name] ===

Phase 1: World Identity      [COMPLETE]
Phase 2: Metaphysical        [COMPLETE]
Phase 3: The Land            [COMPLETE]
...

Entities Created: X
...Geography:
- [Continent Name] (Continent)
- [Region 1], [Region 2], ... (Regions)
- [Mountain Range], [Forest], [River], ... (Features)

Key Decisions:
- Scale: [scope]
- Climate: [climate]
- Regions: [count]

Ready to continue to Phase 4: Powers & People?
```

---

## Phase 4: Powers & People

**Goal:** Establish who lives here and how they're organized.

### Section 4A: Peoples & Species

#### Step 4A.1: Intelligent Species

Ask:
> "What intelligent species inhabit this world?"
>
> 1. **Standard D&D races** - Humans, elves, dwarves, halflings, gnomes, plus common others
> 2. **Humans only** - Only humans exist (skip species questions)
> 3. **Custom selection** - I'll tell you exactly what exists
> 4. **Mix of standard and custom** - D&D basics plus unique species

Store in `decisions.species_approach`.

#### Step 4A.2: Standard Race Details (if applicable)

If using standard races:
> "For the standard races, tell me:"
>
> 1. **Which are common?** (Found everywhere)
> 2. **Which are rare?** (Exist but unusual)
> 3. **Which don't exist?** (Not in this world)
> 4. **Any with unusual roles?** (Dwarves are seafarers, elves are dying out, etc.)

Store in `decisions.race_distribution`.

#### Step 4A.3: Species Tensions

Ask:
> "How do different species relate to each other?"
>
> 1. **Peaceful coexistence** - Species live together harmoniously
> 2. **Historical conflicts** - Old wars, but peace now
> 3. **Active prejudice** - Racism/speciesism is a real problem
> 4. **Segregation** - Species stay in their own lands
> 5. **Integration varies** - Depends on region and culture

Store in `decisions.species_relations`.

#### Step 4A.4: Custom Species

If custom species desired:
> "Tell me about each unique species you want to create:"
>
> For each:
> 1. **Name:**
> 2. **Appearance:** (Brief description)
> 3. **Culture hook:** (One defining trait)
> 4. **Homeland:** (Where they live)
> 5. **Relationship:** (How they relate to other species)

For each custom species:
1. Read template: `Templates/Creatures/Species.md`
2. Generate full details
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Creatures/[Species Name].md`

#### Step 4A.5: Civilization Founders

Ask:
> "What species founded the oldest civilizations in this world?"

Store for historical context.

#### Step 4A.6: Monster Civilizations

Ask:
> "Do any traditionally 'monstrous' species have civilizations? (Orcs, goblins, giants, etc.)"
>
> 1. **No** - Monsters are monsters
> 2. **Yes, some** - Tell me which
> 3. **Most do** - Many "monsters" are just other cultures

Store in `decisions.monster_civilizations`.

---

### Section 4B: Nations & Governments

#### Step 4B.1: Number of Powers

Ask:
> "How many major powers exist in the main region?"
>
> 1. **1 unified** - A single empire or kingdom
> 2. **2-3 rivals** - A few major competing nations
> 3. **4-6 fragmented** - Multiple competing states
> 4. **Many city-states** - Dozens of independent cities
> 5. **No nations** - Tribal, anarchic, or post-collapse

Store in `decisions.power_count`.

#### Step 4B.2: Define Each Nation

For each major power, ask:
> "Tell me about [Nation X]:"
>
> 1. **Name:** What's this nation called?
> 2. **Government type:**
>    - Hereditary monarchy
>    - Elective monarchy
>    - Republic/democracy
>    - Theocracy (religious rule)
>    - Magocracy (mage rule)
>    - Merchant oligarchy
>    - Tribal confederation
>    - Military dictatorship
>    - Other
> 3. **Current ruler:** Name, title, brief personality (2-3 words)
> 4. **Known for:** What is this nation famous for?
> 5. **Greatest strength:**
> 6. **Greatest weakness:**
> 7. **Territory:** Which region(s) do they control?

#### Step 4B.3: International Relations

Ask:
> "How do these powers relate to each other? For each pair or group:"
>
> - Allied
> - Rivals
> - At war
> - Cold war
> - Trade partners
> - Vassal/overlord
> - Historical enemies, current peace
> - Complex (describe)

Store relationships in `decisions.nation_relations`.

#### Step 4B.4: Fallen Powers

Ask:
> "Are there any fallen empires or lost kingdoms in history that still affect the present?"

Store for historical entities.

#### Step 4B.5: Contested Borders

Ask:
> "Where are borders contested or unclear? Any rebel factions or independence movements?"

Store for conflict hooks.

#### Step 4B.6: Create Government Entities

For each nation:
1. Read template: `Templates/Organizations/Government.md`
2. Generate full details using all answers
3. Show preview:
   > "Here's [Nation Name]. Does this government work?"
4. Upon approval, save to `Worlds/[World Name]/Organizations/[Nation Name].md`
5. Update regions with political control connections

---

### Section 4C: Organizations & Factions

#### Step 4C.1: Organization Types

Ask:
> "What types of organizations are influential in this world? Select all that apply:"
>
> 1. **Adventurers' Guild** - Hires and supports adventuring parties
> 2. **Merchants' Guild** - Controls trade and commerce
> 3. **Thieves' Guild** - Organized crime, smuggling, information
> 4. **Assassins' Guild** - Professional killers, political tools
> 5. **Mage Academy** - Trains wizards, researches magic
> 6. **Religious Orders** - Militant or monastic servants of deities
> 7. **Knightly Orders** - Chivalric warriors, often noble-led
> 8. **Secret Societies** - Hidden groups with mysterious goals
> 9. **Criminal Syndicates** - Organized crime beyond thieves
> 10. **Mercenary Companies** - Soldiers for hire
> 11. **Bardic Colleges** - Performers, historians, spies
> 12. **Druid Circles** - Protectors of nature and the old ways

Store selections in `decisions.organization_types` as array.

#### Step 4C.2: Detail Each Organization

For each selected type, ask:
> "Tell me about the [organization type]:"
>
> 1. **Name:** What's it called?
> 2. **Headquarters:** Where is it based?
> 3. **Leader:** Who's in charge? (Name and brief description)
> 4. **Public purpose:** What do people think they do?
> 5. **Secret agenda:** Do they have hidden goals? (Optional)
> 6. **Influence:** How powerful are they? (Local, regional, international)
> 7. **Membership:** Who can join? How?

#### Step 4C.3: Organization Conflicts

Ask:
> "Are any organizations in conflict with each other?"

Store for plot hooks.

#### Step 4C.4: Create Organization Entities

For each organization:
1. Read appropriate template (Guild, Academy, Religious Order, etc.)
2. Generate content
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Organizations/[Name].md`

---

### Phase 4 Summary

Display:
```
=== WORLDBUILDING PROGRESS: [World Name] ===

Phase 1-3: [COMPLETE]
Phase 4: Powers & People     [COMPLETE]
...

Entities Created: X
...
Governments:
- [Nation 1], [Nation 2], ...

Organizations:
- [Org 1], [Org 2], ...

Species (if custom):
- [Species 1], ...

Key Decisions:
- Nations: [count] major powers
- Relations: [brief summary]
- Organizations: [list]

Ready to continue to Phase 5: History & Conflict?
```

---

## Phase 5: History & Conflict

**Goal:** Establish what happened and what tensions exist now.

### Section 5A: The Shape of History

#### Step 5A.1: Historical Divisions

Ask:
> "How do people in this world divide their history?"
>
> 1. **Two ages** - Before and after a defining event
> 2. **Three ages** - Ancient, middle, and modern eras
> 3. **Four+ eras** - Detailed chronological divisions
> 4. **Cyclical view** - History repeats in patterns

Store in `decisions.history_structure`.

#### Step 5A.2: Define Each Age

For each age, ask:
> "Tell me about [Age X]:"
>
> 1. **Name:** What's this era called?
> 2. **Duration:** How long ago, how long did it last?
> 3. **Defining trait:** What characterized this era?
> 4. **End:** What ended this age? (If not current)

Store in `decisions.ages` array.

#### Step 5A.3: Golden Age

Ask:
> "Was there a 'golden age'? What made it golden, and what ended it?"

Store if applicable.

#### Step 5A.4: Dark Age

Ask:
> "Was there a 'dark age' or catastrophe? What caused it and what were the consequences?"

Store if applicable.

#### Step 5A.5: Historical Reliability

Ask:
> "How reliable is historical knowledge in this world?"
>
> 1. **Well-documented** - Accurate records exist
> 2. **Oral traditions** - Stories passed down, some drift
> 3. **Lost to time** - Much is forgotten or destroyed
> 4. **Actively suppressed** - Someone is hiding the truth

Store in `decisions.history_reliability`.

---

### Section 5B: Defining Events

#### Step 5B.1: Major Events

Ask:
> "What 3-5 events most shaped the current world? Select from below or describe your own:"
>
> 1. **World-creation myth** - How the world began
> 2. **Great war** - A conflict that reshaped everything
> 3. **Cataclysm/disaster** - A catastrophe that changed the land
> 4. **Rise of empire** - A power unified or conquered much
> 5. **Fall of empire** - A great power collapsed
> 6. **Divine intervention** - Gods directly changed things
> 7. **Magical catastrophe** - Magic gone wrong, wild magic, etc.
> 8. **First contact** - Peoples met for the first time
> 9. **Plague/famine** - Death swept the land
> 10. **Discovery/invention** - Something changed everything
> 11. **Betrayal/tragedy** - A personal act had world consequences
> 12. **Prophecy given** - A foretelling shaped expectations

Store selections in `decisions.major_events`.

#### Step 5B.2: Detail Each Event

For each selected event, ask:
> "Tell me about [Event Type]:"
>
> 1. **Name:** What's it called?
> 2. **When:** Which age did this occur in?
> 3. **Cause:** What led to this?
> 4. **Key figures:** Who were the major players?
> 5. **Consequences:** What lasting effects did this have?
> 6. **Present impact:** Does this still affect the world today?

#### Step 5B.3: Mystery Events

Ask:
> "Are any historical events shrouded in mystery or misinformation? Things people believe that might not be true?"

Store for plot hooks.

#### Step 5B.4: Create History Entities

For ages and events:
1. Read templates: `Templates/History/Age.md`, `Templates/History/Event.md`, `Templates/History/War.md`, etc.
2. Generate content maintaining timeline consistency
3. Show preview for each, get approval
4. Save to `Worlds/[World Name]/History/[Name].md`
5. Ensure connections to other entities (nations involved, locations affected)

---

### Section 5C: Current Tensions

#### Step 5C.1: Central Conflict

Return to the central conflict from Phase 1 and expand:
> "You mentioned the central tension is: '[central_conflict]'. Let's develop this:"
>
> 1. **What started it?** What triggered this conflict?
> 2. **Who are the factions?** Who's on each side?
> 3. **What do they want?** What would victory look like for each side?

Store expanded details.

#### Step 5C.2: Consequences

Ask:
> "What would happen if nobody intervenes? What are the 'ticking clocks'—things that will happen if heroes don't act?"

Store for urgency hooks.

#### Step 5C.3: Adventure Opportunities

Ask:
> "What opportunities does this conflict create for adventurers?"
>
> Examples:
> - Both sides hiring mercenaries
> - Refugees needing protection
> - Artifacts that could tip the balance
> - Secrets that could end the conflict

Store for quest hooks.

#### Step 5C.4: Prophecies

Ask:
> "Are there any prophecies about how this ends? (Optional)"

If yes, offer to create a Prophecy entity.

#### Step 5C.5: Common View

Ask:
> "What does the common person think about the current situation?"

Store for NPC reactions.

#### Step 5C.6: Update Entities

- Update World Overview with historical timeline
- Add plot hooks to relevant existing entities
- Create Prophecy entity if applicable

---

### Phase 5 Summary

Display:
```
=== WORLDBUILDING PROGRESS: [World Name] ===

Phase 1-4: [COMPLETE]
Phase 5: History & Conflict  [COMPLETE]
...

Entities Created: X
...
History:
- [Age 1], [Age 2], [Age 3] (Ages)
- [Event 1], [Event 2], ... (Events)
- [War/Treaty/etc. if any]

Current Tensions:
- [Summary of central conflict]
- Ticking clocks: [list]

Ready to continue to Phase 6: Places of Interest?
```

---

## Phase 6: Places of Interest

**Goal:** Create the locations adventurers will visit.

### Section 6A: Major Settlements

#### Step 6A.1: Primary City

Ask:
> "What's the most important city in your main region? This is probably where adventures start or return to."
>
> 1. **Name:**
> 2. **Role:** Capital, trade hub, religious center, frontier outpost?
> 3. **Size:** Small city, large city, or metropolis?

#### Step 6A.2: City Details

For the primary city, ask:
> "Tell me more about [City Name]:"
>
> 1. **Known for:** What's this city famous for?
> 2. **Ruler:** Who's in charge? (Can link to government)
> 3. **Districts:** Name 2-3 distinctive neighborhoods and their character
> 4. **Unusual feature:** What's the most interesting or unusual thing?
> 5. **Problems:** What challenges does the city face?
> 6. **Secrets:** What does the city hide?

#### Step 6A.3: Create City Entity

1. Read template: `Templates/Settlements/City.md`
2. Generate comprehensive city details
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Settlements/[City Name].md`

#### Step 6A.4: Secondary Settlements

Ask:
> "How many secondary towns or villages matter for your adventures? For each, I'll need:
> - Name
> - Purpose (trade stop, mining town, fishing village, border post, etc.)
> - One notable feature"

For each:
1. Read appropriate template (Town or Village)
2. Generate content
3. Show preview, get approval
4. Save

#### Step 6A.5: Settlement Sub-Entities

For each major settlement, offer:
> "Would you like me to create details for [Settlement]?"
>
> 1. **Tavern** - A memorable inn where adventurers gather
> 2. **Shops** - Notable merchants and their stores
> 3. **Temple** - The main place of worship
> 4. **Skip for now** - Move on

If yes to any:
1. Read appropriate templates
2. Generate colorful establishments with personality
3. Show preview, get approval
4. Save with proper connections to parent settlement

---

### Section 6B: Strongholds & Fortifications

#### Step 6B.1: Military Locations

Ask:
> "Are there any important fortresses, castles, or military strongholds?"

If yes, for each:
> "Tell me about this stronghold:"
>
> 1. **Name:**
> 2. **Location:** Where is it?
> 3. **Controller:** Who holds it?
> 4. **Purpose:** What does it guard against?
> 5. **State:** Active garrison, ruined, contested?

Create Stronghold entities for each.

---

### Section 6C: Adventure Sites & Dungeons

#### Step 6C.1: Adventure Site Types

Ask:
> "What types of adventure sites exist in your world? Select all that interest you:"
>
> 1. **Ancient ruins** - Remnants of fallen civilizations
> 2. **Forgotten tombs** - Burial sites of the powerful dead
> 3. **Monster lairs** - Where dangerous creatures dwell
> 4. **Cursed locations** - Places tainted by dark magic
> 5. **Natural caves** - Underground networks, possibly inhabited
> 6. **Abandoned mines** - Dug too deep, found something bad
> 7. **Haunted places** - Ghosts, spirits, unfinished business
> 8. **Magical anomalies** - Wild magic zones, planar rifts
> 9. **Sunken temples** - Underwater or buried holy sites
> 10. **Forbidden libraries** - Repositories of dangerous knowledge

Store selections.

#### Step 6C.2: Detail Adventure Sites

For each type selected (or until user says enough), ask:
> "Tell me about a [adventure site type]:"
>
> 1. **Name:**
> 2. **Location:** Where is it?
> 3. **History:** What's its story?
> 4. **Dangers:** What threatens explorers?
> 5. **Treasures:** What might be found?
> 6. **Seekers:** Is anyone else looking for this place?
> 7. **Knowledge:** Is this site common knowledge, rumored, or secret?

#### Step 6C.3: Create Dungeon Entities

For each:
1. Read template: `Templates/Geography/Dungeon.md` or `Templates/Geography/Cave.md`
2. Generate detailed adventure site
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Geography/[Name].md`
5. Connect to nearby regions and relevant history

#### Step 6C.4: Most Dangerous Place

Ask:
> "What's the most dangerous place in the region? This might be an adventure site for higher levels or a place to avoid."

Store for world flavor and future development.

---

### Phase 6 Summary

Display:
```
=== WORLDBUILDING PROGRESS: [World Name] ===

Phase 1-5: [COMPLETE]
Phase 6: Places of Interest  [COMPLETE]
...

Entities Created: X
...
Settlements:
- [City Name] (City) with [Tavern], [Shops], [Temple]
- [Town 1], [Town 2], ... (Towns)
- [Village 1], ... (Villages)

Strongholds:
- [Fortress 1], ...

Adventure Sites:
- [Dungeon 1], [Cave 1], [Ruins 1], ...

Ready to continue to Phase 7: Characters & Details?
```

---

## Phase 7: Characters & Details

**Goal:** Populate the world with people and finishing touches.

### Section 7A: Rulers & Leaders

#### Step 7A.1: Detail Existing Rulers

For each government created in Phase 4, ask:
> "Let's detail the ruler of [Nation]:"
>
> 1. **Full name and titles:**
> 2. **Personality:** (2-3 words)
> 3. **Strength:** What are they good at?
> 4. **Flaw:** What's their fatal weakness?
> 5. **Public reputation:** What do people think of them?
> 6. **Private reality:** What's really going on?
> 7. **Key people:** Advisors, family, rivals?

#### Step 7A.2: Secret Alignments

Ask:
> "Are any rulers secretly villains or heroes? Any playing a different role than expected?"

Store for plot twists.

#### Step 7A.3: Succession Issues

Ask:
> "Any contested successions or problematic heirs?"

Store for political intrigue.

#### Step 7A.4: Create Leader Characters

For each ruler:
1. Read template: `Templates/Characters/Support Character.md`
2. Generate full character with stats, personality, secrets
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Characters/[Name].md`
5. Connect to government and settlement

---

### Section 7B: Quest-Givers & Allies

#### Step 7B.1: NPC Types

Ask:
> "What types of NPCs will give adventurers quests? Select all that apply:"
>
> 1. **Mysterious mentor** - Guides heroes with cryptic wisdom
> 2. **Desperate merchant** - Needs protection or retrieval
> 3. **Haunted noble** - Troubled by secrets or curses
> 4. **Religious figure** - Priest with divine missions
> 5. **Guild leader** - Faction head with jobs to offer
> 6. **Frontier sheriff** - Law in the wilderness
> 7. **Scholarly sage** - Seeker of knowledge
> 8. **Retired adventurer** - Knows the dangers firsthand
> 9. **Royal agent** - Works for the crown secretly
> 10. **Common folk** - Ordinary people in extraordinary trouble

#### Step 7B.2: Detail Quest-Givers

For each type selected, ask:
> "Tell me about the [NPC type]:"
>
> 1. **Name:**
> 2. **Description:** (Brief appearance and manner)
> 3. **Location:** Where are they found?
> 4. **Wants:** What do they need from adventurers?
> 5. **Offers:** What can they provide in return?
> 6. **Secret:** What do they hide?

#### Step 7B.3: Create NPC Entities

For each:
1. Read template: `Templates/Characters/Support Character.md`
2. Generate full NPC
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Characters/[Name].md`

---

### Section 7C: Villains & Antagonists

#### Step 7C.1: Main Villain

Ask:
> "Who is the main villain or antagonist of the current conflict?"
>
> 1. **Name and title:**
> 2. **What do they want?**
> 3. **Why do they want it?** (Motivation—what drives them?)
> 4. **What makes them dangerous?**
> 5. **What's their weakness?**
> 6. **Are they redeemable?**
> 7. **Where do they operate from?**

#### Step 7C.2: Secondary Villains

Ask:
> "Who are the secondary villains or lieutenants? Name 1-3:"

For each, get brief details.

#### Step 7C.3: Grey Area Antagonists

Ask:
> "Are there any 'grey area' antagonists? People who aren't evil but oppose the heroes?"

These make great complex characters.

#### Step 7C.4: Create Villain Entities

For main villain and key lieutenants:
1. Read template: `Templates/Characters/Antagonist.md`
2. Generate compelling villain
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Characters/[Name].md`
5. Connect to organizations, locations, history

---

### Section 7D: Legendary Items (Optional)

#### Step 7D.1: Artifacts Exist?

Ask:
> "Are there any legendary artifacts in this world? Items of great power and history?"

If no, skip to Section 7E.

#### Step 7D.2: Detail Artifacts

For each artifact, ask:
> "Tell me about this artifact:"
>
> 1. **Name:**
> 2. **What does it do?**
> 3. **Origin:** Where did it come from?
> 4. **Current location:** Where is it now?
> 5. **Seekers:** Who wants it?
> 6. **Curse:** Any dangerous properties?

#### Step 7D.3: Create Artifact Entities

For each:
1. Read template: `Templates/Items/Artifact.md`
2. Generate detailed artifact
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Items/[Name].md`

---

### Section 7E: Unique Creatures (Optional)

#### Step 7E.1: Unique Creatures?

Ask:
> "Are there any unique creatures specific to this world? Legendary monsters or special beasts?"

If no, skip to Section 7F.

#### Step 7E.2: Detail Creatures

For each creature, ask:
> "Tell me about this creature:"
>
> 1. **Name:**
> 2. **Description:** What does it look like?
> 3. **Habitat:** Where does it live?
> 4. **Danger:** What makes it threatening?
> 5. **Weakness:** How can it be defeated?
> 6. **Lore:** What do people believe about it?

#### Step 7E.3: Create Creature Entities

For each:
1. Read template: `Templates/Creatures/Monster.md` or appropriate type
2. Generate creature with full stat block if desired
3. Show preview, get approval
4. Save to `Worlds/[World Name]/Creatures/[Name].md`

---

### Section 7F: Daily Life & Culture (Optional but Recommended)

#### Step 7F.1: Calendar

Ask:
> "Would you like me to create a calendar for this world?"

If yes:
> "Tell me about the calendar:"
>
> 1. **Months:** How many? What are they called?
> 2. **Seasons:** How do seasons work?
> 3. **Holy days:** Any religious holidays? (Connect to deities)
> 4. **Secular holidays:** Harvest festivals, founding days, etc.?

Create Calendar entity.

#### Step 7F.2: Currency

Ask:
> "Would you like me to detail the currency system?"

If yes:
> "Tell me about money:"
>
> 1. **Standard currency:** What do people use? (Coins, trade goods)
> 2. **Denominations:** What are the coin types called?
> 3. **Regional variations:** Different currencies in different nations?
> 4. **Valuable goods:** What's valuable besides money?

Create Currency entity.

#### Step 7F.3: Languages

Ask:
> "Would you like me to create languages for this world?"

If yes:
> "Tell me about languages:"
>
> 1. **Common tongue:** What's the trade language called?
> 2. **Regional languages:** What do different peoples speak?
> 3. **Ancient languages:** Any dead languages for old texts?
> 4. **Magical languages:** Languages with power?

Create Language entities.

#### Step 7F.4: Quick Culture Questions

Ask briefly:
> "A few quick culture questions for flavor:"
>
> 1. **Work:** What do common people do for a living?
> 2. **Entertainment:** What do people do for fun?
> 3. **Food:** Any distinctive dishes or drinks?
> 4. **Travel:** How do people get around? How long does it take?

Store answers for flavor in existing entities.

---

### Section 7G: Final Review & Connections

#### Step 7G.1: Entity Summary

Display complete list of all entities created:
```
=== COMPLETE ENTITY LIST: [World Name] ===

World Overview: 1
Concepts: X (Pantheon, Deities, Magic System, etc.)
Geography: X (Continent, Regions, Features)
Organizations: X (Governments, Guilds, etc.)
Settlements: X (Cities, Towns, Villages, Taverns, etc.)
Characters: X (Rulers, NPCs, Villains)
History: X (Ages, Events)
Creatures: X (if any)
Items: X (if any)

TOTAL: X entities
```

#### Step 7G.2: Connection Audit

Review and report on connections:
> "Checking all wikilinks for completeness..."
>
> - Entities with fewer than 3 connections: [list]
> - Orphaned entities (no incoming links): [list]
> - Suggested connections to add: [list]

Offer to update entities with missing connections.

#### Step 7G.3: Gap Analysis

Check for missing elements:
> "Looking for gaps in your world..."
>
> - You have governments but no military organizations. Want to add those?
> - You have deities but no religious orders. Want to add those?
> - [Region X] has no settlements. Want to add some?
> - etc.

Offer to fill gaps.

#### Step 7G.4: Final World Overview Update

Update World Overview with:
- Complete entity links in Quick Reference
- Updated timeline
- All connections
- Adventure hooks summary

#### Step 7G.5: Next Steps

Suggest:
> "Your world [World Name] is ready! Here are some next steps:"
>
> 1. **Expand:** Entities that could use more detail: [list]
> 2. **Adventures:** Plot hooks ready to develop: [list]
> 3. **Characters:** NPCs that need more background: [list]
> 4. **Missing:** Things you might want to add later: [list]
>
> You can always come back with `/worldbuild resume` to continue building!

---

## Resumption Logic

When user invokes `/worldbuild resume` or `/worldbuild [existing world name]`:

1. Check for `Worlds/[World Name]/.worldbuild-state.json`

2. If found, display:
   ```
   === RESUMING: [World Name] ===

   Last session: Phase [X], Section [Y]
   Last question: "[question text]"
   Entities created: [count]

   Options:
   1. Continue where you left off
   2. Start from the beginning of Phase [X]
   3. Jump to a specific phase
   4. Review what's been created
   5. Start a new world instead
   ```

3. Load all decisions and continue from stored position

4. When displaying progress, mark completed sections clearly

---

## Adaptive Skip Logic

Track in state and automatically skip irrelevant sections:

| If user chose... | Skip... |
|------------------|---------|
| No magic | Magic System, Mage Academy, Magic Items, spell-related questions |
| Gods absent/don't exist | Pantheon, Deities, Divine Servants, Temples, Religious Orders |
| Humans only | Species creation, racial tensions, multiple language details |
| Single city scope | Continents, multiple regions, large-scale geography |
| Low fantasy tone | High magic questions, planar travel, direct divine intervention |

Always inform user when skipping:
> "Since you indicated [reason], I'll skip [section]. You can always add this later if needed."

---

## Naming Conventions Reference

When generating names for entities, consult these reference files:

| Reference File | Use For |
|----------------|---------|
| `Templates/Reference/D&D Species Naming Conventions.md` | Species-specific naming patterns (Dwarves, Elves, Halflings, Orcs, etc.) |
| `Templates/Reference/Tolkien Naming Conventions.md` | High fantasy linguistic patterns (Sindarin, Quenya, Khuzdul, etc.) |

### When to Apply

- **During entity generation:** Use naming patterns that match the entity's species, culture, or region
- **For settlements:** Name cities/towns using appropriate linguistic conventions for their dominant culture
- **For characters:** Match names to species (Dwarven names for dwarves, Elvish for elves, etc.)
- **For geography:** Use Tolkien patterns for rivers (-duin), mountains (-gor), forests (-taur), etc.

### Matching Names to Tone

| World Tone | Recommended Naming Style |
|------------|-------------------------|
| Epic Fantasy | Tolkien patterns (Sindarin/Quenya for elves, Norse-inspired for dwarves) |
| Dark Fantasy | Harsher variants, Black Speech influences for villains |
| Sword & Sorcery | Mixed cultural human names, simpler constructions |
| Mythic Fantasy | Quenya (formal/divine), culture-specific for mortals |
| Low Fantasy | Historical human naming patterns (Germanic, Celtic, Slavic) |
| Whimsical Fantasy | Halfling/Gnome patterns, playful constructions |

---

## Entity Creation Standards

When generating any entity:

1. **Read the template first** from `Templates/[Category]/[Type].md`
2. **Use all stored decisions** for consistency (tone, naming patterns, connections)
3. **Fill ALL sections** - don't leave placeholders
4. **Create wikilinks** to existing entities in Connections section
5. **Generate image prompts** based on the specific entity
6. **Match the tone** from Phase 1 decisions
7. **Show preview** and wait for user approval before saving
8. **Offer modifications** - "Would you like to change anything?"
9. **Save with proper formatting** - Title Case filename, proper YAML

---

## Progress Dashboard Format

After each completed phase or on `summary` command:

```
╔══════════════════════════════════════════════════════════════╗
║           WORLDBUILDING PROGRESS: [World Name]               ║
╠══════════════════════════════════════════════════════════════╣
║ Phase 1: World Identity      [COMPLETE]                      ║
║ Phase 2: Metaphysical        [COMPLETE]                      ║
║ Phase 3: The Land            [IN PROGRESS - 3C.2]            ║
║ Phase 4: Powers & People     [NOT STARTED]                   ║
║ Phase 5: History & Conflict  [NOT STARTED]                   ║
║ Phase 6: Places of Interest  [NOT STARTED]                   ║
║ Phase 7: Characters & Details [NOT STARTED]                  ║
╠══════════════════════════════════════════════════════════════╣
║ Entities Created: 15                                         ║
║ - Concepts: 7 (Pantheon, 5 Deities, Magic System)           ║
║ - Geography: 8 (Continent, 4 Regions, 3 Features)           ║
╠══════════════════════════════════════════════════════════════╣
║ Key Decisions:                                               ║
║ - Tone: Dark Fantasy                                         ║
║ - Magic: Rare, Divine-granted                                ║
║ - Gods: Active pantheon of 5                                 ║
║ - Scale: Single continent                                    ║
╠══════════════════════════════════════════════════════════════╣
║ Commands: continue | back | skip | pause | summary | review  ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Completion

When all 7 phases are complete:

```
╔══════════════════════════════════════════════════════════════╗
║              WORLDBUILDING COMPLETE: [World Name]            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Congratulations! Your world is ready for adventure.        ║
║                                                              ║
║  Total Entities Created: [X]                                 ║
║  Categories Covered: All 8                                   ║
║  Wikilinks Created: [Y]                                      ║
║                                                              ║
║  Location: Worlds/[World Name]/                              ║
║                                                              ║
║  Use these commands to continue developing:                  ║
║  - /create-entity [description] for [World Name]            ║
║  - /worldbuild resume to add more                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```
