#!/usr/bin/env python3
"""Enrich protein YAMLs with organism field from PDB GraphQL cache + Uniprot API.

Derives organism for each Uniprot accession by:
  1. GraphQL cache (primary): read rcsb_entity_source_organism from clean
     (single-Uniprot) entities in the PDB cache
  2. GraphQL cache (fusion): if only fusion entities, subtract known fusion
     partner organisms, majority vote the rest
  3. Uniprot REST API (fallback): for the ~84 fusion-only accessions where
     GraphQL data is ambiguous

Usage:
  python3 scripts/enrich_organism.py               # dry-run
  python3 scripts/enrich_organism.py --no-dry-run   # write
  python3 scripts/enrich_organism.py --cache-only   # skip Uniprot API
"""

import argparse
import json
import re
import time
from collections import Counter
from pathlib import Path

import yaml

from scripts._base import fast_load_str

# ─── Paths ────────────────────────────────────────────────────────
BASE = Path(__file__).parent.parent.parent
PROTEINS_DIR = BASE / "xray-mp-wiki" / "proteins_yaml"
CACHE_PATH = BASE / "references" / "uniprot_cache.json"
AUDIT_PATH = BASE / "references" / "enrich_organism_report.json"

# ─── Known fusion partners ────────────────────────────────────────
FUSION_PARTNERS = {
    "P00720",
    "P0A2X6",
    "P0ABE7",
    "P00722",
    "P0AEX9",
    "P63214",
    "P0CD61",
    "P63017",
    "P0AET7",
    "P01574",
}

# ─── Organism normalisation ───────────────────────────────────────
ORGANISM_CANONICAL = {}
# Build from a curated list of common patterns
_COMMON_ORGANISMS = {
    "homo sapiens": "Homo sapiens",
    "homo sapien": "Homo sapiens",
    "escherichia coli": "Escherichia coli",
    "escherichia coli (strain k12)": "Escherichia coli",
    "escherichia coli o157:h7": "Escherichia coli",
    "escherichia coli str. k-12 substr. w3110": "Escherichia coli",
    "streptomyces lividans": "Streptomyces lividans",
    "staphylococcus aureus": "Staphylococcus aureus",
    "mus musculus": "Mus musculus",
    "rattus norvegicus": "Rattus norvegicus",
    "bos taurus": "Bos taurus",
    "saccharomyces cerevisiae": "Saccharomyces cerevisiae",
    "saccharomyces cerevisiae s288c": "Saccharomyces cerevisiae",
    "saccharomyces cerevisiae (strain atcc 204508 / s288c)": "Saccharomyces cerevisiae",
    "arabidopsis thaliana": "Arabidopsis thaliana",
    "drosophila melanogaster": "Drosophila melanogaster",
    "caenorhabditis elegans": "Caenorhabditis elegans",
    "danio rerio": "Danio rerio",
    "sus scrofa": "Sus scrofa",
    "oryctolagus cuniculus": "Oryctolagus cuniculus",
    "enterobacteria phage t4": "Enterobacteria phage T4",
    "clostridium pasteurianum": "Clostridium pasteurianum",
    "mycobacterium smegmatis": "Mycobacterium smegmatis",
    "mycobacterium tuberculosis": "Mycobacterium tuberculosis",
    "thermus thermophilus": "Thermus thermophilus",
    "aquifex aeolicus": "Aquifex aeolicus",
    "archaeoglobus fulgidus": "Archaeoglobus fulgidus",
    "yarrowia lipolytica": "Yarrowia lipolytica",
    "aequorea victoria": "Aequorea victoria",
    "desulfovibrio vulgaris": "Desulfovibrio vulgaris",
    "pyrococcus abyssi": "Pyrococcus abyssi",
}
# Pre-populate from the curated list and also add lowercase variants
for k, v in list(_COMMON_ORGANISMS.items()):
    ORGANISM_CANONICAL[k] = v
    ORGANISM_CANONICAL[k.upper()] = v
    if k != k.lower():
        ORGANISM_CANONICAL[k.lower()] = v


def normalise_organism(name):
    """Normalise organism name to canonical form."""
    key = name.strip().lower()
    if key in ORGANISM_CANONICAL:
        return ORGANISM_CANONICAL[key]

    # Fallback: extract genus + species and try matching
    m = re.match(r"^([a-z]+)\s+([a-z]+)", key)
    if m:
        genus_species = f"{m.group(1)} {m.group(2)}"
        if genus_species in ORGANISM_CANONICAL:
            return ORGANISM_CANONICAL[genus_species]

    # Capitalise properly: first letter uppercase, rest of each word lowercase
    words = name.strip().split()
    if words:
        # First word: capitalize first letter
        # Species epithet: should be lowercase
        result = words[0].capitalize()
        for w in words[1:]:
            # Skip strain designations like O157:H7, K12, etc.
            if w.isupper() or any(c.isdigit() for c in w):
                result += f" {w}"
            elif w.startswith("("):
                result += f" {w}"
            else:
                result += f" {w.lower()}"
        return result
    return name.strip()


