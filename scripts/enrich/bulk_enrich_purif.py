#!/usr/bin/env python3
"""Bulk enrich purification/crystallization fields — local, fast, 0 token cost."""

import re
from pathlib import Path

import yaml

W = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki")

ENTITIES = [
    (re.compile(r"\bddm\b", re.IGNORECASE), "/xray-mp-wiki/reagents/detergents/ddm/", "DDM", "ddm"),
    (re.compile(r"\blmng\b", re.IGNORECASE), "/xray-mp-wiki/reagents/detergents/lmng/", "LMNG", "lmng"),
    (re.compile(r"\bdm\b", re.IGNORECASE), "/xray-mp-wiki/reagents/detergents/dm/", "DM", "dm"),
    (re.compile(r"\bog\b", re.IGNORECASE), "/xray-mp-wiki/reagents/detergents/og/", "OG", "og"),
    (
        re.compile(r"\bchs\b", re.IGNORECASE),
        "/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/",
        "CHS",
        "chs",
    ),
    (re.compile(r"\bldao\b", re.IGNORECASE), "/xray-mp-wiki/reagents/detergents/ldao/", "LDAO", "ldao"),
    (re.compile(r"\btev\b", re.IGNORECASE), "/xray-mp-wiki/reagents/enzymes/tev-protease/", "TEV", "tev"),
    (re.compile(r"\bbril\b", re.IGNORECASE), "/xray-mp-wiki/reagents/protein-tags/bril/", "BRIL", "bril"),
    (re.compile(r"\bflag\b", re.IGNORECASE), "/xray-mp-wiki/reagents/protein-tags/flag-tag/", "FLAG", "flag"),
    (re.compile(r"\bni-nta\b", re.IGNORECASE), "/xray-mp-wiki/reagents/additives/nickel-nta/", "Ni-NTA", "ni-nta"),
    (re.compile(r"\btalon\b", re.IGNORECASE), "/xray-mp-wiki/reagents/additives/talon/", "TALON", "talon"),
    (
        re.compile(r"\bsuperdex[- ]200\b", re.IGNORECASE),
        "/xray-mp-wiki/reagents/additives/superdex-200/",
        "Superdex 200",
        "superdex-200",
    ),
    (re.compile(r"\blcp\b", re.IGNORECASE), "/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/", "LCP", "lcp"),
    (
        re.compile(r"\blipidic cubic phase\b", re.IGNORECASE),
        "/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/",
        "LCP",
        "lcp",
    ),
    (
        re.compile(r"\bsec\b", re.IGNORECASE),
        "/xray-mp-wiki/methods/purification/size-exclusion-chromatography/",
        "SEC",
        "sec",
    ),
    (
        re.compile(r"\bsize exclusion chromatography\b", re.IGNORECASE),
        "/xray-mp-wiki/methods/purification/size-exclusion-chromatography/",
        "SEC",
        "sec",
    ),
    (
        re.compile(r"\bsad\b", re.IGNORECASE),
        "/xray-mp-wiki/methods/structure-determination/single-anomalous-dispersion/",
        "SAD",
        "sad",
    ),
    (re.compile(r"\bmad\b", re.IGNORECASE), "/xray-mp-wiki/methods/structure-determination/mad-phasing/", "MAD", "mad"),
    (
        re.compile(r"\baffinity chromatography\b", re.IGNORECASE),
        "/xray-mp-wiki/methods/purification/affinity-chromatography/",
        "affinity chromatography",
        "affinity-chromatography",
    ),
]


def has_wl(text, ent_name):
    return bool(re.search(r"\[[^\]]+\]\(/xray-mp-wiki/[^)]+\b" + re.escape(ent_name) + r"\b", str(text), re.IGNORECASE))


total_mod = 0
total_links = 0

for yf in sorted((W / "proteins_yaml").rglob("*.yaml")):
    data = yaml.safe_load(yf.read_text())
    if not isinstance(data, dict):
        continue

    modified = False
    links_this = 0
    step_fields = ["detergent", "method", "resin", "buffer", "notes"]
    cry_fields = ["method", "protein_sample", "reservoir", "notes"]

    for p in data.get("purifications", []) or []:
        for s in p.get("steps", []) or []:
            if not isinstance(s, dict):
                continue
            for f in step_fields:
                val = s.get(f, "")
                if not val or not isinstance(val, str):
                    continue
                for pat, path, disp, ent_name in ENTITIES:
                    if not pat.search(val):
                        continue
                    if has_wl(val, ent_name):
                        continue
                    wl = f"[{disp}]({path})"
                    val = pat.sub(wl, val, count=1)
                    s[f] = val
                    modified = True
                    links_this += 1

    # Also check DOI-grouped publications[].purifications structure
    for pub in data.get("publications", []) or []:
        if not isinstance(pub, dict):
            continue
        for p in pub.get("purifications", []) or []:
            if not isinstance(p, dict):
                continue
            for s in p.get("steps", []) or []:
                if not isinstance(s, dict):
                    continue
                for f in step_fields:
                    val = s.get(f, "")
                    if not val or not isinstance(val, str):
                        continue
                    for pat, path, disp, ent_name in ENTITIES:
                        if not pat.search(val):
                            continue
                        if has_wl(val, ent_name):
                            continue
                        wl = f"[{disp}]({path})"
                        val = pat.sub(wl, val, count=1)
                        s[f] = val
                        modified = True
                        links_this += 1

    for c in data.get("crystallizations", []) or []:
        if not isinstance(c, dict):
            continue
        for f in cry_fields:
            val = c.get(f, "")
            if not val or not isinstance(val, str):
                continue
            for pat, path, disp, ent_name in ENTITIES:
                if not pat.search(val.lower()):
                    continue
                if has_wl(val, ent_name):
                    continue
                wl = f"[{disp}]({path})"
                val = pat.sub(wl, val, count=1)
                c[f] = val
                modified = True
                links_this += 1

    if modified:
        raw = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        yf.write_text(raw)
        total_mod += 1
        total_links += links_this

print(f"Modified: {total_mod} files")
print(f"Total wikilinks added: {total_links}")
