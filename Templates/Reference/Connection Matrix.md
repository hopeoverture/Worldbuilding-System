---
tags:
  - reference
  - connections
  - linking
---

# Connection Matrix Reference

This reference defines the expected bidirectional connections between entity types in the worldbuilding system. Use this guide to ensure all entities are properly linked to each other.

## Core Principle: Bidirectional Linking

**When entity A links to entity B, entity B should link back to entity A.**

This creates a web of interconnected entities that:
- Enables navigation through the vault
- Prevents orphaned entities
- Ensures consistency during audits

## Connection Rules by Entity Type

### Characters → Other Entities

| When Character Links To | Target Should Link Back As |
|------------------------|---------------------------|
| Settlement (as homeland) | Characters > Residents / Notable NPCs |
| Settlement (as current location) | Characters > Notable Figures |
| Organization (as member) | Characters > Members / Notable Members |
| Organization (as leader) | Characters > Leader / Guildmaster / Commander |
| Deity (as patron) | Characters > Champions / Followers / Worshippers |
| Other Character (as ally) | Characters > Allies |
| Other Character (as rival) | Characters > Rivals / Enemies |
| Other Character (as family) | Characters > Family |
| Item (as owner) | Characters > Current Owner |
| Historical Event (as participant) | Characters > Key Figures |
| Familiar/Companion (as bonded) | Characters > Bonded To / Master |

### Settlements → Other Entities

| When Settlement Links To | Target Should Link Back As |
|-------------------------|---------------------------|
| Region (as location) | Settlements > Contains / Major Cities |
| Government (as ruler) | Settlements > Major Cities / Capital |
| Organization (as HQ) | Settlements > Based Here / Headquarters |
| Character (as ruler) | Characters > Ruler / Governor |
| Character (as resident) | Characters > Notable NPCs |
| Historical Event (as site) | Settlements > Major Events |
| Deity (as patron) | Settlements > Holy Sites |

### Organizations → Other Entities

| When Organization Links To | Target Should Link Back As |
|---------------------------|---------------------------|
| Settlement (as headquarters) | Organizations > Based Here |
| Government (as parent) | Organizations > Institutions / Military |
| Character (as leader) | Characters > Guildmaster / Commander / Boss |
| Character (as member) | Characters > Members |
| Deity (as patron) | Organizations > Church / Religious Orders |
| Other Organization (as ally) | Organizations > Allied Factions |
| Other Organization (as rival) | Organizations > Rival Factions |
| Historical Event (as founding) | Organizations > Founded In |

### Geography → Other Entities

| When Geography Links To | Target Should Link Back As |
|------------------------|---------------------------|
| Parent Geography (continent→region) | Geography > Regions / Contains |
| Child Geography (region→continent) | Geography > Parent / Part Of |
| Settlement (as contains) | Settlements > Region / Geography |
| Creature (as habitat) | Creatures > Range / Habitat |
| Organization (as territory) | Organizations > Territory |
| Historical Event (as site) | Geography > Major Events |

### Items → Other Entities

| When Item Links To | Target Should Link Back As |
|-------------------|---------------------------|
| Character (as creator) | Characters > Created Items / Notable Works |
| Character (as owner) | Characters > Equipment / Artifacts |
| Settlement (as location) | Items > Famous Products |
| Organization (as possession) | Items > Institutional Artifacts |
| Historical Event (as involved) | Items > Associated Artifacts |
| Deity (as divine) | Items > Divine Artifacts |

### History → Other Entities

| When History Links To | Target Should Link Back As |
|----------------------|---------------------------|
| Geography (as location) | History > Major Events / Site Of |
| Character (as participant) | History > Key Figures |
| Organization (as involved) | History > Defining Moments |
| Settlement (as site) | History > Major Events |
| Other History (as related) | History > Preceding / Subsequent Events |

### Concepts → Other Entities

| When Concept Links To | Target Should Link Back As |
|----------------------|---------------------------|
| Deity (as part of pantheon) | Concepts > Deities / Pantheon |
| Geography (as practiced in) | Concepts > Religions / Languages |
| Organization (as followed by) | Concepts > Associated Religion |
| Character (as follower) | Concepts > Champions / High Priest |

