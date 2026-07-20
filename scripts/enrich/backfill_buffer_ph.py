#!/usr/bin/env python3
"""
Pass 2: Backfill pH into existing buffer_details from free-text `buffer` field.

The first pass (normalize_buffer_compositions.py) parsed reagent names and
concentrations but often missed pH, especially when pH was in its own
comma-separated segment (e.g. "20 mM Tris, 100 mM KCl, pH 7.6") or in
a different component than the buffer wikilink.

This pass reads the free-text `buffer` field, finds pH, and adds it to
every buffer-detail component that's a buffer reagent and has no pH yet.

Usage:
  python3 scripts/backfill_buffer_ph.py               # live
  python3 scripts/backfill_buffer_ph.py --dry-run      # preview
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent
W = BASE / "xray-mp-wiki"
DRY_RUN = "--dry-run" in sys.argv

PH_RE = re.compile(r"pH\s*([\d.]+)", re.IGNORECASE)
# Also catch (pH X.X)
PH_PAREN_RE = re.compile(r"\(pH\s*([\d.]+)\)", re.IGNORECASE)


def _extract_any_ph(text):
    """Try pH X.X anywhere in text, then (pH X.X)."""
    m = PH_RE.search(text)
    if m:
        try:
            return round(float(m.group(1)), 2)
        except ValueError:
            pass
    m = PH_PAREN_RE.search(text)
    if m:
        try:
            return round(float(m.group(1)), 2)
        except ValueError:
            pass
    return None


def main():
    changed = 0
    files_touched = []
    ph_counter = Counter()

    for yf in sorted((W / "proteins_yaml").glob("*.yaml")):
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        modified = False
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
                bd = s.get("buffer_details")
                if not bd or not isinstance(bd, list):
                    continue
                # Check if any buffer component already has pH
                already_has_ph = any(
                    isinstance(c, dict) and c.get("ph") is not None for c in bd
                )
                if already_has_ph:
                    continue
                # Try the free-text buffer field
                bt = str(s.get("buffer", "") or "").strip()
                ph = _extract_any_ph(bt)
                if ph is None:
                    # Maybe the step doesn't have a buffer field but has the
                    # context in step text or the free-text buffer_details
                    # contains a pH mention
                    raw_bt = str(s.get("buffer", "") or "")
                    ph = _extract_any_ph(raw_bt)
                if ph is not None:
                    # Assign pH to buffer-type components first, then any
                    # component if no dedicated buffer was parsed.
                    assigned = False
                    for comp in bd:
                        if not isinstance(comp, dict):
                            continue
                        r = comp.get("reagent", "")
                        if comp.get("ph") is None and "/buffers/" in r:
                            comp["ph"] = ph
                            assigned = True
                            modified = True
                    if not assigned:
                        # No buffer component found — pH is a solution property,
                        # assign to the first component regardless of type.
                        for comp in bd:
                            if isinstance(comp, dict) and comp.get("ph") is None:
                                comp["ph"] = ph
                                assigned = True
                                modified = True
                                break
                    if assigned:
                        ph_counter[ph] += 1

        if modified:
            files_touched.append(yf.stem)
            changed += 1
            if not DRY_RUN:
                raw = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
                yf.write_text(raw)

    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"{mode}: {changed} files modified")
    for ph, c in ph_counter.most_common(10):
        print(f"  pH {ph}: {c} steps")
    if DRY_RUN:
        print("\nRun without --dry-run to apply.")


if __name__ == "__main__":
    main()
