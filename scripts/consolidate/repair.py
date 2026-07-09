#!/usr/bin/env python3
"""
Repair — fix common YAML structural issues.

Consolidates: repair_broken_yamls.py, clean_sources.py, fix_pdb_format.py,
             fill_stale_pdbs.py, check_yaml_wikilinks.py, fix_doubled_paths.py

Usage:
  python3 scripts/consolidate/repair.py --broken-yamls       # fix unparseable YAMLs
  python3 scripts/consolidate/repair.py --clean-sources      # remove dicts from sources
  python3 scripts/consolidate/repair.py --fix-pdbs           # extract PDB codes from strings
  python3 scripts/consolidate/repair.py --fill-pdbs          # fill empty PDBs from MPSTRUC
  python3 scripts/consolidate/repair.py --check-wikilinks    # scan broken wikilinks in YAMLs
  python3 scripts/consolidate/repair.py --fix-doubled-paths  # fix duplicated path segments
  python3 scripts/consolidate/repair.py --all                # run all repairs
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
ARCHIVE = SCRIPTS / "archive"

MAP = {
    "--broken-yamls": "repair_broken_yamls.py",
    "--clean-sources": "clean_sources.py",
    "--fix-pdbs": "fix_pdb_format.py",
    "--fill-pdbs": "fill_stale_pdbs.py",
    "--check-wikilinks": "check_yaml_wikilinks.py",
    "--fix-doubled-paths": "fix_doubled_paths.py",
}


def _run(script_name):
    sp = ARCHIVE / script_name
    if not sp.exists():
        print(f"Error: archived script not found: {sp}")
        return 1
    return subprocess.run([sys.executable, str(sp)]).returncode


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    if args[0] == "--all":
        for _, script in sorted(MAP.items()):
            print(f"\n=== {script} ===")
            _run(script)
    elif args[0] in MAP:
        _run(MAP[args[0]])
    else:
        print(f"Unknown command: {args[0]}")
        print("Available: " + ", ".join(MAP.keys()))
        sys.exit(1)


if __name__ == "__main__":
    main()
