---
tags:
  - reference
  - formatting
  - markdown
  - standards
status: complete
---

# Markdown Formatting Standards

This reference defines consistent formatting conventions for all content in the worldbuilding system. Following these standards ensures readability, searchability, and proper rendering in Obsidian.

---

## Document Structure

### Heading Hierarchy

```markdown
# Entity Title (H1)
Only one H1 per document - the entity name

## Major Sections (H2)
Top-level content divisions

### Subsections (H3)
Breakdowns within major sections

#### Details (H4)
Rarely needed, for complex subsections only
```

**Rules:**
- Never skip heading levels (no H1 → H3)
- Use sentence case for headings: "Physical description" not "Physical Description"
- No punctuation at end of headings
- Leave one blank line before and after headings

---

### Section Order (Entity Templates)

1. **YAML Frontmatter** - Metadata block
2. **Title** (H1) - Entity name
3. **Generation Instructions** - `> [!info]` callout
4. **Core Content Sections** (H2) - Varies by template
5. **Connections** (H2) - Wikilinks to related entities
6. **Image Prompts** (H2) - AI image generation guidance

---

## Text Formatting

### Emphasis

| Format | Usage | Example |
|--------|-------|---------|
| **Bold** | Key terms, important concepts | **The Sundering** changed everything |
| *Italic* | Names of works, ships, emphasis | The ship *Dawn's Promise* |
| `Code` | Game mechanics, dice notation | Roll `2d6+3` for damage |
| ~~Strikethrough~~ | Avoid - use sparingly for corrections | ~~old info~~ |

### Inline Elements

```markdown
**Bold:** Important terms, first mention of key concepts
*Italic:* Foreign words, titles of works, subtle emphasis
`Monospace:` Dice rolls, game mechanics, code references
[[Wikilink]]: Cross-references to other entities
```

---

## Lists

### Unordered Lists

Use `-` for all unordered lists (not `*` or `+`):

```markdown
- First item
- Second item
  - Nested item (2 spaces indent)
  - Another nested item
- Third item
```

### Ordered Lists

Use `1.` for all items (markdown auto-numbers):

```markdown
1. First step
2. Second step
   1. Sub-step (3 spaces indent)
   2. Another sub-step
3. Third step
```

### Definition-Style Lists

For key-value pairs within prose:

```markdown
- **Alignment:** Lawful Good
- **Domain:** Life, Light
- **Symbol:** Golden sun disc
```

---

## Tables

### Basic Table Format

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### Alignment

```markdown
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| Text     | Text     | Text     |
```

### Table Guidelines

- Always include header row
- Use consistent column widths where possible
- Keep tables simple - if more than 5 columns, consider restructuring
- Don't put wikilinks in table cells if they break formatting
- Leave blank line before and after tables

---

## Callouts

Obsidian supports callout boxes using `> [!type]` syntax:

### Common Callout Types

```markdown
> [!info] Information
> General information or context.

> [!warning] Warning
> Important cautions or alerts.

> [!tip] Tip
> Helpful suggestions.

> [!note] Note
> Additional context or clarification.

> [!quote] Quote
> Notable quotes or sayings.

> [!danger] Danger
> Critical warnings.

> [!success] Success
> Positive outcomes or completed items.
```

### Callout Usage in Templates

| Callout Type | When to Use |
|--------------|-------------|
| `[!info]` | Generation instructions, context |
| `[!warning]` | DM notes, spoiler alerts |
| `[!tip]` | Gameplay suggestions |
| `[!quote]` | NPC quotes, prophecies |
| `[!danger]` | Hazards, traps |

---

## Wikilinks

### Basic Syntax

```markdown
[[Entity Name]]                    # Basic link
[[Entity Name|Display Text]]       # Aliased link
[[Entity Name#Section]]            # Section link
[[Entity Name#Section|Display]]    # Section link with alias
```

### Wikilink Guidelines

1. **Match exact entity names** - Case-sensitive
2. **Use aliases sparingly** - Only when grammatically necessary
3. **Link on first mention** - Don't link every occurrence
4. **Avoid linking in headings** - Link in body text instead
5. **Check for broken links** - Run `/audit-world` regularly

### Examples

```markdown
Good: She traveled to [[Thornhaven]] seeking answers.
Good: The [[High King Aldric II|High King]] declared war.
Avoid: [[She]] traveled to [[Thornhaven]] [[seeking]] answers.
```

---

## Code Blocks

### Fenced Code Blocks

Use triple backticks with language identifier:

````markdown
```language
code here
```
````

### Common Languages

| Language | Use For |
|----------|---------|
| `yaml` | Frontmatter examples |
| `markdown` | Markdown examples |
| `json` | Configuration, data |
| `python` | Script examples |
| `bash` | Command line |

### Inline Code

