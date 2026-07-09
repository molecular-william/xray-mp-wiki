#!/usr/bin/env python3
"""
Restructure protein YAMLs from flat-section to DOI-grouped format.

Groups structures[], purifications[], crystallizations[] under publications[] keyed by DOI.
Adds PDBTM sequence + topology data where PDB IDs match.
Keeps shared fields (overview, tags, expression, etc.) at top level.
Uses CommentedMap to serialize as clean YAML (no !!omap tag).

Usage:
  python3 scripts/restructure_proteins.py          # live run
  python3 scripts/restructure_proteins.py --dry-run # preview only
"""

import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

DRY_RUN = "--dry-run" in sys.argv
W = Path(__file__).resolve().parent.parent / "xray-mp-wiki"


# ─── Helpers ──────────────────────────────────────────────────────────────────
def cmap(**kwargs):
    """Shortcut: CommentedMap from keyword args."""
    m = CommentedMap()
    for k, v in kwargs.items():
        m[k] = v
    return m


def cmap_items(items):
    """CommentedMap from list of (key, value) tuples — preserves order."""
    m = CommentedMap()
    for k, v in items:
        m[k] = v
    return m


# ─── PDBTM parser ─────────────────────────────────────────────────────────────
def parse_pdbtm():
    xml_path = W.parent / "raw/datasets/pdbtm_alpha_2025.xml"
    if not xml_path.exists():
        print(f"  [WARN] PDBTM file not found: {xml_path}")
        return {}

    ns = {"pdbtm": "https://pdbtm.unitmp.org"}
    result = {}

    for event, elem in ET.iterparse(xml_path, events=("end",)):
        if elem.tag != f"{{{ns['pdbtm']}}}pdbtm":
            continue
        pdb_id = elem.get("ID", "").lower()
        if not pdb_id:
            elem.clear()
            continue

        chains = {}
        for chain_elem in elem.findall(".//pdbtm:CHAIN", ns):
            chain_id = chain_elem.get("CHAINID", "")
            num_tm = int(chain_elem.get("NUM_TM", 0))
            tm_type = chain_elem.get("TYPE", "")

            seq_elem = chain_elem.find("pdbtm:SEQ", ns)
            seq = ""
            if seq_elem is not None and seq_elem.text:
                seq = "".join(seq_elem.text.split())

            regions = []
            for reg in chain_elem.findall("pdbtm:REGION", ns):
                regions.append(
                    cmap(
                        seq_beg=str(reg.get("seq_beg", 0)),
                        seq_end=str(reg.get("seq_end", 0)),
                        pdb_beg=str(reg.get("pdb_beg", 0)),
                        pdb_end=str(reg.get("pdb_end", 0)),
                        type=reg.get("type", ""),
                    )
                )

            chains[chain_id] = cmap(
                tmd=num_tm,
                type=tm_type,
                residues=seq,
                regions=CommentedSeq(regions),
            )

        if chains:
            result[pdb_id] = chains
        elem.clear()

    print(f"  PDBTM: {len(result)} entries loaded")
    return result


# ─── Restructure ───────────────────────────────────────────────────────────────
REGION_TYPE_MAP = {"H": "Membrane", "1": "Inside", "2": "Outside", "U": "Unknown"}


