#!/usr/bin/env python3
"""Run check_pdb.py for all PDB/DOI pairs and report results."""
import subprocess, sys
from pathlib import Path

BASE = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
CHECK_SCRIPT = BASE / "scripts/check_pdb.py"

# All unique (PDB, DOI) pairs from the 21 files
pairs = {
    "acetylcholine-binding-protein": [("1UV6", "10.1038/nature07461"), ("3EHZ", "10.1038/nature07461")],
    "af-tmem16": [("4L3A", "10.1038/nature12535"), ("4WIS", "10.1038/nature13984")],
    "arabidopsis-nitrate-transporter-nrt1-1": [("4CL4", "10.1038/nature13116"), ("4CL5", "10.1038/nature13116"), ("5A2N", "10.1038/nature13116")],
    "betp": [("2WIT", "10.1038/nature07819"), ("3HFX", "10.1038/nsmb.1788"), ("4C7R", "10.1038/emboj.2013.226"), ("4DOJ", "10.1038/nature11403"), ("3JEO", "10.1038/nature07819"), ("4AIN", "10.1038/nature11403"), ("4AMR", "10.1038/nature11403")],
    "bpe-fluoride-channel": [("5A40", "10.1038/nature14981"), ("5A41", "10.1038/nature14981"), ("6BQO", "10.1016/j.str.2018.02.004")],
    "claudin-19-mouse": [("3X29", "10.1126/science.1261833")],
    "clbm": [("4Z3N", "10.1038/nmicrobiol.2015.9"), ("4Z3P", "10.1038/nmicrobiol.2015.9")],
    "clostridium-boltrea-mray": [("5JNQ", "10.1038/nchembio.2270")],
    "clpp": [("2CLP", "10.1016/j.jmb.2006.05.063"), ("3BF0", "10.1016/j.jmb.2007.11.080")],
    "cmclc": [("3ORG", "10.1126/science.1195230"), ("4FG6", "10.1073/pnas.1205764109")],
    "cp-tric": [("5WUC", "10.1038/ncomms15103"), ("5WUF", "10.1038/ncomms15103")],
    "cysz": [("3TX3", "10.7554/eLife.27829"), ("6D79", "10.7554/eLife.27829"), ("6D9Z", "10.7554/eLife.27829")],
    "cytochrome-b561": [("4O6Y", "10.1073/pnas.1323931111")],
    "cytochrome-b5-reductase": [("6WF2", "10.1016/j.jmb.2020.05.017"), ("1UMK", "10.1016/j.jmb.2020.05.017")],
    "cytochrome-b5": [("4YMK", "10.1038/nature14549"), ("6WF2", "10.1016/j.jmb.2020.05.017"), ("2I96", "10.1016/j.jmb.2020.05.017")],
    "d4-dopamine-receptor": [("5WIU", "10.1126/science.aan5468"), ("5WIV", "10.1126/science.aan5468")],
    "dgot": [("6E9N", "10.1371/journal.pbio.3000260"), ("6E9O", "10.1371/journal.pbio.3000260")],
    "fluc-ec2": [("5A40", "10.1038/nature14981"), ("5KBN", "10.7554/eLife.18767"), ("6B24", "10.7554/eLife.31259"), ("7KKR", "10.7554/eLife.69482"),
                  ("5A43", "10.7554/eLife.31259"), ("6B2A", "10.7554/eLife.31259"), ("6B2B", "10.7554/eLife.31259"), ("6B2D", "10.7554/eLife.31259"),
                  ("7KKA", "10.7554/eLife.69482"), ("7KKB", "10.7554/eLife.69482"), ("7KK8", "10.7554/eLife.69482"), ("7KK9", "10.7554/eLife.69482"),
                  ("5kom", "10.7554/eLife.18767")],
    "glt-ph": [("1XFH", "10.1038/nature03018"), ("2NWL", "10.1038/nature05455"), ("3KBC", "10.1038/nature08616"), ("3V8F", "10.1038/nsmb.2233"),
               ("4IZM", "10.1038/nsmb.2548"), ("4P19", "10.7554/eLife.02283"), ("4X2S", "10.1038/nature14158"), ("5DWY", "10.1038/ncomms13420"),
               ("6V8G", "10.15252/embj.2020105415"), ("6X01", "10.1038/s41586-021-03240-9"), ("7AHK", "10.1126/sciadv.aba9854")],
    "human-claudin-4": [("3X29", "10.1126/science.1261833"), ("7KP4", "10.1073/pnas.2024651118")],
    "human-claudin-9": [("3X29", "10.1126/science.1261833"), ("6OV2", "10.1073/pnas.1908929116")],
}

all_pass = True
for protein, pdb_list in sorted(pairs.items()):
    for pdb, doi in pdb_list:
        result = subprocess.run(
            ["python3", str(CHECK_SCRIPT), pdb, doi],
            capture_output=True, text=True, cwd=str(BASE)
        )
        status = "NOT_FOUND" if result.returncode != 0 else result.stdout.strip()
        ok = "FOUND" in status
        if not ok:
            all_pass = False
        print(f"[{'OK' if ok else 'FAIL'}] {protein}: {pdb} / {doi} → {status}")
        if not ok:
            print(f"  stderr: {result.stderr.strip()[:200]}")

print(f"\nOverall: {'ALL PASS' if all_pass else 'SOME FAILURES'}")
