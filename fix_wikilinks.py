#!/usr/bin/env python3
"""
Fix broken wikilink paths in xray-mp-wiki rendered .md files.

Applies path mappings: wrong_path -> correct_path throughout all .md files.
"""

import os
import re
import sys

# Path to the wiki content directory
WIKI_DIR = "/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki"

# Path mappings: (wrong_path, correct_path)
# These are URL-style paths that appear in wikilinks within .md files
MAPPINGS = [
    # Concepts - pages exist at different subdirectory
    ("/xray-mp-wiki/concepts/construct-design/n-terminal-t4-lysozyme-fusion/",
     "/xray-mp-wiki/concepts/signaling-receptors/n-terminal-t4-lysozyme-fusion/"),
    ("/xray-mp-wiki/concepts/enzyme-mechanisms/bcs1-folded-protein-translocation/",
     "/xray-mp-wiki/concepts/transport-mechanisms/bcs1-folded-protein-translocation/"),
    ("/xray-mp-wiki/concepts/miscellaneous/antibiotic-efflux-pump/",
     "/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/"),
    ("/xray-mp-wiki/concepts/miscellaneous/binding-change-mechanism/",
     "/xray-mp-wiki/concepts/enzyme-mechanisms/binding-change-mechanism/"),
    ("/xray-mp-wiki/concepts/miscellaneous/disulfide-bond-formation/",
     "/xray-mp-wiki/concepts/enzyme-mechanisms/disulfide-bond-formation/"),
    ("/xray-mp-wiki/concepts/miscellaneous/lipid-annulus/",
     "/xray-mp-wiki/concepts/membrane-mimetics/lipid-annulus/"),
    ("/xray-mp-wiki/concepts/miscellaneous/selective-lipid-binding/",
     "/xray-mp-wiki/concepts/membrane-mimetics/selective-lipid-binding/"),
    ("/xray-mp-wiki/concepts/miscellaneous/tetraspanin-family/",
     "/xray-mp-wiki/concepts/protein-families/tetraspanin-family/"),
    ("/xray-mp-wiki/concepts/rhodopsin-mechanisms/proton-release-channel-archaeal-rhodopsins/",
     "/xray-mp-wiki/concepts/transport-mechanisms/proton-release-channel-archaeal-rhodopsins/"),
    ("/xray-mp-wiki/concepts/signaling-receptors/allosteric-regulation/",
     "/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/"),
    ("/xray-mp-wiki/concepts/signaling-receptors/dry-motif/",
     "/xray-mp-wiki/concepts/structural-mechanisms/dry-motif/"),
    ("/xray-mp-wiki/concepts/signaling-receptors/gpcr-ionic-lock/",
     "/xray-mp-wiki/concepts/structural-mechanisms/gpcr-ionic-lock/"),
    ("/xray-mp-wiki/concepts/signaling-receptors/npxxy-motif/",
     "/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/"),
    ("/xray-mp-wiki/concepts/structural-mechanisms/electrostatic-gating-sodium-pump/",
     "/xray-mp-wiki/concepts/transport-mechanisms/electrostatic-gating-sodium-pump/"),
    ("/xray-mp-wiki/concepts/structural-mechanisms/outer-membrane/",
     "/xray-mp-wiki/concepts/membrane-mimetics/outer-membrane/"),
    ("/xray-mp-wiki/concepts/structural-mechanisms/selectivity-filter/",
     "/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/"),
    ("/xray-mp-wiki/concepts/structural-mechanisms/yidc-oxa1-alb3-insertase-family/",
     "/xray-mp-wiki/concepts/protein-families/yidc-oxa1-alb3-insertase-family/"),
    # ("/xray-mp-wiki/concepts/transport-mechanisms/proton-coupled-transport/",
    #  "/xray-mp-wiki/concepts/transport-mechanisms/proton-exit-channel/"),

    # Proteins
    ("/xray-mp-wiki/proteins/enzymes/aquifex-aeolicus-ftsh/",
     "/xray-mp-wiki/proteins/aquifex-aeolicus-ftsh/"),
    ("/xray-mp-wiki/proteins/enzymes/dtpa/",
     "/xray-mp-wiki/proteins/slc-transporters/dtpa/"),
    ("/xray-mp-wiki/proteins/gpcrs/beta2-adrenergic-receptor/",
     "/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/"),
    ("/xray-mp-wiki/proteins/gpcr/5-ht2a-receptor/",
     "/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/"),
    ("/xray-mp-wiki/proteins/gpcr/5-ht2b-receptor/",
     "/xray-mp-wiki/proteins/gpcr/5ht2b-receptor/"),
    ("/xray-mp-wiki/proteins/gpcr/adenosine-a1-receptor/",
     "/xray-mp-wiki/proteins/gpcr/human-adenosine-a1-receptor-a1ar/"),
    ("/xray-mp-wiki/proteins/pumps-atpases/gastric-h-k-atpase/",
     "/xray-mp-wiki/proteins/pumps-atpases/gastric-hk-atpase/"),

    # Reagents
    ("/xray-mp-wiki/reagents/additives/sds/",
     "/xray-mp-wiki/reagents/detergents/sds/"),
    ("/xray-mp-wiki/reagents/enzymes/factor-xa/",
     "/xray-mp-wiki/reagents/additives/factor-xa/"),
    ("/xray-mp-wiki/reagents/enzymes/tevp-protease/",
     "/xray-mp-wiki/reagents/additives/tevp-protease/"),
    ("/xray-mp-wiki/reagents/peptides/gp67-signal-peptide/",
     "/xray-mp-wiki/reagents/additives/gp67-signal-peptide/"),
    ("/xray-mp-wiki/reagents/vectors/pfastbac1/",
     "/xray-mp-wiki/reagents/additives/pfastbac1/"),
    ("/xray-mp-wiki/reagents/ligands/am251/",
     "/xray-mp-wiki/reagents/additives/am251/"),
    ("/xray-mp-wiki/reagents/ligands/biil284/",
     "/xray-mp-wiki/reagents/additives/biil284/"),
]


