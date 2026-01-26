#!/usr/bin/env python3
"""
Validate Templates - Check YAML frontmatter, required fields, and structure.

Validates that entity files and templates have proper YAML frontmatter,
required fields based on entity type, and consistent structure.

Usage:
    python validate_templates.py <path> [--fix] [--verbose]
    python validate_templates.py Worlds/Eldermyr
    python validate_templates.py Templates/Characters/Protagonist.md --verbose

Examples:
    python validate_templates.py Worlds/Eldermyr           # Validate all entities in world
    python validate_templates.py Templates/                # Validate all templates
    python validate_templates.py Worlds/Eldermyr --fix     # Fix auto-fixable issues
"""

import argparse
import io
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import yaml

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# Universal required fields for all entities
UNIVERSAL_REQUIRED = ['tags', 'name', 'status']

# Valid status values
VALID_STATUS = ['draft', 'in-progress', 'complete']

# Entity-specific required fields based on tags
ENTITY_REQUIRED_FIELDS = {
    'character': ['species', 'alignment', 'location'],
    'protagonist': ['species', 'alignment', 'occupation'],
    'antagonist': ['species', 'alignment', 'occupation'],
    'settlement': ['population', 'government', 'region'],
    'city': ['population', 'government', 'region'],
    'town': ['population', 'government', 'region'],
    'village': ['population', 'region'],
    'organization': ['organization_type', 'headquarters'],
    'geography': ['geography_type', 'climate', 'terrain'],
    'region': ['climate', 'terrain'],
    'creature': ['creature_type', 'size', 'challenge_rating'],
    'monster': ['creature_type', 'size', 'challenge_rating'],
    'item': ['item_type', 'rarity'],
    'weapon': ['weapon_type', 'damage', 'rarity'],
    'armor': ['armor_type', 'base_ac', 'rarity'],
    'deity': ['domains', 'alignment', 'symbol'],
    'history': ['date', 'location'],
    'event': ['date', 'location'],
    'encounter': ['encounter_type', 'difficulty', 'party_level'],
}


