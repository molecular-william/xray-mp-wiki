#!/usr/bin/env python3
"""
Enrich wiki YAML files with inline wikilinks and cross-references.

Usage:
  YAML_TYPE=concepts_yaml DRY_RUN=1 python3 scripts/enrich_wikilinks.py
  YAML_TYPE=reagents_yaml python3 scripts/enrich_wikilinks.py

Entity types: proteins_yaml, reagents_yaml, methods_yaml, concepts_yaml
"""

import json
import os
import re
import sys
from pathlib import Path

DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"
FIRST_N = int(os.environ.get("FIRST_N", "0")) or None
YAML_TYPE = os.environ.get("YAML_TYPE", "proteins_yaml")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INNER_WIKI = PROJECT_ROOT / "xray-mp-wiki"
YAML_DIR = INNER_WIKI / YAML_TYPE
CATALOG_PATH = PROJECT_ROOT / "references" / "entity_catalog.json"
MAX_CROSS_REFS = 10
MIN_MATCH_LEN = 3

SKIP_FIELDS = {
    "title",
    "tags",
    "sources",
    "type",
    "category",
    "layout",
    "created",
    "updated",
    "pdb_id",
    "verified",
    "space_group",
    "cell_dimensions",
    "r_work_r_free",
}
SKIP_RECURSE = {"cross_references", "cross_refs_text", "related_concepts", "related_concepts_text"}
EXTRA_SKIP_REAGENT = {
    "chemical_name",
    "heavy_atom",
    "synthesis",
    "molecular_weight",
    "solubility",
    "stability",
    "storage",
    "cas_number",
    "formula",
    "purity",
    "source_vendor",
    "catalog_number",
}

# Load enrichment data from JSON file (data extracted from code for maintainability)
_DATA_PATH = Path(__file__).resolve().parent / "enrich_wikilinks_data.json"
with open(_DATA_PATH) as _f:
    _ENRICH_DATA = json.load(_f)
STOPLIST = set(_ENRICH_DATA["STOPLIST"])
ALWAYS_LINK = set(_ENRICH_DATA["ALWAYS_LINK"])
DISPLAY_OVERRIDES = {k: v for k, v in _ENRICH_DATA["DISPLAY_OVERRIDES"].items()}


def load_catalog():
    with open(CATALOG_PATH) as f:
        catalog = json.load(f)
    page_paths = {}
    for od in ["proteins", "reagents", "methods", "concepts"]:
        for pf in (INNER_WIKI / od).rglob("*.md"):
            rel = pf.relative_to(INNER_WIKI)
            page_paths[pf.stem] = f"/xray-mp-wiki/{rel.parent}/{pf.stem}/"
    aliases = []
    for key, info in catalog.items():
        title = info.get("title", key)
        fn = info.get("filename", f"{key}.md")
        stem = fn.replace(".md", "")
        path = page_paths.get(stem)
        if not path:
            path = f"/xray-mp-wiki/{info.get('type', 'proteins')}/{stem}/"
        kl = key.lower()
        if kl in STOPLIST:
            continue
        display = determine_display(key, title)
        tier = classify_tier(key, kl, display)
        aliases.append((kl, display, path, tier))
        am = re.search(r"\(([A-Z][A-Z0-9\-_]+)\)\s*$", title)
        if am:
            acro = am.group(1).lower()
            if acro != kl and len(acro) >= 2:
                aliases.append((acro, display, path, "HIGH"))
        dlow = display.lower().replace("-", " ").replace("_", " ")
        if dlow != kl and len(dlow) >= 5 and dlow not in STOPLIST:
            words = dlow.split()
            if len(words) >= 2:
                aliases.append((dlow, display, path, "MEDIUM"))
    aliases.sort(key=lambda a: -len(a[0]))
    return aliases, page_paths


def determine_display(key, title):
    k = key.lower()
    if k in DISPLAY_OVERRIDES:
        return DISPLAY_OVERRIDES[k]
    am = re.search(r"\(([A-Z][A-Z0-9\-_]+)\)\s*$", title)
    if am:
        return am.group(1)
    if len(key) <= 6 and key.isalpha() and key.islower():
        return key.upper()
    return title


