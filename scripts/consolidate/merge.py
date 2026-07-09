#!/usr/bin/env python3
"""
Merge — find and merge duplicate entities in the wiki.

Consolidates: find_duplicate_*.py, find_merge_candidates.py,
             merge_duplicate_*.py, batch_merge_proteins.py

Usage:
  python3 scripts/consolidate/merge.py --find --type proteins     # find duplicate candidates
  python3 scripts/consolidate/merge.py --find --all               # find across all types
  python3 scripts/consolidate/merge.py --execute proteins         # merge interactively
  python3 scripts/consolidate/merge.py --batch proteins           # execute pre-approved batch
  python3 scripts/consolidate/merge.py --dry-run                  # preview all merges
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
ARCHIVE = SCRIPTS / "archive"


def _run(script_name, *args):
    """Run an archived script, forwarding args."""
    sp = ARCHIVE / script_name
    if not sp.exists():
        print(f"Error: archived script not found: {sp}")
        sys.exit(1)
    cmd = [sys.executable, str(sp)] + list(args)
    return subprocess.run(cmd).returncode


def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(0)

    if args[0] == "--find":
        target = args[1] if len(args) > 1 else "proteins"
        if target == "--all":
            for t in ["proteins", "reagents", "concepts", "methods"]:
                _run(f"find_duplicate_{t}.py")
        else:
            _run(f"find_duplicate_{target}.py")

    elif args[0] == "--execute":
        target = args[1] if len(args) > 1 else "proteins"
        _run(f"merge_duplicate_{target}.py")

    elif args[0] == "--batch":
        _run("batch_merge_proteins.py")

    elif args[0] == "--candidates":
        _run("find_merge_candidates.py")

    elif args[0] == "--dry-run":
        _run("find_merge_candidates.py", "--dry-run")

    else:
        print(f"Unknown command: {args[0]}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
