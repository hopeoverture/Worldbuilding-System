#!/usr/bin/env python3
"""
Check Metadata - Find inconsistent or missing YAML metadata fields.

Analyzes entity files across a world to identify metadata inconsistencies,
missing fields, and potential data quality issues.

Usage:
    python check_metadata.py <world_name> [--verbose] [--field FIELD]

Examples:
    python check_metadata.py Eldermyr
    python check_metadata.py Eldermyr --field status
    python check_metadata.py Eldermyr --verbose
"""

import argparse
import io
import os
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any
import yaml

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def extract_yaml_frontmatter(content: str) -> Optional[dict]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None

    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return None

    yaml_end = end_match.start() + 3
    yaml_content = content[4:yaml_end]

    try:
        return yaml.safe_load(yaml_content) or {}
    except yaml.YAMLError:
        return None


def find_world_path(world_name: str) -> Path:
    """Find the world directory."""
    script_dir = Path(__file__).parent.parent

    if Path(world_name).is_dir():
        return Path(world_name)

    worlds_path = script_dir / 'Worlds' / world_name
    if worlds_path.is_dir():
        return worlds_path

    raise FileNotFoundError(f"World not found: {world_name}")


def categorize_by_tags(yaml_data: dict) -> str:
    """Determine entity category from tags."""
    tags = yaml_data.get('tags', [])
    if not tags:
        return 'unknown'

    # Priority order for category detection
    category_tags = [
        'character', 'protagonist', 'antagonist', 'support',
        'settlement', 'city', 'town', 'village', 'tavern', 'shop',
        'organization', 'guild', 'government', 'military',
        'geography', 'region', 'continent', 'forest', 'mountain',
        'creature', 'monster', 'animal', 'species',
        'item', 'weapon', 'armor', 'artifact',
        'deity', 'pantheon', 'religion',
        'history', 'event', 'war', 'battle',
        'encounter', 'combat', 'social', 'exploration',
    ]

    for tag in category_tags:
        if tag in tags:
            return tag

    return tags[0] if tags else 'unknown'


def analyze_metadata(world_path: Path) -> Dict[str, Any]:
    """Analyze all metadata in a world."""
    results = {
        'files': [],
        'field_usage': defaultdict(lambda: {'count': 0, 'empty': 0, 'values': Counter()}),
        'by_category': defaultdict(list),
        'issues': [],
    }

    md_files = list(world_path.rglob('*.md'))
    skip_files = {'README.md', 'World Overview.md'}
    md_files = [f for f in md_files if f.name not in skip_files and '.obsidian' not in str(f)]

    for file_path in md_files:
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            results['issues'].append((file_path, f"Cannot read: {e}"))
            continue

        yaml_data = extract_yaml_frontmatter(content)
        if yaml_data is None:
            results['issues'].append((file_path, "No valid YAML frontmatter"))
            continue

        category = categorize_by_tags(yaml_data)
        rel_path = file_path.relative_to(world_path)

        file_info = {
            'path': rel_path,
            'name': yaml_data.get('name', file_path.stem),
            'category': category,
            'fields': yaml_data,
        }
        results['files'].append(file_info)
        results['by_category'][category].append(file_info)

        # Track field usage
        for field, value in yaml_data.items():
            results['field_usage'][field]['count'] += 1
            if value is None or value == '' or value == []:
                results['field_usage'][field]['empty'] += 1
            else:
                # Track common values for enumerable fields
                if isinstance(value, (str, int, float, bool)):
                    results['field_usage'][field]['values'][str(value)] += 1
                elif isinstance(value, list) and len(value) < 10:
                    for v in value:
                        if isinstance(v, str):
                            results['field_usage'][field]['values'][v] += 1

    return results


def report_field_consistency(results: Dict[str, Any], field: Optional[str] = None):
    """Report on field usage consistency."""
    print("\n" + "=" * 60)
    print("FIELD USAGE ANALYSIS")
    print("=" * 60)

    total_files = len(results['files'])

    if field:
        # Report on specific field
        fields_to_check = [field]
    else:
        # Report on all fields
        fields_to_check = sorted(results['field_usage'].keys())

    for f in fields_to_check:
        if f not in results['field_usage']:
            print(f"\nField '{f}' not found in any files.")
            continue

        data = results['field_usage'][f]
        usage_pct = data['count'] / total_files * 100 if total_files > 0 else 0
        empty_pct = data['empty'] / data['count'] * 100 if data['count'] > 0 else 0

        print(f"\n{f}:")
        print(f"  Used in: {data['count']}/{total_files} files ({usage_pct:.1f}%)")
        print(f"  Empty/null: {data['empty']} ({empty_pct:.1f}%)")

        # Show value distribution for enumerable fields
        if data['values'] and len(data['values']) <= 20:
            print("  Value distribution:")
            for value, count in data['values'].most_common(10):
                val_display = value[:40] + '...' if len(value) > 40 else value
                print(f"    - {val_display}: {count}")


