#!/usr/bin/env python3
"""
Classify free-text expression.system strings into canonical categories.

Adds `expression.class` field with one of:
  e-coli, sf9, hek293, pichia-pastoris, saccharomyces-cerevisiae,
  hi5, native-tissue, cell-free, lexsy, other-bacterial,
  other-eukaryotic, not-specified

Usage:
  python3 scripts/classify_expression.py              # live
  python3 scripts/classify_expression.py --dry-run     # preview only
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
W = BASE / "xray-mp-wiki"
DRY_RUN = "--dry-run" in sys.argv

# Order matters: first match wins (most specific first)
CLASS_PATTERNS = [
    (r"\be\.?\s*coli\b|\bescherichia\b", "e-coli"),
    (r"\bpichia\b", "pichia-pastoris"),
    (r"\bsaccharomyces\b", "saccharomyces-cerevisiae"),
    (r"\bsf9\b|\bsf21\b|\bspodoptera\b", "sf9"),
    (r"\bbaculovirus\b", "sf9"),
    (r"\bhi5\b|\bhigh.?five\b|\bhigh5\b|\btrichoplusia\b", "hi5"),
    (r"\bhek\b|\b293\b", "hek293"),
    (r"\bbacmam\b", "hek293"),
    (r"\blexsy\b|\bleishmania\b", "lexsy"),
    (r"\bcell.?free\b|\bin.?vitro\b", "cell-free"),
    (r"\bcho\b", "other-eukaryotic"),
    (r"\bcos-?\d?\b", "other-eukaryotic"),
    (
        r"\bbacillus\b|\blactococcus\b|\bcorynebacterium\b|\bmycobacterium\b|\bpseudomonas\b|\blactobacillus\b|\bsalmonella\b",
        "other-bacterial",
    ),
    (r"\bschizosaccharomyces\b|\byarrowia\b", "other-eukaryotic"),
    (r"\bnative\b", "native-tissue"),
    (
        r"not specified|not determined|not detailed|not mentioned|not found|not available|unknown|inferred|presumed",
        "not-specified",
    ),
    (r"\bsynthetic\b|\bchemically synthesized\b|\bpeptide\b", "cell-free"),
    (
        r"\bhalobacterium\b|\bnatronomonas\b|\bthermus\b|\brhodopseudomonas\b|\brhodospirillum\b|\bthermochromatium\b|\bcyanidium\b|\bthermosynechococcus\b|\bmethylococcus\b|\bralstonia\b|\bdesulfovibrio\b|\baquifex\b|\bheliobacterium\b|\bsalinibacter\b|\bilyobacter\b|\benterococcus\b",
        "other-bacterial",
    ),
    (r"\bspinach\b|\bspinacia\b|\bpisum\b|\bchlamydomonas\b", "other-eukaryotic"),
]


def classify(system_text):
    """Return canonical class name for a free-text expression system string."""
    if not system_text or not system_text.strip():
        return "not-specified"
    # Strip wikilinks
    clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", system_text.lower())
    for pattern, class_name in CLASS_PATTERNS:
        if re.search(pattern, clean):
            return class_name
    return "not-specified"


def main():
    total = 0
    skipped = 0
    class_counter = Counter()
    changes = []

    for yf in sorted((W / "proteins_yaml").glob("*.yaml")):
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue

        expr = data.get("expression", {}) or {}
        sys_text = (expr.get("system", "") or "").strip()
        if not sys_text:
            continue

        total += 1

        # Skip if already has expression.class
        if isinstance(expr, dict) and expr.get("class"):
            skipped += 1
            continue

        ec = classify(sys_text)
        if isinstance(expr, dict):
            data["expression"]["class"] = ec
        else:
            data["expression"] = {"system": sys_text, "class": ec}

        class_counter[ec] += 1
        changes.append((yf.stem, sys_text[:60], ec))

        if not DRY_RUN:
            # Write back
            raw = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
            yf.write_text(raw)

    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"{mode}: {len(changes)} proteins classified (skipped {skipped} with existing class)")
    print(f"Coverage: {len(changes)}/{total} ({100 * len(changes) // total}%)")
    print("\nClass distribution:")
    for c, n in class_counter.most_common():
        print(f"  {c:<25} {n}")
    print("\nSample classifications:")
    for slug, sys_t, ec in changes[:15]:
        print(f"  {slug:<30} → {ec:<20} ({sys_t})")

    if DRY_RUN:
        print("\nRun without --dry-run to apply.")


if __name__ == "__main__":
    main()