def get_all_md_files(root_dir):
    """Walk the directory tree and collect all .md files."""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip .git directories
        dirnames[:] = [d for d in dirnames if d != '.git']
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files


def fix_wikilinks_in_file(filepath, mappings):
    """Fix all wikilink path mappings in a single .md file. Returns (changed, changes_count)."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content
    total_replacements = 0

    for wrong_path, correct_path in mappings:
        # Escape regex special chars in the path for safe matching
        escaped_wrong = re.escape(wrong_path)
        count = len(re.findall(escaped_wrong, content))
        if count > 0:
            content = content.replace(wrong_path, correct_path)
            total_replacements += count

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, total_replacements
    return False, 0


def main():
    md_files = get_all_md_files(WIKI_DIR)
    print(f"Found {len(md_files)} .md files to scan")

    # Collect per-mapping stats first
    for wrong_path, correct_path in MAPPINGS:
        total_occurrences = 0
        affected_files = set()
        for filepath in md_files:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            # Count occurrences without trailing slash too (some href links might omit it)
            wrong_path_no_slash = wrong_path.rstrip('/')
            matches = content.count(wrong_path) + content.count(wrong_path_no_slash) - content.count(wrong_path)
            if matches > 0:
                total_occurrences += matches
                affected_files.add(filepath)
        if total_occurrences > 0:
            print(f"  {wrong_path} -> {correct_path}")
            print(f"    → {total_occurrences} occurrences across {len(affected_files)} files")

    # Apply fixes
    print("\n--- Applying fixes ---")
    total_modified = 0
    total_fixes = 0
    mapping_stats = {wrong: 0 for wrong, _ in MAPPINGS}

    for filepath in md_files:
        changed, changes_count = fix_wikilinks_in_file(filepath, MAPPINGS)
        if changed:
            total_modified += 1
            total_fixes += changes_count
            relpath = os.path.relpath(filepath, WIKI_DIR)
            print(f"  Modified: {relpath} ({changes_count} fixes)")

    print(f"\n=== Summary ===")
    print(f"Files scanned: {len(md_files)}")
    print(f"Files modified: {total_modified}")
    print(f"Total wikilink fixes applied: {total_fixes}")

    # Verify no remaining wrong paths
    remaining = 0
    for wrong_path, correct_path in MAPPINGS:
        for filepath in md_files:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            if wrong_path in content:
                remaining += 1
                print(f"  WARNING: '{wrong_path}' still present in {os.path.relpath(filepath, WIKI_DIR)}")

    if remaining == 0:
        print("✓ All mappings applied cleanly - no remaining wrong paths.")
    else:
        print(f"⚠ {remaining} unresolved occurrences remain (may need manual review).")

    return 0 if remaining == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
