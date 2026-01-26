---
tags:
  - reference
  - dnd-5e-2024
  - validation
  - mechanics
status: complete
---

# D&D 5e 2024 Stat Block Validation

> [!info] Validation Checklist
> Use this reference when generating creatures, NPCs, or characters to ensure mechanical accuracy and D&D 5e 2024 compliance.

## Challenge Rating & Experience Points

The Challenge Rating (CR) must match the expected XP reward. Use this table to verify alignment.

| CR | XP | Prof Bonus | Suggested AC | Suggested HP | Suggested Attack | Suggested Damage/Round |
|----|-----|------------|--------------|--------------|------------------|----------------------|
| 0 | 0 or 10 | +2 | 10-13 | 1-6 | +3 | 0-1 |
| 1/8 | 25 | +2 | 13 | 7-35 | +3 | 2-3 |
| 1/4 | 50 | +2 | 13 | 36-49 | +3 | 4-5 |
| 1/2 | 100 | +2 | 13 | 50-70 | +3 | 6-8 |
| 1 | 200 | +2 | 13 | 71-85 | +3 | 9-14 |
| 2 | 450 | +2 | 13 | 86-100 | +3 | 15-20 |
| 3 | 700 | +2 | 13 | 101-115 | +4 | 21-26 |
| 4 | 1,100 | +2 | 14 | 116-130 | +5 | 27-32 |
| 5 | 1,800 | +3 | 15 | 131-145 | +6 | 33-38 |
| 6 | 2,300 | +3 | 15 | 146-160 | +6 | 39-44 |
| 7 | 2,900 | +3 | 15 | 161-175 | +6 | 45-50 |
| 8 | 3,900 | +3 | 16 | 176-190 | +7 | 51-56 |
| 9 | 5,000 | +4 | 16 | 191-205 | +7 | 57-62 |
| 10 | 5,900 | +4 | 17 | 206-220 | +7 | 63-68 |
| 11 | 7,200 | +4 | 17 | 221-235 | +8 | 69-74 |
| 12 | 8,400 | +4 | 17 | 236-250 | +8 | 75-80 |
| 13 | 10,000 | +5 | 18 | 251-265 | +8 | 81-86 |
| 14 | 11,500 | +5 | 18 | 266-280 | +8 | 87-92 |
| 15 | 13,000 | +5 | 18 | 281-295 | +8 | 93-98 |
| 16 | 15,000 | +5 | 18 | 296-310 | +9 | 99-104 |
| 17 | 18,000 | +6 | 19 | 311-325 | +10 | 105-110 |
| 18 | 20,000 | +6 | 19 | 326-340 | +10 | 111-116 |
| 19 | 22,000 | +6 | 19 | 341-355 | +10 | 117-122 |
| 20 | 25,000 | +6 | 19 | 356-400 | +10 | 123-140 |
| 21 | 33,000 | +7 | 19 | 401-445 | +11 | 141-158 |
| 22 | 41,000 | +7 | 19 | 446-490 | +11 | 159-176 |
| 23 | 50,000 | +7 | 19 | 491-535 | +11 | 177-194 |
| 24 | 62,000 | +7 | 19 | 536-580 | +12 | 195-212 |
| 25 | 75,000 | +8 | 19 | 581-625 | +12 | 213-230 |
| 26 | 90,000 | +8 | 19 | 626-670 | +12 | 231-248 |
| 27 | 105,000 | +8 | 19 | 671-715 | +13 | 249-266 |
| 28 | 120,000 | +8 | 19 | 716-760 | +13 | 267-284 |
| 29 | 135,000 | +9 | 19 | 761-805 | +13 | 285-302 |
| 30 | 155,000 | +9 | 19 | 806-850 | +14 | 303-320 |

---

## Proficiency Bonus by Level/CR

| Level/CR | Proficiency Bonus |
|----------|-------------------|
| 1-4 | +2 |
| 5-8 | +3 |
| 9-12 | +4 |
| 13-16 | +5 |
| 17-20 | +6 |
| 21-24 | +7 |
| 25-28 | +8 |
| 29-30 | +9 |

---

## Ability Score Calculations

### Standard Array
For balanced characters: **15, 14, 13, 12, 10, 8**

### Point Buy (27 points)

