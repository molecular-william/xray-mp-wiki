#!/usr/bin/env python3
"""
Enrich purification step labels with controlled step_type taxonomy.

Maps 614 unique free-text step labels to ~19 step_type values, enabling
queries like "which detergents are used at solubilization vs SEC step?"
and "how often is detergent exchange performed?"

Usage:
  python3 scripts/enrich_step_types.py             # live
  python3 scripts/enrich_step_types.py --dry-run   # preview only
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
W = BASE / "xray-mp-wiki"
DRY_RUN = "--dry-run" in sys.argv

# Step-type classification patterns (ordered most-specific first)
STEP_PATTERNS = [
    (r"\bsonication\b", "lysis"),
    (r"\bfrench press\b", "lysis"),
    (r"\bmicrofluidiz\w+\b", "lysis"),
    (r"\bcell (lysis|disruption|harvest)\b", "lysis"),
    (r"\bhomogenization\b", "lysis"),
    (r"\bmembrane (preparation|isolation|extraction|vesicle|fraction)\b", "membrane_prep"),
    (r"\bsolubilization\b", "solubilization"),
    (r"\bdetergent (extraction|solubilization|exchange)\b", "solubilization"),
    (r"\bultracentrifugation\b", "clarification"),
    (r"\bcentrifugation\b", "clarification"),
    (r"\b(protein )?expression\b", "expression"),
    (r"\bcell (culture|growth)\b", "expression"),
    (r"\bfermentation\b", "expression"),
    (r"\bbaculovirus\b", "expression"),
    (r"\binfection\b", "expression"),
    (r"\binduction\b", "expression"),
    (r"\bharvesting\b", "expression"),
    (r"\btag (cleavage|removal|remove)\b", "tag_cleavage"),
    (r"\btev (cleavage|protease|digest)\b", "tag_cleavage"),
    (r"\b(protease|3c|prescission|thrombin|factor[\s-]xa) cleavage\b", "tag_cleavage"),
    (r"\bimmobilized metal\b", "binding"),
    (r"\bni-nta\b", "binding"),
    (r"\bimac\b", "binding"),
    (r"\bstrep-tactin\b", "binding"),
    (r"\bcobalt (affinity|resin|agarose)\b", "binding"),
    (r"\b(anti[-\s]?flag|flag[- ]?agarose)\b", "binding"),
    (r"\bamylose resin\b", "binding"),
    (r"\b(calmodulin|cbp) (chromatography|binding|resin)\b", "binding"),
    (r"\b(glutathione|gst) (sepharose|resin|affinity)\b", "binding"),
    (r"\bpulldown\b", "binding"),
    (r"\bbatch binding\b", "binding"),
    (r"\bbinding\b(?!.*(?:elution|wash))", "binding"),
    (r"\baffinity (chromatography|purification|capture)\b", "binding"),
    (r"\b(ion[-\s]?exchange|anion[-\s]?exchange|cation[-\s]?exchange)\b", "ion_exchange"),
    (r"\b(mono q|mono s|q sepharose|sp sepharose|deae|resource [qs])\b", "ion_exchange"),
    (r"\b(size exclusion|size-exclusion) chromatography\b", "sec"),
    (r"\b\bsec\b(?!.*(?:mals|dls))", "sec"),
    (r"\bgel filtration\b", "sec"),
    (r"\bsuperdex\b", "sec"),
    (r"\bsuperose\b", "sec"),
    (r"\b(hydrophobic interaction|hic|phenyl sepharose|butyl sepharose)\b", "hic"),
    (r"\b(hydroxyapatite)\b", "hic"),
    (r"\bconcentrat\w+\b", "concentration"),
    (r"\bultrafiltrat\w+\b", "concentration"),
    (r"\b(amicon|centriprep|centricon|vivaspin)\b", "concentration"),
    (r"\bdialysis\b", "dialysis"),
    (r"\bdesalting\b", "dialysis"),
    (r"\belution\b", "elution"),
    (r"\bwash\b", "wash"),
    (r"\bdetergent exchange\b", "exchange"),
    (r"\bbuffer exchange\b", "exchange"),
    (r"\bon[-\s]?column exchange\b", "exchange"),
    (r"\blcp (reconstitution|setup|crystallization)\b", "crystallization_setup"),
    (r"\breconstitution\b", "crystallization_setup"),
    (r"\b(nanobody|complex) formation\b", "complex_formation"),
    (r"\bligand incubation\b", "complex_formation"),
    (r"\b(deglycosylat|pngase|endoglycosidase|endoh)\b", "deglycosylation"),
    (r"\baggregate removal\b", "polishing"),
    (r"\balkylation\b", "modification"),
    (r"\breduction\b", "modification"),
    (r"\bcarboxymethylation\b", "modification"),
    (r"\bpurification\b", "purification"),
    (r"\bpolishing\b", "polishing"),
]


def classify_step(label):
    """Map step label string to list of step_type values."""
    if not label:
        return []
    # Strip wikilink syntax for matching
    clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", label.lower())
    # Remove step numbering prefixes
    clean = re.sub(r"^[\d\s.()\[\]-]+\s*", "", clean)
    if not clean.strip():
        return []

    types = []
    for pattern, st in STEP_PATTERNS:
        if re.search(pattern, clean):
            types.append(st)

    # 'purification' is only used if no more specific type matches
    if len(types) > 1 and "purification" in types:
        types.remove("purification")
    if len(types) > 1 and "binding" in types and any(t in types for t in ["wash", "elution"]):
        pass  # keep both for compound steps

    return types


def main():
    total_files = 0
    total_steps = 0
    type_counter = Counter()
    unchanged = 0

    for yf in sorted((W / "proteins_yaml").glob("*.yaml")):
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue

        modified = False

        # Check both old (top-level) and DOI-grouped (nested) structures
        purif_sources = list(data.get("purifications", []) or [])
        for pub in data.get("publications", []) or []:
            if isinstance(pub, dict):
                purif_sources.extend(pub.get("purifications", []) or [])

        for p in purif_sources:
            if not isinstance(p, dict):
                continue
            for s in p.get("steps", []) or []:
                if not isinstance(s, dict):
                    continue
                label = s.get("step", "")
                if not label:
                    continue
                # Skip if already has a step_type
                if s.get("step_type"):
                    unchanged += 1
                    continue

                types = classify_step(str(label))
                if types:
                    s["step_type"] = types[0]  # Use primary type
                    if len(types) > 1:
                        s["step_subtype"] = types[1]  # Secondary for compound steps
                    modified = True
                    total_steps += 1
                    type_counter[types[0]] += 1

        if modified:
            total_files += 1
            if not DRY_RUN:
                raw = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
                yf.write_text(raw)

    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"{mode}: {total_steps} steps classified in {total_files} files")
    print(f"  (skipped {unchanged} steps with existing step_type)")
    print("\nStep type distribution:")
    for t, c in type_counter.most_common():
        print(f"  {t:<25} {c}")
    if DRY_RUN:
        print("\nRun without --dry-run to apply.")


if __name__ == "__main__":
    main()