### Creatures → Other Entities

| When Creature Links To | Target Should Link Back As |
|-----------------------|---------------------------|
| Geography (as habitat) | Creatures > Native Wildlife / Monsters |
| Character (as companion) | Creatures > Familiars / Companions |
| Organization (as associated) | Creatures > Heraldic / Controlled |
| Historical Event (as involved) | Creatures > Legendary Beasts |

## Connection Density Targets

| Entity Type | Minimum Links | Target Links | Must Have Incoming |
|-------------|---------------|--------------|-------------------|
| Characters | 3 | 5-8 | 2+ |
| Settlements | 4 | 6-10 | 3+ |
| Organizations | 3 | 5-8 | 2+ |
| Geography | 3 | 5-7 | 2+ |
| Items | 2 | 4-6 | 1+ |
| History | 3 | 5-7 | 2+ |
| Concepts | 3 | 5-8 | 2+ |
| Creatures | 2 | 4-6 | 1+ |

## Orphan Detection

An **orphan entity** has 0 incoming links from other entities. This means nothing references it.

**To fix orphans:**
1. Identify what type of entity could reference it
2. Find appropriate parent/related entities
3. Add links in those entities pointing to the orphan
4. Ensure at least 2 incoming links

## Audit Integration

The `/audit-world` skill uses this matrix to:
- **Check 2:** Verify bidirectional connections exist
- **Check 4:** Detect orphan entities with no incoming links
- **Check 6:** Validate cross-entity consistency

## Common Connection Patterns

### Settlement-Character-Organization Triangle
```
Settlement ←→ Organization (HQ)
     ↑              ↑
     └──── Character ────┘
         (resident & member)
```

### Deity-Religion-Temple Chain
```
Deity ←→ Religion ←→ Temple ←→ Settlement
         ↓                       ↓
    Religious Order ←→ Characters (clergy)
```

### Government-Military-Settlement Web
```
Government ←→ Military ←→ Stronghold
     ↓              ↓           ↓
  Capital ←→ Garrison ←→ Region
```

### History-Geography-Character Timeline
```
Age ←→ Event ←→ Battle
 ↓        ↓        ↓
Region ← Settlement → Characters (participants)
```

## Quick Reference: Required Connections by Template

| Template | Must Link To |
|----------|-------------|
| Character | Settlement (home), Organization (if any), Geography (homeland) |
| Settlement | Region, Government (ruler), Characters (ruler, NPCs) |
| Organization | Settlement (HQ), Characters (leader), Government (if applicable) |
| Geography | Parent geography, Settlements, Organizations (rulers) |
| Item | Creator or Owner, Location |
| History | Location, Key Figures |
| Deity | Pantheon, Religion, Characters (high priest) |
| Creature | Habitat (geography), Related creatures |

## Circular Reference Detection

**Valid Circular Patterns (expected):**
- Mutual allies: A → B (ally) and B → A (ally) ✓
- Parent-child: Region → Settlement (contains) and Settlement → Region (part of) ✓
- Organization membership: Org → Character (member) and Character → Org (member of) ✓

**Warning Patterns (may indicate error):**
- A → B → C → A forming a "part of" chain (geographic impossibility)
- Historical events forming causal loops (Event A caused Event B which caused Event A)
- Deity hierarchies with cycles (God A serves God B serves God A)

The `/audit-world` skill checks for problematic circular references and reports them as warnings.

## Consolidation Notes

This Connection Matrix is the **single source of truth** for bidirectional linking rules. The following skills reference this file:
- `/audit-world` - Check 2 (Bidirectional Connection Audit)
- `/link-entities` - Relationship type suggestions
- `/create-entity` - Reciprocal link creation
- `/populate-entity` - Reciprocal link patterns
- `/expand-entity` - Connection deepening

When adding new entity types or relationship patterns, update this file first, then update the individual skills if needed.