def report_category_consistency(results: Dict[str, Any]):
    """Report on field consistency within categories."""
    print("\n" + "=" * 60)
    print("CATEGORY FIELD ANALYSIS")
    print("=" * 60)

    for category, files in sorted(results['by_category'].items()):
        if len(files) < 2:
            continue

        print(f"\n{category.upper()} ({len(files)} files)")
        print("-" * 40)

        # Find all fields used in this category
        all_fields: Dict[str, int] = defaultdict(int)
        for f in files:
            for field in f['fields'].keys():
                all_fields[field] += 1

        # Report fields not used consistently
        total = len(files)
        inconsistent = []
        for field, count in sorted(all_fields.items()):
            if count < total:
                inconsistent.append((field, count, total))

        if inconsistent:
            print("  Inconsistent fields (not in all files):")
            for field, count, total in inconsistent:
                print(f"    - {field}: {count}/{total}")
        else:
            print("  All fields consistent across category")


def report_missing_fields(results: Dict[str, Any]):
    """Report on commonly missing fields."""
    print("\n" + "=" * 60)
    print("MISSING FIELD ANALYSIS")
    print("=" * 60)

    # Required fields all entities should have
    universal_required = ['tags', 'name', 'aliases', 'status', 'image']

    total_files = len(results['files'])

    print("\nUniversal required fields:")
    for field in universal_required:
        data = results['field_usage'].get(field, {'count': 0, 'empty': 0})
        missing = total_files - data['count']
        empty = data['empty']

        if missing > 0 or empty > 0:
            print(f"  {field}:")
            if missing > 0:
                print(f"    Missing from {missing} files")
            if empty > 0:
                print(f"    Empty in {empty} files")
        else:
            print(f"  {field}: OK (all files have non-empty values)")


def report_issues(results: Dict[str, Any]):
    """Report on files with issues."""
    if not results['issues']:
        return

    print("\n" + "=" * 60)
    print("FILES WITH ISSUES")
    print("=" * 60)

    for path, issue in results['issues']:
        print(f"\n{path}:")
        print(f"  {issue}")


def list_empty_fields(results: Dict[str, Any], verbose: bool = False):
    """List files with empty important fields."""
    print("\n" + "=" * 60)
    print("EMPTY FIELD INSTANCES")
    print("=" * 60)

    important_fields = ['name', 'status', 'location', 'alignment', 'challenge_rating', 'level']

    for file_info in results['files']:
        empty_important = []
        for field in important_fields:
            if field in file_info['fields']:
                value = file_info['fields'][field]
                if value is None or value == '' or value == []:
                    empty_important.append(field)

        if empty_important:
            print(f"\n{file_info['name']}:")
            print(f"  Path: {file_info['path']}")
            print(f"  Empty fields: {', '.join(empty_important)}")


def main():
    parser = argparse.ArgumentParser(
        description='Check metadata consistency across world entities.'
    )
    parser.add_argument('world', help='World name or path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed output')
    parser.add_argument('--field', '-f', help='Analyze specific field only')
    parser.add_argument('--category', '-c', help='Analyze specific category only')
    parser.add_argument('--empty', '-e', action='store_true', help='Show files with empty fields')

    args = parser.parse_args()

    try:
        world_path = find_world_path(args.world)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Analyzing metadata: {world_path}")

    results = analyze_metadata(world_path)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total files analyzed: {len(results['files'])}")
    print(f"Total unique fields: {len(results['field_usage'])}")
    print(f"Categories found: {len(results['by_category'])}")
    print(f"Files with issues: {len(results['issues'])}")

    # Category breakdown
    print("\nEntities by category:")
    for cat, files in sorted(results['by_category'].items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(files)}")

    # Detailed reports
    if args.field:
        report_field_consistency(results, args.field)
    elif args.verbose:
        report_field_consistency(results)

    if args.verbose or args.category:
        report_category_consistency(results)

    report_missing_fields(results)

    if args.empty:
        list_empty_fields(results, args.verbose)

    report_issues(results)

    # Final recommendations
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)

    total_files = len(results['files'])
    status_usage = results['field_usage'].get('status', {}).get('count', 0)
    if status_usage < total_files:
        print(f"- Add 'status' field to {total_files - status_usage} files")

    empty_count = sum(1 for f in results['files']
                     if any(f['fields'].get(k) in [None, '', []]
                           for k in ['name', 'status']))
    if empty_count > 0:
        print(f"- Fill in empty required fields in {empty_count} files")

    if results['issues']:
        print(f"- Fix YAML issues in {len(results['issues'])} files")

    print("- Run 'python validate_templates.py <world> --fix' to auto-fix issues")


if __name__ == '__main__':
    main()