def build_publications(data, pdbtm_lookup):
    """Group flat structures/purifications/crystallizations by DOI source."""
    doi_order = []

    def track(d):
        if d and d not in doi_order:
            doi_order.append(d)

    structs = data.get("structures", []) or []
    struct_by_doi = defaultdict(list)
    for s in structs:
        if isinstance(s, dict):
            src = s.get("source", "") or "unpublished"
            track(src)
            struct_by_doi[src].append(s)

    purifs = data.get("purifications", []) or []
    purif_by_doi = defaultdict(list)
    for p in purifs:
        if isinstance(p, dict):
            src = p.get("source", "") or "unpublished"
            track(src)
            purif_by_doi[src].append(p)

    xtals = data.get("crystallizations", []) or []
    xtal_by_doi = defaultdict(list)
    for c in xtals:
        if isinstance(c, dict):
            src = c.get("source", "") or "unpublished"
            track(src)
            xtal_by_doi[src].append(c)

    publications = CommentedSeq()
    for doi in doi_order:
        entry = CommentedMap()
        entry["source"] = doi

        # Structures
        src_structs = struct_by_doi.get(doi, [])
        if src_structs:
            clean = CommentedSeq()
            for s in src_structs:
                cs = CommentedMap()
                for k, v in s.items():
                    if k != "source":
                        cs[k] = v
                clean.append(cs)
            entry["structures"] = clean

        # Purifications
        src_purifs = purif_by_doi.get(doi, [])
        if src_purifs:
            clean = CommentedSeq()
            for p in src_purifs:
                cp = CommentedMap()
                for k, v in p.items():
                    if k != "source":
                        cp[k] = v
                clean.append(cp)
            entry["purifications"] = clean

        # Crystallizations
        src_xtals = xtal_by_doi.get(doi, [])
        if src_xtals:
            clean = CommentedSeq()
            for c in src_xtals:
                cc = CommentedMap()
                for k, v in c.items():
                    if k != "source":
                        cc[k] = v
                clean.append(cc)
            entry["crystallizations"] = clean

        # PDBTM sequences
        seqs = CommentedSeq()
        for s in src_structs:
            pdb_raw = s.get("pdb_id", "")
            if not isinstance(pdb_raw, str):
                continue
            pdb_id = pdb_raw.lower()
            if len(pdb_id) != 4 or not pdb_id.isalnum():
                continue
            if pdb_id in pdbtm_lookup:
                for chain_id, chain_data in pdbtm_lookup[pdb_id].items():
                    if not chain_data.get("residues"):
                        continue
                    seq_entry = CommentedMap()
                    seq_entry["source"] = "pdbtm"
                    seq_entry["pdb_id"] = pdb_id
                    seq_entry["chain"] = chain_id
                    seq_entry["tmd"] = str(chain_data["tmd"])
                    seq_entry["type"] = chain_data["type"]
                    seq_entry["residues"] = chain_data["residues"]

                    regions = CommentedSeq()
                    for r in chain_data["regions"]:
                        regions.append(
                            cmap_items(
                                [
                                    ("begin", r["seq_beg"]),
                                    ("end", r["seq_end"]),
                                    ("pdb_begin", r["pdb_beg"]),
                                    ("pdb_end", r["pdb_end"]),
                                    ("location", REGION_TYPE_MAP.get(r["type"], "Unknown")),
                                ]
                            )
                        )
                    if regions:
                        seq_entry["topology"] = regions
                    seqs.append(seq_entry)

        if seqs:
            entry["sequences"] = seqs
        publications.append(entry)

    return publications


