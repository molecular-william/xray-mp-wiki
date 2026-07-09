#!/usr/bin/env python3
"""Rebuild the wiki catalog table in index.md from actual files on disk.

Scans all category directories, reads frontmatter titles from every page,
and adds missing entries to the catalog table. Idempotent — running multiple
times produces identical output. Safe to run alongside generate/update scripts
(which call maintain_catalog() for single-entry updates).

Also supports batch processing mode (subagent result merging) via --results flag.

Usage:
  python scripts/rebuild_indexes.py [--force]
  python scripts/rebuild_indexes.py --results <json_file> [--force] [--lint]

  --force   Rebuild entire table from scratch (remove all entries, rescan).
            Default: add only missing entries (merge mode).
  --results <path>  Process batch results from subagent JSON file.
  --lint              Run lint.py after processing and exit on failure.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Batch processing imports
import json

from _base import collect_pages, rebuild_catalog
from wiki_manifest import cmd_update_entity_index, load_manifest


def update_manifest_from_results(results_file):
    """Update manifest, CSV, and entity_index from subagent results.

    Args:
        results_file: path to JSON file with subagent results

    Returns:
        number of DOIs processed
    """
    if not Path(results_file).exists():
        print(f"Error: Results file not found: {results_file}")
        return 0

    with open(results_file) as f:
        results = json.load(f)

    if not isinstance(results, list):
        print("Error: Results file must contain a JSON array")
        return 0

    manifest = load_manifest()

    # Group results by DOI
    doi_results = {}
    for result in results:
        doi = result.get("doi", "")
        if not doi:
            continue
        if doi not in doi_results:
            doi_results[doi] = {
                "status": result.get("status", "done"),
                "pages": [],
                "entity_names": [],
                "entity_type": result.get("entity_type", "protein"),
                "actions": [],
                "comments": result.get("comments", ""),
            }
        if result.get("page_path"):
            doi_results[doi]["pages"].append(result["page_path"])
        if result.get("entity_names"):
            doi_results[doi]["entity_names"].extend(result["entity_names"])
        if result.get("actions"):
            doi_results[doi]["actions"].extend(result["actions"])

    # Move DOIs from current_batch to processed
    moved = 0
    skipped = 0
    for doi, info in doi_results.items():
        if doi in manifest["current_batch"]:
            del manifest["current_batch"][doi]
            moved += 1
        else:
            skipped += 1

        manifest["processed"][doi] = {
            "status": info["status"],
            "pages": info["pages"],
            "entity_names": info["entity_names"],
            "entity_type": info["entity_type"],
            "actions": info["actions"],
            "comments": info["comments"],
        }

    # Save manifest
    from wiki_manifest import save_manifest

    save_manifest(manifest)
    print(f"Manifest updated: {moved} DOIs moved to processed, {skipped} already processed")

    # CSV update is deprecated — manifest is the source of truth
    pass

    # Rebuild entity_index
    cmd_update_entity_index()

    return moved


def run_lint():
    """Run lint.py to check for issues."""
    import subprocess

    print("Running lint check...")
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "lint.py")],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent.parent),
    )

    if result.returncode == 0:
        print("Lint passed: no issues found")
    else:
        print("Lint found issues:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)

    return result.returncode == 0


def main():
    force = "--force" in sys.argv
    results_file = None
    lint_flag = "--lint" in sys.argv

    # Parse --results flag
    if "--results" in sys.argv:
        idx = sys.argv.index("--results")
        if idx + 1 < len(sys.argv):
            results_file = sys.argv[idx + 1]
        else:
            print("Error: --results requires a file path")
            sys.exit(1)

    if results_file:
        # Batch processing mode
        print(f"Processing batch results from {results_file}...")
        moved = update_manifest_from_results(results_file)
        if moved == 0:
            print("No DOIs were moved. Check results file format.")
            sys.exit(1)

        # Rebuild catalog
        print("Rebuilding wiki catalog...")
        entries = collect_pages()
        print(f"  Found {len(entries)} pages across 4 categories")
        added = rebuild_catalog(entries, force=force)
        print(f"  Added {added} new entries to catalog")

        # Run lint if requested
        if lint_flag:
            if not run_lint():
                print("Exiting due to lint failures.")
                sys.exit(1)

        print(f"Batch processing complete: {moved} DOIs processed")
    else:
        # Standard catalog rebuild mode
        print(f"Rebuilding wiki catalog (force={force})...")
        entries = collect_pages()
        print(f"  Found {len(entries)} pages across 4 categories")
        added = rebuild_catalog(entries, force=force)
        print(f"  Added {added} new entries to catalog")

        if force:
            print(f"  Total entries: {len(entries)}")

        # Run lint if requested
        if lint_flag:
            if not run_lint():
                print("Exiting due to lint failures.")
                sys.exit(1)


if __name__ == "__main__":
    main()
