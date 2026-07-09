#!/usr/bin/env python3
"""
Batch 1 buffer normalization runner.
Processes buffer_review_batch1.json entries using buffer_step_patch.py.
Dry-run first, then live apply.
pH only on buffer components (reagents/buffers/*).
"""
import json
import subprocess
import sys
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "buffer_step_patch.py"
REVIEW = ROOT / "references" / "buffer_review_batch1.json"
YAML_DIR = ROOT / "xray-mp-wiki" / "proteins_yaml"

review = json.loads(REVIEW.read_text())

print(f"Loaded {len(review)} entries from review file")
print(f"Mode: {'DRY-RUN' if DRY_RUN else 'LIVE'}")
print("pH only on buffer components\n")

# Collect entries by file
entries_by_file = {}
for entry in review:
    fname = entry["file"]
    if fname not in entries_by_file:
        entries_by_file[fname] = []
    entries_by_file[fname].append(entry)

print(f"Unique files: {len(entries_by_file)}")

# Verify files exist
missing = []
for fname in entries_by_file:
    yaml_path = YAML_DIR / fname
    if not yaml_path.exists():
        missing.append(fname)

if missing:
    print(f"\nWARNING: {len(missing)} files not found in {YAML_DIR}:")
    for m in missing:
        print(f"  MISSING: {m}")

ok_missing = set(missing)
existing_entries = [e for e in review if e["file"] not in ok_missing]
print(f"\nProcessing {len(existing_entries)} entries across {len(entries_by_file) - len(missing)} existing files\n")

success = 0
fail = 0
skipped = 0

for entry in existing_entries:
    fname = entry["file"]
    yaml_path = YAML_DIR / fname
    pub_idx = entry["pub_idx"]
    step_idx = entry["step_idx"]
    fix_type = entry["fix_type"]

    # Build details array: pH only on buffer components
    details_raw = entry.get("existing_details") or []
    details = []
    for det in details_raw:
        reagent = det["reagent"]
        conc = det.get("concentration")
        unit = det.get("unit")
        ph = det.get("ph")

        # pH only on buffer components (/reagents/buffers/)
        is_buffer = "/reagents/buffers/" in reagent

        detail_entry = {"reagent": reagent}
        if conc is not None:
            detail_entry["concentration"] = str(conc)
        if unit is not None:
            detail_entry["unit"] = unit
        if ph is not None and is_buffer:
            detail_entry["ph"] = ph
        details.append(detail_entry)

    details_json = json.dumps(details)

    cmd = ["python3", str(SCRIPT)]
    if DRY_RUN:
        cmd.append("--dry-run")
    cmd.extend([str(yaml_path), str(pub_idx), str(step_idx), details_json])

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)

    if result.returncode == 0:
        print(result.stdout.strip())
        success += 1
    else:
        print(f"FAIL {fname} pub[{pub_idx}].steps[{step_idx}]: {result.stderr.strip()}")
        fail += 1

print(f"\n{'='*60}")
print(f"Results: {success} OK, {fail} FAIL, {skipped} SKIPPED")
if DRY_RUN:
    print("To apply: run without --dry-run")