def is_fusion_organism(name):
    """Check if organism name looks like a common fusion partner source."""
    key = name.lower()
    if "phage" in key:
        return True
    if "escherichia" in key and "coli" in key:
        return True
    if "synthetic" in key:
        return True
    return False


# ═══════════════════════════════════════════════════════════════════
#  Phase 1: Collect unique Uniprots from YAMLs
# ═══════════════════════════════════════════════════════════════════


def collect_unique_uniprots():
    """Scan all protein YAMLs, return {protein_name: [uniprots]} and all unique."""
    protein_uniprots = {}
    all_unique = set()

    for yf in sorted(PROTEINS_DIR.glob("*.yaml")):
        name = yf.stem
        try:
            data = fast_load_str(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        uid = data.get("uniprot_id", "")
        if not uid:
            continue
        if isinstance(uid, str):
            unis = [uid]
        else:
            unis = uid
        protein_uniprots[name] = unis
        all_unique.update(unis)

    return protein_uniprots, sorted(all_unique)


# ═══════════════════════════════════════════════════════════════════
#  Phase 2: Resolve organism from GraphQL cache
# ═══════════════════════════════════════════════════════════════════


def resolve_from_cache(unique_uniprots):
    """Derive organism for each Uniprot from the PDB GraphQL cache.

    Returns: {uniprot: {organism: count, ...}} for each accession,
             plus a set of accessions that need API fallback.
    """
    cache = {}
    if CACHE_PATH.exists():
        cache = json.loads(CACHE_PATH.read_text())
    if not cache:
        print("  WARNING: No cache found. Run enrich_uniprot.py first.")
        return {}, set(unique_uniprots)

    results = {}  # uniprot → {organism_norm: count}
    needs_api = set()

    for acc in unique_uniprots:
        # Collect organisms from ALL entities containing this Uniprot
        org_counter = Counter()
        clean_org_counter = Counter()  # from single-Uniprot entities only

        for pdb, entities in cache.items():
            for eid, info in entities.items():
                unis = info.get("uniprots", [])
                if acc in unis:
                    orgs = [normalise_organism(o) for o in info.get("organisms", [])]
                    for o in orgs:
                        org_counter[o] += 1
                    if len(unis) == 1:
                        for o in orgs:
                            clean_org_counter[o] += 1

        if not org_counter:
            needs_api.add(acc)
            continue

        # Strategy 1: use clean entities if available
        if clean_org_counter:
            winner = clean_org_counter.most_common(1)[0]
            results[acc] = {winner[0]: winner[1]}
            continue

        # Strategy 2: fusion-only — remove fusion-partner organisms
        filtered = Counter()
        for o, c in org_counter.items():
            if not is_fusion_organism(o):
                filtered[o] = c

        if not filtered:
            # All organisms look like fusion sources — might be wrong
            # Use the original and flag
            results[acc] = dict(org_counter.most_common(1))
            continue

        ranked = filtered.most_common()
        if len(ranked) == 1 or ranked[0][1] > ranked[1][1]:
            results[acc] = {ranked[0][0]: ranked[0][1]}
        else:
            # Still tied — needs API
            needs_api.add(acc)

    return results, needs_api


# ═══════════════════════════════════════════════════════════════════
#  Phase 3: Uniprot REST API fallback
# ═══════════════════════════════════════════════════════════════════

UNIPROT_BATCH_URL = "https://rest.uniprot.org/uniprotkb/accessions"


def resolve_from_api(accessions, cache_only=False):
    """Fetch organism from Uniprot REST API in batches.

    Returns: {accession: organism_string}
    """
    if not accessions or cache_only:
        return {}

    results = {}
    acc_list = sorted(accessions)

    # Batch in groups of 50
    for i in range(0, len(acc_list), 50):
        batch = acc_list[i : i + 50]
        ids = ",".join(batch)
        url = f"{UNIPROT_BATCH_URL}?accessions={ids}"
        print(f"  Fetching batch {i // 50 + 1}: {len(batch)} accessions...")

        try:
            resp = requests.get(url, timeout=30, headers={"Accept": "application/json"})
            resp.raise_for_status()
            data = resp.json()
            for entry in data.get("results", []):
                acc = entry.get("primaryAccession", "")
                org_info = entry.get("organism", {})
                sci_name = (org_info or {}).get("scientificName", "")
                if acc and sci_name:
                    results[acc] = normalise_organism(sci_name)
        except requests.exceptions.RequestException as exc:
            print(f"    ERROR: {exc}")

        if i + 50 < len(acc_list):
            time.sleep(0.3)

    return results


# ═══════════════════════════════════════════════════════════════════
#  Phase 4: Write to YAML
# ═══════════════════════════════════════════════════════════════════


def update_yaml_organism(yaml_path, organism, dry_run=True):
    """Add organism field to a protein YAML. Returns True if changed."""
    if not yaml_path.exists():
        return False
    original = yaml_path.read_text()
    data = fast_load_str(original)
    if not isinstance(data, dict):
        return False

    existing = data.get("organism", "")
    if existing == organism:
        return False

    data["organism"] = organism
    data["updated"] = "2026-07-03"

    new_yaml = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    if dry_run:
        print(f"  [DRY-RUN] {yaml_path.name}: {existing or '(none)'} → {organism}")
        return True

    yaml_path.write_text(new_yaml)
    verify = fast_load_str(yaml_path.read_text())
    if verify.get("organism", "") != organism:
        print(f"  ERROR: Verification failed for {yaml_path.name}")
        return False
    print(f"  {yaml_path.name}: {existing or '(none)'} → {organism}")
    return True


# ═══════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════


def main():
    parser = argparse.ArgumentParser(description="Enrich protein YAMLs with organism field")
    parser.add_argument("--no-dry-run", action="store_true")
    parser.add_argument("--dry-run", action="store_true", dest="force_dry")
    parser.add_argument("--cache-only", action="store_true", help="Skip Uniprot API, use GraphQL cache only")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    dry_run = not args.no_dry_run or args.force_dry

    print("=" * 60)
    print(f"Organism Enrichment — {'DRY RUN' if dry_run else 'LIVE RUN'}")
    print("=" * 60)

    # ── Step 1: Collect unique Uniprots ──────────────────────
    print("\n[1/4] Collecting unique Uniprot accessions...")
    protein_uniprots, unique_accs = collect_unique_uniprots()
    print(f"  Proteins with uniprot_id: {len(protein_uniprots)}")
    print(f"  Unique accessions: {len(unique_accs)}")

    if args.limit:
        unique_accs = unique_accs[: args.limit]

    # ── Step 2: Resolve from GraphQL cache ───────────────────
    print("\n[2/4] Resolving organism from GraphQL cache...")
    cache_results, needs_api = resolve_from_cache(unique_accs)
    print(f"  Resolved from cache: {len(cache_results)}")
    print(f"  Needs API fallback: {len(needs_api)}")

    # ── Step 3: Resolve from Uniprot API ─────────────────────
    api_results = {}
    if needs_api:
        print(f"\n[3/4] Fetching {len(needs_api)} accessions from Uniprot API...")
        api_results = resolve_from_api(list(needs_api), cache_only=args.cache_only)
        print(f"  Resolved from API: {len(api_results)}")

    # Merge: cache results take priority, API fills gaps
    organism_map = {}  # uniprot → organism_string
    for acc, org_dict in cache_results.items():
        organism_map[acc] = max(org_dict, key=org_dict.get)
    for acc, org in api_results.items():
        organism_map[acc] = org

    # ── Step 4: Write to YAMLs ───────────────────────────────
    print("\n[4/4] Writing organism field to YAMLs...")
    written = 0
    skipped = 0
    missing_org = 0

    for protein_name, unis in sorted(protein_uniprots.items()):
        if args.limit and written + skipped + missing_org >= args.limit:
            break

        # Get organism for the primary Uniprot(s)
        # Filter out known fusion partners for organism lookup
        target_unis = [u for u in unis if u not in FUSION_PARTNERS]
        if not target_unis:
            target_unis = unis  # fallback if all are fusion partners

        # Use a weighted counter: count total entity occurrences per organism
        org_counter = Counter()
        for u in target_unis:
            if u in organism_map:
                # organism_map stores {organism: count_in_cache}
                # weight by the cache count
                weight = 1
                if u in cache_results:
                    for _, c in cache_results[u].items():
                        weight = max(weight, c)
                org_counter[organism_map[u]] += weight

        if not org_counter:
            print(f"  SKIP {protein_name}: no organism found for {unis}")
            missing_org += 1
            continue

        organism = org_counter.most_common(1)[0][0]
        if len(org_counter) > 1:
            print(f"  NOTE: {protein_name} has mixed organisms: {dict(org_counter)} → using {organism}")

        yf = PROTEINS_DIR / f"{protein_name}.yaml"
        if update_yaml_organism(yf, organism, dry_run=dry_run):
            written += 1
        else:
            skipped += 1

    if dry_run:
        print(f"\n  DRY-RUN: Would update {written} files ({skipped} already correct, {missing_org} missing)")
    else:
        print(f"\n  Written: {written} files ({skipped} already correct, {missing_org} missing)")

    # Audit report
    report = {
        "run_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "dry_run": dry_run,
        "proteins_with_uniprot": len(protein_uniprots),
        "unique_accessions": len(unique_accs),
        "resolved_from_cache": len(cache_results),
        "needed_api_fallback": len(needs_api),
        "resolved_from_api": len(api_results),
        "total_written": written,
        "total_skipped": skipped,
        "total_missing": missing_org,
    }
    AUDIT_PATH.write_text(json.dumps(report, indent=2))
    print(f"\nAudit report: {AUDIT_PATH}")
    print(f"{'=' * 60}")
    print(f"Done. {'DRY-RUN — use --no-dry-run to write' if dry_run else 'Changes written.'}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
