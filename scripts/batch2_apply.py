#!/usr/bin/env python3
"""
Batch 2 buffer normalization processor.
Applies Pass 2 buffer normalization to buffer_review_batch2.json (79 files, 134 steps).

Usage:
  python3 scripts/batch2_apply.py --dry-run   # Preview all changes
  python3 scripts/batch2_apply.py             # Apply all changes
  python3 scripts/batch2_apply.py --summary   # Summary counts only

pH is only set on buffer components (/reagents/buffers/).
pH values are written as strings to pass strict YAML validation.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REVIEW_FILE = Path(__file__).resolve().parent.parent / 'references' / 'buffer_review_batch2.json'
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATCH_SCRIPT = PROJECT_ROOT / 'scripts' / 'buffer_step_patch.py'
PROTEINS_DIR = PROJECT_ROOT / 'xray-mp-wiki' / 'proteins_yaml'

# pH extraction regex
PH_RE = re.compile(r'pH\s*([\d.]+)', re.IGNORECASE)

def extract_ph_from_text(buffer_text):
    """Extract pH value from buffer text. Returns first pH found or None."""
    m = PH_RE.search(buffer_text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None

def build_details(entry):
    """
    Build the details array for a review entry.
    - For fill_buffer: use existing_details, extract pH from buffer_text for buffer components
    - For new_details: return None (no details to apply)
    
    pH is ONLY applied to buffer components (/reagents/buffers/).
    pH values are written as strings to pass YAML validation.
    """
    fix_type = entry['fix_type']
    existing = entry.get('existing_details')
    buffer_text = entry.get('buffer_text', '')

    if fix_type == 'new_details' and existing is None:
        return None

    if existing is None:
        return None

    # Extract pH from buffer text
    ph_from_text = extract_ph_from_text(buffer_text)

    # Build the details array
    details = []
    for d in existing:
        entry = {
            'reagent': d['reagent'],
            'concentration': d.get('concentration'),
            'unit': d.get('unit'),
        }

        is_buffer = '/buffers/' in d['reagent']

        if is_buffer:
            # Apply pH if present in existing_details or extracted from buffer_text
            ph = d.get('ph')
            if ph is None and ph_from_text is not None:
                ph = ph_from_text
            # Write pH as string to pass YAML validation (must be quoted)
            if ph is not None:
                entry['ph'] = str(ph)
        # Non-buffer components get no ph field

        details.append(entry)

    return details

def main():
    dry_run = '--dry-run' in sys.argv
    summary_only = '--summary' in sys.argv

    with open(REVIEW_FILE) as f:
        reviews = json.load(f)

    # Stats
    by_type = {}
    for r in reviews:
        by_type.setdefault(r['fix_type'], 0)
        by_type[r['fix_type']] += 1

    print(f"Batch 2: {len(reviews)} steps across {len(set(r['file'] for r in reviews))} files")
    for t, c in sorted(by_type.items()):
        print(f"  {t}: {c}")

    if summary_only:
        return

    ok_count = 0
    error_count = 0
    skip_count = 0
    files_modified = set()

    for i, r in enumerate(reviews):
        file_name = r['file']
        pub_idx = r['pub_idx']
        step_idx = r['step_idx']
        fix_type = r['fix_type']

        yaml_path = PROTEINS_DIR / file_name
        if not yaml_path.exists():
            print(f"  [{i+1}] SKIP: {file_name} not found")
            skip_count += 1
            continue

        # Build the details to apply
        details = build_details(r)
        if details is None:
            print(f"  [{i+1}] SKIP: {file_name} pub[{pub_idx}].steps[{step_idx}] ({fix_type}) — no details to apply")
            skip_count += 1
            continue

        details_json = json.dumps(details)

        # Call buffer_step_patch.py
        cmd = [sys.executable, str(PATCH_SCRIPT)]
        if dry_run:
            cmd.append('--dry-run')
        cmd.extend([str(yaml_path), str(pub_idx), str(step_idx), details_json])

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        out = result.stdout.strip()
        err = result.stderr.strip()
        label = "[DRY-RUN]" if dry_run else "[APPLY]"

        if result.returncode == 0:
            print(f"  {label} [{i+1}] {out}")
            ok_count += 1
            if not dry_run:
                files_modified.add(file_name)
        else:
            if 'Step not found' in err or 'Step not found' in out:
                print(f"  {label} [{i+1}] SKIP (step not found): {file_name} pub[{pub_idx}].steps[{step_idx}]")
                skip_count += 1
            else:
                print(f"  {label} [{i+1}] ERROR: {file_name} pub[{pub_idx}].steps[{step_idx}]: {err or out}")
                error_count += 1

    print(f"\n{'='*60}")
    mode = "DRY-RUN" if dry_run else "APPLY"
    print(f"{mode} complete: {ok_count} OK, {error_count} errors, {skip_count} skipped")
    print(f"Files touched: {len(files_modified)}")

if __name__ == '__main__':
    main()
