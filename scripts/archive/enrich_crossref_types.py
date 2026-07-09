#!/usr/bin/env python3
"""
Add controlled `type` field to all cross_references in YAML files.

Usage:
  python3 scripts/enrich_crossref_types.py --dry-run    # preview changes
  python3 scripts/enrich_crossref_types.py --execute    # apply changes

Controlled types are defined in references/AGENT-MANIFEST.md §9.
"""

import re
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent.parent
try:
    import yaml  # noqa: F401
except ImportError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
    import yaml  # noqa: F401

# ─── Controlled type taxonomy ──────────────────────────────────

TYPE_RULES = [
    # (type_name, regex_pattern, fallback_keywords)
    (
        "detergent_used",
        r"\b(detergent|ddm|lmng|og\b|dm\b|ldao|chaps|sodium\.?cholate|maltoside|glucoside|solubilization)\b.*\b(used|purification|solubilization|crystallization|extraction)",
        ["detergent", "ddm", "lmng", "solubilization", "maltoside", "glucoside"],
    ),
    (
        "buffer_component",
        r"\b(buffer|tris|hepes|mops|pipes|mes|nacl|kcl|glycerol|edta|dtt|β\.?me|ammonium|phosphate)\b.*\b(component|buffer|purification|crystallization|ph\b)",
        ["buffer component", "tris", "hepes", "glycerol", "edta", "nacl"],
    ),
    (
        "additive_used",
        r"\b(additive|peg\b|precipitant|cryoprotectant|imidazole|ligand|additive)\b.*\b(used|purification|crystallization|buffer|screen)",
        ["additive", "peg", "precipitant", "cryoprotectant", "imidazole"],
    ),
    (
        "ligand_bound",
        r"\b(ligand|cofactor|agonist|antagonist|inhibitor|substrate|bound|binding|co.?crystallized|cofactor|modulator)\b",
        ["ligand", "agonist", "antagonist", "inhibitor", "cofactor", "bound", "binding", "co-crystallized"],
    ),
    (
        "method_used",
        r"\b(method|technique|chromatography|spectroscopy|diffraction|fsec|sec\b|hplc|ms\b|nmr|mass spec|assay)\b",
        ["method", "technique", "chromatography", "spectroscopy", "fsec", "sec"],
    ),
    (
        "fusion_tag",
        r"\b(fusion|tag\b|his\b|flag|gst|mbp|t4l|bril|gfp|mbp|fusion protein)\b.*\b(tag|fusion|crystallization|purification|expression)",
        ["fusion", "tag", "his", "flag", "t4l", "bril", "gfp"],
    ),
    (
        "crystallization_method",
        r"\b(crystallization|vapor.?diffusion|lcp|microbatch|hanging.?drop|sitting.?drop|bicelle|lipid.?cubic.?phase)\b",
        ["crystallization", "lcp", "vapor diffusion", "hanging drop", "bicelle"],
    ),
    (
        "purification_method",
        r"\b(purification|affinity|ion.?exchange|size.?exclusion|sec\b|nickel|ni.?nta|talon|gel.?filtration)\b",
        ["purification", "affinity", "ni-nta", "size exclusion", "ion exchange", "talon", "gel filtration"],
    ),
    (
        "related_protein",
        r"\b(related|homolog|homologue|ortholog|paralog|similar)\b.*\b(protein|structure|family|sequence)",
        ["related protein", "homolog", "ortholog", "paralog", "similar structure"],
    ),
    (
        "related_concept",
        r"\b(concept|mechanism|principle|pathway|function|illustrate)\b",
        ["concept", "mechanism", "principle", "function", "pathway"],
    ),
    (
        "entity_mentioned",
        r"\b(mentioned|referenced|discussed|cited|described|text|appears?)\b",
        ["mentioned", "referenced", "discussed", "text"],
    ),
    (
        "antibiotic_selection",
        r"\b(antibiotic|selection|resistance|ampicillin|kanamycin|chloramphenicol)\b",
        ["antibiotic", "selection", "ampicillin", "kanamycin"],
    ),
    (
        "family_member",
        r"\b(family|subfamily|class|group|superfamily)\b.*\b(member|protein|transporter|channel|receptor)",
        ["family member", "subfamily", "superfamily"],
    ),
    (
        "comparative_study",
        r"\b(compared|comparison|study|paper|same|work|article|reference)\b",
        ["compared", "comparison", "study", "paper"],
    ),
    (
        "expression_system",
        r"\b(expression|sf9|baculovirus|hepk|e\.?coli|pichia|cell.?free)\b.*\b(system|expression|produced|expressed)",
        ["expression system", "sf9", "baculovirus", "expression", "produced in"],
    ),
]


