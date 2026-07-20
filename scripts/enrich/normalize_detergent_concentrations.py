#!/usr/bin/env python3
"""
Pass 1: Normalize free-text detergent fields into structured detergent_details.
Append-only — preserves original `detergent` field.

Usage:
  python3 scripts/normalize_detergent_concentrations.py               # live
  python3 scripts/normalize_detergent_concentrations.py --dry-run      # preview
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
W = BASE / "xray-mp-wiki"
DRY_RUN = "--dry-run" in sys.argv

# ── Detergent name map (auto-built from YAML directory) ──────────────

DETERGENT_NAME_MAP = {}
DETERGENT_SLUGS = set()

rd = W / "reagents_yaml"
for yf in sorted(rd.glob("*.yaml")):
    slug = yf.stem
    try:
        data = yaml.safe_load(yf.read_text())
        if not isinstance(data, dict): continue
        tags = data.get("tags", []) or []
        if not any("detergent" in (t or "") for t in tags): continue
        title = data.get("title", slug)
        DETERGENT_SLUGS.add(slug)
        DETERGENT_NAME_MAP[title.lower().strip()] = slug
        m = re.search(r"\(([^)]+)\)", title)
        if m:
            abbr = m.group(1).strip().lower()
            if abbr and abbr != slug and abbr not in DETERGENT_SLUGS:
                DETERGENT_NAME_MAP[abbr] = slug
        DETERGENT_NAME_MAP[slug.lower()] = slug
    except Exception:
        continue

ADDITIONAL = {
    "dodecylmaltoside": "ddm", "lauryl maltose neopentyl glycol": "lmng",
    "chaps": "chapso", "triton": "triton-x-100", "triton x-100": "triton-x-100",
    "nonylglucoside": "ng", "n-nonyl-beta-d-glucoside": "ng",
    "beta-dodecyl maltoside": "ddm", "beta-decylmaltoside": "dm",
    "decylmaltoside": "dm", "octylglucoside": "og",
    "n-octyl-beta-d-glucopyranoside": "og", "n-octyl-beta-d-thioglucoside": "otg",
    "octylthioglucoside": "otg",
    "n-dodecyl-n,n-(dimethylammonio)butyrate": "ddmab", "ddmab": "ddmab",
}
DETERGENT_NAME_MAP.update(ADDITIONAL)

# ── Regexes ──────────────────────────────────────────────────────────

LINK_EXTRACT = re.compile(r"\[([^\]]+)\]\([^)]+/reagents/detergents/([^/)]+)/?\)")

CONC_RE = re.compile(
    r"([\d.]+)\s*"
    r"((?:%\s*\(w/v\)|%(?!\w)|mg\s*/\s*ml|mg/ml|"
    r"µg/ml|μg/ml|mM|µM|μM|M)(?=\s|$|\)|,|/|;|\+|\|))",
    re.IGNORECASE,
)

PAREN_QUALIFIER = re.compile(r"\s*\((?:w/v|v/v|w/w)\)\s*", re.IGNORECASE)

MULTI_SEP = re.compile(
    r"\s*(?:[,/;]|\s+and\s+|\s*\+\s*|\s+with\s+|\s+in\s+)\s*",
    re.IGNORECASE,
)


def slug_from_text(raw_text):
    m = LINK_EXTRACT.search(raw_text)
    slug = m.group(2).lower().strip() if m else None
    conc_val, conc_unit = None, None
    cm = CONC_RE.search(raw_text)
    if cm:
        conc_val = cm.group(1)
        conc_unit = cm.group(2).strip()
        if conc_unit:
            conc_unit = re.sub(r"\s+", "", conc_unit)
            if re.match(r"%\(v/v\)$", conc_unit):
                conc_unit = "%"
            elif re.match(r"%\(w/v\)$", conc_unit):
                conc_unit = "%"
            elif conc_unit.startswith("%"):
                conc_unit = "%"
    if slug:
        return slug, conc_val, conc_unit
    clean = raw_text.lower().strip()
    if clean in DETERGENT_NAME_MAP:
        return DETERGENT_NAME_MAP[clean], conc_val, conc_unit
    stripped = re.sub(r"^[\d.,\s%µmμm/()w/v+\-]+", "", clean).strip()
    if stripped and stripped in DETERGENT_NAME_MAP:
        return DETERGENT_NAME_MAP[stripped], conc_val, conc_unit
    words = set(w for w in re.findall(r"[a-z0-9-]+", stripped if stripped else clean) if len(w) >= 3)
    for word in words:
        if word in DETERGENT_NAME_MAP:
            return DETERGENT_NAME_MAP[word], conc_val, conc_unit
    best_match, best_count = None, 0
    for word in words:
        for name, nslug in DETERGENT_NAME_MAP.items():
            if re.search(r"\b" + re.escape(word) + r"\b", name):
                n_matches = sum(1 for w in words if re.search(r"\b" + re.escape(w) + r"\b", name))
                if n_matches > best_count:
                    best_count, best_match = n_matches, nslug
    if best_match and best_count >= 2:
        return best_match, conc_val, conc_unit
    return None, conc_val, conc_unit


def parse_detergent(det_text):
    if isinstance(det_text, list):
        det_text = " ".join(str(x) for x in det_text)
    det_text = str(det_text).strip()
    skip_words = {"not specified", "n/a", "-", "--", "none", "not applicable",
                  "see supplementary", "see supplementary materials", "see supplementary information"}
    if not det_text or det_text.lower() in skip_words:
        return []
    results, seen_slugs = [], set()
    # First pass: extract wikilinks
    for m in LINK_EXTRACT.finditer(det_text):
        slug = m.group(2).lower().strip()
        if slug not in DETERGENT_SLUGS:
            continue
        ctx = det_text[max(0, m.start() - 40): m.end() + 20]
        cm = CONC_RE.search(ctx)
        conc_val = cm.group(1) if cm else None
        conc_unit = cm.group(2).strip() if cm else None
        if conc_unit:
            conc_unit = re.sub(r"\s+", "", conc_unit)
        if slug not in seen_slugs:
            results.append({"reagent": f"/xray-mp-wiki/reagents/detergents/{slug}/",
                            "concentration": str(conc_val) if conc_val is not None else None,
                            "unit": conc_unit})
            seen_slugs.add(slug)
    # Second pass: split on separators, resolve each part
    text_plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", det_text)
    text_plain = PAREN_QUALIFIER.sub(" ", text_plain)
    for part in MULTI_SEP.split(text_plain):
        part = part.strip()
        if not part: continue
        slug, conc_val, conc_unit = slug_from_text(part)
        if slug and slug not in seen_slugs:
            results.append({"reagent": f"/xray-mp-wiki/reagents/detergents/{slug}/",
                            "concentration": str(conc_val) if conc_val is not None else None,
                            "unit": conc_unit})
            seen_slugs.add(slug)
    return results


def main():
    total_steps = parsed = empty = skipped = 0
    type_counter = Counter()
    changes = []
    for yf in sorted((W / "proteins_yaml").glob("*.yaml")):
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict): continue
        modified = False
        purif_sources = list(data.get("purifications", []) or [])
        for pub in data.get("publications", []) or []:
            if isinstance(pub, dict):
                purif_sources.extend(pub.get("purifications", []) or [])
        for p in purif_sources:
            if not isinstance(p, dict): continue
            for s in p.get("steps", []) or []:
                if not isinstance(s, dict): continue
                total_steps += 1
                dt = s.get("detergent", "") or ""
                existing_dd = s.get("detergent_details")
                if existing_dd is not None:
                    has_conc = any(
                        d.get("concentration") is not None and str(d.get("concentration", "")).strip()
                        for d in (existing_dd if isinstance(existing_dd, list) else [existing_dd])
                    )
                    if has_conc:
                        skipped += 1
                        continue
                    # Merge: fill null concentration from parse
                    details = parse_detergent(dt)
                    if details:
                        merged = list(existing_dd) if isinstance(existing_dd, list) else [existing_dd]
                        updated = False
                        for existing in merged:
                            e_slug = existing.get("reagent", "").rstrip("/").split("/")[-1] if existing.get("reagent") else ""
                            for pe in details:
                                p_slug = pe.get("reagent", "").rstrip("/").split("/")[-1] if pe.get("reagent") else ""
                                if e_slug == p_slug:
                                    if not existing.get("concentration"):
                                        existing["concentration"] = pe.get("concentration")
                                        existing["unit"] = pe.get("unit")
                                        updated = True
                                    break
                        if updated:
                            s["detergent_details"] = merged
                            type_counter["conc-filled"] += 1
                            modified = True
                    skipped += 1
                    continue
                details = parse_detergent(dt)
                if details:
                    s["detergent_details"] = details
                    parsed += 1
                    modified = True
                    n = len(details)
                    if n == 1:
                        type_counter["single-detergent"] += 1
                        type_counter["with-concentration" if details[0]["concentration"] is not None else "name-only"] += 1
                    else:
                        type_counter["multi-detergent"] += 1
                else:
                    empty += 1
        if modified:
            changes.append(yf.stem)
            if not DRY_RUN:
                raw = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
                yf.write_text(raw)
    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"{mode}: {parsed} new steps, {type_counter.get('conc-filled',0)} conc-filled, {empty} empty, {skipped} skipped")
    print(f"  ({len(changes)} files modified)")
    for t, c in type_counter.most_common():
        print(f"  {c:5} | {t}")
    if DRY_RUN:
        print("\nRun without --dry-run to apply.")


if __name__ == "__main__":
    main()
