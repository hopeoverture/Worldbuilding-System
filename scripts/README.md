# Scripts

Python utility scripts for batch operations on worldbuilding vaults.

## Requirements

- Python 3.8+
- PyYAML: `pip install pyyaml`

## Available Scripts

### linkify_world.py

Batch add `[[wikilinks]]` to all entity files in a world. Scans for mentions of existing entity names and aliases, then wraps them in wikilink syntax.

```bash
# Apply changes
python scripts/linkify_world.py Eldermyr

# Preview changes without modifying files
python scripts/linkify_world.py Eldermyr --dry-run

# Show detailed output
python scripts/linkify_world.py Eldermyr --verbose
```

**Features:**
- Reads aliases from YAML frontmatter
- Respects existing wikilinks, code blocks, and tables
- Generates partial name matches (e.g., "Lord Draven" from "Lord Draven Karath")
- Tracks and reports ambiguous references
- Windows/Linux/Mac compatible

---

### validate_templates.py

Check YAML frontmatter, required fields, and document structure across templates and entities.

```bash
# Validate all entities in a world
python scripts/validate_templates.py Worlds/Eldermyr

# Validate all templates
python scripts/validate_templates.py Templates/

# Validate single file with verbose output
python scripts/validate_templates.py Templates/Characters/Protagonist.md --verbose

# Auto-fix issues where possible
python scripts/validate_templates.py Worlds/Eldermyr --fix
```

**Checks:**
- YAML frontmatter exists and is valid
- Universal required fields: `tags`, `name`, `status`
- Entity-specific required fields based on tags
- Valid `status` values: `draft`, `in-progress`, `complete`
- Numeric field ranges (ability scores 1-30, level 1-20)
- H1 heading presence
- Connections section wikilinks

**Auto-fixable issues:**
- Missing universal fields (adds with defaults)
- Invalid status values (resets to `draft`)
- Aliases not in list format

---

### find_orphans.py

Detect entities with no inbound links from other entities. Orphan entities may need connections added to integrate them into the world.

```bash
# Find all orphans (0 inbound links)
python scripts/find_orphans.py Eldermyr

# Find entities with fewer than 2 inbound links
python scripts/find_orphans.py Eldermyr --min-links 2

# Group results by category folder
python scripts/find_orphans.py Eldermyr --by-category

# Verbose output
python scripts/find_orphans.py Eldermyr --verbose
```

**Output:**
- Lists completely orphaned entities (0 inbound links)
- Lists low-connectivity entities (below threshold)
- Shows orphan rate percentage
- Provides recommendations for fixing

---

### check_metadata.py

Analyze YAML metadata consistency across all entities in a world. Identifies missing fields, empty values, and inconsistent field usage.

```bash
# Basic analysis
python scripts/check_metadata.py Eldermyr

# Analyze specific field
python scripts/check_metadata.py Eldermyr --field status

# Show files with empty fields
python scripts/check_metadata.py Eldermyr --empty

# Full verbose report
python scripts/check_metadata.py Eldermyr --verbose
```

**Reports:**
- Field usage statistics across all files
- Value distribution for enumerable fields
- Category-specific field consistency
- Missing required fields
- Files with YAML issues

---

### fix_table_links.py

Fix wikilinks that break table formatting. Handles edge cases where wikilinks containing pipes interfere with markdown table syntax.

```bash
python scripts/fix_table_links.py Worlds/Eldermyr
```

---

## Performance Notes

| World Size | Entity Count | Script Runtime |
|------------|--------------|----------------|
| Small | < 50 | < 5 seconds |
| Medium | 50-150 | 5-30 seconds |
| Large | 150-300 | 30-90 seconds |
| Very Large | 300+ | 1-3 minutes |

For very large worlds:
- Use `--dry-run` first to preview changes
- Consider running scripts on specific categories
- Scripts are single-threaded; performance scales linearly

---

## Workflow Recommendations

### After Creating New Entities

```bash
# 1. Add wikilinks to new content
python scripts/linkify_world.py <world>

# 2. Validate structure
python scripts/validate_templates.py Worlds/<world>

# 3. Check for orphans
python scripts/find_orphans.py <world>
```

### Quality Audit

```bash
# 1. Check metadata consistency
python scripts/check_metadata.py <world> --verbose

# 2. Find entities needing connections
python scripts/find_orphans.py <world> --min-links 2

# 3. Validate and fix issues
python scripts/validate_templates.py Worlds/<world> --fix
```

### Before Session Prep

```bash
# Quick validation
python scripts/validate_templates.py Worlds/<world> --quiet

# Check key NPCs aren't orphaned
python scripts/find_orphans.py <world>
```

---

## Common Issues

### YAML Parse Errors

If scripts report YAML errors:
1. Check for unquoted special characters (`:`, `#`, `[`, `]`)
2. Ensure wikilinks are quoted: `location: "[[Place Name]]"`
3. Verify proper indentation (2 spaces for arrays)

### Encoding Issues

On Windows, if you see garbled characters:
- Scripts automatically set UTF-8 encoding
- Ensure terminal supports UTF-8
- Files should be saved as UTF-8

### Missing Dependencies

```bash
pip install pyyaml
```

---

## Integration with Skills

These scripts complement the Claude Code skills:

| Script | Related Skill |
|--------|---------------|
| `linkify_world.py` | `/linkify --world` |
| `validate_templates.py` | `/validate-template`, `/audit-world` |
| `find_orphans.py` | `/audit-world`, `/link-entities auto` |
| `check_metadata.py` | `/audit-world` |

The Python scripts are faster for bulk operations, while skills provide interactive guidance.