| Score | Modifier | Point Cost |
|-------|----------|------------|
| 8 | -1 | 0 |
| 9 | -1 | 1 |
| 10 | +0 | 2 |
| 11 | +0 | 3 |
| 12 | +1 | 4 |
| 13 | +1 | 5 |
| 14 | +2 | 7 |
| 15 | +2 | 9 |

### Modifier Calculation
```
Modifier = floor((Score - 10) / 2)
```

| Score | Modifier |
|-------|----------|
| 1 | -5 |
| 2-3 | -4 |
| 4-5 | -3 |
| 6-7 | -2 |
| 8-9 | -1 |
| 10-11 | +0 |
| 12-13 | +1 |
| 14-15 | +2 |
| 16-17 | +3 |
| 18-19 | +4 |
| 20-21 | +5 |
| 22-23 | +6 |
| 24-25 | +7 |
| 26-27 | +8 |
| 28-29 | +9 |
| 30 | +10 |

---

## Combat Calculations

### Attack Bonus
```
Attack Bonus = Proficiency Bonus + Ability Modifier
```
- **Melee weapons:** Use STR modifier (or DEX if finesse)
- **Ranged weapons:** Use DEX modifier (or STR if thrown)
- **Spell attacks:** Use spellcasting ability modifier

### Damage
```
Average Damage = (dice count × (die size + 1) / 2) + modifier
```

| Die | Average |
|-----|---------|
| d4 | 2.5 |
| d6 | 3.5 |
| d8 | 4.5 |
| d10 | 5.5 |
| d12 | 6.5 |

**Example:** 2d6+3 = (2 × 3.5) + 3 = 10 average damage

### Spell Save DC
```
Spell Save DC = 8 + Proficiency Bonus + Spellcasting Ability Modifier
```

### Saving Throws
```
Saving Throw Bonus = Ability Modifier + Proficiency Bonus (if proficient)
```

---

## Armor Class Calculations

### Unarmored
```
AC = 10 + DEX modifier
```

### Light Armor

| Armor | Base AC | Formula |
|-------|---------|---------|
| Padded | 11 | 11 + DEX mod |
| Leather | 11 | 11 + DEX mod |
| Studded Leather | 12 | 12 + DEX mod |

### Medium Armor

| Armor | Base AC | Formula |
|-------|---------|---------|
| Hide | 12 | 12 + DEX mod (max 2) |
| Chain Shirt | 13 | 13 + DEX mod (max 2) |
| Scale Mail | 14 | 14 + DEX mod (max 2) |
| Breastplate | 14 | 14 + DEX mod (max 2) |
| Half Plate | 15 | 15 + DEX mod (max 2) |

### Heavy Armor

| Armor | AC | STR Required |
|-------|-----|--------------|
| Ring Mail | 14 | - |
| Chain Mail | 16 | STR 13 |
| Splint | 17 | STR 15 |
| Plate | 18 | STR 15 |

### Shield
```
+2 AC
```

### Natural Armor (Monsters)
```
AC = 10 + DEX modifier + Natural Armor Bonus
```
Or use a fixed value based on creature concept.

### Unarmored Defense (Classes)
- **Barbarian:** 10 + DEX mod + CON mod
- **Monk:** 10 + DEX mod + WIS mod

---

## Hit Point Calculations

### Characters
```
Level 1: Hit Die Maximum + CON modifier
Level 2+: (Hit Die Average or Roll) + CON modifier per level
```

| Class | Hit Die | Average |
|-------|---------|---------|
| Sorcerer, Wizard | d6 | 4 |
| Bard, Cleric, Druid, Monk, Rogue, Warlock | d8 | 5 |
| Fighter, Paladin, Ranger | d10 | 6 |
| Barbarian | d12 | 7 |

**Example:** Level 5 Fighter with +2 CON
```
Level 1: 10 (d10 max) + 2 = 12
Level 2-5: 4 × (6 + 2) = 32
Total: 12 + 32 = 44 HP
```

### Monsters
```
HP = (Hit Dice count × Hit Die average) + (Hit Dice count × CON modifier)
```

| Size | Hit Die |
|------|---------|
| Tiny | d4 |
| Small | d6 |
| Medium | d8 |
| Large | d10 |
| Huge | d12 |
| Gargantuan | d20 |

