#!/usr/bin/env python3
"""
Normalize free-text detergent fields into structured detergent_details array.

Adds `detergent_details` to purification steps — an array of {reagent, concentration, unit}.
Keeps original `detergent` field intact (append-only per P6).

Usage:
  python3 scripts/normalize_detergent.py               # live
  python3 scripts/normalize_detergent.py --dry-run      # preview only
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
W = BASE / "xray-mp-wiki"
DRY_RUN = "--dry-run" in sys.argv

# ── Detergent name map (auto-built from YAML directory) ──────────────

DETERGENT_NAME_MAP = {}  # lowercase name/alias → slug
DETERGENT_SLUGS = set()  # all known detergent slugs

rd = W / "xray-mp-wiki" / "reagents_yaml"
for yf in sorted(rd.glob("*.yaml")):
    slug = yf.stem
    try:
        data = yaml.safe_load(yf.read_text())
        if not isinstance(data, dict):
            continue
        tags = data.get("tags", []) or []
        if not any("detergent" in (t or "") for t in tags):
            continue
        title = data.get("title", slug)
        DETERGENT_SLUGS.add(slug)
        DETERGENT_NAME_MAP[title.lower().strip()] = slug
        # Parenthetical abbreviations: "n-Dodecyl (DDM)" → ddm
        m = re.search(r"\(([^)]+)\)", title)
        if m:
            abbr = m.group(1).strip().lower()
            if abbr and abbr != slug and abbr not in DETERGENT_SLUGS:
                DETERGENT_NAME_MAP[abbr] = slug
        # Slug itself (lowest priority — overwritten by more specific names)
        DETERGENT_NAME_MAP[slug.lower()] = slug
    except Exception:
        continue

# Common synonyms not covered by YAML titles
ADDITIONAL = {
    "dodecylmaltoside": "ddm",
    "lauryl maltose neopentyl glycol": "lmng",
    "chaps": "chapso",
}
DETERGENT_NAME_MAP.update(ADDITIONAL)

# ── Regexes ──────────────────────────────────────────────────────────

LINK_EXTRACT = re.compile(r"\[([^\]]+)\]\([^)]+/reagents/detergents/([^/)]+)/?\)")
# Concentration: number followed by unit. Capture unit variants.
CONC_RE = re.compile(r"([\d.]+)\s*((?:%\s*\(w/v\)|%|mM|µM|μM|mM|M)(?=\s|$|\)|,|/))")


def slug_from_text(raw_text):
    """Best-effort resolve a raw text fragment to a detergent slug.
    Returns (slug, concentration_value, concentration_unit).
    """
    # Try wikilink first
    m = LINK_EXTRACT.search(raw_text)
    if m:
        slug = m.group(2).lower().strip()
    else:
        slug = None

    # Extract concentration
    conc_val, conc_unit = None, None
    cm = CONC_RE.search(raw_text)
    if cm:
        conc_val = float(cm.group(1))
        conc_unit = cm.group(2).replace("(w/v)", "").strip()
        if conc_unit.startswith("%"):
            conc_unit = "%"

    if slug:
        return slug, conc_val, conc_unit

    # No wikilink — try name resolution from raw text
    clean = raw_text.lower().strip()
    # Strip concentration prefix: "0.5% (w/v) ddm" → "ddm"
    stripped = re.sub(r"^[\d.,\s%µµm/()w/v+\-]+", "", clean).strip()

    # Direct map lookup
    if clean in DETERGENT_NAME_MAP:
        return DETERGENT_NAME_MAP[clean], conc_val, conc_unit

    if stripped in DETERGENT_NAME_MAP:
        return DETERGENT_NAME_MAP[stripped], conc_val, conc_unit

    # Word-level matching: split stripped txt into words, check if any known
    words = set(re.findall(r"[a-z0-9-]+", stripped))
    for word in words:
        if word in DETERGENT_NAME_MAP:
            return DETERGENT_NAME_MAP[word], conc_val, conc_unit

    # Fuzzy: does any known name contain this word (or vice versa)?
    for word in words:
        for name, slug in DETERGENT_NAME_MAP.items():
            # Word-boundary-aware substring match
            if re.search(r"\b" + re.escape(word) + r"\b", name):
                return slug, conc_val, conc_unit
            if re.search(r"\b" + re.escape(name) + r"\b", word):
                return slug, conc_val, conc_unit

    return None, conc_val, conc_unit


def parse_detergent(det_text):
    """Parse a full detergent field into a list of normalized detail dicts.
    Returns [] if nothing can be extracted (for 'Not specified', empty, etc).
    """
    if isinstance(det_text, list):
        det_text = " ".join(str(x) for x in det_text)
    det_text = str(det_text).strip()
    if not det_text or det_text.lower() in ("not specified", "n/a", "-", "none", "not applicable"):
        return []

    # First pass: extract wikilinks directly
    results = []
    seen_slugs = set()
    for m in LINK_EXTRACT.finditer(det_text):
        slug = m.group(2).lower().strip()
        # Get concentration from surrounding text
        conc_val, conc_unit = None, None
        ctx = det_text[max(0, m.start() - 30) : m.end() + 10]
        cm = CONC_RE.search(ctx)
        if cm:
            conc_val = float(cm.group(1))
            conc_unit = cm.group(2).replace("(w/v)", "").strip()
            if conc_unit.startswith("%"):
                conc_unit = "%"
        if slug not in seen_slugs:
            results.append(
                {
                    "reagent": f"/xray-mp-wiki/reagents/detergents/{slug}/",
                    "concentration": str(conc_val) if conc_val is not None else None,
                    "unit": conc_unit,
                }
            )
            seen_slugs.add(slug)

    # Second pass: split raw text on separators and resolve each part
    # Strip wikilinks from the text for raw parsing
    text_plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", det_text)
    # Split on , / ; (these separate different detergents)
    parts = re.split(r"\s*[,/;]\s*", text_plain)

    for part in parts:
        part = part.strip()
        if not part:
            continue
        slug, conc_val, conc_unit = slug_from_text(part)
        if slug and slug not in seen_slugs:
            results.append(
                {
                    "reagent": f"/xray-mp-wiki/reagents/detergents/{slug}/",
                    "concentration": str(conc_val) if conc_val is not None else None,
                    "unit": conc_unit,
                }
            )
            seen_slugs.add(slug)

    return results


def main():
    total_steps = 0
    parsed = 0
    empty = 0
    skipped_already = 0
    type_counter = Counter()
    changes = []

    for yf in sorted((W / "proteins_yaml").glob("*.yaml")):
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        modified = False

        # Scan both old and DOI-grouped structures
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
                total_steps += 1
                # Skip if already has detergent_details
                if s.get("detergent_details") is not None:
                    skipped_already += 1
                    continue

                dt = s.get("detergent", "") or ""
                details = parse_detergent(dt)
                if details:
                    s["detergent_details"] = details
                    parsed += 1
                    modified = True
                    n = len(details)
                    if n == 1:
                        type_counter["single-detergent"] += 1
                        if details[0]["concentration"] is not None:
                            type_counter["with-concentration"] += 1
                        else:
                            type_counter["name-only"] += 1
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
    print(f"{mode}: {parsed} steps parsed, {empty} empty, {skipped_already} already had detergent_details")
    print(f"  ({len(changes)} files modified)")
    print("\nBreakdown:")
    for t, c in type_counter.most_common():
        print(f"  {c:5} | {t}")

    if DRY_RUN:
        print("\nRun without --dry-run to apply.")


if __name__ == "__main__":
    main()
