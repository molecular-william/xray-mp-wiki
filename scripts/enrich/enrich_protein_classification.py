#!/usr/bin/env python3
"""
Enrich wiki protein YAMLs with mpstruc/tcdb classification fields.

Adds:
  mpstruc_classification:
    subgroup: "..."              # from mpstrucAlphaHlxTbl
    pdb_dois:                    # from MPSTRUC_XRAY (PDB → DOI mapping)
      1ABC: "doi/10.xxxx##yyyy"
  tcdb_classification:
    tc_id: "1.A.1.1.1"          # from TCDB
    superfamily: "The ... Superfamily"

Also flags: PDBs from MPSTRUC whose canonical DOI is NOT in protein sources[].

Usage:
  DRY_RUN=1 python3 scripts/enrich_protein_classification.py   # preview only
  python3 scripts/enrich_protein_classification.py              # live run
"""

import csv
import os
from pathlib import Path

DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
YAML_DIR = PROJECT_ROOT / "xray-mp-wiki" / "proteins_yaml"


def load_datasets():
    """Load all three datasets into memory."""
    # ── MPSTRUC_XRAY: pdbCode → {doi, title, keywords} ──
    pdb_to_doi = {}  # pdbCode.upper() → doi
    doi_to_pdbs = {}  # doi.lower() → [pdbCode, ...]
    pdb_info = {}  # pdbCode.upper() → {doi, title, method}

    with open(PROJECT_ROOT / "raw" / "datasets" / "MPSTRUC_20250620_XRAY.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pdb = row["pdbCode"].strip().upper()
            doi = row.get("doi", "").strip().lower()
            if pdb and doi and doi != "-1":
                pdb_to_doi[pdb] = doi
                doi_to_pdbs.setdefault(doi, []).append(pdb)
                pdb_info[pdb] = {
                    "doi": doi,
                    "title": row.get("struct_title", "").strip(),
                    "method": row.get("method", "").strip(),
                }

    # ── mpstrucAlphaHlxTbl: pdbCode → subgroup info ──
    pdb_subgroup = {}  # pdbCode.upper() → {subgroup, name, res, species, taxdom}
    subgroup_pdbs = {}  # subgroup → [pdbCode, ...]

    with open(PROJECT_ROOT / "raw" / "datasets" / "mpstrucAlphaHlxTbl_20250620.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            group = row.get("group", "").strip()  # noqa: F841
            subgroup = row.get("subgroup", "").strip()
            # Index by BOTH main_struc and member_struc
            for col, name_col, res_col, species_col, taxdom_col in [
                ("main_struc", "main_name", "main_res", "main_species", "main_taxdom"),
                ("member_struc", "member_name", "member_res", "member_species", "member_taxdom"),
            ]:
                pdb = row.get(col, "").strip().upper()
                if pdb and subgroup:
                    entry = {
                        "subgroup": subgroup,
                        "name": row.get(name_col, "").strip(),
                        "resolution": row.get(res_col, "").strip(),
                        "species": row.get(species_col, "").strip(),
                        "tax_domain": row.get(taxdom_col, "").strip(),
                    }
                    # Keep first occurrence (main overrides member)
                    if pdb not in pdb_subgroup:
                        pdb_subgroup[pdb] = entry
                    subgroup_pdbs.setdefault(subgroup, set()).add(pdb)

    # ── TCDB: pdbCode → [{tc_id, superfamily}] ──
    pdb_tcdb = {}  # pdbCode.upper() → [{"tc_id": ..., "superfamily": ...}, ...]

    with open(PROJECT_ROOT / "raw" / "datasets" / "tcdb_20260310.tsv") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) >= 3:
                pdb = parts[0].strip().upper()
                tc_id = parts[1].strip()
                superfamily = parts[2].strip()
                if pdb and tc_id:
                    pdb_tcdb.setdefault(pdb, []).append(
                        {
                            "tc_id": tc_id,
                            "superfamily": superfamily,
                        }
                    )
                elif pdb and not tc_id:
                    pdb_tcdb.setdefault(pdb, []).append(
                        {
                            "tc_id": "?",
                            "superfamily": superfamily or "Unknown",
                        }
                    )

    return pdb_to_doi, doi_to_pdbs, pdb_info, pdb_subgroup, subgroup_pdbs, pdb_tcdb


def normalize_doi(d):
    """Normalize wiki DOI format (doi/10.xxxx##yyyy) to standard (10.xxxx/yyyy)."""
    d = d.strip()
    if d.startswith("doi/"):
        d = d[4:]
    # Replace ## with /
    d = d.replace("##", "/")
    return d.lower()


def collect_pdbs(data, doi_to_pdbs, pdb_to_doi):
    """Collect all PDB IDs for a protein from YAML structures + DOI cross-ref.

    Returns:
        (yaml_pdbs: set of PDBs from structures[].pdb_id,
         doi_pdbs: set of PDBs from DOI lookup in MPSTRUC_XRAY,
         protein_dois: list of normalized DOIs from sources[])
    """
    yaml_pdbs = set()
    doi_pdbs = set()
    protein_dois = []

    # From sources[]
    sources = data.get("sources", []) or []
    for s in sources:
        nd = normalize_doi(s)
        if nd:
            protein_dois.append(nd)
            # Look up PDBs for this DOI
            if nd in doi_to_pdbs:
                doi_pdbs.update(doi_to_pdbs[nd])

    # From structures[].pdb_id
    structs = data.get("structures", []) or []
    for s in structs:
        pid = s.get("pdb_id", "")
        if not pid or not isinstance(pid, str):
            continue
        pid = pid.strip().strip("—").strip("-").strip()
        if pid and pid != "":
            yaml_pdbs.add(pid.upper())

    return yaml_pdbs, doi_pdbs, protein_dois


def build_mpstruc_classification(all_pdbs, pdb_subgroup, pdb_to_doi, protein_dois):
    """Build mpstruc_classification dict, including pdb_dois mapping.

    Returns:
        (mpstruc_dict, warnings_list)
    """
    if not all_pdbs:
        return None, []

    subgroups = set()
    pdb_dois = {}
    warnings = []

    for pdb in sorted(all_pdbs):
        # Look up subgroup
        entry = pdb_subgroup.get(pdb)
        if entry:
            subgroups.add(entry["subgroup"])

        # Build pdb_dois from MPSTRUC_XRAY
        mpstruc_doi = pdb_to_doi.get(pdb)
        if mpstruc_doi:
            pdb_dois[pdb] = f"doi/{mpstruc_doi.replace('/', '##')}"
            # Check if this DOI is in the protein's sources
            if mpstruc_doi not in protein_dois:
                warnings.append(
                    f"PDB {pdb} canonical DOI (doi/{mpstruc_doi.replace('/', '##')}) "
                    f"from MPSTRUC not found in sources[]"
                )

    if not subgroups and not pdb_dois:
        return None, warnings

    result = {}
    if len(subgroups) == 1:
        result["subgroup"] = list(subgroups)[0]
    elif len(subgroups) > 1:
        result["subgroups"] = sorted(subgroups)

    if pdb_dois:
        result["pdb_dois"] = dict(sorted(pdb_dois.items()))

    return result, warnings


def build_tcdb_classification(all_pdbs, pdb_tcdb):
    """Build tcdb_classification dict.

    Returns None if no TCDB match found.
    """
    if not all_pdbs:
        return None

    matches = []
    seen_tc = set()

    for pdb in sorted(all_pdbs):
        entries = pdb_tcdb.get(pdb, [])
        for e in entries:
            key = e["tc_id"]
            if key not in seen_tc:
                seen_tc.add(key)
                matches.append(e)

    if not matches:
        return None

    if len(matches) == 1:
        return {"tc_id": matches[0]["tc_id"], "superfamily": matches[0]["superfamily"]}

    # Multiple TCDB entries → store as list
    return {"entries": matches}


def enrich_one(fpath, doi_to_pdbs, pdb_to_doi, pdb_info, pdb_subgroup, pdb_tcdb):
    """Enrich a single protein YAML file.

    Returns dict with enrichment stats and messages.
    """
    import yaml as yml

    fname = fpath.name
    raw = fpath.read_text()
    data = yml.safe_load(raw)
    if not isinstance(data, dict):
        return {"file": fname, "status": "skip", "reason": "not a dict"}

    yaml_pdbs, doi_pdbs, protein_dois = collect_pdbs(data, doi_to_pdbs, pdb_to_doi)
    all_pdbs = yaml_pdbs | doi_pdbs

    if not all_pdbs:
        return {"file": fname, "status": "skip", "reason": "no PDBs found"}

    warnings = []
    changes = {}

    # ── mpstruc_classification ──
    mpstruc_result, mpstruc_warnings = build_mpstruc_classification(all_pdbs, pdb_subgroup, pdb_to_doi, protein_dois)
    warnings.extend(mpstruc_warnings)

    old_mpstruc = data.pop("mpstruc_classification", None)
    if mpstruc_result:
        data["mpstruc_classification"] = mpstruc_result
        changes["mpstruc_classification"] = "added" if old_mpstruc is None else "updated"
    elif old_mpstruc is not None:
        changes["mpstruc_classification"] = "removed (no match)"

    # ── tcdb_classification ──
    old_tcdb = data.pop("tcdb_classification", None)
    tcdb_result = build_tcdb_classification(all_pdbs, pdb_tcdb)
    if tcdb_result:
        data["tcdb_classification"] = tcdb_result
        changes["tcdb_classification"] = "added" if old_tcdb is None else "updated"
    elif old_tcdb is not None:
        changes["tcdb_classification"] = "removed (no match)"

    if not changes:
        return {"file": fname, "status": "no_change"}

    # Write back
    if not DRY_RUN:
        new_yaml = yml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        fpath.write_text(new_yaml)

    # Collect PDB stats
    pdb_sources = {}
    for pdb in sorted(yaml_pdbs):
        info = pdb_info.get(pdb, {})
        pdb_sources[pdb] = {
            "source": "YAML structures[].pdb_id",
            "mpstruc_doi": info.get("doi", None),
        }
    for pdb in sorted(doi_pdbs - yaml_pdbs):
        info = pdb_info.get(pdb, {})
        pdb_sources[pdb] = {
            "source": "DOI cross-ref (MPSTRUC_XRAY)",
            "mpstruc_doi": info.get("doi", None),
        }

    return {
        "file": fname,
        "status": "enriched",
        "changes": changes,
        "yaml_pdbs": len(yaml_pdbs),
        "doi_pdbs": len(doi_pdbs - yaml_pdbs),
        "total_pdbs": len(all_pdbs),
        "subgroup": mpstruc_result.get("subgroup") or mpstruc_result.get("subgroups", [None])[0]
        if mpstruc_result
        else None,
        "tcdb": bool(tcdb_result),
        "warnings": warnings,
    }


def main():
    print(f"Mode: {'DRY RUN' if DRY_RUN else 'LIVE'}")
    print(f"Protein YAMLs: {len(list(YAML_DIR.glob('*.yaml')))}")
    print()

    # Load datasets
    print("Loading datasets...")
    pdb_to_doi, doi_to_pdbs, pdb_info, pdb_subgroup, subgroup_pdbs, pdb_tcdb = load_datasets()
    print(f"  MPSTRUC_XRAY: {len(pdb_to_doi)} PDBs, {len(doi_to_pdbs)} unique DOIs")
    print(f"  AlphaHlxTbl:  {len(pdb_subgroup)} PDBs with subgroup, {len(subgroup_pdbs)} subgroups")
    print(f"  TCDB:         {len(pdb_tcdb)} PDBs with classification")
    print()

    # Enrich all protein YAMLs
    results = []
    all_warnings = []
    for fpath in sorted(YAML_DIR.glob("*.yaml")):
        r = enrich_one(fpath, doi_to_pdbs, pdb_to_doi, pdb_info, pdb_subgroup, pdb_tcdb)
        results.append(r)
        if r.get("warnings"):
            all_warnings.extend(r["warnings"])

    # Stats
    enriched = [r for r in results if r["status"] == "enriched"]
    no_change = [r for r in results if r["status"] == "no_change"]
    skipped = [r for r in results if r["status"] == "skip"]

    print(f"{'=' * 60}")
    print("RESULTS:")
    print(f"  Enriched:  {len(enriched)}")
    print(f"  No change: {len(no_change)} (no dataset match)")
    print(f"  Skipped:   {len(skipped)} (no PDBs in YAML)")
    print()

    # mpstruc stats
    with_mpstruc = sum(1 for r in enriched if r.get("subgroup"))
    with_tcdb = sum(1 for r in enriched if r.get("tcdb"))
    print(f"  With mpstruc subgroup: {with_mpstruc}")
    print(f"  With TCDB classification: {with_tcdb}")
    print()

    # PDB source breakdown
    yaml_only_pdbs = sum(r["yaml_pdbs"] for r in enriched)
    doi_only_pdbs = sum(r.get("doi_pdbs", 0) for r in enriched)
    print(f"  PDBs from YAML structures[].pdb_id: {yaml_only_pdbs}")
    print(f"  PDBs from DOI cross-ref only:       {doi_only_pdbs}")
    print()

    # Warnings
    if all_warnings:
        print(f"{'=' * 60}")
        print(f"WARNINGS ({len(all_warnings)}):")
        print()
        # Deduplicate warnings
        seen_warnings = set()
        for w in all_warnings:
            if w not in seen_warnings:
                seen_warnings.add(w)
                print(f"  ⚠ {w}")
        print()

    # Changes breakdown
    add_mpstruc = sum(1 for r in enriched if r.get("changes", {}).get("mpstruc_classification") == "added")
    upd_mpstruc = sum(1 for r in enriched if r.get("changes", {}).get("mpstruc_classification") == "updated")
    rem_mpstruc = sum(1 for r in enriched if r.get("changes", {}).get("mpstruc_classification") == "removed")
    add_tcdb = sum(1 for r in enriched if r.get("changes", {}).get("tcdb_classification") == "added")
    upd_tcdb = sum(1 for r in enriched if r.get("changes", {}).get("tcdb_classification") == "updated")
    rem_tcdb = sum(1 for r in enriched if r.get("changes", {}).get("tcdb_classification") == "removed")
    print(f"mpstruc_classification: {add_mpstruc} added, {upd_mpstruc} updated, {rem_mpstruc} removed")
    print(f"tcdb_classification:    {add_tcdb} added, {upd_tcdb} updated, {rem_tcdb} removed")
    print()

    if DRY_RUN:
        print("DRY RUN complete. No files written.")
    else:
        print("LIVE run complete. All YAMLs written.")
        print()
        print("Next steps recommended:")
        print("  1. Validate enriched YAMLs: python3 scripts/validate_yaml.py protein <name> --strict")
        print("  2. Regenerate pages: python3 scripts/generate_page.py protein <name> --yes")
        print("  3. Rebuild index: python3 scripts/rebuild_indexes.py --force")


if __name__ == "__main__":
    main()
