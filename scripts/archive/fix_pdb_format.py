#!/usr/bin/env python3
"""
Fix non-standard PDB format entries in protein YAMLs.

Extracts actual 4-char PDB codes from descriptive fields like:
  '1P7B (Structure I)'       → pdb_id: 1P7B, notes: + "(Structure I)"
  '3H5M (rebuilt)'            → pdb_id: 3H5M, notes: + "(rebuilt)"
  '(not deposited)'           → pdb_id: ''
  '4EY'                       → pdb_id: 4EY (flag for review if not found in dataset)

Usage:
  DRY_RUN=1 python3 scripts/fix_pdb_format.py
  python3 scripts/fix_pdb_format.py
"""

import os
import re
from pathlib import Path

DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
YAML_DIR = PROJECT_ROOT / "xray-mp-wiki" / "proteins_yaml"

# Keywords that indicate no PDB was deposited
NO_PDB_KEYWORDS = [
    "not deposited",
    "not explicitly deposited",
    "not deposited in pdb",
    "not specified",
    "no pdb",
    "no structure deposited",
    "pdb not deposited",
    "no accession",
    "not in pdb",
    "not available",
    "not stated",
    "not found in text",
    "not determined",
    "not stated in raw paper",
]

# Text patterns that indicate no PDB code (exact match after strip)
NO_PDB_EXACT = {
    "~",
    "--",
    "—",
    "-",
    "n/a",
    "unknown",
    "tbd",
    "to be determined",
    "pending",
    "unsolved",
    "not deposited in pdb per paper",
}


def is_valid_pdb(s):
    """Check if string is a valid 4-char PDB code."""
    return bool(re.match(r"^[A-Z0-9]{4}$", s))


# Words that look like PDB codes but aren't
PDB_STOPLIST = {
    "form",
    "type",
    "wild",
    "full",
    "long",
    "high",
    "low",
    "open",
    "free",
    "post",
    "pre-",
    "data",
    "cell",
    "site",
    "side",
    "core",
    "loop",
    "turn",
    "main",
    "this",
    "that",
    "with",
    "from",
    "iso",
    "not",
    "new",
    "old",
    "apo",
    "holo",
    "xtal",
    "cryo",
    "calc",
    "mod",
    "ref",
    "init",
    "part",
    "unit",
    "mode",
    "node",
}


def extract_pdb_from_text(text):
    """
    Try to extract PDB code from a descriptive field.
    Returns (pdb_code, remainder) or (None, text) if no PDB found.
    """
    t = text.strip()
    if not t:
        return None, t

    # Check if it's already valid
    if is_valid_pdb(t.upper()):
        return t.upper(), ""

    # Check if whole text is "not deposited" or similar
    t_lower = t.lower().strip("—").strip("-").strip()
    if t_lower in (
        "not specified",
        "not deposited",
        "not explicitly deposited",
        "not deposited in pdb per paper",
        "none",
        "null",
        "n/a",
        "unknown",
        "",
    ):
        return None, ""

    # Strategy 1: Text starts with a 4-char PDB, optionally followed by parenthetical
    # e.g., "1P7B (Structure I)", "3H5M (rebuilt)", "3KG2 (reference structure)"
    m = re.match(r"^([A-Z0-9]{4})\s*(?:[\(\[].+?[\)\]])?\s*$", t, re.IGNORECASE)
    if m:
        pdb = m.group(1).upper()
        if pdb.lower() not in PDB_STOPLIST:
            # Extract the parenthetical part as remainder
            paren = re.search(r"[\(\[].+?[\)\]]", t)
            rest = paren.group(0) if paren else ""
            return pdb, rest

    # Strategy 2: Text is just a 4-char code followed by short note (no colon/slash)
    # e.g., "4EY" — but only if it looks like a PDB, not a word
    m = re.match(r"^([A-Z0-9]{4})\s*$", t, re.IGNORECASE)
    if m:
        pdb = m.group(1).upper()
        if pdb.lower() not in PDB_STOPLIST:
            return pdb, ""

    # Strategy 3: Contains "PDB XXXX" or "accession XXXX" or "deposited as XXXX"
    m = re.search(r"(?:PDB|accession|deposited\s+(?:as\s+)?|code\s+)([A-Z0-9]{4})\b", t, re.IGNORECASE)
    if m:
        pdb = m.group(1).upper()
        if pdb.lower() not in PDB_STOPLIST:
            return pdb, t

    # Strategy 4: Text is entirely wrapped in parens/brackets and has no valid PDB
    # e.g., "(U18666A-bound structure)", "[tamoxifen complex]"
    if re.match(r"^[\(\[].+[\)\]]$", t):
        return None, ""

    # Strategy 5: Known placeholder terms
    if t.lower() in ("tbd", "to be determined", "pending", "unknown"):
        return None, ""

    return None, t