def classify_reason(reason):
    """Classify a cross-reference reason string into a controlled type."""
    r = reason.lower().strip()

    # Try regex first (more precise)
    for type_name, pattern, _ in TYPE_RULES:
        if re.search(pattern, r, re.IGNORECASE):
            return type_name

    # Fallback: keyword matching
    for type_name, _, keywords in TYPE_RULES:
        for kw in keywords:
            if kw in r:
                return type_name

    return None  # Will be set to "related"


def process_yaml(yaml_path, dry_run=True):
    """Process a single YAML file, adding type fields to cross_references."""
    import yaml as _yaml

    with open(yaml_path) as f:
        data = _yaml.safe_load(f)

    if not data or not isinstance(data, dict):
        return [], data

    cr_list = data.get("cross_references", [])
    if not cr_list:
        return [], data

    changes = []

    for i, cr in enumerate(cr_list):
        if not isinstance(cr, dict):
            continue
        if "type" in cr:
            continue  # Already has a type
        reason = cr.get("reason", "")
        if not reason:
            cr["type"] = "related"
            changes.append((i, "(empty)", "related"))
            continue

        classified = classify_reason(reason)
        assigned = classified if classified else "related"
        cr["type"] = assigned
        changes.append((i, reason[:50], assigned))

    return changes, data


def main():
    dry_run = "--dry-run" in sys.argv
    execute = "--execute" in sys.argv

    if not dry_run and not execute:
        print("Usage: python3 scripts/enrich_crossref_types.py --dry-run  (preview)")
        print("       python3 scripts/enrich_crossref_types.py --execute  (apply changes)")
        sys.exit(1)

    mode = "DRY RUN" if dry_run else "EXECUTE"
    print(f"=== Cross-Reference Type Enrichment ({mode}) ===\n")

    import yaml as _yaml

    total_files = 0
    total_refs = 0
    changed_refs = 0
    type_counts = Counter()
    no_type_count = 0

    for yaml_dir in ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]:
        dir_path = BASE / "xray-mp-wiki" / yaml_dir
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.yaml")):
            changes, data = process_yaml(f, dry_run)
            if not changes:
                continue
            total_files += 1
            total_refs += len(data.get("cross_references", []))
            changed_refs += len(changes)

            for idx, reason_preview, assigned in changes:
                type_counts[assigned] += 1

            if not dry_run and changes:
                # Write back the modified YAML
                with open(f, "w") as fh:
                    _yaml.dump(data, fh, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Files with new types: {total_files}")
    print(f"Cross-refs checked:    {total_refs}")
    print(f"New type fields added: {changed_refs}")
    print()

    if type_counts:
        print("Type distribution:")
        for t, count in type_counts.most_common():
            print(f"  {t:25s} {count:5d}")

    if no_type_count:
        print(f"\n(!) {no_type_count} refs could not be classified (will be 'related')")

    print(f"\n{'DRY RUN — no changes written' if dry_run else 'Changes applied.'}")
    if dry_run:
        print("Run with --execute to apply.")


if __name__ == "__main__":
    main()
