#!/usr/bin/env python3
"""Rebuild references/entity_catalog.json from manifest or YAML files on disk.

By default reads from wiki_manifest.json (fast — reuses manifest's scan).
Use --from-filesystem to scan YAML files directly (slow but independent).

Usage:
  python3 scripts/rebuild_entity_catalog.py
  python3 scripts/rebuild_entity_catalog.py --from-filesystem
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import yaml  # noqa: F401 — side-effect guard: exit if PyYAML missing
except ImportError:
    print("Error: PyYAML not installed. Install with: pip install pyyaml")
    sys.exit(1)

from _base import BASE_DIR, fast_load_str, parallel_load_yamls

WIKI_ROOT = BASE_DIR / "xray-mp-wiki"
CATALOG_PATH = BASE_DIR / "references" / "entity_catalog.json"
MANIFEST_PATH = BASE_DIR / "wiki_manifest.json"
YAML_DIRS = ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]


def build_from_manifest():
    """Build catalog from the manifest's entity_index (fast — no YAML re-scan)."""
    if not MANIFEST_PATH.exists():
        print("Manifest not found. Run 'wiki_manifest.py rebuild' first, or use --from-filesystem.")
        return {}

    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

    catalog = {}
    entity_index = manifest.get("entity_index", {})
    for key, info in entity_index.items():
        catalog[key] = {
            "type": info.get("type", "proteins"),
            "title": info.get("title", key),
            "filename": f"{key}.md",
            "uniprot_id": info.get("uniprot_id", ""),
        }
    return catalog


def build_from_filesystem():
    """Build catalog by scanning all YAML files using parallel loader."""
    catalog = {}
    for d in YAML_DIRS:
        yaml_dir = WIKI_ROOT / d
        if not yaml_dir.exists():
            continue
        paths = sorted(yaml_dir.glob("*.yaml"))
        for path, data in parallel_load_yamls(paths):
            if data and "title" in data:
                catalog[path.stem] = {
                    "type": d.replace("_yaml", ""),
                    "title": data["title"],
                    "filename": f"{path.stem}.md",
                }
    return catalog


def main():
    use_filesystem = "--from-filesystem" in sys.argv

    if use_filesystem:
        catalog = build_from_filesystem()
        source = "filesystem scan"
    else:
        catalog = build_from_manifest()
        source = "manifest entity_index"

    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2))
    print(f"entity_catalog.json: {len(catalog)} entries written from {source}")


if __name__ == "__main__":
    main()