def repack_yaml(data):
    """Re-pack YAML preserving field ordering."""
    import yaml as yml

    class OrderedDumper(yml.Dumper):
        pass

    def dict_representer(dumper, data):
        return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(dict, dict_representer)

    return yml.dump(
        data,
        Dumper=OrderedDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )


def main():
    import yaml as yml

    _ = yml

    print(f"Mode: {'DRY RUN' if DRY_RUN else 'LIVE'}")
    print()

    total_fixed = 0
    total_review = 0

    for yf in sorted(YAML_DIR.glob("*.yaml")):
        name = yf.stem
        raw = yf.read_text()
        data = yml.safe_load(raw)
        if not isinstance(data, dict):
            continue

        structures = data.get("structures", [])
        if not structures:
            continue

        modified = False
        for si, s in enumerate(structures):
            if not isinstance(s, dict):
                continue

            pdb = s.get("pdb_id", "")
            if not pdb or not isinstance(pdb, str):
                continue

            # Skip already-valid PDB codes
            if is_valid_pdb(pdb.strip().upper()):
                continue

            # Skip empty/placeholder fields
            stripped = pdb.strip().strip("—").strip("-")
            if not stripped:
                continue

            # Check for exact match no-PDB patterns first
            if stripped.lower() in NO_PDB_EXACT:
                old_notes = s.get("notes", "") or ""
                note = f"[Previously listed as: {stripped[:60]}]"
                if old_notes:
                    s["notes"] = f"{old_notes} {note}"
                else:
                    s["notes"] = note
                s["pdb_id"] = ""
                modified = True
                total_fixed += 1
                if DRY_RUN:
                    print(f"  {name}: structures[{si}] cleared ({stripped})")
                else:
                    print(f"  CLEARED {name}: structures[{si}] ({stripped})")
                continue

            # Check for "not deposited" keywords
            if any(kw in stripped.lower() for kw in NO_PDB_KEYWORDS):
                old_notes = s.get("notes", "") or ""
                note = f"[Previously listed as: {stripped[:60]}]"
                if old_notes:
                    s["notes"] = f"{old_notes} {note}"
                else:
                    s["notes"] = note
                s["pdb_id"] = ""
                modified = True
                total_fixed += 1
                if DRY_RUN:
                    print(f"  {name}: structures[{si}] cleared (not deposited)")
                else:
                    print(f"  CLEARED {name}: structures[{si}] (not deposited)")
                continue

            # Try to extract PDB code from descriptive text
            pdb_code, remainder = extract_pdb_from_text(stripped)

            if pdb_code and is_valid_pdb(pdb_code):
                old_notes = s.get("notes", "") or ""
                if remainder:
                    note = f"[{stripped[:80]}]"
                    if old_notes:
                        s["notes"] = f"{old_notes} {note}"
                    else:
                        s["notes"] = note
                elif len(stripped) > 4 and stripped.upper() != pdb_code:
                    # e.g., "4EY" → pdb_code="4EY" but not 4 chars → still flag
                    note = f"[Orig: {stripped[:60]}]"
                    if old_notes:
                        s["notes"] = f"{old_notes} {note}"

                s["pdb_id"] = pdb_code
                modified = True
                total_fixed += 1
                tag = " (DRY RUN)" if DRY_RUN else ""
                print(f"  FIXED {name}: structures[{si}] '{stripped[:50]}' → PDB {pdb_code}{tag}")
            else:
                # Could not extract — flag for manual review
                total_review += 1
                print(f"  ⚠ REVIEW {name}: structures[{si}] '{stripped[:60]}' — unrecognizable")

        if modified and not DRY_RUN:
            yf.write_text(repack_yaml(data))

    print()
    print(f"  Fixed:        {total_fixed}")
    print(f"  Needs review: {total_review}")
    print(f"  Mode: {'DRY RUN' if DRY_RUN else 'LIVE'}")


if __name__ == "__main__":
    main()
