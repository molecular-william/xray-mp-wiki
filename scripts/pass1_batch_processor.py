#!/usr/bin/env python3
"""
Process Pass 2 batch 1 detergent normalization entries.
Reads the review JSON and applies each fix via detergent_step_patch.py,
verifying with --dry-run before applying.

For fill_conc with concentrations already present → apply
For new_details with resolvable names → parse and create
All others → skip
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

PROJECT = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
REVIEW_FILE = PROJECT / "references" / "detergent_review_batch1.json"
SCRIPT = PROJECT / "scripts" / "detergent_step_patch.py"
YAML_DIR = PROJECT / "xray-mp-wiki" / "proteins_yaml"
REAGENT_DIR = PROJECT / "xray-mp-wiki" / "reagents_yaml"

# ── Build detergent name map ──
DETERGENT_NAME_MAP = {}
DETERGENT_SLUGS = set()
for yf in sorted(REAGENT_DIR.glob("*.yaml")):
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
        m = re.search(r"\(([^)]+)\)", title)
        if m:
            abbr = m.group(1).strip().lower()
            if abbr and abbr != slug and abbr not in DETERGENT_SLUGS:
                DETERGENT_NAME_MAP[abbr] = slug
        DETERGENT_NAME_MAP[slug.lower()] = slug
    except Exception:
        continue

# Manual name→slug additions for common names/aliases not covered by YAML titles
ADDITIONAL = {
    "dodecylmaltoside": "ddm",
    "lauryl maltose neopentyl glycol": "lmng",
    "chaps": "chapso",
    "triton": "triton-x-100",
    "triton x-100": "triton-x-100",
    "triton-x": "triton-x-100",
    "nonylglucoside": "ng",
    "n-nonyl-beta-d-glucoside": "ng",
    "n-nonyl-β-d-glucoside": "ng",
    "beta-dodecyl maltoside": "ddm",
    "beta-dodecyl-maltoside": "ddm",
    "beta-decylmaltoside": "dm",
    "decylmaltoside": "dm",
    "decyl-beta-d-maltoside": "dm",
    "n-decyl-beta-d-maltoside": "dm",
    "n-decyl-β-d-maltoside": "dm",
    "octylglucoside": "og",
    "n-octyl-beta-d-glucopyranoside": "og",
    "n-octyl-β-d-glucopyranoside": "og",
    "beta-octyl-d-glucopyranoside": "og",
    "n-octyl-beta-d-thioglucoside": "otg",
    "octylthioglucoside": "otg",
    "n-dodecyl-n,n-(dimethylammonio)butyrate": "ddmab",
    "ddmab": "ddmab",
    "lmn": "lmng",
    "lmng": "lmng",
    "mng-3": "mng-3-c8",
    "mng": "lmng",
    "sucrose monododecanoate": "sucrose-monododecanoate",
    "monododecanoate": "sucrose-monododecanoate",
    "c12e8": "c12e8",
    "c12e6": "octaethylene-glycol-mono-n-dodecylether",
    "beta-ng": "ng",
    "cholate": "sodium-cholate",
    "cholesterol hemisuccinate": "cholesterol-hydrogen-succinate",
    "chs": "cholesterol-hydrogen-succinate",
}
DETERGENT_NAME_MAP.update(ADDITIONAL)

# ── Regexes ──
LINK_EXTRACT = re.compile(r"\[([^\]]+)\]\([^)]+/reagents/detergents/([^/)]+)/?\)")
CONC_RE = re.compile(
    r"([\d.]+)\s*"
    r"((?:%\s*\(w/v\)|%(?!\w)|"
    r"mg\s*/\s*ml|mg\s*ml|mg/ml|"
    r"µg\s*/\s*ml|µg/ml|"
    r"μg\s*/\s*ml|μg/ml|"
    r"ng\s*/\s*μl|ng/μl|"
    r"mM|µM|μM|M)(?=\s|$|\)|,|/|;|\+|\|))",
    re.IGNORECASE,
)

def slug_from_text(text_fragment):
    """Resolve a text fragment to a detergent slug."""
    clean = text_fragment.lower().strip()
    if clean in DETERGENT_NAME_MAP:
        return DETERGENT_NAME_MAP[clean]
    stripped = re.sub(r"^[\d.,\s%µμmM/()w/v+\-]+", "", clean).strip()
    if stripped and stripped in DETERGENT_NAME_MAP:
        return DETERGENT_NAME_MAP[stripped]
    words = set(w for w in re.findall(r"[a-z0-9-]+", stripped if stripped else clean) if len(w) >= 3)
    for word in words:
        if word in DETERGENT_NAME_MAP:
            return DETERGENT_NAME_MAP[word]
    # Fuzzy: word-boundary substring match
    best_match, best_count = None, 0
    for word in words:
        for name, nslug in DETERGENT_NAME_MAP.items():
            if re.search(r"\b" + re.escape(word) + r"\b", name):
                n_matches = sum(1 for w in words if re.search(r"\b" + re.escape(w) + r"\b", name))
                if n_matches > best_count:
                    best_count = n_matches
                    best_match = nslug
    if best_match and best_count >= 2:
        return best_match
    return None

def extract_conc_from_text(text):
    cm = CONC_RE.search(text)
    if cm:
        conc_val = cm.group(1)
        conc_unit = cm.group(2).strip()
        if conc_unit:
            conc_unit = re.sub(r"\s+", "", conc_unit)
            if re.match(r"%\(v/v\)$", conc_unit) or re.match(r"%\(w/v\)$", conc_unit) or conc_unit.startswith("%"):
                conc_unit = "%"
        return conc_val, conc_unit
    return None, None

def is_empty_text(txt):
    """Check if text is effectively empty (no useful content)."""
    t = txt.strip()
    if not t:
        return True
    if t in ("—", "-", "--", "n/a", "none", "not specified", "not applicable",
             "see supplementary", "see supplementary materials", "see supplementary information",
             "as above", ","):
        return True
    return False

def parse_detergent_for_entry(det_text):
    """Parse detergent text into list of detail dicts with proper reagent paths."""
    if is_empty_text(det_text):
        return []

    results = []
    seen_slugs = set()

    # First pass: extract from wikilinks
    for m in LINK_EXTRACT.finditer(det_text):
        slug = m.group(2).lower().strip()
        if slug not in DETERGENT_SLUGS:
            continue
        ctx = det_text[max(0, m.start() - 40):m.end() + 20]
        conc_val, conc_unit = extract_conc_from_text(ctx)
        if slug not in seen_slugs:
            results.append({
                "reagent": f"/xray-mp-wiki/reagents/detergents/{slug}/",
                "concentration": str(conc_val) if conc_val is not None else None,
                "unit": conc_unit
            })
            seen_slugs.add(slug)

    # Second pass: split plain text on separators and resolve each part
    text_plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", det_text)
    text_plain = re.sub(r"\s*\((?:w/v|v/v|w/w)\)\s*", " ", text_plain, flags=re.IGNORECASE)
    parts = re.split(r"\s*(?:[,/;]|\s+and\s+|\s*\+\s*|\s+with\s+|\s+in\s+)\s*", text_plain, flags=re.IGNORECASE)

    for part in parts:
        part = part.strip()
        if not part or part in ("—", "-", "--"):
            continue
        slug = slug_from_text(part)
        if slug and slug not in seen_slugs:
            conc_val, conc_unit = extract_conc_from_text(part)
            results.append({
                "reagent": f"/xray-mp-wiki/reagents/detergents/{slug}/",
                "concentration": str(conc_val) if conc_val is not None else None,
                "unit": conc_unit
            })
            seen_slugs.add(slug)

    return results

def main():
    review = json.loads(REVIEW_FILE.read_text())
    total = len(review)
    ok = 0
    failed = []
    skipped = []

    for idx, entry in enumerate(review):
        filename = entry["file"]
        pub_idx = entry["pub_idx"]
        step_idx = entry["step_idx"]
        fix_type = entry["fix_type"]
        existing = entry.get("existing_details")
        det_text = entry.get("detergent_text", "")

        yaml_path = YAML_DIR / filename
        if not yaml_path.exists():
            failed.append(f"{filename}: file not found")
            continue

        # Determine what to pass
        if fix_type == "fill_conc":
            # Use existing_details (may have concentrations filled from review)
            if existing is not None:
                details_json = json.dumps(existing)
            else:
                details_json = "[]"

            # Only apply if there's actually a non-null concentration to set
            has_conc = False
            if isinstance(existing, list):
                has_conc = any(
                    d.get("concentration") is not None and str(d.get("concentration", "")).strip()
                    for d in existing
                )
            if not has_conc:
                skipped.append(f"{filename}[{pub_idx}].steps[{step_idx}]: no concentration data in review")
                continue

        elif fix_type == "new_details":
            # Parse detergent_text to create proper details
            parsed = parse_detergent_for_entry(det_text)
            if not parsed:
                skipped.append(f"{filename}[{pub_idx}].steps[{step_idx}]: could not resolve detergent from text")
                continue
            details_json = json.dumps(parsed)
        else:
            failed.append(f"{filename}[{pub_idx}].steps[{step_idx}]: unknown fix_type {fix_type}")
            continue

        # Build command
        cmd = [
            sys.executable, str(SCRIPT),
            str(yaml_path), str(pub_idx), str(step_idx),
            details_json
        ]

        # Step 1: Dry run
        dry_cmd = cmd + ["--dry-run"]
        result = subprocess.run(dry_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            failed.append(f"{filename}[{pub_idx}].steps[{step_idx}]: DRY-RUN ERROR: {result.stderr.strip() or result.stdout.strip()}")
            continue

        dry_output = result.stdout.strip()

        # Step 2: Apply for real (no --dry-run)
        real_cmd = cmd
        result2 = subprocess.run(real_cmd, capture_output=True, text=True)
        if result2.returncode != 0:
            failed.append(f"{filename}[{pub_idx}].steps[{step_idx}]: APPLY ERROR: {result2.stderr.strip() or result2.stdout.strip()}")
            continue

        ok += 1
        print(f"[{ok}/{total}] {filename} pub[{pub_idx}].steps[{step_idx}] ({fix_type}) ✓")
        print(f"  DRY: {dry_output}")

    # Summary
    print(f"\n{'='*60}")
    print(f"APPLIED:  {ok}/{total}")
    print(f"SKIPPED:  {len(skipped)}")
    print(f"FAILURES: {len(failed)}")
    if skipped:
        print("\nSkipped entries:")
        for s in skipped:
            print(f"  - {s}")
    if failed:
        print("\nFailures:")
        for f in failed:
            print(f"  - {f}")
    return 0 if not failed else 1

if __name__ == "__main__":
    sys.exit(main())
