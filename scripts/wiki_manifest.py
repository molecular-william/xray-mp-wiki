#!/usr/bin/env python3
"""
Manage the wiki DOI processing manifest.

The manifest tracks which DOIs from raw/papers/ have been processed into
YAML sources (xray-mp-wiki/*_yaml/) and which remain pending.

Manifest structure:
{
  "last_run": "...",
  "entity_index": {
    "kcsa": {
      "path": "proteins/kcsa.md",
      "type": "proteins",
      "source_dois": ["10.1073##pnas.1901888116", ...],
      "last_updated": "2026-06-11"
    }
  },
  "processed": {
    "10.1073##pnas.1901888116": {"status": "done", "comments": "ok"}
  },
  "current_batch": {
    "10.xxxx##yyyy": {"status": "pending"}
  }
}

Usage:
  python scripts/wiki_manifest.py rebuild [--skip-file references/known-skip-dois.md]
    Rebuild manifest from filesystem truth.
    Scans raw/papers/*.md for all DOIs and xray-mp-wiki/*_yaml/*.yaml
    for processed DOIs. Computes pending = raw - yaml.
    Optionally loads skips from a file (one DOI per line).

  python scripts/wiki_manifest.py status
    Print current manifest state.

  python scripts/wiki_manifest.py reset
    Delete the manifest file.

  python scripts/wiki_manifest.py load
    Print pending DOIs (one per line).

  python scripts/wiki_manifest.py check-entity <name>
    Check if entity exists in the wiki.

  python scripts/wiki_manifest.py update-entity-index
    Rebuild entity_index from YAML files on disk.
"""

import json
import sys
from datetime import date
from pathlib import Path

import yaml as yaml_lib

BASE_DIR = Path(__file__).parent.parent
MANIFEST_PATH = BASE_DIR / "wiki_manifest.json"
RAW_DIR = BASE_DIR / "raw/papers"
YAML_DIRS = {
    "proteins": BASE_DIR / "xray-mp-wiki/proteins_yaml",
    "reagents": BASE_DIR / "xray-mp-wiki/reagents_yaml",
    "methods": BASE_DIR / "xray-mp-wiki/methods_yaml",
    "concepts": BASE_DIR / "xray-mp-wiki/concepts_yaml",
}


# ---------------------------------------------------------------------------
# Module-level overrides for testing
# ---------------------------------------------------------------------------
def _get_raw_dir():
    return Path(BASE_DIR) / "raw/papers"


def _get_yaml_dirs():
    return {
        "proteins": Path(BASE_DIR) / "xray-mp-wiki/proteins_yaml",
        "reagents": Path(BASE_DIR) / "xray-mp-wiki/reagents_yaml",
        "methods": Path(BASE_DIR) / "xray-mp-wiki/methods_yaml",
        "concepts": Path(BASE_DIR) / "xray-mp-wiki/concepts_yaml",
    }


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------


