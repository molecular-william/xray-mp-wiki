#!/usr/bin/env python3
"""Generate _data/stats.yml for the Jekyll landing page from aggregate_stats.json + filesystem scan.
Run after any bulk enrichment pass to keep landing page stats current."""
import json
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
STATS_JSON = BASE / "references/stats/aggregate_stats.json"
DATA_DIR = BASE / "xray-mp-wiki" / "_data"

d = json.loads(STATS_JSON.read_text())

entity_types = {
    "proteins": len(list((BASE / "xray-mp-wiki/proteins_yaml").glob("*.yaml"))),
    "reagents": len(list((BASE / "xray-mp-wiki/reagents_yaml").glob("*.yaml"))),
    "methods": len(list((BASE / "xray-mp-wiki/methods_yaml").glob("*.yaml"))),
    "concepts": len(list((BASE / "xray-mp-wiki/concepts_yaml").glob("*.yaml"))),
}

family_data = d.get("family_coverage", {})
res_data = d.get("resolution_distribution", {})
total_family_structs = sum(family_data.values()) if family_data else 0

sorted_families = sorted(family_data.items(), key=lambda x: -x[1]) if family_data else []
top_families = [{"name": k.replace("g protein coupled receptors", "GPCRs")
                         .replace("atp binding cassette (abc)", "ABC")
                         .replace("major facilitator superfamily (mfs)", "MFS"),
                   "count": v} for k, v in sorted_families[:10]]

# Detergent matrix: {family: {detergent: count}}
det_matrix = d.get("detergent_matrix", {})
det_counts = {}
for family, dets in det_matrix.items():
    if isinstance(dets, dict):
        for det, cnt in dets.items():
            det_counts[det] = det_counts.get(det, 0) + cnt
sorted_dets = sorted(det_counts.items(), key=lambda x: -x[1])[:10]
slug_to_label = {
    "ddm": "DDM", "lmng": "LMNG", "dm": "DM", "cholesterol-hydrogen-succinate": "CHS",
    "og": "OG", "ng": "NG", "chaps": "CHAPS", "chapso": "CHAPSO", "ldao": "LDAO",
    "cymal-5": "Cymal-5", "cymal-6": "Cymal-6", "digitonin": "Digitonin",
    "fc-12": "FC-12", "fc-14": "FC-14", "triton-x-100": "Triton X-100",
    "dodecylphosphocholine": "DPC", "otg": "OTG",
    "n-dodecyl-beta-d-maltoside": "DDM",
}
top_detergents = [{"name": slug_to_label.get(k, k.upper()), "count": v}
                  for k, v in sorted_dets]

expr_data = d.get("expression_systems", {})
sorted_expr = sorted(expr_data.items(), key=lambda x: -x[1])[:8]
top_expressions = [{"name": k, "count": v} for k, v in sorted_expr]

step_data = d.get("step_profiles", {})
if step_data and isinstance(next(iter(step_data.values())), dict):
    flat_steps = {k: sum(v.values()) if isinstance(v, dict) else v for k, v in step_data.items()}
else:
    flat_steps = step_data
sorted_steps = sorted(flat_steps.items(), key=lambda x: -x[1])[:10]
top_steps = [{"name": k, "count": v} for k, v in sorted_steps]

stats = {
    "entities": {"total_pages": sum(entity_types.values()),
                 "total_structures": total_family_structs, **entity_types},
    "resolution": {"mean": res_data.get("overall_mean", "N/A"),
                   "median": res_data.get("overall_median", "N/A")},
    "top_families": top_families,
    "top_detergents": top_detergents,
    "top_expressions": top_expressions,
    "top_steps": top_steps,
}

DATA_DIR.mkdir(parents=True, exist_ok=True)
with open(DATA_DIR / "stats.yml", "w") as f:
    yaml.dump(stats, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
print(f"Wrote {DATA_DIR / 'stats.yml'}")
print(f"  {stats['entities']['total_pages']} pages, {stats['entities']['total_structures']} structures")
print(f"  Mean resolution: {stats['resolution']['mean']}Å, Median: {stats['resolution']['median']}Å")
print(f"  Top detergents: {', '.join(d['name'] for d in top_detergents[:5])}")