**Example:** Large creature with 8d10 and +3 CON
```
HP = (8 × 5.5) + (8 × 3) = 44 + 24 = 68 (8d10+24)
```

---

## Legendary & Mythic Features

### Legendary Resistance
Creatures CR 5+ should consider having Legendary Resistance:
```
Legendary Resistance (3/Day): If the creature fails a saving throw,
it can choose to succeed instead.
```

| CR Range | Recommended Uses |
|----------|-----------------|
| CR 5-10 | 1-2/day |
| CR 11-16 | 2-3/day |
| CR 17-20 | 3/day |
| CR 21+ | 3-5/day |

### Legendary Actions
For boss-tier creatures (CR 5+):
```
The creature can take 3 legendary actions, choosing from the options below.
Only one legendary action can be used at a time and only at the end of
another creature's turn. Spent legendary actions are regained at the start
of the creature's turn.
```

**Common Legendary Actions:**
- **Detect:** Make a Perception check (0 actions)
- **Move:** Move up to half speed without provoking (1 action)
- **Attack:** Make one weapon attack (1-2 actions)
- **Special:** Use a unique ability (2-3 actions)

### Lair Actions
For creatures with established lairs:
```
On initiative count 20 (losing initiative ties), the creature can take a
lair action to cause one of the following effects:
```

### Mythic Actions (CR 20+)
For truly legendary creatures:
```
If the creature's mythic trait is active, it can use the options below
as legendary actions for 1 hour after using [Mythic Trait Name].
```

---

## Validation Checklist

### Before Finalizing a Creature

- [ ] **CR matches XP** from the CR/XP table
- [ ] **Proficiency bonus** matches CR/level
- [ ] **Ability modifiers** calculated correctly: (score - 10) / 2
- [ ] **Attack bonus** = Proficiency + Ability modifier
- [ ] **Damage** average is appropriate for CR
- [ ] **Spell Save DC** = 8 + Proficiency + Ability modifier
- [ ] **HP** matches hit dice formula with CON modifier
- [ ] **AC** calculated correctly for armor type
- [ ] **Saving throw proficiencies** match class or CR expectations

### For CR 5+ Creatures

- [ ] Consider **Legendary Resistance**
- [ ] Consider **Legendary Actions** (if boss-tier)
- [ ] Consider **Lair Actions** (if has lair)
- [ ] Consider **Multiattack** if appropriate

### For Spellcasters

- [ ] **Spell slots** match level
- [ ] **Spells known/prepared** appropriate for level
- [ ] **Concentration** tracked (only 1 concentration spell at a time)
- [ ] **Cantrip damage** scales with level (5th, 11th, 17th)

---

## Common Mistakes to Avoid

1. **Mismatched CR and XP** - Always verify the XP reward matches the CR
2. **Wrong proficiency bonus** - Use the table, not guessing
3. **Incorrect modifier math** - (Score - 10) / 2, round DOWN
4. **Forgetting CON to HP** - Every hit die gets CON modifier
5. **AC too high or low** - Should match the CR expectations
6. **Overpowered Multiattack** - Extra attacks multiply damage significantly
7. **Missing Legendary features** - High-CR boss creatures need them
8. **Spell slots mismatch** - Verify against class spell slot table

---

## Quick Reference: 5e 2024 Changes

### Species (formerly Race)
- Now called "Species" in 2024 rules
- Ability score increases come from Background, not species
- Species provides traits, size, speed, and proficiencies

### Backgrounds
- Now grant:
  - +2 to one ability score, +1 to another (or +1 to three)
  - Origin Feat (1st-level feat)
  - Skill proficiencies
  - Tool proficiency or language
  - Starting equipment

### Weapon Mastery
Classes can unlock Mastery properties on specific weapons:
- **Cleave** - Hit additional creature after reducing HP to 0
- **Graze** - Deal ability modifier damage on miss
- **Nick** - Extra attack with light weapon
- **Push** - Push target 10 feet
- **Sap** - Target has disadvantage on next attack
- **Slow** - Reduce target's speed by 10 feet
- **Topple** - Target must succeed on CON save or go prone
- **Vex** - Advantage on next attack against target

### Encounter Difficulty (2024)
| Difficulty | XP Budget per Character |
|------------|------------------------|
| Low | Level × 25 |
| Moderate | Level × 50 |
| High | Level × 75 |