class ValidationResult:
    """Container for validation results."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.fixable: List[Tuple[str, str]] = []  # (issue, fix_description)

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def add_error(self, message: str, fixable: bool = False, fix_desc: str = None):
        self.errors.append(message)
        if fixable and fix_desc:
            self.fixable.append((message, fix_desc))

    def add_warning(self, message: str):
        self.warnings.append(message)

    def add_info(self, message: str):
        self.info.append(message)


def extract_yaml_frontmatter(content: str) -> Tuple[Optional[dict], int, int, str]:
    """Extract YAML frontmatter from markdown content.

    Returns (yaml_dict, start_pos, end_pos, error_message).
    """
    if not content.startswith('---'):
        return None, -1, -1, "No YAML frontmatter found (file must start with ---)"

    # Find the closing ---
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return None, -1, -1, "Unclosed YAML frontmatter (missing closing ---)"

    yaml_end = end_match.start() + 3
    yaml_content = content[4:yaml_end]

    try:
        data = yaml.safe_load(yaml_content)
        if data is None:
            return {}, 0, yaml_end + end_match.end() - end_match.start(), None
        return data, 0, yaml_end + end_match.end() - end_match.start(), None
    except yaml.YAMLError as e:
        return None, -1, -1, f"Invalid YAML syntax: {e}"


def validate_file(file_path: Path, verbose: bool = False) -> ValidationResult:
    """Validate a single file."""
    result = ValidationResult(file_path)

    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        result.add_error(f"Cannot read file: {e}")
        return result

    # Extract YAML frontmatter
    yaml_data, start, end, error = extract_yaml_frontmatter(content)

    if error:
        result.add_error(error)
        return result

    if yaml_data is None:
        yaml_data = {}

    # Check universal required fields
    for field in UNIVERSAL_REQUIRED:
        if field not in yaml_data:
            result.add_error(f"Missing required field: {field}",
                           fixable=True, fix_desc=f"Add {field}: '' to frontmatter")
        elif yaml_data[field] is None or yaml_data[field] == '':
            if field != 'image':  # image can be empty
                result.add_warning(f"Field '{field}' is empty")

    # Check status value
    if 'status' in yaml_data:
        status = yaml_data['status']
        if status and status not in VALID_STATUS:
            result.add_error(f"Invalid status '{status}'. Must be one of: {', '.join(VALID_STATUS)}",
                           fixable=True, fix_desc=f"Change status to 'draft'")

    # Check tags and entity-specific fields
    tags = yaml_data.get('tags', [])
    if not tags:
        result.add_warning("No tags defined")
    elif isinstance(tags, list):
        for tag in tags:
            if tag in ENTITY_REQUIRED_FIELDS:
                for field in ENTITY_REQUIRED_FIELDS[tag]:
                    if field not in yaml_data:
                        result.add_warning(f"Missing recommended field for {tag}: {field}")

    # Check aliases format
    aliases = yaml_data.get('aliases', [])
    if aliases is not None and not isinstance(aliases, list):
        result.add_error("'aliases' must be a list",
                        fixable=True, fix_desc="Convert aliases to list format")

    # Check for H1 heading
    body = content[end:] if end > 0 else content
    h1_match = re.search(r'^# .+', body, re.MULTILINE)
    if not h1_match:
        result.add_warning("No H1 heading found in document body")

    # Check for wikilinks in connections section
    connections_match = re.search(r'## Connections?\s*\n(.*?)(?=\n##|\Z)', body, re.DOTALL | re.IGNORECASE)
    if connections_match:
        connections_text = connections_match.group(1)
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', connections_text)
        if not wikilinks:
            result.add_info("Connections section exists but has no wikilinks")
        elif verbose:
            result.add_info(f"Found {len(wikilinks)} connections")

    # Check numeric fields for valid ranges
    numeric_checks = {
        'level': (1, 20, "Level"),
        'armor_class': (1, 30, "AC"),
        'strength': (1, 30, "STR"),
        'dexterity': (1, 30, "DEX"),
        'constitution': (1, 30, "CON"),
        'intelligence': (1, 30, "INT"),
        'wisdom': (1, 30, "WIS"),
        'charisma': (1, 30, "CHA"),
    }

    for field, (min_val, max_val, display) in numeric_checks.items():
        if field in yaml_data and yaml_data[field] is not None:
            try:
                val = int(yaml_data[field])
                if val < min_val or val > max_val:
                    result.add_warning(f"{display} value {val} outside expected range ({min_val}-{max_val})")
            except (ValueError, TypeError):
                pass  # Non-numeric value, might be intentional

    if verbose:
        result.add_info(f"YAML fields found: {', '.join(yaml_data.keys())}")

    return result


def validate_directory(dir_path: Path, verbose: bool = False) -> List[ValidationResult]:
    """Validate all .md files in a directory recursively."""
    results = []

    for file_path in sorted(dir_path.rglob('*.md')):
        # Skip certain files
        if file_path.name in ['README.md', 'World Overview.md']:
            continue
        if '.obsidian' in str(file_path):
            continue

        result = validate_file(file_path, verbose)
        results.append(result)

    return results


def apply_fixes(file_path: Path, result: ValidationResult) -> bool:
    """Apply auto-fixes to a file. Returns True if changes were made."""
    if not result.fixable:
        return False

    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception:
        return False

    yaml_data, start, end, error = extract_yaml_frontmatter(content)
    if error or yaml_data is None:
        return False

    modified = False

    # Add missing universal fields
    for field in UNIVERSAL_REQUIRED:
        if field not in yaml_data:
            if field == 'tags':
                yaml_data[field] = []
            elif field == 'status':
                yaml_data[field] = 'draft'
            else:
                yaml_data[field] = ''
            modified = True

    # Fix invalid status
    if 'status' in yaml_data and yaml_data['status'] not in VALID_STATUS:
        yaml_data['status'] = 'draft'
        modified = True

    # Convert aliases to list if needed
    if 'aliases' in yaml_data and not isinstance(yaml_data['aliases'], list):
        yaml_data['aliases'] = [yaml_data['aliases']] if yaml_data['aliases'] else []
        modified = True

    if modified:
        # Reconstruct the file
        body = content[end:]
        new_yaml = yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_yaml}---{body}"
        file_path.write_text(new_content, encoding='utf-8')
        return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description='Validate templates and entity files for proper YAML and structure.'
    )
    parser.add_argument('path', help='File or directory to validate')
    parser.add_argument('--fix', action='store_true', help='Apply auto-fixes where possible')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed output')
    parser.add_argument('--quiet', '-q', action='store_true', help='Only show errors')

    args = parser.parse_args()

    target = Path(args.path)

    if not target.exists():
        # Try relative to script location
        script_dir = Path(__file__).parent.parent
        target = script_dir / args.path
        if not target.exists():
            print(f"Error: Path not found: {args.path}")
            sys.exit(1)

    if target.is_file():
        results = [validate_file(target, args.verbose)]
    else:
        results = validate_directory(target, args.verbose)

    # Process results
    total_files = len(results)
    valid_files = sum(1 for r in results if r.is_valid)
    total_errors = sum(len(r.errors) for r in results)
    total_warnings = sum(len(r.warnings) for r in results)
    fixes_applied = 0

    for result in results:
        if not result.errors and not result.warnings and args.quiet:
            continue

        if result.errors or result.warnings or args.verbose:
            print(f"\n{result.file_path.name}")
            print("-" * len(result.file_path.name))

        for error in result.errors:
            print(f"  ERROR: {error}")

        if not args.quiet:
            for warning in result.warnings:
                print(f"  WARNING: {warning}")

        if args.verbose:
            for info in result.info:
                print(f"  INFO: {info}")

        if args.fix and result.fixable:
            if apply_fixes(result.file_path, result):
                fixes_applied += 1
                print(f"  FIXED: Applied {len(result.fixable)} auto-fixes")

    # Summary
    print(f"\n{'='*50}")
    print(f"Validation Summary")
    print(f"{'='*50}")
    print(f"Files checked: {total_files}")
    print(f"Valid files: {valid_files}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    if args.fix:
        print(f"Files fixed: {fixes_applied}")

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == '__main__':
    main()
