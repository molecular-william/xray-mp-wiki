#!/usr/bin/env python3
"""
Pass 1: Normalize free-text buffer fields into structured buffer_details.
Append-only — preserves original `buffer` field.

Usage:
  python3 scripts/normalize_buffer_compositions.py               # live
  python3 scripts/normalize_buffer_compositions.py --dry-run      # preview
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
W = BASE / "xray-mp-wiki"
DRY_RUN = "--dry-run" in sys.argv

# ── Reagent name map (all reagents, categorized by subdirectory tag) ─

REAGENT_NAME_MAP = {}

rd = W / "reagents_yaml"
for yf in sorted(rd.glob("*.yaml")):
    slug = yf.stem
    try:
        data = yaml.safe_load(yf.read_text())
        if not isinstance(data, dict): continue
        tags = data.get("tags", []) or []
        category = None
        for t in tags:
            if t.startswith("subdirectory-"):
                category = t.replace("subdirectory-", "")
                break
        if not category: continue
        title = data.get("title", slug)
        REAGENT_NAME_MAP[title.lower().strip()] = (slug, category)
        m = re.search(r"\(([^)]+)\)", title)
        if m:
            abbr = m.group(1).strip().lower()
            if abbr and abbr not in REAGENT_NAME_MAP:
                REAGENT_NAME_MAP[abbr] = (slug, category)
        REAGENT_NAME_MAP[slug.lower()] = (slug, category)
    except Exception:
        continue

ADDITIONAL = {
    "nacl": ("sodium-chloride", "additives"), "mgcl2": ("magnesium-chloride", "additives"),
    "kcl": ("potassium-chloride", "additives"), "beta-me": ("beta-mercaptoethanol", "additives"),
    "tcep": ("tcep", "additives"), "dtt": ("dtt", "additives"), "edta": ("edta", "additives"),
    "glycerol": ("glycerol", "additives"), "sucrose": ("sucrose", "additives"),
    "imidazole": ("imidazole", "additives"), "tris-hcl": ("tris", "buffers"),
    "hepes": ("hepes", "buffers"), "tris": ("tris", "buffers"),
    "sodium phosphate": ("sodium-phosphate", "buffers"), "na-phosphate": ("sodium-phosphate", "buffers"),
    "phosphate": ("sodium-phosphate", "buffers"), "pbs": ("pbs", "buffers"),
    "tbs": ("tbs", "buffers"),
    "mops": ("mops", "buffers"), "mes": ("mes", "buffers"),
    "bis-tris": ("bis-tris", "buffers"), "sodium-citrate": ("sodium-citrate", "buffers"),
    "capss": ("caps", "buffers"), "caps": ("caps", "buffers"),
    "kpi": ("potassium-phosphate", "buffers"), "na-k-tartrate": ("sodium-potassium-tartrate", "additives"),
    "kh2po4": ("kh2po4", "additives"), "k2hpo4": ("k2hpo4", "additives"),
    "nah2po4": ("sodium-phosphate-monobasic", "additives"), "na2hpo4": ("sodium-phosphate-dibasic", "additives"),
}
REAGENT_NAME_MAP.update(ADDITIONAL)

# ── Regexes ───┘

REAGENT_LINK = re.compile(r"\[([^\]]+)\]\([^)]*/reagents/(buffers|additives|detergents)/([^/)]+)/?\)")
CONC_RE = re.compile(r"~?([\d.]+)\s*((?:%\s*\([vw]/[vw]\)|%(?!\w)|mg\s*/\s*ml|mg/ml|mM|M|µM|μM|×?\s*x\b)(?=\s|$|\)|,|;))", re.IGNORECASE)
PH_RE = re.compile(r"pH\s*([\d.]+)", re.IGNORECASE)
# Also catch (pH X.X) with surrounding parens
PH_PAREN_RE = re.compile(r"\(pH\s*([\d.]+)\)", re.IGNORECASE)
COMPONENT_SPLIT = re.compile(r",\s*(?![^()]*\))")
SKIP_PATTERNS = re.compile(r"(protease inhibitor|complete\s*protease|supplemented with|containing|in the presence of|see supplementary|not specified|n/a|none)\b", re.IGNORECASE)
UNIT_QUALIFIER = re.compile(r"\s*\([vw]/[vw]\)", re.IGNORECASE)


def _extract_ph(text):
    """Try pH X.X first, then (pH X.X)."""
    m = PH_RE.search(text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    m = PH_PAREN_RE.search(text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    return None


def reagent_path(cat, slug):
    return f"/xray-mp-wiki/reagents/{cat}/{slug}/"


def parse_buffer(buf_text):
    if isinstance(buf_text, list):
        buf_text = " ".join(str(x) for x in buf_text)
    buf_text = str(buf_text).strip()
    # Pre-clean: strip ]] noise, double spaces
    buf_text = re.sub(r"\]+", "", buf_text)
    buf_text = re.sub(r"\s{2,}", " ", buf_text)
    skip_words = {"not specified", "n/a", "-", "--", "none", "not applicable",
                  "see supplementary", "see supplementary materials"}
    if not buf_text or buf_text.lower() in skip_words:
        return []
    results, seen_slugs = [], set()
    # First pass: extract wikilinks with component boundary parsing
    for m in REAGENT_LINK.finditer(buf_text):
        slug = m.group(3).lower().strip()
        cat = m.group(2)
        if slug in seen_slugs: continue
        comp_start = buf_text.rfind(",", 0, m.start())
        comp_start = 0 if comp_start == -1 else comp_start + 1
        comp_end = buf_text.find(",", m.end())
        comp_end = len(buf_text) if comp_end == -1 else comp_end
        component = buf_text[comp_start:comp_end].strip()
        cm = CONC_RE.search(component)
        conc = cm.group(1) if cm else None
        unit = cm.group(2).strip() if cm else None
        if unit:
            unit = UNIT_QUALIFIER.sub("", unit).strip()
            unit = re.sub(r"\s+", "", unit)
        ph = None
        if cat == "buffers":
            ph = _extract_ph(component)
        results.append({"reagent": reagent_path(cat, slug),
                        "concentration": str(conc) if conc is not None else None,
                        "unit": unit, "ph": ph})
        seen_slugs.add(slug)
    # Second pass: split on commas, resolve unlinked components
    text_plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", buf_text)
    for comp in COMPONENT_SPLIT.split(text_plain):
        comp = comp.strip()
        if not comp or SKIP_PATTERNS.search(comp) or len(comp) < 3:
            continue
        ph = _extract_ph(comp) if "pH" in comp else None
        m = REAGENT_LINK.search(comp)
        if m:
            slug, cat = m.group(3).lower().strip(), m.group(2)
            if slug in seen_slugs: continue
            cm = CONC_RE.search(comp)
            conc = cm.group(1) if cm else None
            unit = cm.group(2).strip() if cm else None
            if unit:
                unit = UNIT_QUALIFIER.sub("", unit).strip()
                unit = re.sub(r"\s+", "", unit)
            if cat == "buffers":
                ph = _extract_ph(comp)
            results.append({"reagent": reagent_path(cat, slug), "concentration": str(conc) if conc is not None else None,
                            "unit": unit, "ph": ph})
            seen_slugs.add(slug)
        else:
            cm = CONC_RE.search(comp)
            conc = cm.group(1) if cm else None
            unit = cm.group(2).strip() if cm else None
            if unit:
                unit = UNIT_QUALIFIER.sub("", unit).strip()
                unit = re.sub(r"\s+", "", unit)
            clean = comp.lower().strip()
            stripped = re.sub(r"^[\d.,\s%µμ/()+\-]+", "", clean).strip()
            # Also strip leading unit abbreviation that the conc regex may leave (e.g. 'mm' from mM)
            stripped = re.sub(r"^(?:mm|µm|μm|mg/ml)\b", "", stripped).strip()
            stripped = re.sub(r"\s*hcl\s*$", "", stripped).strip()
            name_match = None
            for name in (clean, stripped):
                if name in REAGENT_NAME_MAP:
                    name_match = REAGENT_NAME_MAP[name]
                    break
            if not name_match and stripped:
                # Normalize: strip common suffixes/prefixes
                normed = re.sub(r"\s*(-so4|-h2so4|-naoh|-hcl)\s*$", "", stripped)
                normed = re.sub(r"^na-(hepes|h?epes|mes|mops|tris|caps|phosphate)\b", r"\1", normed)
                normed = re.sub(r"^(hepes|h?epes)-naoh\b", r"\1", normed)
                # Split on / for multi-component entries
                for part in normed.split("/"):
                    part = part.strip()
                    if part in REAGENT_NAME_MAP:
                        name_match = REAGENT_NAME_MAP[part]
                        break
                if not name_match:
                    words = set(w for w in re.findall(r"[a-z0-9-]+", normed) if len(w) >= 3)
                    for word in words:
                        if word in REAGENT_NAME_MAP:
                            name_match = REAGENT_NAME_MAP[word]
                            break
            if name_match:
                slug, cat = name_match
                if slug not in seen_slugs:
                    results.append({"reagent": reagent_path(cat, slug),
                                    "concentration": str(conc) if conc is not None else None,
                                    "unit": unit, "ph": None})
                    seen_slugs.add(slug)
    return results


def main():
    total_steps = parsed = empty = skipped = 0
    buf_counter = Counter()
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
                if s.get("buffer_details") is not None:
                    skipped += 1
                    continue
                bt = s.get("buffer", "") or ""
                details = parse_buffer(bt)
                if details:
                    s["buffer_details"] = details
                    parsed += 1
                    modified = True
                    for d in details:
                        slug = d.get("reagent", "").rstrip("/").split("/")[-1] if d.get("reagent") else ""
                        buf_counter[slug] += 1
                else:
                    empty += 1
        if modified:
            changes.append(yf.stem)
            if not DRY_RUN:
                raw = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
                yf.write_text(raw)
    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"{mode}: {parsed} steps, {empty} empty, {skipped} skipped ({len(changes)} files)")
    for slug, count in buf_counter.most_common(10):
        print(f"  {count:5} | {slug}")
    if DRY_RUN:
        print("\nRun without --dry-run to apply.")


if __name__ == "__main__":
    main()
