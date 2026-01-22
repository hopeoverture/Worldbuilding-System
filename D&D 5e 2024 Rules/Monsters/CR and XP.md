# Challenge Rating and Experience Points

This reference provides the official D&D 5e (2024) Challenge Rating to Experience Points conversion table, along with guidelines for building and validating monster stat blocks.

## CR to XP Conversion Table

| CR | XP | Proficiency Bonus |
|----|-----|-------------------|
| 0 | 0 or 10 | +2 |
| 1/8 | 25 | +2 |
| 1/4 | 50 | +2 |
| 1/2 | 100 | +2 |
| 1 | 200 | +2 |
| 2 | 450 | +2 |
| 3 | 700 | +2 |
| 4 | 1,100 | +2 |
| 5 | 1,800 | +3 |
| 6 | 2,300 | +3 |
| 7 | 2,900 | +3 |
| 8 | 3,900 | +3 |
| 9 | 5,000 | +4 |
| 10 | 5,900 | +4 |
| 11 | 7,200 | +4 |
| 12 | 8,400 | +4 |
| 13 | 10,000 | +5 |
| 14 | 11,500 | +5 |
| 15 | 13,000 | +5 |
| 16 | 15,000 | +5 |
| 17 | 18,000 | +6 |
| 18 | 20,000 | +6 |
| 19 | 22,000 | +6 |
| 20 | 25,000 | +6 |
| 21 | 33,000 | +7 |
| 22 | 41,000 | +7 |
| 23 | 50,000 | +7 |
| 24 | 62,000 | +7 |
| 25 | 75,000 | +8 |
| 26 | 90,000 | +8 |
| 27 | 105,000 | +8 |
| 28 | 120,000 | +8 |
| 29 | 135,000 | +9 |
| 30 | 155,000 | +9 |

## Proficiency Bonus by Level (Characters)

| Level | Proficiency Bonus |
|-------|-------------------|
| 1-4 | +2 |
| 5-8 | +3 |
| 9-12 | +4 |
| 13-16 | +5 |
| 17-20 | +6 |

## Ability Score Modifiers

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

**Formula:** `modifier = floor((score - 10) / 2)`

## Hit Dice by Size

| Size | Hit Die | Average HP per Die |
|------|---------|-------------------|
| Tiny | d4 | 2.5 |
| Small | d6 | 3.5 |
| Medium | d8 | 4.5 |
| Large | d10 | 5.5 |
| Huge | d12 | 6.5 |
| Gargantuan | d20 | 10.5 |

## Hit Dice by Class

| Class | Hit Die | Average HP per Die |
|-------|---------|-------------------|
| Barbarian | d12 | 7 |
| Fighter | d10 | 6 |
| Paladin | d10 | 6 |
| Ranger | d10 | 6 |
| Bard | d8 | 5 |
| Cleric | d8 | 5 |
| Druid | d8 | 5 |
| Monk | d8 | 5 |
| Rogue | d8 | 5 |
| Warlock | d8 | 5 |
| Sorcerer | d6 | 4 |
| Wizard | d6 | 4 |

## HP Calculation Formulas

### Characters
```
HP = (hit_die_max + CON_mod) + ((level - 1) × (hit_die_avg + CON_mod))
```

**Example:** Level 5 Fighter with CON 16 (+3)
- First level: 10 (d10 max) + 3 (CON) = 13
- Levels 2-5: 4 × (6 + 3) = 36
- Total: 13 + 36 = **49 HP**

### Monsters
```
HP = (hit_dice_count × hit_die_avg) + (hit_dice_count × CON_mod)
```
Displayed as: `X (YdZ + W)` where:
- X = calculated average HP
- Y = number of hit dice
- Z = hit die type based on size
- W = total CON modifier bonus (Y × CON_mod)

**Example:** Large creature (d10), 5 hit dice, CON 14 (+2)
- Average: 5 × 5.5 = 27.5 (round to 27 or 28)
- CON bonus: 5 × 2 = 10
- Total: 27 + 10 = **37 HP**
- Displayed: **37 (5d10 + 10)**

## Attack Bonus Calculation

```
Attack Bonus = Proficiency Bonus + Ability Modifier
```

| Attack Type | Primary Ability |
|-------------|-----------------|
| Melee (standard) | Strength |
| Melee (finesse) | Strength OR Dexterity |
| Ranged | Dexterity |
| Thrown | Strength (or DEX if finesse) |
| Spell Attack | Spellcasting Ability |

## Spell Save DC Calculation

```
Spell Save DC = 8 + Proficiency Bonus + Spellcasting Ability Modifier
```

| Class | Spellcasting Ability |
|-------|---------------------|
| Bard | Charisma |
| Cleric | Wisdom |
| Druid | Wisdom |
| Paladin | Charisma |
| Ranger | Wisdom |
| Sorcerer | Charisma |
| Warlock | Charisma |
| Wizard | Intelligence |
| Artificer | Intelligence |

