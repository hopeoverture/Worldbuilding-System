#!/usr/bin/env python3
"""
Linkify World - Batch add [[wikilinks]] to all entity files in a world.

Scans all entity files and adds wikilinks around mentions of other existing
entities. Respects aliases from YAML frontmatter.

Usage:
    python linkify_world.py <world_name> [--dry-run] [--verbose]

Examples:
    python linkify_world.py Eldermyr
    python linkify_world.py Eldermyr --dry-run
    python linkify_world.py Eldermyr --verbose
"""

import argparse
import io
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
import yaml

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


class EntityIndex:
    """Index of all entities and their aliases."""

    def __init__(self):
        # Maps name/alias (lowercase) -> (canonical_name, file_path)
        self.lookup: Dict[str, Tuple[str, Path]] = {}
        # Set of all indexed file paths
        self.files: Set[Path] = set()
        # Track which partial names are ambiguous (appear in multiple entities)
        self.ambiguous: Set[str] = set()

    def add_entity(self, canonical_name: str, file_path: Path, aliases: List[str] = None):
        """Add an entity to the index with its aliases."""
        self.files.add(file_path)

        # Add canonical name
        self.lookup[canonical_name.lower()] = (canonical_name, file_path)

        # Add aliases
        if aliases:
            for alias in aliases:
                if alias and alias.strip():
                    alias_lower = alias.lower().strip()
                    # Check for conflicts
                    if alias_lower in self.lookup:
                        existing_canonical, _ = self.lookup[alias_lower]
                        if existing_canonical.lower() != canonical_name.lower():
                            self.ambiguous.add(alias_lower)
                    self.lookup[alias_lower] = (canonical_name, file_path)

    def get_sorted_names(self) -> List[str]:
        """Get all names sorted by length (longest first) for matching."""
        # Exclude ambiguous names from matching
        return sorted(
            [k for k in self.lookup.keys() if k not in self.ambiguous],
            key=len,
            reverse=True
        )


def extract_yaml_frontmatter(content: str) -> Tuple[dict, int, int]:
    """Extract YAML frontmatter from markdown content.

    Returns (yaml_dict, start_pos, end_pos) or (None, -1, -1) if not found.
    """
    if not content.startswith('---'):
        return None, -1, -1

    # Find the closing ---
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return None, -1, -1

    yaml_end = end_match.start() + 3
    yaml_content = content[4:yaml_end]

    try:
        data = yaml.safe_load(yaml_content)
        return data, 0, yaml_end + end_match.end() - end_match.start()
    except yaml.YAMLError:
        return None, -1, -1


