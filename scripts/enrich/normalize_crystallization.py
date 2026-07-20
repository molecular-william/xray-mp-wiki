#!/usr/bin/env python3
"""
Deterministic Pass 1: Parse crystallization entries and add structured
crystallization_details to protein YAMLs.

Dry-run mode: --dry-run (prints report, no changes)
Production mode: no flag (writes changes)

Follows the same pattern as normalize_buffer_compositions.py:
- Auto-builds reagent name map from YAML directories
- Parses free-text via regex
- Adds structured parallel field alongside existing free-text
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml as std_yaml

BASE = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
DRY_RUN = "--dry-run" in sys.argv


# ─── Reagent name map (auto-built from reagent YAMLs) ──────────────
# Maps lowercase names and parenthetical abbreviations to wiki slugs
def build_reagent_map():
    """Build {lowercase_name: slug} and {abbreviation: slug} maps from reagent YAMLs."""
    name_map = {}
    for yf in sorted(BASE.glob("xray-mp-wiki/reagents_yaml/*.yaml")):
        try:
            data = std_yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not data:
            continue
        slug = yf.stem
        title = data.get("title", "")
        if not title:
            continue
        # Map title (lowercased)
        name_map[title.lower().strip()] = slug
        # Map parenthetical abbreviation: "n-Dodecyl-beta-D-maltopyranoside (DDM)" → ddm
        m = re.search(r"\(([^)]+)\)\s*$", title)
        if m:
            abbr = m.group(1).lower().strip()
            if abbr not in name_map:
                name_map[abbr] = slug
        # Map chemical stem for common reagents
        for stem in [slug.replace("-", " ").lower()]:
            name_map[stem] = slug

    # Add common known aliases
    manual = {
        "peg": "peg",
        "peg 400": "peg-400",
        "peg400": "peg-400",
        "peg 4000": "peg-4000",
        "peg4000": "peg-4000",
        "peg 3350": "peg-3350",
        "peg3350": "peg-3350",
        "mpd": "mpd",
        "glycerol": "glycerol",
        "tcep": "tcep",
        "beta-mercaptoethanol": "beta-mercaptoethanol",
        "dtt": "dtt",
        "sodium chloride": "sodium-chloride",
        "nacl": "sodium-chloride",
        "ammonium sulfate": "ammonium-sulfate",
        "ammonium sulphate": "ammonium-sulfate",
        "calcium chloride": "calcium-chloride",
        "cacl2": "calcium-chloride",
        "magnesium chloride": "magnesium-chloride",
        "mgcl2": "magnesium-chloride",
        "sodium citrate": "citrate",
        "tris": "tris",
        "tris-hcl": "tris",
        "hepes": "hepes",
        "mes": "mes",
        "imidazole": "imidazole",
        "sodium acetate": "acetate",
        "ammonium acetate": "ammonium-acetate",
        "sodium phosphate": "sodium-phosphate",
        "potassium phosphate": "potassium-phosphate",
        "monoolein": "monoolein",
        "cholesterol": "cholesterol",
    }
    name_map.update(manual)
    return name_map


REAGENT_MAP = build_reagent_map()

# ─── Controlled vocabulary ─────────────────────────────────────────
METHOD_LC_MAP = {
    "lcp": "lcp",
    "lipidic cubic phase": "lcp",
    "cubic phase": "lcp",
    "vapor diffusion": "vapor-diffusion",
    "vapor-diffusion": "vapor-diffusion",
    "sitting drop": "vapor-diffusion",
    "hanging drop": "vapor-diffusion",
    "microbatch": "microbatch",
    "dialysis": "dialysis",
    "bicelle": "bicelle",
    "nanodisc": "nanodisc",
    "free interface diffusion": "free-interface-diffusion",
    "counter diffusion": "counter-diffusion",
}

# ─── Regex patterns ─────────────────────────────────────────────────

# Temperature: "20 C", "20 °C", "20°C", "20", "293 K", "20-22 C"
TEMP_RE = re.compile(
    r"(\d+[\d.]*(?:\s*[–-]\s*\d+[\d.]*)?)\s*"  # value or range
    r"(°?\s*[CcKk]|°C|°\s*C)?"  # optional unit
)

# pH: "pH 7.5", "pH7.5", "pH 5.6"
PH_RE = re.compile(r"pH\s*(\d+\.?\d*)", re.IGNORECASE)

# Concentration + unit at start of reservoir component
# Handles: "0.1 M", "100 mM", "30%", "30% (w/v)", "1.7-2.0 M"
CONC_RE = re.compile(
    r"([\d.]+(?:[–-][\d.]+)?)\s*"  # value or range
    r"(%|M|mM|mM)"  # unit
    r"(?:\s*\([^)]*\))?"  # optional (w/v) qualifier
)

# PEG pattern: "PEG 400", "PEG400", "PEG 4000", "polyethylene glycol 400"
PEG_RE = re.compile(r"(?:PEG|polyethylene\s*glycol)\s*-?\s*(\d+)", re.IGNORECASE)

# Buffer names commonly found in reservoir strings
BUFFER_NAMES = [
    "tris",
    "hepes",
    "mes",
    "mops",
    "imidazole",
    "citrate",
    "acetate",
    "phosphate",
    "bicine",
    "tricine",
    "cacodylate",
    "ada",
    "pipes",
    "bes",
    "tes",
    "ches",
    "caps",
    "epes",
    "glycine",
    "sodium acetate",
    "sodium citrate",
    "sodium phosphate",
    "potassium phosphate",
    "bis-tris",
    "bis-tris propane",
]

# ─── Reservoir parsing ─────────────────────────────────────────────


def resolve_reagent(name):
    """Resolve a reagent name to a wiki slug."""
    key = name.lower().strip().rstrip(".")
    if key in REAGENT_MAP:
        return REAGENT_MAP[key]
    # Try removing common suffixes
    for suffix in [" buffer", " (sodium salt)", " (disodium)", "-hcl", " (sodium)"]:
        if key.endswith(suffix):
            key2 = key[: -len(suffix)].strip()
            if key2 in REAGENT_MAP:
                return REAGENT_MAP[key2]
    return None


def classify_component(name):
    """Classify a reservoir component by type."""
    name_lower = name.lower()
    if any(
        b in name_lower
        for b in [
            "tris",
            "hepes",
            "mes",
            "mops",
            "citrate",
            "acetate",
            "phosphate",
            "bicine",
            "imidazole",
            "cacodylate",
            "glycine",
            "pipes",
            "bes",
            "tes",
            "ches",
        ]
    ):
        return "buffer"
    if any(s in name_lower for s in ["peg", "polyethylene glycol", "mpd", "jeffamine"]):
        return "precipitant"
    if "glycerol" in name_lower:
        return "additive"
    if any(
        s in name_lower
        for s in [
            "nacl",
            "mgcl2",
            "cacl2",
            "ammonium sulfate",
            "sodium chloride",
            "magnesium chloride",
            "calcium chloride",
            "sodium citrate",
            "sodium phosphate",
            "potassium phosphate",
        ]
    ):
        return "salt"
    return "additive"


def parse_reservoir(text):
    """Parse a reservoir string into structured components.
    Returns list of {reagent, concentration, unit, role} dicts.
    """
    components = []

    # Strip wikilinks for cleaner parsing but keep the text
    clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Also handle double-wikilink corruption
    clean = re.sub(r"\[\[([^\]]+)\]\]\([^)]+\)", r"\1", clean)

    # Split on commas, semicolons (not inside parentheses)
    parts = re.split(r"[,;](?![^(]*\))", clean)

    for part in parts:
        part = part.strip()
        if not part or part.lower() in ["not specified", "--", "none", ""]:
            continue

        # Skip LCP-specific: "lipidic mesophase", "monoolein", etc.
        if re.search(r"lipidic\s*(mesophase|phase)|cubic\s*phase", part, re.I):
            continue

        # Try to extract concentration + unit
        cm = CONC_RE.search(part)
        if not cm:
            continue

        conc_val = cm.group(1)
        unit = cm.group(2)
        rest = part[cm.end() :].strip()

        # Determine what this component is
        # Check for PEG
        peg_m = PEG_RE.search(part)
        if peg_m:
            slug = f"peg-{peg_m.group(1)}"
            if slug not in REAGENT_MAP.values():
                slug = "peg"
            components.append(
                {
                    "reagent": f"/xray-mp-wiki/reagents/additives/{slug}/",
                    "concentration": conc_val,
                    "unit": "%",
                    "role": "precipitant",
                    "note": rest[:60] if len(rest) > 60 else rest,
                }
            )
            continue

        # Extract the name from the rest (between concentration and end)
        # Remove pH from the rest for name extraction
        name_part = PH_RE.sub("", rest).strip()
        # Remove parentheses
        name_part = re.sub(r"\([^)]*\)", "", name_part).strip()
        # Take first significant word(s) as the name
        name_words = name_part.split()
        if name_words:
            # Try increasingly longer prefixes
            name_candidate = ""
            slug = None
            for w in name_words[:4]:
                w_clean = w.strip(".,;!?")
                name_candidate = (name_candidate + " " + w_clean).strip()
                slug = resolve_reagent(name_candidate)
                if slug:
                    break

            if not slug:
                slug = resolve_reagent(name_words[0].strip(".,;!?"))

            if slug:
                # Determine role
                role = classify_component(name_candidate if name_candidate else name_words[0])

                # Determine correct unit and type path
                if role == "precipitant":
                    type_path = "additives"
                elif role == "buffer":
                    type_path = "buffers"
                elif role == "salt":
                    type_path = "additives"
                else:
                    type_path = "additives"

                components.append(
                    {
                        "reagent": f"/xray-mp-wiki/reagents/{type_path}/{slug}/",
                        "concentration": conc_val,
                        "unit": "%" if unit == "%" else "M" if unit == "M" else "mM",
                        "role": role,
                    }
                )

    return components


# ─── Main processing ──────────────────────────────────────────────

stats = Counter()
total_crys = 0
parsed_reservoirs = 0
parsed_temps = 0
parsed_methods = 0

yaml_files_modified = []

for yf in sorted(BASE.glob("xray-mp-wiki/proteins_yaml/*.yaml")):
    try:
        data = std_yaml.safe_load(yf.read_text())
    except Exception:
        continue
    if not data:
        continue

    file_changed = False

    for pub in data.get("publications", []):
        for c in pub.get("crystallizations", []):
            total_crys += 1

            # Skip if already has crystallization_details
            if "crystallization_details" in c:
                continue

            details = {}
            has_content = False

            # ── Parse method ──
            method = c.get("method", "")
            if method:
                method_lower = method.lower()
                for key, lc_val in METHOD_LC_MAP.items():
                    if key in method_lower:
                        details["method_lc"] = lc_val
                        parsed_methods += 1
                        has_content = True
                        break

            # ── Parse temperature ──
            temp = c.get("temperature", "")
            if temp and temp not in ["Not specified", "--", "not specified in main text", ""]:
                tm = TEMP_RE.search(temp)
                if tm:
                    val = tm.group(1)
                    unit_raw = tm.group(2) or ""
                    if "K" in unit_raw.upper():
                        details["temperature_value"] = val
                        details["temperature_unit"] = "K"
                    else:
                        details["temperature_value"] = val
                        details["temperature_unit"] = "C"
                    parsed_temps += 1
                    has_content = True
                elif "room temperature" in temp.lower():
                    details["temperature_value"] = "20"
                    details["temperature_unit"] = "C"
                    has_content = True

            # ── Parse reservoir ──
            reservoir = c.get("reservoir", "")
            if reservoir and reservoir not in ["Not specified", "--", "not specified in main text", ""]:
                # Extract pH
                phm = PH_RE.search(reservoir)
                if phm:
                    details["ph"] = phm.group(1)

                # Parse components
                comps = parse_reservoir(reservoir)
                if comps:
                    details["reservoir_components"] = comps
                    parsed_reservoirs += 1
                    has_content = True

            # ── Check for LCP-specific fields ──
            if details.get("method_lc") == "lcp":
                lipid = c.get("lipid", "")
                if lipid and lipid not in ["Not specified", "--"]:
                    # Basic lipid name extraction
                    lipid_clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", lipid)
                    details["lipid_note"] = lipid_clean[:100]

                mr = c.get("mixing_ratio", "")
                if mr and mr not in ["Not specified", "--"]:
                    details["mixing_ratio"] = str(mr)

                plr = c.get("protein_to_lipid_ratio", "")
                if plr and plr not in ["Not specified", "--"]:
                    details["protein_to_lipid_ratio"] = str(plr)

            # ── Detect method variant ──
            if details.get("method_lc") == "vapor-diffusion":
                method_lower = method.lower()
                if "sitting" in method_lower:
                    details["method_variant"] = "sitting-drop"
                elif "hanging" in method_lower:
                    details["method_variant"] = "hanging-drop"

            if has_content:
                c["crystallization_details"] = details
                file_changed = True
                stats["crys_with_details"] += 1
            else:
                stats["crys_no_details"] += 1

    if file_changed:
        yaml_files_modified.append(yf.name)
        if not DRY_RUN:
            from ruamel.yaml import YAML

            ry = YAML()
            ry.preserve_quotes = True
            ry.indent(mapping=2, sequence=4, offset=2)
            ry.dump(data, yf)

# ─── Report ────────────────────────────────────────────────────────

print("=" * 60)
print(f"Crystallization Details — {'DRY RUN' if DRY_RUN else 'PRODUCTION RUN'}")
print("=" * 60)
print(f"Total crystallization entries: {total_crys}")
print(
    f"Entries with parsed details:  {stats.get('crys_with_details', 0)} ({100 * stats.get('crys_with_details', 0) / max(total_crys, 1):.1f}%)"
)
print(f"Entries not parsed:           {stats.get('crys_no_details', 0)}")
print(f"Reservoirs parsed:            {parsed_reservoirs}")
print(f"Temperatures parsed:          {parsed_temps}")
print(f"Methods classified:           {parsed_methods}")
print(f"YAML files modified:          {len(yaml_files_modified)}")

if DRY_RUN and yaml_files_modified:
    print("\nSample files that would be modified (first 20):")
    for fn in yaml_files_modified[:20]:
        print(f"  {fn}")

    # Show a few examples of what would be added
    print("\nSample crystallization_details output (first 3):")
    shown = 0
    for yf in sorted(BASE.glob("xray-mp-wiki/proteins_yaml/*.yaml")):
        if shown >= 3:
            break
        try:
            data = std_yaml.safe_load(yf.read_text())
        except Exception:
            continue
        for pub in data.get("publications", []):
            for c in pub.get("crystallizations", []):
                if "crystallization_details" in c and shown < 3:
                    print(f"\n  File: {yf.name}")
                    print(f"  Reservoir: {c.get('reservoir', '')[:80]}...")
                    import json

                    print(f"  Details: {json.dumps(c['crystallization_details'], indent=4)}")
                    shown += 1

    print(f"\n{'=' * 60}")
    print("DRY RUN COMPLETE. No files changed.")
    print("Run without --dry-run to apply.")
else:
    print(f"\n{'=' * 60}")
    print(f"PRODUCTION RUN COMPLETE. {len(yaml_files_modified)} files updated.")
