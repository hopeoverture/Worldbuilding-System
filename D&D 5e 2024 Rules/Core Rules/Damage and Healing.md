---
tags:
  - dnd-5e-2024
  - rules
  - core-rules
  - damage
  - healing
---

# Damage and Healing

> [!info] Quick Reference
> Hit points represent health and vitality. Damage reduces hit points; healing restores them. At 0 hit points, a creature is dying or dead.

---

## Hit Points

### Maximum Hit Points
Determined at character creation and when leveling up:
- **Level 1**: Maximum value of your Hit Die + Constitution modifier
- **Higher Levels**: Roll Hit Die (or take average) + Constitution modifier per level

### Current Hit Points
- Can't exceed maximum
- Track damage by subtracting from current HP
- At 0 HP: Unconscious and dying

### Temporary Hit Points
- Buffer that absorbs damage first
- Don't stack—use the higher value if you gain more
- Lost before regular HP
- Can't be healed—only granted again
- Usually last until depleted or you finish a Long Rest

---

## Damage

### Damage Rolls
When you deal damage:
**Damage = Weapon/Spell Dice + Ability Modifier + Bonus Damage**

### Multiple Damage Types
If an effect deals multiple damage types (e.g., flame tongue sword: slashing + fire):
- Roll total damage
- Apply resistances/immunities to each portion separately

### Damage Resistance
Take **half damage** from the damage type (rounded down).

### Damage Vulnerability
Take **double damage** from the damage type.

### Damage Immunity
Take **no damage** from the damage type.

### Stacking
- Multiple resistances to the same type: Still half damage
- Multiple vulnerabilities: Still double damage
- Resistance + Vulnerability: They cancel out (normal damage)

---

## Damage Types

| Type | Typical Sources |
|------|----------------|
| **Acid** | Corrosive substances, black dragon breath |
| **Bludgeoning** | Clubs, falling, constriction |
| **Cold** | Ice spells, white dragon breath, extreme cold |
| **Fire** | Flames, red dragon breath, lava |
| **Force** | Pure magical energy (*Magic Missile*, *Eldritch Blast*) |
| **Lightning** | Electric shocks, blue dragon breath |
| **Necrotic** | Life-draining magic, undead touches |
| **Piercing** | Arrows, spears, bites |
| **Poison** | Venomous bites, toxic gas, green dragon breath |
| **Psychic** | Mental attacks, mind flayer abilities |
| **Radiant** | Holy damage, divine spells, sunlight |
| **Slashing** | Swords, claws, axes |
| **Thunder** | Concussive force, *Thunderwave* |

---

## Healing

### Regaining Hit Points
- Can't exceed maximum HP
- 0 HP creature that receives healing: Regains consciousness immediately

### Sources of Healing
- **Spells**: *Cure Wounds*, *Healing Word*, *Heal*, etc.
- **Potions**: Potions of Healing
- **Rest**: Short Rest (Hit Dice) and Long Rest (full HP)
- **Class Features**: Lay on Hands, Second Wind, etc.

---

## Dropping to 0 Hit Points

### Instant Death
If damage reduces you to 0 HP **and** remaining damage equals or exceeds your hit point maximum:
**You die instantly.**

### Falling Unconscious
If damage reduces you to 0 HP without killing you:
- Fall Unconscious (see Conditions)
- Begin making Death Saving Throws

---

## Death Saving Throws

Made at the start of each of your turns while at 0 HP:

### Rolling
- Roll d20 (no modifiers unless from a feature)
- **10 or higher**: Success
- **9 or lower**: Failure

### Special Results
- **Natural 20**: Regain 1 HP, regain consciousness
- **Natural 1**: Counts as **two** failures

### Outcomes

| Result | Effect |
|--------|--------|
| 3 Successes | Stabilized (unconscious, no longer dying) |
| 3 Failures | Death |

Successes and failures don't need to be consecutive.

### Taking Damage at 0 HP
- Any damage = 1 death save failure
- Critical hit = 2 death save failures
- Damage ≥ max HP = instant death

### Healing at 0 HP
- Any healing: Regain consciousness, reset death saves
- Stabilized creatures remain at 0 HP until healed

---

## Stabilizing a Creature

### Without Magic
- Use an action
- Make DC 10 Wisdom (Medicine) check
- Success: Creature is Stable (0 HP, unconscious, no death saves)

### With Magic
- *Spare the Dying* cantrip
- Any healing spell or effect

### Stable Creatures
- Remain at 0 HP and unconscious
- Regain 1 HP after 1d4 hours
- Taking damage restarts death saving throws

---

## Knocking a Creature Out

When you reduce a creature to 0 HP with a **melee attack**, you can choose to knock it out:
- Creature drops to 1 HP instead
- Falls Unconscious
- Begins a Short Rest
- Regains consciousness when it receives any healing or after the rest

This must be declared when the damage is dealt.

---

## Massive Damage (Optional Rule)

If you take damage equal to half your HP maximum or more from a single hit:
- Make DC 15 Constitution saving throw
- Failure: Roll on the System Shock table (in DMG)

---

## Object Hit Points

Objects have AC and HP. Damaging objects:
- Immunity to poison and psychic damage
- May have damage threshold (ignore damage below the threshold)
- Resistance or immunity to certain types based on material

| Size | Fragile HP | Resilient HP |
|------|-----------|--------------|
| Tiny | 2 (1d4) | 5 (2d4) |
| Small | 3 (1d6) | 10 (3d6) |
| Medium | 4 (1d8) | 18 (4d8) |
| Large | 5 (1d10) | 27 (5d10) |

## Related
- [[Combat]]
- [[Conditions]]
- [[Resting]]