def generate_partial_names(canonical_name: str) -> List[str]:
    """Generate partial name variations for automatic matching.

    Examples:
        "Lord Draven Karath" -> ["Draven", "Lord Draven"]
        "Lady Margret Thorne" -> ["Margret", "Lady Margret"]
        "Ser Aldric Thorne" -> ["Aldric", "Ser Aldric"]
        "Edric Valdren" -> ["Edric"]
        "Grimhild the Smith" -> ["Grimhild"]
        "Captain Alonzo the Bold" -> ["Alonzo", "Captain Alonzo"]
        "High King Aldric II" -> ["Aldric II", "King Aldric", "King Aldric II"]
        "High Confessor Maren" -> ["Maren", "Confessor Maren"]
        "The Mad King" -> [] (no good partial)
        "House Thorne" -> [] (organization, not person)
    """
    partials = []

    # Skip organizations and concepts (they start with "The " or "House ")
    if canonical_name.startswith(('The ', 'House ', 'Magic of ')):
        return partials

    # Titles that can prefix names (ordered by length for proper matching)
    TITLES = [
        'High King', 'High Queen', 'High Confessor', 'High Priest', 'High Priestess',
        'Archmagister', 'Grandmaster', 'Grand Master',
        'Lord', 'Lady', 'Ser', 'Sir', 'Dame',
        'King', 'Queen', 'Prince', 'Princess', 'Duke', 'Duchess',
        'Count', 'Countess', 'Baron', 'Baroness',
        'Captain', 'Admiral', 'General', 'Commander', 'Marshal',
        'Master', 'Magister', 'Confessor', 'Priest', 'Priestess',
        'Brother', 'Sister', 'Father', 'Mother',
    ]

    # Check for "Name the Epithet" pattern (e.g., "Grimhild the Smith")
    the_match = re.match(r'^(.+?)\s+the\s+.+$', canonical_name, re.IGNORECASE)
    if the_match:
        first_part = the_match.group(1).strip()
        # Check if the first part has a title
        for title in TITLES:
            if first_part.lower().startswith(title.lower() + ' '):
                # "Captain Alonzo the Bold" -> "Alonzo", "Captain Alonzo"
                name_after_title = first_part[len(title)+1:].strip()
                if name_after_title and len(name_after_title) >= 3:
                    partials.append(name_after_title)
                    partials.append(f"{title} {name_after_title}")
                break
        else:
            # No title, just use the first part (e.g., "Grimhild" from "Grimhild the Smith")
            if first_part and len(first_part) >= 3:
                partials.append(first_part)
        return partials

    # Check for titled names (e.g., "Lord Draven Karath", "High King Aldric II")
    for title in TITLES:
        if canonical_name.lower().startswith(title.lower() + ' '):
            rest = canonical_name[len(title)+1:].strip()
            parts = rest.split()

            if len(parts) >= 1:
                first_name = parts[0]

                # Check for Roman numerals at the end (e.g., "Aldric II")
                has_numeral = len(parts) >= 2 and re.match(r'^[IVX]+$', parts[-1])

                if has_numeral:
                    # "High King Aldric II" -> "Aldric II", "King Aldric", "King Aldric II"
                    name_with_numeral = f"{first_name} {parts[-1]}"
                    if len(name_with_numeral) >= 3:
                        partials.append(name_with_numeral)

                    # Also add shorter title + name combinations
                    # "High King" -> "King"
                    short_title = title.split()[-1] if ' ' in title else title
                    partials.append(f"{short_title} {first_name}")
                    partials.append(f"{short_title} {name_with_numeral}")
                else:
                    # "Lord Draven Karath" -> "Draven", "Lord Draven"
                    if len(first_name) >= 3:
                        partials.append(first_name)
                        partials.append(f"{title} {first_name}")

            return partials

    # No title - check for simple "FirstName LastName" pattern
    parts = canonical_name.split()
    if len(parts) == 2:
        first_name = parts[0]
        # Only add first name if it's substantial (avoid short words)
        if len(first_name) >= 3 and first_name[0].isupper():
            partials.append(first_name)

    return partials


def build_entity_index(world_path: Path) -> EntityIndex:
    """Build an index of all entities in the world."""
    index = EntityIndex()

    for md_file in world_path.rglob('*.md'):
        # Skip non-entity files
        if md_file.name in ['README.md', 'World Overview.md']:
            continue

        content = md_file.read_text(encoding='utf-8')
        yaml_data, _, _ = extract_yaml_frontmatter(content)

        # Get canonical name from YAML or filename
        canonical_name = md_file.stem  # filename without .md
        if yaml_data and yaml_data.get('name'):
            canonical_name = yaml_data['name']

        # Get explicit aliases from YAML
        aliases = []
        if yaml_data and yaml_data.get('aliases'):
            aliases = yaml_data['aliases']
            if isinstance(aliases, str):
                aliases = [aliases]

        # Also add filename as an alias if different from canonical
        if md_file.stem.lower() != canonical_name.lower():
            aliases.append(md_file.stem)

        # Generate automatic partial name aliases
        auto_partials = generate_partial_names(canonical_name)
        aliases.extend(auto_partials)

        index.add_entity(canonical_name, md_file, aliases)

    return index


def find_section_boundaries(content: str) -> Tuple[int, int]:
    """Find the content area to process (exclude YAML, Image Prompts, Connections).

    Returns (start, end) positions of processable content.
    """
    # Skip YAML frontmatter
    _, _, yaml_end = extract_yaml_frontmatter(content)
    start = yaml_end if yaml_end > 0 else 0

    # Find where to stop (Image Prompts or Connections section, whichever comes first)
    end = len(content)

    # Look for Image Prompts section
    image_match = re.search(r'\n## Image Prompts?\s*\n', content)
    if image_match:
        end = min(end, image_match.start())

    # Look for Connections section
    conn_match = re.search(r'\n## Connections?\s*\n', content)
    if conn_match:
        end = min(end, conn_match.start())

    return start, end


