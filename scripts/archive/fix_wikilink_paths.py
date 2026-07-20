#!/usr/bin/env python3
"""
Batch fixer for stale wiki link paths.

Reads path rewrite rules from path_fixes.json and applies them across
all .md and .yaml files in the wiki. Run after any migration that
changes entity locations.

Optimized: single combined regex pass per file instead of N patterns × N files.

Usage:
  python3 scripts/fix_wikilink_paths.py             # live
  python3 scripts/fix_wikilink_paths.py --dry-run   # preview only
"""

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
WIKI = BASE / "xray-mp-wiki"
FIXES_FILE = BASE / "scripts" / "path_fixes.json"

DRY_RUN = "--dry-run" in sys.argv


def _build_combined_pattern(fixes):
    """
    Build ONE compiled regex that matches any old path.

    Keys sorted longest-first so 'reagents/proteases/tev-protease' is tried
    before 'reagents/enzymes/tev-protease' — no partial prefix overlap.
    The callback looks up the matched key in the dict for the replacement.
    """
    # Sort by length descending so longer paths match before shorter prefixes
    items = sorted(fixes.items(), key=lambda x: -len(x[0]))

    parts = []
    lookup = {}
    for old, new in items:
        label = f"P{len(parts)}"
        lookup[label] = (old, new)
        parts.append(f"(?P<{label}>{re.escape(old)})")

    pattern = rf"(?<=/xray-mp-wiki/)(?:{'|'.join(parts)})(?=[/\s)\\]|$)"

    def _replacer(m):
        """Callback: look up which alternation group matched, return new path."""
        for label, (old, new) in lookup.items():
            if m.group(label) is not None:
                return new
        return m.group(0)  # fallback — should never fire

    return re.compile(pattern), _replacer


def _iter_wiki_files():
    """Yield paths to .md and .yaml files, skipping __pycache__."""
    for ext in ("*.md", "*.yaml"):
        for fp in sorted(WIKI.rglob(ext)):
            if "__pycache__" in str(fp):
                continue
            yield fp


def main():
    fixes = json.loads(FIXES_FILE.read_text())
    pattern, replacer = _build_combined_pattern(fixes)

    total_fixes = 0
    affected_files = 0

    for fp in _iter_wiki_files():
        # Quick pre-filter: skip files that can't possibly contain a wiki link
        # We read a small chunk first to check for the anchor string
        try:
            first_block = fp.read_bytes()[:4096]
        except OSError:
            continue

        if b"/xray-mp-wiki/" not in first_block:
            # Might still have a link deeper in the file — check file size
            # For files under 4K, if no anchor found, skip
            if fp.stat().st_size < 4096:
                continue

        text = fp.read_text()
        new_text, count = pattern.subn(replacer, text)

        if count:
            total_fixes += count
            affected_files += 1
            if DRY_RUN:
                print(f"  WOULD FIX ({count:>3}): {fp.relative_to(WIKI)}")
            else:
                fp.write_text(new_text)

    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"\n{mode}: {total_fixes} fixes across {affected_files} files")

    if DRY_RUN:
        print("Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
