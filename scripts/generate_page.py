#!/usr/bin/env python3
"""
Unified page generator for xray-mp-wiki.

Usage:
  python generate_page.py <type> <name> [--dry-run] [--diff] [--yes]

Examples:
  python generate_page.py protein atpcc1
  python generate_page.py reagent ddm --dry-run
  python generate_page.py method size-exclusion-chromatography --diff
  python generate_page.py concept biased-agonism --yes

Entity types: protein, reagent, method, concept

Input:  xray-mp-wiki/<type>s_yaml/<name>.yaml
Output: xray-mp-wiki/<type>s/<name>.md (or subdirectory for reagents/methods)

Options:
  --dry-run   Print generated page to stdout without writing
  --diff      Show unified diff against existing page before writing
  --yes       Skip overwrite confirmation
"""

import sys
from pathlib import Path

# Add scripts directory and renderers subdirectory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "renderers"))

from _base import (
    BASE_DIR,
    find_concept_subdir,
    find_method_subdir,
    find_protein_subdir,
    find_reagent_subdir,
    generate_main,
    load_yaml,
    parse_args,
)

# Entity type configuration
TYPE_CONFIG = {
    "protein": {
        "yaml_dir": "proteins_yaml",
        "output_dir": "proteins",
        "renderer": "protein_page_renderer",
        "subdir_fn": find_protein_subdir,
    },
    "reagent": {
        "yaml_dir": "reagents_yaml",
        "output_dir": "reagents",
        "renderer": "reagent_page_renderer",
        "subdir_fn": find_reagent_subdir,
    },
    "method": {
        "yaml_dir": "methods_yaml",
        "output_dir": "methods",
        "renderer": "method_page_renderer",
        "subdir_fn": find_method_subdir,
    },
    "concept": {
        "yaml_dir": "concepts_yaml",
        "output_dir": "concepts",
        "renderer": "concept_page_renderer",
        "subdir_fn": find_concept_subdir,
    },
}


def make_subdir_fn(config):
    """Return closure that adjusts output_path by entity type's subdir."""
    finder = config["subdir_fn"]
    if finder is None:
        return None

    def subdir_fn(yaml_path, output_path, name):
        yaml_data = load_yaml(yaml_path)
        subdir = finder(yaml_data, name)
        if subdir:
            output_path = Path(output_path).parent / subdir / f"{name}.md"
        return output_path

    return subdir_fn


def main():
    if len(sys.argv) < 3:
        print("Usage: generate_page.py <type> <name> [--dry-run] [--diff] [--yes]")
        print("Types: protein, reagent, method, concept")
        sys.exit(1)

    entity_type = sys.argv[1]
    name = sys.argv[2]

    if entity_type not in TYPE_CONFIG:
        print(f"Error: Unknown type '{entity_type}'. Must be one of: {', '.join(TYPE_CONFIG.keys())}")
        sys.exit(1)

    config = TYPE_CONFIG[entity_type]

    # Build paths (always flat output path first)
    yaml_path = BASE_DIR / "xray-mp-wiki" / config["yaml_dir"] / f"{name}.yaml"
    output_path = BASE_DIR / "xray-mp-wiki" / config["output_dir"] / f"{name}.md"

    # Get subdirectory adjustment function (generate_main will call it)
    subdir_fn = make_subdir_fn(config)

    # Import renderer module
    renderer = __import__(config["renderer"])

    # Parse args (skip the first 2 args: script name, type, name)
    extra_args = [a for a in sys.argv[3:]]
    parse_args(extra_args, entity_type, ["yes"])
    skip_catalog = "--skip-catalog" in sys.argv

    # Generate - subdir_fn will be called by generate_main internally
    generate_main(renderer, name, yaml_path, output_path, subdir_fn, skip_catalog=skip_catalog)


if __name__ == "__main__":
    main()
