#!/usr/bin/env python3
"""
Verify — run source-truth verification checks on wiki data.

Consolidates: check_protein_identity_in_paper.py, check_protein_pdb_in_paper.py,
             check_alias_matches.py, validate_protein_data.py

Usage:
  python3 scripts/consolidate/verify.py --pdb-in-paper <protein>   # check PDBs against raw papers
  python3 scripts/consolidate/verify.py --identity <protein>        # check protein identity
  python3 scripts/consolidate/verify.py --alias-matches             # find broken-link→page matches
  python3 scripts/consolidate/verify.py --all-proteins              # comprehensive protein data check
  python3 scripts/consolidate/verify.py --all                       # run all checks
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
ARCHIVE = SCRIPTS / "archive"


def _run(script, *args):
    sp = ARCHIVE / script
    if not sp.exists():
        print(f"Error: archived script not found: {sp}")
        return 1
    cmd = [sys.executable, str(sp)] + list(args)
    return subprocess.run(cmd).returncode


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    if args[0] == "--pdb-in-paper" and len(args) >= 2:
        _run("check_protein_pdb_in_paper.py", *args[1:])
    elif args[0] == "--identity" and len(args) >= 2:
        _run("check_protein_identity_in_paper.py", *args[1:])
    elif args[0] == "--alias-matches":
        _run("check_alias_matches.py")
    elif args[0] == "--all-proteins":
        _run("validate_protein_data.py")
    elif args[0] == "--all":
        print("=== check_alias_matches ===")
        _run("check_alias_matches.py")
        print("\n=== validate_protein_data ===")
        _run("validate_protein_data.py")
    else:
        print(f"Unknown: {args[0]}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