def classify_tier(key, kl, display):
    if kl in ALWAYS_LINK:
        return "HIGH"
    if len(kl) < 4:
        return "SKIP"
    if any(c.isdigit() for c in key):
        return "HIGH"
    if len(kl) >= 3 and key.isupper() and key.isalpha():
        return "HIGH"
    if len(kl) <= 10 and ("-" in kl or "_" in kl):
        return "HIGH"
    if " " in display and len(display.split()) >= 2:
        return "MEDIUM"
    if len(kl) >= 6:
        return "LOW"
    return "SKIP"


def get_self_path(filename, page_paths):
    """Look up entity's own page path from pre-built page_paths dict (O(1), not O(N))."""
    fn = filename.replace(".yaml", "")
    path = page_paths.get(fn)
    return path


def normalize_path(p):
    return p.rstrip("/")


def get_plain_regions(text):
    regions = []
    lp = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
    pos = 0
    for m in lp.finditer(text):
        if m.start() > pos:
            regions.append((pos, m.start(), False))
        regions.append((m.start(), m.end(), True))
        pos = m.end()
    if pos < len(text):
        regions.append((pos, len(text), False))
    return regions


def find_matches(text, start, end, aliases, self_paths):
    matches = {}
    region = text[start:end]
    for ename, dname, lpath, tier in aliases:
        if not ename or not lpath or len(ename) < MIN_MATCH_LEN:
            continue
        if self_paths and normalize_path(lpath) in self_paths:
            continue
        pat = re.compile(r"(?<![a-zA-Z0-9_/])" + re.escape(ename) + r"(?![a-zA-Z0-9_\-])", re.IGNORECASE)
        for m in pat.finditer(region):
            ab_s, ab_e = start + m.start(), start + m.end()
            if not any(ab_s < e and ab_e > s for (s, e) in matches):
                matches[(ab_s, ab_e)] = (dname, lpath)
    result = [(s, e, dn, lp) for (s, e), (dn, lp) in matches.items()]
    result.sort(key=lambda x: -x[0])
    return result


def apply_to_string(text, aliases, self_paths):
    if not text or not isinstance(text, str):
        return text, set()
    all_matches = []
    for start, end, is_link in get_plain_regions(text):
        if not is_link:
            all_matches.extend(find_matches(text, start, end, aliases, self_paths))
    if not all_matches:
        return text, set()
    all_matches.sort(key=lambda x: -x[0])
    linked = set()
    result = text
    for start, end, dname, lpath in all_matches:
        result = result[:start] + f"[{dname}]({lpath})" + result[end:]
        linked.add(lpath)
    return result, linked


def walk_and_enrich(obj, aliases, self_paths):
    """Recursively walk YAML dict/list, enriching string values."""
    all_linked = set()
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            kl = str(key).lower()
            if kl in SKIP_FIELDS or kl in SKIP_RECURSE:
                continue
            if kl in EXTRA_SKIP_REAGENT and "reagents" in str(YAML_DIR):
                continue
            if isinstance(value, str):
                nv, linked = apply_to_string(value, aliases, self_paths)
                if linked:
                    obj[key] = nv
                    all_linked.update(linked)
            elif isinstance(value, (dict, list)):
                all_linked.update(walk_and_enrich(value, aliases, self_paths))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, str):
                nv, linked = apply_to_string(item, aliases, self_paths)
                if linked:
                    obj[i] = nv
                    all_linked.update(linked)
            elif isinstance(item, (dict, list)):
                all_linked.update(walk_and_enrich(item, aliases, self_paths))
    return all_linked


def get_reason(path):
    if "/detergents/" in path:
        return "Detergent used in purification or crystallization"
    if "/buffers/" in path:
        return "Buffer component used in purification or crystallization"
    if "/additives/" in path or "/lipids/" in path:
        return "Additive used in purification or crystallization buffers"
    if "/methods/" in path:
        return "Method used in structure determination or purification"
    if "/protein-tags/" in path:
        return "Fusion tag for crystallization or purification"
    if "/concepts/" in path:
        return "Related biological concept"
    if "/ligands/" in path or "/cofactors/" in path:
        return "Related ligand or cofactor"
    if "/proteins/" in path:
        return "Related protein structure"
    if "/antibodies/" in path:
        return "Antibody used in crystallization or binding studies"
    if "/antibiotics/" in path:
        return "Antibiotic used in selection"
    return "Entity mentioned in text"


