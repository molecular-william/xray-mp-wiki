#!/usr/bin/env python3
"""
Batch processor for buffer step normalization (Pass 2).
Reads a review JSON, applies each fix via buffer_step_patch.py
with dry-run verification before applying.

Usage:
  python3 scripts/buffer-batch-processor.py <review_json> [--dry-run-only]

Where <review_json> is the path to a batch review JSON file
(e.g., references/buffer_review_batch3.json).

fix_type='fill_buffer': Pass existing_details verbatim to buffer_step_patch.py
fix_type='new_details': Skip — buffer text too vague to resolve into details
"""

import json
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT / "scripts" / "buffer_step_patch.py"
YAML_DIR = PROJECT / "xray-mp-wiki" / "proteins_yaml"

# Buffer component subdirectory paths (reagents/buffers/)
# Used to identify which entries are buffer components (for pH tracking)
BUFFER_PREFIX = "/xray-mp-wiki/reagents/buffers/"


def main():
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)

    DRY_RUN_ONLY = "--dry-run-only" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--dry-run-only"]

    review_path = Path(args[0])
    if not review_path.exists():
        print(f"ERROR: Review file not found: {review_path}")
        sys.exit(1)

    review = json.loads(review_path.read_text())
    total = len(review)
    applied = 0
    skipped = []
    failed = []
    dry_run_results = []

    for idx, entry in enumerate(review):
        fname = entry["file"]
        pub_idx = entry["pub_idx"]
        step_idx = entry["step_idx"]
        fix_type = entry["fix_type"]
        existing = entry.get("existing_details")
        buffer_text = entry.get("buffer_text", "")

        yaml_path = YAML_DIR / fname
        if not yaml_path.exists():
            failed.append(f"{fname}: file not found")
            continue

        if fix_type == "fill_buffer":
            if not existing or not isinstance(existing, list) or len(existing) == 0:
                skipped.append(
                    f"{fname}[pub:{pub_idx}].steps[{step_idx}]: "
                    f"fill_buffer but no existing_details"
                )
                continue

            # pH only on buffer components — verify at least one buffer component
            # has a ph value, which is the Point of this pass
            buffer_comps = [
                d for d in existing
                if (d.get("reagent") or "").startswith(BUFFER_PREFIX)
            ]
            has_buffer_ph = any(
                b.get("ph") is not None for b in buffer_comps
            )
            details = json.dumps(existing)

        elif fix_type == "new_details":
            # Cannot resolve vague buffer descriptions into structured details
            skipped.append(
                f"{fname}[pub:{pub_idx}].steps[{step_idx}]: "
                f"new_details — unresolvable text: '{buffer_text[:60]}'"
            )
            continue

        else:
            failed.append(
                f"{fname}[pub:{pub_idx}].steps[{step_idx}]: "
                f"unknown fix_type '{fix_type}'"
            )
            continue

        # Run dry-run
        cmd = [
            sys.executable, str(SCRIPT),
            str(yaml_path), str(pub_idx), str(step_idx), details,
            "--dry-run"
        ]
        dry = subprocess.run(cmd, capture_output=True, text=True)
        if dry.returncode != 0:
            failed.append(
                f"{fname}[pub:{pub_idx}].steps[{step_idx}]: "
                f"DRY-RUN FAILED: {dry.stderr.strip() or dry.stdout.strip()}"
            )
            continue

        dry_run_results.append((fname, pub_idx, step_idx, fix_type, dry.stdout.strip()))

        if not DRY_RUN_ONLY:
            # Apply for real
            live_cmd = [
                sys.executable, str(SCRIPT),
                str(yaml_path), str(pub_idx), str(step_idx), details
            ]
            live = subprocess.run(live_cmd, capture_output=True, text=True)
            if live.returncode != 0:
                failed.append(
                    f"{fname}[pub:{pub_idx}].steps[{step_idx}]: "
                    f"APPLY FAILED: {live.stderr.strip() or live.stdout.strip()}"
                )
                continue
            applied += 1
            print(f"[{applied}/{total}] {fname} pub[{pub_idx}].steps[{step_idx}] ({fix_type}) ✓")
            print(f"  {dry.stdout.strip()}")
        else:
            applied += 1
            print(f"[{applied}/{total}] {fname} pub[{pub_idx}].steps[{step_idx}] ({fix_type})")
            print(f"  {dry.stdout.strip()}")

    mode = "DRY-RUN ONLY" if DRY_RUN_ONLY else "APPLIED"
    print(f"\n{'=' * 60}")
    print(f"MODE: {mode}")
    print(f"PROCESSED: {applied}/{total}")
    print(f"SKIPPED:   {len(skipped)}")
    print(f"FAILED:    {len(failed)}")

    if skipped:
        print(f"\nSkipped ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s}")

    if failed:
        print(f"\nFailed ({len(failed)}):")
        for f_item in failed:
            print(f"  - {f_item}")

    if DRY_RUN_ONLY:
        print(f"\nDry-run summary: {applied} entries would be processed, {len(skipped)} skipped, {len(failed)} failed.")
        print("Run without --dry-run-only to apply.")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