def find_existing_wikilinks(content: str) -> Set[Tuple[int, int]]:
    """Find all existing wikilinks and return their positions."""
    positions = set()
    for match in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content):
        positions.add((match.start(), match.end()))
    return positions


def is_inside_wikilink(pos: int, wikilink_positions: Set[Tuple[int, int]]) -> bool:
    """Check if a position is inside an existing wikilink."""
    for start, end in wikilink_positions:
        if start <= pos < end:
            return True
    return False


def is_inside_code_block(content: str, pos: int) -> bool:
    """Check if a position is inside a code block."""
    # Find all code block boundaries before this position
    code_blocks = list(re.finditer(r'```', content[:pos]))
    # If odd number of ``` markers, we're inside a code block
    return len(code_blocks) % 2 == 1


def is_inside_table_row(content: str, pos: int) -> bool:
    """Check if a position is inside a markdown table row.

    Table rows start with | and the line contains multiple | characters.
    We can't use display text (|) in wikilinks inside tables.
    """
    # Find the start of the current line
    line_start = content.rfind('\n', 0, pos)
    if line_start == -1:
        line_start = 0
    else:
        line_start += 1  # Move past the newline

    # Find the end of the current line
    line_end = content.find('\n', pos)
    if line_end == -1:
        line_end = len(content)

    line = content[line_start:line_end]

    # Check if line looks like a table row (starts with | or contains multiple |)
    stripped = line.strip()
    if stripped.startswith('|') or stripped.count('|') >= 2:
        return True
    return False


def linkify_content(content: str, index: EntityIndex, source_file: Path,
                    verbose: bool = False) -> Tuple[str, List[str]]:
    """Add wikilinks to content for all matching entities.

    Returns (modified_content, list_of_changes).
    """
    changes = []
    start_pos, end_pos = find_section_boundaries(content)
    wikilink_positions = find_existing_wikilinks(content)

    # Get the portion of content we'll modify
    prefix = content[:start_pos]
    processable = content[start_pos:end_pos]
    suffix = content[end_pos:]

    # Track positions we've already linked (to avoid double-linking)
    linked_positions: Set[Tuple[int, int]] = set()

    # Short/generic phrases that cause false positives when used as aliases
    EXCLUDED_ALIASES = {
        'the three',      # Often means "3 things", not "The Faith of the Three"
        'the power',      # Too generic
        'the figure',     # Too generic
        'the reach',      # Too generic (vs "The Karath Reach")
        'the academy',    # Could mean any academy
        'the faith',      # Could mean faith in general
    }

    # Process each entity name (longest first)
    for name_lower in index.get_sorted_names():
        canonical_name, entity_path = index.lookup[name_lower]

        # Don't self-link
        if entity_path == source_file:
            continue

        # Skip short generic aliases that cause false positives
        if name_lower in EXCLUDED_ALIASES:
            continue

        # Skip names that contain apostrophes - these are often item names
        # ("Grimhild's Commission") or contractions that cause false positives
        if "'" in name_lower or "'" in name_lower:
            # Only match full item names, not partial possessive matches
            # Check if this is a full canonical name (not a generated partial)
            if name_lower != canonical_name.lower():
                continue

        # Build regex pattern for word boundary matching
        # Escape special regex characters in the name
        escaped_name = re.escape(name_lower)
        # Allow for case-insensitive matching
        # Use word boundaries with custom exclusions for wikilinks
        # (?<!\[) - not preceded by [
        # (?<!\w) - not preceded by word char
        # (?!\]) - not followed by ]
        # (?!\w) - not followed by word char (but allow 's for possessives)
        pattern = rf"(?<!\[)(?<!\w)({escaped_name})(?![\]\w])"

        # Find all matches in the processable content
        for match in re.finditer(pattern, processable, re.IGNORECASE):
            match_start = start_pos + match.start()
            match_end = start_pos + match.end()
            matched_text = match.group(1)

            # Skip if inside existing wikilink
            if is_inside_wikilink(match_start, wikilink_positions):
                continue

            # Skip if inside code block
            if is_inside_code_block(content, match_start):
                continue

            # Skip if we've already linked something overlapping this position
            overlap = False
            for ls, le in linked_positions:
                if not (match_end <= ls or match_start >= le):
                    overlap = True
                    break
            if overlap:
                continue

            # Record this position as linked
            linked_positions.add((match_start, match_end))

            # Check if we're inside a table row (can't use | in wikilinks there)
            in_table = is_inside_table_row(content, match_start)

            # Determine the replacement
            if matched_text.lower() == canonical_name.lower():
                # Exact match (possibly different case)
                if matched_text == canonical_name or in_table:
                    # Use simple link (no display text) if exact match OR in table
                    replacement = f'[[{canonical_name}]]'
                else:
                    replacement = f'[[{canonical_name}|{matched_text}]]'
            else:
                # Partial/alias match
                if in_table:
                    # In tables, use canonical name without display text
                    replacement = f'[[{canonical_name}]]'
                else:
                    # Outside tables, use display text to preserve original text
                    replacement = f'[[{canonical_name}|{matched_text}]]'

            changes.append((match_start - start_pos, match_end - start_pos,
                           matched_text, replacement, canonical_name))

    # Apply changes in reverse order (so positions don't shift)
    changes.sort(key=lambda x: x[0], reverse=True)

    change_descriptions = []
    for pos_start, pos_end, original, replacement, canonical in changes:
        processable = processable[:pos_start] + replacement + processable[pos_end:]
        change_descriptions.append(f"  '{original}' -> {replacement}")

    return prefix + processable + suffix, change_descriptions


