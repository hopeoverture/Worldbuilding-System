#!/usr/bin/env python3
"""
Fix Table Links - Remove display text from wikilinks inside markdown tables.

The linkify script accidentally added [[Entity|display]] links inside table rows,
which breaks table formatting because | is the column delimiter.

This script fixes those by converting [[Entity|display]] to [[Entity]] in tables.

Usage:
    python fix_table_links.py <world_name> [--dry-run]
"""

import argparse
import io
import re
import sys
from pathlib import Path

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def fix_table_links_in_line(line: str) -> tuple[str, int]:
    """Fix wikilinks with display text in a table row.

    Returns (fixed_line, count_of_fixes).
    """
    if not line.strip().startswith('|') and line.count('|') < 2:
        return line, 0

    fixes = 0
    # Pattern to find [[Entity|display]] and replace with [[Entity]]
    # We need to be careful not to match the table delimiters

    def replace_link(match):
        nonlocal fixes
        entity = match.group(1)
        fixes += 1
        return f'[[{entity}]]'

    # Match [[something|something_else]] but not table delimiters
    fixed_line = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', replace_link, line)

    return fixed_line, fixes


def fix_file(file_path: Path, dry_run: bool = False) -> tuple[int, list[str]]:
    """Fix all table links in a file.

    Returns (total_fixes, list_of_changes).
    """
    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    total_fixes = 0
    changes = []
    new_lines = []

    for i, line in enumerate(lines):
        fixed_line, fixes = fix_table_links_in_line(line)
        new_lines.append(fixed_line)

        if fixes > 0:
            total_fixes += fixes
            changes.append(f"  Line {i+1}: {fixes} link(s) fixed")

    if total_fixes > 0 and not dry_run:
        file_path.write_text('\n'.join(new_lines), encoding='utf-8')

    return total_fixes, changes


def fix_world(world_name: str, dry_run: bool = False):
    """Fix all table links in a world."""
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    worlds_dir = base_dir / 'Worlds'

    world_path = worlds_dir / world_name
    if not world_path.exists():
        print(f"Error: World '{world_name}' not found at {world_path}")
        sys.exit(1)

    print(f"{'[DRY RUN] ' if dry_run else ''}Fixing table links in: {world_name}")
    print()

    total_files = 0
    files_fixed = 0
    total_links_fixed = 0

    for md_file in sorted(world_path.rglob('*.md')):
        total_files += 1
        fixes, changes = fix_file(md_file, dry_run)

        if fixes > 0:
            files_fixed += 1
            total_links_fixed += fixes
            rel_path = md_file.relative_to(world_path)
            print(f"{'[DRY RUN] ' if dry_run else ''}Fixed: {rel_path} ({fixes} links)")

    print()
    print("=" * 50)
    print(f"{'[DRY RUN] ' if dry_run else ''}FIX COMPLETE: {world_name}")
    print("=" * 50)
    print(f"Files scanned: {total_files}")
    print(f"Files fixed:   {files_fixed}")
    print(f"Links fixed:   {total_links_fixed}")

    if dry_run:
        print()
        print("This was a dry run. No files were modified.")


def main():
    parser = argparse.ArgumentParser(
        description='Fix wikilinks with display text inside markdown tables.'
    )
    parser.add_argument('world', help='Name of the world to fix')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be changed without modifying files')

    args = parser.parse_args()
    fix_world(args.world, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
