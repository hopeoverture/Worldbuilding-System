# Troubleshooting Guide

Common issues and solutions for the Worldbuilding System.

---

## YAML Errors

### "Invalid YAML frontmatter"

**Symptoms:** Entity won't load properly, validation scripts fail

**Common Causes:**

1. **Unquoted special characters**
   ```yaml
   # Wrong
   name: Lord Aldric: The Brave

   # Right
   name: "Lord Aldric: The Brave"
   ```

2. **Unquoted wikilinks**
   ```yaml
   # Wrong
   location: [[Thornhaven]]

   # Right
   location: "[[Thornhaven]]"
   ```

3. **Improper list formatting**
   ```yaml
   # Wrong
   tags: character, protagonist

   # Right
   tags:
     - character
     - protagonist
   # Or
   tags: [character, protagonist]
   ```

4. **Missing closing `---`**
   Ensure your frontmatter has both opening and closing `---` markers.

**Fix:** Run `python scripts/validate_templates.py <file> --fix` to auto-correct common issues.

---

### "Duplicate key in YAML"

**Symptoms:** Only first value is used, data loss

**Cause:** Same field appears twice in frontmatter

```yaml
# Wrong
name: "Aldric"
species: "Human"
name: "Lord Aldric"  # Duplicate!

# Right
name: "Lord Aldric"
species: "Human"
```

**Fix:** Search for and remove duplicate fields manually.

---

## Broken Links

### "Broken wikilink: [[Entity Name]]"

**Symptoms:** Wikilinks don't navigate anywhere, audit shows broken links

**Common Causes:**

1. **Entity doesn't exist yet**
   - Create the entity using `/create-entity`
   - Or remove/update the link

2. **Name mismatch**
   - Check exact spelling and capitalization
   - Wikilinks are case-sensitive
   - `[[Thornhaven]]` ≠ `[[thornhaven]]`

3. **File was renamed**
   - Update all references to use new name
   - Run `/linkify --world <world>` to refresh links

**Fix:** Run `/audit-world <world> --fix` to get suggestions.

---

### Orphan Entities (No Inbound Links)

**Symptoms:** Entity exists but isn't referenced anywhere

**Check:** Run `python scripts/find_orphans.py <world>`

**Fix Options:**
1. Add references in related entities
2. Use `/link-entities <entity> <related>` to create bidirectional links
3. Run `/link-entities auto <world>` to scan for missing connections

---

## D&D 5e Stat Errors

### "Proficiency bonus doesn't match level/CR"

| Level/CR | Correct Proficiency |
|----------|---------------------|
| 1-4 | +2 |
| 5-8 | +3 |
| 9-12 | +4 |
| 13-16 | +5 |
| 17-20 | +6 |
| 21-24 | +7 |
| 25-28 | +8 |
| 29-30 | +9 |

**Fix:** Update `proficiency_bonus:` in the frontmatter.

---

### "Attack bonus calculation error"

**Formula:** Attack Bonus = Proficiency + Ability Modifier

**Example:** Level 5 Fighter with STR 18
- Proficiency: +3
- STR Modifier: +4
- Attack Bonus: +7

**Check:** Ensure the attack bonus in stat blocks matches this formula.

---

### "HP doesn't match hit dice"

**Monster Formula:** HP = (Hit Dice count × Hit Die average) + (Hit Dice count × CON modifier)

| Size | Hit Die | Average |
|------|---------|---------|
| Tiny | d4 | 2.5 |
| Small | d6 | 3.5 |
| Medium | d8 | 4.5 |
| Large | d10 | 5.5 |
| Huge | d12 | 6.5 |
| Gargantuan | d20 | 10.5 |

**Example:** Large creature with 8d10 and CON +3
- HP = (8 × 5.5) + (8 × 3) = 44 + 24 = 68

**Fix:** Recalculate HP using the formula above.

---

## Script Errors

### "ModuleNotFoundError: No module named 'yaml'"

**Fix:** Install PyYAML
```bash
pip install pyyaml
```

---

### "World not found: [name]"

**Cause:** Script can't locate the world directory

**Check:**
- Run script from repository root
- World name matches folder name exactly (case-sensitive)
- World exists in `Worlds/` directory

**Try:**
```bash
python scripts/linkify_world.py Worlds/Eldermyr  # Full path
python scripts/linkify_world.py Eldermyr         # Just name
```

---

### "UnicodeDecodeError"

**Cause:** File contains non-UTF-8 characters

**Fix:**
1. Open the file in a text editor
2. Save as UTF-8 encoding
3. Or add encoding flag: `python script.py --encoding utf-8`

---

## Obsidian Issues

### Wikilinks Not Working

**Symptoms:** Clicking `[[Link]]` does nothing or shows "Page not found"