def load_manifest():
    """Load manifest from disk, or return empty structure."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {
        "last_run": "",
        "entity_index": {},
        "processed": {},
        "current_batch": {},
    }


def save_manifest(manifest):
    """Write manifest to disk."""
    manifest["last_run"] = str(date.today())
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Saved {MANIFEST_PATH}")


# ---------------------------------------------------------------------------
# Filesystem scanning (YAML-first — source of truth)
# ---------------------------------------------------------------------------


def scan_yaml_entity_index():
    """Build entity_index from YAML source files (*_yaml/*.yaml).

    Returns:
        dict: entity_name -> {path, type, source_dois, last_updated, title}
    """
    entity_index = {}

    for etype, yaml_dir in _get_yaml_dirs().items():
        if not yaml_dir.exists():
            continue

        for yf in sorted(yaml_dir.glob("*.yaml")):
            entity_name = yf.stem
            try:
                data = yaml_lib.safe_load(yf.read_text())
            except Exception:
                data = None

            sources = []
            last_updated = ""
            title = entity_name
            if isinstance(data, dict):
                raw_sources = data.get("sources", []) or []
                for s in raw_sources:
                    doi = str(s).strip().replace("doi/", "")
                    if doi:
                        sources.append(doi)
                last_updated = str(data.get("updated", "")) or ""
                title = str(data.get("title", entity_name))

            # Build path as it would appear after page generation
            path = f"{etype}/{entity_name}.md"

            entity_index[entity_name] = {
                "path": path,
                "type": etype,
                "source_dois": sources,
                "last_updated": last_updated,
                "title": title,
                "uniprot_id": str(data.get("uniprot_id", "")) if isinstance(data, dict) else "",
            }

    return entity_index


def scan_raw_dois():
    """Return set of all DOI stems from raw/papers/ (lowercased).

    Uses case-insensitive glob via listdir + lower() to handle
    mixed-case filenames like 10.1073##PNAS.xxx.md.
    """
    raw_dir = _get_raw_dir()
    if not raw_dir.exists():
        return set()
    dois = set()
    for f in raw_dir.iterdir():
        if f.is_file() and f.suffix.lower() == ".md":
            dois.add(f.stem.lower())
    return dois


def scan_yaml_dois():
    """Return set of all unique DOIs referenced in YAML sources (lowercased).

    Also returns the entity_index as a bonus.
    """
    yaml_dois = set()
    entity_index = scan_yaml_entity_index()
    for info in entity_index.values():
        for doi in info["source_dois"]:
            yaml_dois.add(doi.lower())
    return yaml_dois, entity_index


def load_skip_dois(skip_path=None):
    """Load skip DOIs from a file (one DOI per line, # comments ignored).

    Args:
        skip_path: Path to skip file. If None, look for
                   references/known-skip-dois.md in project root.

    Returns:
        set of lowercased DOI strings
    """
    if skip_path:
        p = Path(skip_path)
    else:
        p = BASE_DIR / "references/known-skip-dois.md"

    if not p.exists():
        return set()

    skips = set()
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Strip leading '- ' if file uses markdown list format
        line = line.lstrip("- ").strip()
        # Strip trailing comment: first standalone '#' not part of '##'
        # Use regex to find # preceded by a space (inline comment marker)
        import re

        m = re.search(r"\s+#\s+", line)
        if m:
            line = line[: m.start()].strip()
        elif " #" in line and "##" not in line:
            line = line.split("#")[0].strip()
        if line:
            skips.add(line.lower())
    return skips


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def cmd_rebuild(skip_path=None):
    """Rebuild manifest from filesystem truth.

    1. Scan raw/papers/ for all DOIs
    2. Scan * _yaml/ for source DOIs → processed
    3. Compute pending = raw − yaml
    4. Build entity_index from YAMLs
    5. Optionally load skip classifications
    """
    raw_dois = scan_raw_dois()
    yaml_dois, entity_index = scan_yaml_dois()
    skip_dois = load_skip_dois(skip_path)

    processed_raw = raw_dois & yaml_dois
    pending_raw = raw_dois - yaml_dois

    # Build processed dict
    processed = {}
    for doi in sorted(raw_dois):
        if doi in processed_raw:
            processed[doi] = {"status": "done"}
        elif doi in skip_dois:
            processed[doi] = {"status": "done", "comments": "skip — not a membrane protein"}

    # Build current_batch = remaining unprocessed DOIs not skipped
    current_batch = {}
    for doi in sorted(pending_raw):
        if doi not in skip_dois:
            current_batch[doi] = {"status": "pending"}

    manifest = {
        "last_run": str(date.today()),
        "entity_index": entity_index,
        "processed": processed,
        "current_batch": current_batch,
    }

    save_manifest(manifest)

    # Print summary
    print("\nManifest rebuilt from filesystem:")
    print(f"  Raw papers:           {len(raw_dois)}")
    print(f"  YAML source DOIs:     {len(yaml_dois)}")
    print(f"  Processed (raw∩yaml): {len(processed_raw)}")
    print(f"  Skipped:              {len(skip_dois & raw_dois)}")
    print(f"  Pending:              {len(current_batch)}")
    print(f"  Entity index:         {len(entity_index)}")

    # Show breakdown
    type_counts = {}
    for info in entity_index.values():
        t = info["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    if type_counts:
        print(f"    by type: {', '.join(f'{k}={v}' for k, v in sorted(type_counts.items()))}")

    return manifest


def cmd_status():
    """Print current manifest state."""
    manifest = load_manifest()

    if not manifest.get("entity_index") and not manifest.get("processed"):
        print("Manifest not built yet. Run: python scripts/wiki_manifest.py rebuild")
        return

    print(f"Last run:     {manifest.get('last_run', 'never')}")
    print(f"Processed:    {len(manifest.get('processed', {}))}")
    print(f"Entities:     {len(manifest.get('entity_index', {}))}")
    print(f"Pending:      {len(manifest.get('current_batch', {}))}")

    if manifest.get("current_batch"):
        items = list(manifest["current_batch"].items())
        print(f"\nFirst {min(10, len(items))} pending:")
        for doi, _ in items[:10]:
            print(f"  {doi}")
        if len(items) > 10:
            print(f"  ... and {len(items) - 10} more")

    if manifest.get("processed"):
        # Count skips
        skip_count = sum(1 for v in manifest["processed"].values() if "skip" in v.get("comments", ""))
        print(f"\n  (includes {skip_count} skipped DOIs)")

    # Type breakdown from entity_index
    type_counts = {}
    for info in manifest.get("entity_index", {}).values():
        t = info.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
    if type_counts:
        print(f"  Entity types: {', '.join(f'{k}={v}' for k, v in sorted(type_counts.items()))}")


def cmd_reset():
    """Delete the manifest file."""
    if MANIFEST_PATH.exists():
        MANIFEST_PATH.unlink()
        print(f"Deleted {MANIFEST_PATH}")
    else:
        print("Manifest not found.")


def cmd_load():
    """Print pending DOIs, one per line."""
    manifest = load_manifest()
    for doi, info in manifest.get("current_batch", {}).items():
        if info.get("status") == "pending":
            print(doi)


def check_entity(entity_name):
    """Check if an entity exists in the wiki.

    Args:
        entity_name: Entity name (e.g., "kcsa")

    Returns:
        dict with: exists (bool), info (dict or None), action ("update"/"create")
    """
    manifest = load_manifest()
    entity_index = manifest.get("entity_index", {})

    if entity_name in entity_index:
        return {
            "exists": True,
            "info": entity_index[entity_name],
            "action": "update",
        }
    else:
        return {
            "exists": False,
            "info": None,
            "action": "create",
        }


def cmd_update_entity_index():
    """Rebuild entity_index from YAML files on disk."""
    print("Scanning YAML files to build entity_index...")
    entity_index = scan_yaml_entity_index()
    manifest = load_manifest()
    manifest["entity_index"] = entity_index
    save_manifest(manifest)

    print(f"Entity index built: {len(entity_index)} entities")
    type_counts = {}
    for info in entity_index.values():
        t = info["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    for t, c in sorted(type_counts.items()):
        print(f"  {t}: {c}")


# ---------------------------------------------------------------------------
# CLI dispatch
# ---------------------------------------------------------------------------


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "rebuild":
        skip_path = None
        if "--skip-file" in sys.argv:
            idx = sys.argv.index("--skip-file")
            if idx + 1 < len(sys.argv):
                skip_path = sys.argv[idx + 1]
        cmd_rebuild(skip_path)

    elif cmd == "status":
        cmd_status()

    elif cmd == "reset":
        cmd_reset()

    elif cmd == "load":
        cmd_load()

    elif cmd == "update-entity-index":
        cmd_update_entity_index()

    elif cmd == "check-entity":
        if len(sys.argv) < 3:
            print("Usage: wiki_manifest.py check-entity <entity_name>")
            sys.exit(1)
        result = check_entity(sys.argv[2])
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["exists"] else 1)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