def linkify_world(world_name: str, dry_run: bool = False, verbose: bool = False):
    """Linkify all entities in a world."""
    # Find the worlds directory
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    worlds_dir = base_dir / 'Worlds'

    if not worlds_dir.exists():
        print(f"Error: Worlds directory not found at {worlds_dir}")
        sys.exit(1)

    world_path = worlds_dir / world_name
    if not world_path.exists():
        print(f"Error: World '{world_name}' not found at {world_path}")
        print(f"\nAvailable worlds:")
        for d in worlds_dir.iterdir():
            if d.is_dir() and not d.name.startswith('.'):
                print(f"  - {d.name}")
        sys.exit(1)

    print(f"{'[DRY RUN] ' if dry_run else ''}Linkifying world: {world_name}")
    print(f"World path: {world_path}")
    print()

    # Build entity index
    print("Building entity index...")
    index = build_entity_index(world_path)
    print(f"Indexed {len(index.files)} entities with {len(index.lookup)} names/aliases")
    if index.ambiguous:
        print(f"Skipping {len(index.ambiguous)} ambiguous names: {', '.join(sorted(index.ambiguous))}")
    print()

    # Process each entity file
    total_files = 0
    files_modified = 0
    total_links_added = 0

    for md_file in sorted(world_path.rglob('*.md')):
        # Skip non-entity files
        if md_file.name in ['README.md']:
            continue

        total_files += 1
        content = md_file.read_text(encoding='utf-8')

        new_content, changes = linkify_content(content, index, md_file, verbose)

        if changes:
            files_modified += 1
            total_links_added += len(changes)

            rel_path = md_file.relative_to(world_path)
            print(f"{'[DRY RUN] ' if dry_run else ''}Modified: {rel_path} (+{len(changes)} links)")

            if verbose:
                for change in changes:
                    print(change)
                print()

            if not dry_run:
                md_file.write_text(new_content, encoding='utf-8')

    # Summary
    print()
    print("=" * 50)
    print(f"{'[DRY RUN] ' if dry_run else ''}LINKIFY COMPLETE: {world_name}")
    print("=" * 50)
    print(f"Files scanned:  {total_files}")
    print(f"Files modified: {files_modified}")
    print(f"Links added:    {total_links_added}")

    if dry_run:
        print()
        print("This was a dry run. No files were modified.")
        print("Run without --dry-run to apply changes.")


def main():
    parser = argparse.ArgumentParser(
        description='Batch add [[wikilinks]] to all entity files in a world.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python linkify_world.py Eldermyr
    python linkify_world.py Eldermyr --dry-run
    python linkify_world.py Eldermyr --verbose
        """
    )
    parser.add_argument('world', help='Name of the world to linkify')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be changed without modifying files')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Show detailed changes for each file')

    args = parser.parse_args()

    linkify_world(args.world, dry_run=args.dry_run, verbose=args.verbose)


if __name__ == '__main__':
    main()
