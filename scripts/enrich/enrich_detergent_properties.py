#!/usr/bin/env python3
"""
Enrich detergent/lipid reagent YAMLs with physical properties from the
Anatrace Detergent Brochure.

Reads references/anatrace_detergent_data.json, matches entries to
reagent YAMLs by name, and adds cmc/mw/aggregation_number/source fields.

Usage:
  python3 scripts/enrich_detergent_properties.py             # live
  python3 scripts/enrich_detergent_properties.py --dry-run   # preview only
"""

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE / "references" / "anatrace_detergent_data.json"
BROCHURE_PATH = BASE / "raw" / "miscellaneous" / "Anatrace-Detergents-Brochure.pdf"
BROCHURE_SOURCE = f"pdf/{BROCHURE_PATH.relative_to(BASE)}"

DRY_RUN = "--dry-run" in sys.argv

# Name mapping: patterns in the Anatrace catalog → wiki YAML slugs
# Ordered most-specific first to avoid false matches
NAME_MAP = [
    # Exact common-name matches
    (r"CHAPS", "chaps"),
    (r"CHAPSO", "chapso"),
    (r"LAPAO", "lapao"),
    (r"IPTG", "iptg"),
    # CYMALs
    (r"CYMAL-1", "cymal-1"),
    (r"CYMAL-2", "cymal-2"),
    (r"CYMAL-3", "cymal-3"),
    (r"CYMAL-4", "cymal-4"),
    (r"CYMAL-5", "cymal-5"),
    (r"CYMAL-6", "cymal-6"),
    (r"CYMAL-7", "cymal-7"),
    # Fos-Cholines
    (r"Fos-Choline-8", "fos-choline-8"),
    (r"Fos-Choline-9", "fos-choline-9"),
    (r"Fos-Choline-10", "fos-choline-10"),
    (r"Fos-Choline-11", "fos-choline-11"),
    (r"Fos-Choline-12", "fos-choline-12"),
    (r"Fos-Choline-13", "fos-choline-13"),
    (r"Fos-Choline-14", "fos-choline-14"),
    (r"Fos-Choline-15", "fos-choline-15"),
    (r"Fos-Choline-16", "fos-choline-16"),
    # Anapoe/Triton
    (r"Anapoe-X-100", "triton-x-100"),
    (r"Anapoe-20", "tween-20"),
    (r"Anapoe-80", "tween-80"),
    (r"Anapoe-35", "tween-35"),
    (r"Anapoe-58", "tween-58"),
    # Detergent core names
    (r"DDM|n-Dodecyl-?b-?D-Maltoside|n-Dodecyl-?β-?D-Maltopyranoside|Lauryl Maltoside", "ddm"),
    (r"DM|n-Decyl-?b-?D-Maltoside|n-Decyl-?β-?D-Maltopyranoside|Decyl Maltoside", "dm"),
    (r"OG|n-Octyl-?b-?D-Glucoside|n-Octyl-?β-?D-Glucopyranoside|Octyl Glucoside", "og"),
    (r"NG|n-Nonyl-?b-?D-Glucoside|n-Nonyl-?β-?D-Glucopyranoside|Nonyl Glucoside", "ng"),
    (r"LMNG|Lauryl Maltose Neopentyl Glycol", "lmng"),
    (r"DMNG|Decyl Maltose Neopentyl Glycol", "dmng"),
    (r"OGNG|Octyl Glucose Neopentyl Glycol", "ogng"),
    (r"LDAO|n-Dodecyl-N,N-Dimethylamine-N-Oxide|Dodecyldimethylamine-N-Oxide", "ldao"),
    (r"C8E4|Tetraethylene Glycol Monooctyl Ether", "c8e4"),
    (r"C8E6|Hexaethylene Glycol Monooctyl Ether", "c8e6"),
    (r"C10E5|Pentaethylene Glycol Monodecyl Ether", "c10e5"),
    (r"C10E6|Hexaethylene Glycol Monodecyl Ether", "c10e6"),
    (r"C12E8|Octaethylene Glycol Monododecyl Ether", "c12e8"),
    (r"C12E9|Nonaethylene Glycol Monododecyl Ether", "c12e9"),
    # Bile acid derivatives
    (r"BigChap|Big.CHAP", "big-chap"),
    (r"Deoxycholic Acid", "deoxycholic-acid"),
    (r"Sodium Cholate", "sodium-cholate"),
    (r"CHAPS", "chaps"),
    # Others
    (r"Digitonin", "digitonin"),
    (r"Zwittergent 3-12", "zwittergent-3-12"),
    (r"HEGA-9", "hega-9"),
    (r"HEGA-10", "hega-10"),
    (r"HEGA-11", "hega-11"),
    (r"MEGA-8", "mega-8"),
    (r"MEGA-9", "mega-9"),
    (r"MEGA-10", "mega-10"),
    # Thioglucosides
    (r"n-Octyl-?b-?D-Thioglucopyranoside|OTG|Octyl Thioglucoside", "otg"),
    (r"n-Nonyl-?b-?D-Thioglucopyranoside", "ntg"),
    (r"n-Decyl-?b-?D-Thioglucopyranoside", "dtg"),
    (r"n-Dodecyl-?b-?D-Thiomaltopyranoside", "dod-malto-thio"),
    (r"n-Decyl-?b-?D-Thiomaltopyranoside", "decyl-thiomalto"),
    # Nonyl/N-alkyl maltosides
    (r"n-Nonyl-?b-?D-Maltopyranoside", "nonyl-maltoside"),
    (r"n-Octyl-?b-?D-Maltopyranoside", "octyl-maltoside"),
    (r"n-Undecyl-?b-?D-Maltopyranoside", "undecyl-maltoside"),
    (r"n-Tridecyl-?b-?D-Maltopyranoside", "tridecyl-maltoside"),
    # Anameg
    (r"Anameg-7", "anameg-7"),
    # NDSB
    (r"NDSB-195", "ndsb-195"),
    (r"NDSB-201", "ndsb-201"),
    (r"NDSB-256", "ndsb-256"),
    # Anzergent
    (r"Anzergent 3-8", "anzergent-3-8"),
    (r"Anzergent 3-10", "anzergent-3-10"),
    (r"Anzergent 3-12", "anzergent-3-12"),
    (r"Anzergent 3-14", "anzergent-3-14"),
    (r"Anzergent 3-16", "anzergent-3-16"),
]