Use for:
- Dice notation: `1d20+5`
- Ability scores: `STR 18 (+4)`
- DC values: `DC 15`
- Damage: `2d6 slashing`
- Spell slots: `3rd level`

---

## Numbers and Statistics

### Game Statistics Format

```markdown
**Armor Class:** 15 (chain shirt)
**Hit Points:** 52 (8d8 + 16)
**Speed:** 30 ft.

| STR | DEX | CON | INT | WIS | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 16 (+3) | 14 (+2) | 15 (+2) | 10 (+0) | 12 (+1) | 8 (-1) |
```

### Number Formatting

| Type | Format | Example |
|------|--------|---------|
| Population | Use commas | 15,000 |
| Gold pieces | Abbreviate | 500 gp |
| Distances | Spell out or abbreviate consistently | 30 feet or 30 ft. |
| Dates | World-specific calendar | 3rd of Springrise, 1247 |
| Ranges | En-dash | 5-10 days |

---

## Capitalization

### Always Capitalize

- Entity names: **Thornhaven**, **The Iron Duke**
- Proper nouns: **The Sundering**, **Crown of Stars**
- Titles before names: **King Aldric**, **High Priestess Mira**
- Species names: **Elf**, **Dwarf**, **Human** (when referring to the species)
- Deity names: **Pelor**, **The Raven Queen**
- Organization names: **The Merchant's Guild**, **The Silver Hand**

### Never Capitalize (Unless Starting Sentence)

- Common nouns: king, priestess, guild, city
- Directions: north, south, eastern
- Seasons: spring, winter
- General references: the old king, a merchant's guild

### Title Case vs. Sentence Case

| Context | Style | Example |
|---------|-------|---------|
| File names | Title Case | `Mountain Range.md` |
| Headings | Sentence case | `## Physical description` |
| Table headers | Sentence case | `| Location | Population |` |
| Entity names | Title Case | `The Whispering Woods` |

---

## Punctuation

### Oxford Comma

Always use the Oxford comma in lists:

```markdown
Good: Swords, shields, and armor
Avoid: Swords, shields and armor
```

### Em-Dashes

Use em-dashes (---) for parenthetical statements:

```markdown
The king---known for his temper---refused to negotiate.
```

### Quotation Marks

- Use double quotes for dialogue: "Stand and deliver!"
- Use single quotes for quotes within quotes: "He said 'never' and walked away."
- Use double quotes in YAML: `name: "Lord Aldric"`

---

## Spacing and Line Breaks

### Paragraph Spacing

- One blank line between paragraphs
- One blank line before and after headings
- One blank line before and after code blocks
- One blank line before and after tables
- One blank line before and after callouts

### Line Length

- No hard limit, but aim for readable lengths
- Break long sentences naturally
- Don't force line breaks mid-sentence

### Trailing Whitespace

- Remove trailing spaces at end of lines
- Exception: Two spaces for intentional line breaks in some contexts

---

## Special Characters

### Escaping

Escape special markdown characters when needed:

```markdown
\* Asterisk
\# Hash
\[ Bracket
\| Pipe
\` Backtick
```

### Unicode

- Avoid excessive Unicode symbols
- Use standard ASCII when possible
- Exception: Proper names with diacritics (Élowen, Björn)

---

## Image References

### Image Syntax

```markdown
![[Image Name.png]]           # Obsidian embed
![[Image Name.png|300]]       # With width
![Alt text](path/to/image)    # Standard markdown
```

### Image Guidelines

- Store images in entity folder or central `Assets/` folder
- Use descriptive filenames: `Lord-Aldric-Portrait.png`
- Reference in YAML frontmatter: `image: "[[Lord-Aldric-Portrait.png]]"`
- Include alt text for accessibility

---

## YAML Frontmatter

### Formatting Rules

```yaml
---
tags:
  - character
  - protagonist
name: "Lord Aldric Karath"
aliases:
  - "The Iron Duke"
  - "Aldric"
status: complete
image: "[[Lord Aldric.png]]"
---
```

### Key Points

- Always start and end with `---`
- Use 2-space indentation for arrays
- Quote strings containing special characters
- Quote all wikilinks
- No trailing commas

---

## Quick Reference Checklist

Before saving an entity:

- [ ] Single H1 heading matching entity name
- [ ] Consistent heading hierarchy (no skipped levels)
- [ ] Wikilinks use `[[Entity Name]]` format
- [ ] Lists use `-` for unordered, `1.` for ordered
- [ ] Tables have header rows and proper formatting
- [ ] Numbers formatted consistently
- [ ] Callouts use correct `> [!type]` syntax
- [ ] YAML frontmatter properly formatted
- [ ] No trailing whitespace
- [ ] One blank line between sections

---

## Integration with Tools

This guide supports:
- `/validate-template` - Checks formatting compliance
- `/audit-world` - Identifies formatting issues
- `/linkify` - Follows wikilink conventions
- All template creation skills