**Checks:**
1. Is the target file in the vault?
2. Does the filename match exactly (including spaces)?
3. Is Obsidian indexing complete? (Check status bar)

**Fix:** Restart Obsidian or manually navigate to the file.

---

### Graph View Empty or Incomplete

**Symptoms:** Graph shows fewer connections than expected

**Causes:**
1. Obsidian hasn't indexed all files yet
2. Links use aliases that aren't being resolved
3. Files are outside the vault folder

**Fix:**
1. Wait for indexing (check bottom status bar)
2. Press Ctrl/Cmd+R to reload
3. Check Settings > Files & Links > Detect all file extensions

---

### Templates Not Working

**Symptoms:** `{{title}}` doesn't get replaced

**Cause:** Obsidian Templates plugin not configured

**Fix:**
1. Settings > Core Plugins > Enable "Templates"
2. Settings > Templates > Set template folder to `Templates/`
3. Use Ctrl/Cmd+T to insert template

---

## MCP Server Issues

### "MCP server not responding"

**Symptoms:** Skills that depend on MCP fail

**Checks:**
1. Is `.mcp.json` present in repository root?
2. Are MCP packages installed?
   ```bash
   npm install -g obsidian-mcp @modelcontextprotocol/server-memory @modelcontextprotocol/server-fetch
   ```
3. Is `enableAllProjectMcpServers: true` in `.claude/settings.json`?

---

## Skill/Command Errors

### "Skill not found"

**Symptoms:** `/skill-name` doesn't work

**Checks:**
1. Skill file exists in `.claude/skills/`
2. Using correct skill name (check `CLAUDE.md` for list)
3. AI assistant has access to skills directory

---

### "/audit-world takes too long"

**Cause:** Large world with many entities

**Solutions:**
1. Audit specific categories:
   ```
   /audit-world MyWorld --category Characters
   ```
2. Use Python scripts for bulk operations:
   ```bash
   python scripts/validate_templates.py Worlds/MyWorld
   ```
3. See Performance Guidelines in `CLAUDE.md`

---

### "/generate-image fails"

**Requirements:**
1. OpenAI API key configured
2. Image prompt section filled in entity
3. Entity created with `/create-entity` (includes prompts)

**Check:** Open the entity file and verify `## Image Prompts` section has filled `**Prompt:**` fields.

---

## Common Mistakes

### Forgetting Bidirectional Links

**Problem:** Character links to Settlement, but Settlement doesn't link back

**Prevention:**
- Always add links in both directions
- Run `/audit-world` to check
- Use `/link-entities` which creates both directions

---

### Using Level AND CR

**Problem:** Both `level:` and `challenge_rating:` are filled

**Rule:** Use ONE or the other:
- `level:` for PC-style characters with class features
- `challenge_rating:` for NPC/monster-style stat blocks

---

### Mixing Template Types

**Problem:** Using Protagonist template for a minor NPC

**Better:**
- **Protagonist/Antagonist:** Major characters with full backstory
- **Support Character:** Important recurring NPCs
- **NPC Stat Block:** Combat-focused, minimal story
- **Background Character:** Mentioned but rarely seen

---

### Broken Table Formatting

**Problem:** Tables render incorrectly

**Common Causes:**
1. Missing header separator row
   ```markdown
   | Header | Header |
   |--------|--------|  <- This row is required
   | Cell   | Cell   |
   ```
2. Wikilinks with pipes break tables
   ```markdown
   # Wrong
   | Name | [[Lord Aldric|Aldric]] |

   # Right (avoid aliases in tables)
   | Name | [[Lord Aldric]] |
   ```

**Fix:** Run `python scripts/fix_table_links.py <world>`

---

## Getting More Help

### Documentation
- `CLAUDE.md` - Complete reference
- `GETTING_STARTED.md` - Quick start guide
- `Templates/Reference/` - Detailed guides

### Scripts
```bash
# Validate everything
python scripts/validate_templates.py Worlds/MyWorld --verbose

# Find orphan entities
python scripts/find_orphans.py MyWorld

# Check metadata consistency
python scripts/check_metadata.py MyWorld
```

### Report Issues
https://github.com/anthropics/claude-code/issues

---

## Quick Diagnostic Checklist

When something doesn't work:

- [ ] Is the file valid YAML? (check frontmatter syntax)
- [ ] Is the file in the correct folder?
- [ ] Are all wikilinks using exact entity names?
- [ ] Does the entity have `status:` field?
- [ ] Are numeric values in valid ranges?
- [ ] Have you run `/audit-world` recently?
- [ ] Are required dependencies installed?
- [ ] Is Obsidian fully indexed?

Most issues can be diagnosed by running:
```bash
python scripts/validate_templates.py <path> --verbose
```