def restructure_one(yf, pdbtm_lookup):
    """Return (CommentedMap, stats_dict) or (None, {'error': ...})."""
    try:
        data = YAML().load(yf.read_text())
    except Exception as e:
        return None, {"error": str(e)[:80]}
    if not isinstance(data, dict):
        return None, {"error": "not a dict"}

    new = CommentedMap()

    # Shared fields (preserve order)
    for k in [
        "title",
        "created",
        "updated",
        "tags",
        "type",
        "layout",
        "category",
        "mpstruc_classification",
        "tcdb_classification",
        "organism",
        "residues",
    ]:
        v = data.get(k)
        if v is not None:
            new[k] = v

    # Sources list
    all_dois = []
    seen = set()
    for sec in ["structures", "purifications", "crystallizations"]:
        for item in data.get(sec, []) or []:
            if isinstance(item, dict):
                src = item.get("source", "")
                if src and src not in seen:
                    seen.add(src)
                    all_dois.append(src)
    if all_dois:
        new["sources"] = CommentedSeq(all_dois)

    # Expression (single dict, no source — stays top-level)
    expr = data.get("expression")
    if isinstance(expr, dict):
        ne = CommentedMap()
        for k, v in expr.items():
            ne[k] = v
        new["expression"] = ne

    # Overview & biological_insights
    for k in ["overview", "biological_insights"]:
        v = data.get(k)
        if v is not None:
            new[k] = v

    # Cross-references
    cr = data.get("cross_references")
    if cr:
        new["cross_references"] = cr

    # Verified
    if "verified" in data:
        new["verified"] = data["verified"]

    # DOI-grouped publications
    pubs = build_publications(data, pdbtm_lookup)
    if pubs:
        new["publications"] = pubs

    # Catch-all for any remaining fields
    known = {
        "title",
        "created",
        "updated",
        "tags",
        "type",
        "layout",
        "category",
        "mpstruc_classification",
        "tcdb_classification",
        "organism",
        "residues",
        "sources",
        "expression",
        "overview",
        "biological_insights",
        "cross_references",
        "verified",
        "publications",
        "structures",
        "purifications",
        "crystallizations",
    }
    for k, v in data.items():
        if k not in known and v is not None:
            new[k] = v

    # Stats
    old_structs = sum(1 for pub in pubs for _ in pub.get("structures", []))
    n_purif = sum(1 for pub in pubs for _ in pub.get("purifications", []))
    n_xtal = sum(1 for pub in pubs for _ in pub.get("crystallizations", []))
    n_seq = sum(1 for pub in pubs for _ in pub.get("sequences", []))

    return new, {
        "dois": len(pubs),
        "structs": old_structs,
        "purifs": n_purif,
        "xtals": n_xtal,
        "seqs": n_seq,
    }


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("Loading PDBTM data...")
    pdbtm_lookup = parse_pdbtm()
    print(f"Processing proteins (dry_run={DRY_RUN})...\n")

    yamls = sorted((W / "proteins_yaml").rglob("*.yaml"))
    yaml_out = YAML()
    yaml_out.preserve_quotes = True
    yaml_out.indent(mapping=2, sequence=4, offset=2)
    yaml_out.width = 120

    total = 0
    modified = 0
    errors = []
    sums = defaultdict(int)

    for yf in yamls:
        total += 1
        new_data, stats = restructure_one(yf, pdbtm_lookup)

        if "error" in stats:
            errors.append((yf.stem, stats["error"]))
            continue

        if DRY_RUN and stats["dois"] > 0:
            modified += 1
            parts = []
            if stats["structs"]:
                parts.append(f"{stats['structs']}s")
            if stats["purifs"]:
                parts.append(f"{stats['purifs']}p")
            if stats["xtals"]:
                parts.append(f"{stats['xtals']}x")
            if stats["seqs"]:
                parts.append(f"{stats['seqs']}seq")
            print(f"  {yf.stem:40s} {stats['dois']} DOIs  ({', '.join(parts)})")
        elif not DRY_RUN:
            if stats["dois"] > 0 or True:  # write even if nothing changed (format unification)
                new_data["updated"] = "2026-06-29"
                yaml_out.dump(new_data, yf.open("w"))
                modified += 1

        for k in sums:
            sums[k] += stats.get(k, 0)

    print(f"\nTotal: {total} proteins")
    print(f"Modified: {modified}")
    if errors:
        print(f"Skipped (errors): {len(errors)}")
        for name, err in errors[:5]:
            print(f"  {name}: {err}")
    if not DRY_RUN:
        print(f"\n  Publications: {sums['dois']}")
        print(f"  Structures: {sums['structs']}")
        print(f"  Purifications: {sums['purifs']}")
        print(f"  Crystallizations: {sums['xtals']}")
        print(f"  PDBTM sequences: {sums['seqs']}")


if __name__ == "__main__":
    main()