def load_anatrace_data():
    return json.loads(DATA_FILE.read_text())


def match_slug(name, product_no):
    """Match an Anatrace entry to a wiki YAML slug."""
    # Clean the name for matching
    name_clean = name.replace("\u2010", "-").replace("\u2212", "-").replace("\u03b2", "b")
    name_clean = name_clean.replace("\u03b1", "a")

    for pattern, slug in NAME_MAP:
        if re.search(pattern, name_clean, re.IGNORECASE):
            return slug
    return None


def main():
    entries = load_anatrace_data()
    reagents_dir = BASE / "xray-mp-wiki" / "reagents_yaml"

    # Build slug → data mapping
    slug_map = {}
    for e in entries:
        slug = match_slug(e["name"], e["product_no"])
        if slug:
            if slug not in slug_map:
                slug_map[slug] = e
            # Prefer entries with more data
            existing = slug_map[slug]
            existing_fields = sum(1 for v in [existing["fw"], existing["cmc_mM"], existing["aggregation_no"]] if v)
            new_fields = sum(1 for v in [e["fw"], e["cmc_mM"], e["aggregation_no"]] if v)
            if new_fields > existing_fields:
                slug_map[slug] = e

    # Enrich each matched YAML
    total_enriched = 0
    for slug, anatrace in sorted(slug_map.items()):
        yaml_path = reagents_dir / f"{slug}.yaml"
        if not yaml_path.exists():
            print(f"  SKIP: {slug}.yaml not found")
            continue

        # Read YAML
        import yaml as yl

        try:
            data = yl.safe_load(yaml_path.read_text())
        except Exception as e:
            print(f"  ERROR: {slug}.yaml parse failed: {e}")
            continue

        if not isinstance(data, dict):
            continue

        # Check if already has these fields
        has_cmc = data.get("cmc") is not None
        has_mw = data.get("mw") is not None
        has_aggr = data.get("aggregation_number") is not None

        if has_cmc and has_mw and has_aggr:
            continue  # Already fully enriched

        # Build source string
        source_str = f"Anatrace Detergent Brochure (product {anatrace['product_no']})"

        # Add fields
        modified = False

        if not has_cmc and anatrace["cmc_mM"] is not None:
            data["cmc"] = str(anatrace["cmc_mM"])
            data["cmc_source"] = source_str
            modified = True

        if not has_mw and anatrace["fw"] is not None:
            data["mw"] = str(anatrace["fw"])
            data["mw_source"] = source_str
            modified = True

        if not has_aggr and anatrace["aggregation_no"] is not None:
            data["aggregation_number"] = str(anatrace["aggregation_no"])
            data["aggregation_source"] = source_str
            modified = True

        if modified:
            if not DRY_RUN:
                from ruamel.yaml import YAML

                ryaml = YAML()
                ryaml.default_flow_style = False
                ryaml.allow_unicode = True
                ryaml.sort_keys = False
                ryaml.dump(data, Path(yaml_path).open("w"))

            total_enriched += 1
            fields = []
            if not has_cmc and anatrace["cmc_mM"]:
                fields.append(f"cmc={anatrace['cmc_mM']}mM")
            if not has_mw and anatrace["fw"]:
                fields.append(f"mw={anatrace['fw']}")
            if not has_aggr and anatrace["aggregation_no"]:
                fields.append(f"aggr={anatrace['aggregation_no']}")
            mode = "WOULD ENRICH" if DRY_RUN else "ENRICHED"
            print(f"  {mode}: {slug}.yaml — {', '.join(fields)}")

    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"\n{mode}: {total_enriched} YAML files enriched")
    if DRY_RUN:
        print("Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
