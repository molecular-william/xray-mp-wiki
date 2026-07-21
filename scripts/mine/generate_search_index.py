#!/usr/bin/env python3
"""Generate _data/search_index.json for client-side search.
Reads entity_catalog.json + filesystem to get title/path/tags per entity.
Run after any rebuild_entity_catalog pass."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE / "xray-mp-wiki" / "_data"
CATALOG = BASE / "references/entity_catalog.json"

# Build slug→path mapping from rendered .md pages
slug_to_path = {}
for pattern in ["proteins/*/*.md", "reagents/*/*.md", "methods/*/*.md", "concepts/*/*.md"]:
    for f in (BASE / "xray-mp-wiki").glob(pattern):
        slug = f.stem
        rel = f.relative_to(BASE / "xray-mp-wiki")
        slug_to_path[slug] = "/xray-mp-wiki/" + str(rel.parent) + "/" + slug + "/"

catalog = json.loads(CATALOG.read_text()) if CATALOG.exists() else {}

entries = []
for slug, entry in catalog.items():
    if not isinstance(entry, dict):
        continue
    etype = entry.get("type", "")
    title = entry.get("title", slug)
    path = slug_to_path.get(slug, f"/xray-mp-wiki/{etype}/{slug}/")
    entries.append({
        "title": title,
        "slug": slug,
        "type": etype.rstrip("s"),  # "proteins" → "protein"
        "path": path,
        "tags": entry.get("tags", []),
        "category_display": {"protein": "Protein", "reagent": "Reagent",
                             "method": "Method", "concept": "Concept"}.get(etype.rstrip("s"), etype),
    })

DATA_DIR.mkdir(parents=True, exist_ok=True)
out = DATA_DIR / "search_index.json"
with open(out, "w") as f:
    json.dump(entries, f, indent=2)
print(f"Wrote {len(entries)} entries to {out}")