def get_display(path, aliases):
    np = normalize_path(path)
    for en, dn, lp, ti in aliases:
        if normalize_path(lp) == np:
            return dn
    return path.split("/")[-1].replace("-", " ").title()


def prefilter_aliases(content, aliases):
    cl = content.lower()
    return [a for a in aliases if a[0] in cl]


def enrich_file(fname, aliases, page_paths, dry=False):
    import yaml as yml

    fp = YAML_DIR / fname
    raw = fp.read_text()
    data = yml.safe_load(raw)
    if not isinstance(data, dict):
        print(f"  SKIP {fname}: not a dict")
        return None

    sp = get_self_path(fname, page_paths)
    sps = {normalize_path(sp)} if sp else set()
    fa = prefilter_aliases(raw, aliases)
    dc = data
    linked = walk_and_enrich(dc, fa, sps)

    existing = dc.get("cross_references", []) or []
    exist_paths = {normalize_path(r.get("path", "")) for r in existing if isinstance(r, dict)}
    avail = MAX_CROSS_REFS - len(existing)
    added_cr = 0

    for lp in sorted(linked):
        if added_cr >= avail:
            break
        np = normalize_path(lp)
        if np in exist_paths or (sps and np in sps):
            continue
        existing.append({"path": lp, "title": get_display(lp, fa), "reason": get_reason(lp)})
        exist_paths.add(np)
        added_cr += 1
    dc["cross_references"] = existing

    tag = " (DRY RUN)" if dry else ""
    if not linked:
        print(f"  {fname}: no links{tag}")
        return {"file": fname, "wikilinks": 0, "cross_refs": 0}
    print(f"  {fname}: {len(linked)} links, {added_cr} cross-refs{tag}")

    if not dry:
        fp.write_text(yml.dump(dc, default_flow_style=False, allow_unicode=True, sort_keys=False))
        import subprocess

        etype = (
            "method"
            if "methods" in str(YAML_DIR)
            else "reagent"
            if "reagents" in str(YAML_DIR)
            else "protein"
            if "proteins" in str(YAML_DIR)
            else "concept"
        )
        r = subprocess.run(
            [sys.executable, "scripts/validate_yaml.py", etype, fname.replace(".yaml", ""), "--strict"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
        )
        if r.returncode != 0:
            print(f"  ⚠ VALIDATION FAILED for {fname}")
            print(f"     {r.stdout.split(chr(10))[0]}")
    return {"file": fname, "wikilinks": len(linked), "cross_refs": added_cr}


def main():
    aliases, page_paths = load_catalog()
    etype = (
        "concept"
        if "concepts" in str(YAML_DIR)
        else "method"
        if "methods" in str(YAML_DIR)
        else "reagent"
        if "reagents" in str(YAML_DIR)
        else "protein"
    )
    print(f"Mode: {YAML_TYPE} ({etype}) | Aliases: {len(aliases)}")
    wl_pat = re.compile(r"\[.*?\]\(/xray-mp-wiki/")
    to_enrich = [f.name for f in sorted(YAML_DIR.glob("*.yaml")) if not wl_pat.search(f.read_text())]
    print(f"To enrich: {len(to_enrich)}")
    if not to_enrich:
        print("All done!")
        return
    files = to_enrich[:FIRST_N] if FIRST_N else to_enrich
    results = []
    for fname in files:
        r = enrich_file(fname, aliases, page_paths, dry=DRY_RUN)
        if r:
            results.append(r)
    tw = sum(r["wikilinks"] for r in results)
    tc = sum(r["cross_refs"] for r in results)
    mode = "DRY RUN" if DRY_RUN else "ENRICHED"
    print(f"\n{'=' * 60}")
    print(f"{mode}: {len(results)} files, {tw} wikilinks, {tc} cross-refs")


if __name__ == "__main__":
    main()