## Monster CR Guidelines

### Defensive CR (based on HP and AC)

| CR | HP Range | Expected AC |
|----|----------|-------------|
| 0 | 1-6 | ≤13 |
| 1/8 | 7-35 | 13 |
| 1/4 | 36-49 | 13 |
| 1/2 | 50-70 | 13 |
| 1 | 71-85 | 13 |
| 2 | 86-100 | 13 |
| 3 | 101-115 | 13 |
| 4 | 116-130 | 14 |
| 5 | 131-145 | 15 |
| 6 | 146-160 | 15 |
| 7 | 161-175 | 15 |
| 8 | 176-190 | 16 |
| 9 | 191-205 | 16 |
| 10 | 206-220 | 17 |
| 11 | 221-235 | 17 |
| 12 | 236-250 | 17 |
| 13 | 251-265 | 18 |
| 14 | 266-280 | 18 |
| 15 | 281-295 | 18 |
| 16 | 296-310 | 18 |
| 17 | 311-325 | 19 |
| 18 | 326-340 | 19 |
| 19 | 341-355 | 19 |
| 20 | 356-400 | 19 |

### Offensive CR (based on Damage per Round and Attack Bonus)

| CR | Damage/Round | Attack Bonus | Save DC |
|----|--------------|--------------|---------|
| 0 | 0-1 | ≤3 | ≤13 |
| 1/8 | 2-3 | 3 | 13 |
| 1/4 | 4-5 | 3 | 13 |
| 1/2 | 6-8 | 3 | 13 |
| 1 | 9-14 | 3 | 13 |
| 2 | 15-20 | 3 | 13 |
| 3 | 21-26 | 4 | 13 |
| 4 | 27-32 | 5 | 14 |
| 5 | 33-38 | 6 | 15 |
| 6 | 39-44 | 6 | 15 |
| 7 | 45-50 | 6 | 15 |
| 8 | 51-56 | 7 | 16 |
| 9 | 57-62 | 7 | 16 |
| 10 | 63-68 | 7 | 16 |
| 11 | 69-74 | 8 | 17 |
| 12 | 75-80 | 8 | 17 |
| 13 | 81-86 | 8 | 18 |
| 14 | 87-92 | 8 | 18 |
| 15 | 93-98 | 8 | 18 |
| 16 | 99-104 | 9 | 18 |
| 17 | 105-110 | 10 | 19 |
| 18 | 111-116 | 10 | 19 |
| 19 | 117-122 | 10 | 19 |
| 20 | 123-140 | 10 | 19 |

### Final CR Calculation
1. Calculate Defensive CR from HP and AC
2. Calculate Offensive CR from damage and attack bonus
3. Average the two values
4. Adjust for special traits (resistance, flight, spellcasting, etc.)

## Legendary Features by CR

| CR | Legendary Resistance | Legendary Actions | Lair Actions |
|----|---------------------|-------------------|--------------|
| 0-4 | Not typical | Not typical | Rare |
| 5-9 | Optional | Optional | Optional |
| 10-14 | 2/Day recommended | 2 actions | Common |
| 15-19 | 3/Day recommended | 3 actions | Expected |
| 20-24 | 3/Day required | 3 actions | Expected |
| 25-30 | 3/Day + Mythic | 3+ actions | Expected |

## Creature Types (5e 2024)

1. **Aberration** - Alien entities from beyond the multiverse
2. **Beast** - Natural animals and creatures
3. **Celestial** - Good-aligned beings from the Upper Planes
4. **Construct** - Created beings, usually animated by magic
5. **Dragon** - Winged reptilian creatures of ancient lineage
6. **Elemental** - Creatures from the Elemental Planes
7. **Fey** - Creatures from the Feywild
8. **Fiend** - Evil-aligned beings from the Lower Planes
9. **Giant** - Humanoid creatures of great size
10. **Humanoid** - Bipedal peoples including humans, elves, dwarves
11. **Monstrosity** - Unnatural creatures, often created by magic
12. **Ooze** - Amorphous creatures
13. **Plant** - Vegetable creatures
14. **Undead** - Once-living creatures animated by magic or curse

## Validation Checklist

When auditing a stat block, verify:

- [ ] CR matches XP from conversion table
- [ ] Proficiency bonus matches CR/Level
- [ ] Ability modifiers calculated correctly
- [ ] Attack bonuses = Proficiency + Ability Mod
- [ ] Spell Save DC = 8 + Proficiency + Spellcasting Mod
- [ ] HP formula uses correct hit die for size/class
- [ ] HP average calculated correctly
- [ ] Saving throw proficiencies add proficiency bonus
- [ ] Skill proficiencies add proficiency bonus
- [ ] Multiattack damage totals match offensive CR expectations
- [ ] CR 5+ creatures have appropriate legendary features
- [ ] Creature type is valid 5e type
- [ ] Size matches hit die used in HP formula
