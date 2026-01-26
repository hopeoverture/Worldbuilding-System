#!/usr/bin/env python3
"""
Find Orphans - Detect entities with no inbound links from other entities.

Scans a world directory and identifies entities that are not referenced
by any other entity. These "orphan" entities may need connections added.

Usage:
    python find_orphans.py <world_name> [--verbose] [--min-links N]

Examples:
    python find_orphans.py Eldermyr
    python find_orphans.py Eldermyr --verbose
    python find_orphans.py Eldermyr --min-links 2  # Show entities with fewer than 2 inbound links
"""

import argparse
import io
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple
import yaml

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def extract_yaml_frontmatter(content: str) -> Tuple[dict, str]:
    """Extract YAML frontmatter and return (data, body)."""
    if not content.startswith('---'):
        return {}, content

    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}, content

    yaml_end = end_match.start() + 3
    yaml_content = content[4:yaml_end]
    body_start = yaml_end + end_match.end() - end_match.start() + 3

    try:
        data = yaml.safe_load(yaml_content)
        return data or {}, content[body_start:]
    except yaml.YAMLError:
        return {}, content


def get_entity_name(file_path: Path) -> str:
    """Get entity name from file (prefers YAML name, falls back to filename)."""
    try:
        content = file_path.read_text(encoding='utf-8')
        yaml_data, _ = extract_yaml_frontmatter(content)
        if yaml_data.get('name'):
            return yaml_data['name']
    except Exception:
        pass
    return file_path.stem


def get_entity_aliases(file_path: Path) -> List[str]:
    """Get all names an entity might be referenced by."""
    aliases = []
    try:
        content = file_path.read_text(encoding='utf-8')
        yaml_data, _ = extract_yaml_frontmatter(content)

        # Add canonical name
        name = yaml_data.get('name', file_path.stem)
        aliases.append(name)
        aliases.append(file_path.stem)  # Also add filename

        # Add explicit aliases
        yaml_aliases = yaml_data.get('aliases', [])
        if yaml_aliases:
            aliases.extend(yaml_aliases)
    except Exception:
        aliases.append(file_path.stem)

    return [a for a in aliases if a]  # Filter empty


def extract_wikilinks(content: str) -> Set[str]:
    """Extract all wikilink targets from content."""
    # Match [[Target]] or [[Target|Display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    matches = re.findall(pattern, content)
    return set(matches)


def find_world_path(world_name: str) -> Path:
    """Find the world directory."""
    script_dir = Path(__file__).parent.parent

    # Try direct path first
    if Path(world_name).is_dir():
        return Path(world_name)

    # Try Worlds/ subdirectory
    worlds_path = script_dir / 'Worlds' / world_name
    if worlds_path.is_dir():
        return worlds_path

    raise FileNotFoundError(f"World not found: {world_name}")


def analyze_world(world_path: Path, verbose: bool = False) -> Tuple[Dict[str, int], Dict[str, Path]]:
    """
    Analyze all entities in a world for inbound link counts.

    Returns:
        (inbound_counts, entity_paths) where:
        - inbound_counts: dict mapping entity name (lowercase) to count of inbound links
        - entity_paths: dict mapping entity name (lowercase) to file path
    """
    # Build index of all entities
    entity_paths: Dict[str, Path] = {}  # lowercase name -> path
    entity_aliases: Dict[str, str] = {}  # lowercase alias -> lowercase canonical name

    md_files = list(world_path.rglob('*.md'))

    # Skip certain files
    skip_files = {'README.md', 'World Overview.md'}
    md_files = [f for f in md_files if f.name not in skip_files and '.obsidian' not in str(f)]

    if verbose:
        print(f"Found {len(md_files)} entity files")

    # First pass: build entity index
    for file_path in md_files:
        canonical = get_entity_name(file_path)
        canonical_lower = canonical.lower()
        entity_paths[canonical_lower] = file_path

        for alias in get_entity_aliases(file_path):
            entity_aliases[alias.lower()] = canonical_lower

    # Initialize inbound counts
    inbound_counts: Dict[str, int] = {name: 0 for name in entity_paths.keys()}

    # Second pass: count inbound links
    for file_path in md_files:
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            continue

        source_name = get_entity_name(file_path).lower()
        wikilinks = extract_wikilinks(content)

        for link_target in wikilinks:
            target_lower = link_target.lower()

            # Try to resolve to canonical name
            if target_lower in entity_aliases:
                resolved = entity_aliases[target_lower]
            elif target_lower in entity_paths:
                resolved = target_lower
            else:
                continue  # Link to non-existent entity

            # Don't count self-links
            if resolved != source_name:
                if resolved in inbound_counts:
                    inbound_counts[resolved] += 1

    return inbound_counts, entity_paths


def main():
    parser = argparse.ArgumentParser(
        description='Find orphan entities with no inbound links.'
    )
    parser.add_argument('world', help='World name or path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed output')
    parser.add_argument('--min-links', type=int, default=1,
                       help='Minimum inbound links required (default: 1)')
    parser.add_argument('--by-category', action='store_true',
                       help='Group results by category folder')

    args = parser.parse_args()

    try:
        world_path = find_world_path(args.world)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Analyzing: {world_path}")
    print("=" * 50)

    inbound_counts, entity_paths = analyze_world(world_path, args.verbose)

    # Find entities below minimum link threshold
    orphans: List[Tuple[str, int, Path]] = []
    for name, count in inbound_counts.items():
        if count < args.min_links:
            orphans.append((name, count, entity_paths[name]))

    if not orphans:
        print(f"\nNo orphans found! All entities have at least {args.min_links} inbound link(s).")
        return

    # Sort by count (ascending), then by name
    orphans.sort(key=lambda x: (x[1], x[0]))

    if args.by_category:
        # Group by parent folder
        by_category: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        for name, count, path in orphans:
            category = path.parent.name
            by_category[category].append((name, count))

        print(f"\nOrphans by Category (< {args.min_links} inbound links):")
        print("-" * 50)

        for category in sorted(by_category.keys()):
            items = by_category[category]
            print(f"\n{category}/ ({len(items)} orphans)")
            for name, count in items:
                print(f"  - {name} ({count} inbound)")
    else:
        print(f"\nOrphan Entities (< {args.min_links} inbound links):")
        print("-" * 50)

        zero_links = [o for o in orphans if o[1] == 0]
        few_links = [o for o in orphans if o[1] > 0]

        if zero_links:
            print(f"\nCompletely Orphaned (0 inbound links): {len(zero_links)}")
            for name, count, path in zero_links:
                rel_path = path.relative_to(world_path)
                print(f"  - {name}")
                if args.verbose:
                    print(f"    Path: {rel_path}")

        if few_links:
            print(f"\nLow Connectivity (1-{args.min_links - 1} inbound links): {len(few_links)}")
            for name, count, path in few_links:
                print(f"  - {name} ({count} inbound)")

    # Summary
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    total_entities = len(entity_paths)
    orphan_count = len(orphans)
    connected_count = total_entities - orphan_count

    print(f"Total entities: {total_entities}")
    print(f"Connected (>= {args.min_links} inbound): {connected_count}")
    print(f"Orphans (< {args.min_links} inbound): {orphan_count}")
    print(f"Orphan rate: {orphan_count / total_entities * 100:.1f}%")

    # Recommendations
    if orphan_count > 0:
        print("\nRecommendations:")
        print("  1. Run '/link-entities auto' to find potential connections")
        print("  2. Review orphans and add references in related entities")
        print("  3. Consider if orphans should be connected to World Overview")


if __name__ == '__main__':
    main()
