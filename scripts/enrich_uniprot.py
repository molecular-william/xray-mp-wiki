#!/usr/bin/env python3
"""Enrich protein YAMLs with uniprot_id via RCSB PDB GraphQL API.

Uses PDBTM chain IDs (from publications[].sequences[].chain) to directly
look up the Uniprot accession of the membrane protein's polymer entity.
Falls back to majority-vote across all PDBs for proteins without PDBTM data.

Method:
  Primary (chain-based):
    1. Collect (PDB, chain) pairs from PDBTM sequences in YAML
    2. For each pair, find the polymer entity whose auth_asym_ids contains
       the chain → extract its uniprot_ids
    3. Fusion entities (multiple uniprots) → filter known fusion partners
    4. Verify consistency across all chain pairs for a protein

  Fallback (majority-vote):
    For proteins without PDBTM chain data, vote across all PDBs.
    Selects the Uniprot appearing in the most PDBs, rejecting fusion
    partners and using organism heuristic for ties.

Usage:
  python3 scripts/enrich_uniprot.py               # run (default dry-run)
  python3 scripts/enrich_uniprot.py --no-dry-run   # actually write
  python3 scripts/enrich_uniprot.py --limit 50     # test first 50
  python3 scripts/enrich_uniprot.py --cache-only   # use cached data only
  python3 scripts/enrich_uniprot.py --skip-existing
"""

import argparse
import json
import re
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests
import yaml

# ─── Project paths ────────────────────────────────────────────────
BASE = Path(__file__).parent.parent
PROTEINS_DIR = BASE / "xray-mp-wiki" / "proteins_yaml"
CACHE_PATH = BASE / "references" / "uniprot_cache.json"
AUDIT_PATH = BASE / "references" / "enrich_uniprot_report.json"

# ─── Known fusion partners ────────────────────────────────────────
FUSION_PARTNERS = {
    "P00720",  # T4 Lysozyme (T4L)
    "P0A2X6",  # BRIL (apocytochrome b562 RIL)
    "P0ABE7",  # BRIL variant / E. coli cytochrome b562
    "P00722",  # Beta-galactosidase
    "P0AEX9",  # MBP (E. coli)
    "P63214",  # SUMO (Smt3)
    "P0CD61",  # GST
    "P63017",  # Ubiquitin
    "P0AET7",  # Protein G B1 domain
    "P01574",  # Protein A (Staphylococcus)
}

# ─── GraphQL query ────────────────────────────────────────────────
QUERY_TEMPLATE = """\
{{
  entries(entry_ids: [{ids}]) {{
    polymer_entities {{
      rcsb_polymer_entity_container_identifiers {{
        uniprot_ids
        entry_id
        entity_id
        auth_asym_ids
      }}
      rcsb_entity_source_organism {{
        scientific_name
      }}
      entity_poly {{
        rcsb_entity_polymer_type
      }}
    }}
  }}
}}
"""

# ─── Uniprot accession validator ──────────────────────────────────
UNIPROT_RE = re.compile(
    r"^[OPQ][0-9][A-Z0-9]{3}[0-9]|"
    r"[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}$"
)


def is_valid_uniprot(acc):
    return bool(UNIPROT_RE.match(acc)) if acc else False


def filter_fusion(uniprots):
    """Remove known fusion partners from a list, return remaining."""
    return [u for u in uniprots if u not in FUSION_PARTNERS]


# ═══════════════════════════════════════════════════════════════════
#  Phase 1a: Data collection from YAML files
# ═══════════════════════════════════════════════════════════════════


def collect_chain_pairs():
    """Scan all protein YAMLs for PDBTM chain data.

    Returns:
        chain_proteins: {protein_name: [(pdb, chain), ...]}
        vote_fallback_proteins: {protein_name: [pdb_ids]}  (for vote fallback)
        all_pdbs: sorted list of all unique PDB IDs
    """
    chain_proteins = {}
    vote_fallback_proteins = {}
    all_pdbs = set()

    for yf in sorted(PROTEINS_DIR.glob("*.yaml")):
        name = yf.stem
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue

        chains = []
        struct_pdbs = set()

        for pub in data.get("publications") or []:
            if not isinstance(pub, dict):
                continue
            # Collect PDBTM chain pairs
            for seq in pub.get("sequences", []):
                pdb = (seq.get("pdb_id") or "").strip().upper()
                chain = (seq.get("chain") or "").strip()
                if pdb and chain and re.match(r"^[0-9][A-Z0-9]{3}$", pdb):
                    chains.append((pdb, chain))
                    all_pdbs.add(pdb)
            # Collect all structure PDBs for fallback
            for struct in pub.get("structures", []):
                if not isinstance(struct, dict):
                    continue
                pdb = (struct.get("pdb_id") or "").strip().upper()
                if re.match(r"^[0-9][A-Z0-9]{3}$", pdb):
                    struct_pdbs.add(pdb)
                    all_pdbs.add(pdb)

        if chains:
            chain_proteins[name] = chains
        # Always store structure PDBs for vote fallback
        if struct_pdbs:
            vote_fallback_proteins[name] = sorted(struct_pdbs)

    return chain_proteins, vote_fallback_proteins, sorted(all_pdbs)


# ═══════════════════════════════════════════════════════════════════
#  Phase 1b: GraphQL batch resolver
# ═══════════════════════════════════════════════════════════════════


class GraphQLResolver:
    """Resolve PDB → {entity → {uniprots, auth_asym_ids}} via RCSB PDB GraphQL."""

    ENDPOINT = "https://data.rcsb.org/graphql"
    BATCH_SIZE = 400
    REQUEST_DELAY = 0.5

    def __init__(self, cache_only=False):
        self.cache_only = cache_only
        self._cache = self._load_cache()

    def _load_cache(self):
        if CACHE_PATH.exists():
            return json.loads(CACHE_PATH.read_text())
        return {}

    def _save_cache(self):
        CACHE_PATH.write_text(json.dumps(self._cache, indent=2))
        print(f"  Cache saved: {len(self._cache)} PDBs")

    def resolve(self, pdb_ids):
        """Return {pdb_id: {entity_id: {uniprots, organisms, auth_asym_ids}}}."""
        uncached = [p for p in pdb_ids if p not in self._cache]
        if uncached:
            print(f"  Uncached PDBs: {len(uncached)} / {len(pdb_ids)}")
            if self.cache_only:
                print("  --cache-only set, skipping API calls")
            else:
                self._fetch_batches(uncached)
                self._save_cache()
        else:
            print(f"  All {len(pdb_ids)} PDBs in cache")

        result = {}
        for pdb in pdb_ids:
            cached = self._cache.get(pdb)
            if cached:
                result[pdb] = cached
        return result

    def _fetch_batches(self, pdb_ids):
        for i in range(0, len(pdb_ids), self.BATCH_SIZE):
            batch = pdb_ids[i : i + self.BATCH_SIZE]
            print(f"  Querying batch {i // self.BATCH_SIZE + 1}: {len(batch)} PDBs...")
            ids_str = ", ".join(f'"{p}"' for p in batch)
            query = QUERY_TEMPLATE.format(ids=ids_str)

            try:
                resp = requests.post(self.ENDPOINT, json={"query": query}, timeout=60)
                resp.raise_for_status()
                data = resp.json()
                errors = data.get("errors", [])
                if errors:
                    print(f"    WARNING: {len(errors)} GraphQL errors:")
                    for e in errors[:3]:
                        print(f"      {e.get('message', '')[:120]}")
                self._process_entries(data.get("data", {}).get("entries", []))
            except requests.exceptions.RequestException as exc:
                print(f"    ERROR: {exc}")

            if i + self.BATCH_SIZE < len(pdb_ids):
                time.sleep(self.REQUEST_DELAY)

    def _process_entries(self, entries):
        """Parse GraphQL response entries into cache."""
        for entry in entries:
            pdb_id = None
            entities_data = {}

            for pe in entry.get("polymer_entities") or []:
                cid = pe.get("rcsb_polymer_entity_container_identifiers") or {}
                if not pdb_id:
                    pdb_id = (cid.get("entry_id") or "").upper()
                entity_id = cid.get("entity_id") or "?"

                uniprots = cid.get("uniprot_ids")
                valid = [u for u in (uniprots or []) if is_valid_uniprot(u)]

                auth_asym_ids = cid.get("auth_asym_ids") or []

                organisms = []
                for org in pe.get("rcsb_entity_source_organism") or []:
                    name = org.get("scientific_name") or ""
                    if name:
                        organisms.append(name)

                if valid or auth_asym_ids:
                    entities_data[entity_id] = {
                        "uniprots": valid,
                        "organisms": list(set(organisms)),
                        "auth_asym_ids": auth_asym_ids,
                    }

            if pdb_id:
                self._cache[pdb_id] = entities_data


# ═══════════════════════════════════════════════════════════════════
#  Phase 1c: Uniprot selectors
# ═══════════════════════════════════════════════════════════════════


def select_by_chain(chain_pairs, pdb_data):
    """Resolve Uniprot using PDBTM chain → entity mapping.

    For each (PDB, chain) pair:
      1. Find the entity whose auth_asym_ids contains the chain
      2. Extract uniprot_ids from that entity
      3. If fusion (multiple uniprots), filter known partners

    Returns: (uniprot_ids_list, confidence, debug_dict) or (None, reason, debug)
    """
    candidates = set()
    per_pair = {}  # (pdb, chain) → uniprots found

    for pdb, chain in chain_pairs:
        entities = pdb_data.get(pdb.upper(), {})
        matched = []

        for eid, info in entities.items():
            auth_chains = [c.upper() for c in info.get("auth_asym_ids", [])]
            if chain.upper() in auth_chains:
                unis = info.get("uniprots", [])
                if unis:
                    filtered = filter_fusion(unis)
                    matched = filtered if filtered else unis
                break

        per_pair[(pdb.upper(), chain.upper())] = matched
        for u in matched:
            candidates.add(u)

    if not candidates:
        return None, "chain_no_mapping", {"chain_pairs": chain_pairs, "per_pair": per_pair}

    # Single candidate — clean
    if len(candidates) == 1:
        return (
            [candidates.pop()],
            "high",
            {"chain_pairs": chain_pairs, "per_pair": per_pair, "n_pairs": len(chain_pairs)},
        )

    # Multiple candidates: are they from different entities (complex) or same (fusion)?
    unique_sets = set()
    for pair_key, matched in per_pair.items():
        if matched and len(matched) == 1:
            unique_sets.add(tuple(matched))

    # Different chain pairs → different single Uniprots → legitimate complex
    if len(unique_sets) > 1:
        flat = sorted(set(sum([list(s) for s in unique_sets], [])))
        return (
            flat,
            "multi_high",
            {
                "chain_pairs": chain_pairs,
                "per_pair": per_pair,
                "n_candidates": len(flat),
            },
        )

    # Same entity fusion — majority vote then organism heuristic
    candidate_counts = Counter()
    for pdb, chain in chain_pairs:
        for u in per_pair.get((pdb.upper(), chain.upper()), []):
            candidate_counts[u] += 1

    ranked = candidate_counts.most_common()
    if ranked[0][1] > ranked[1][1]:
        return (
            [ranked[0][0]],
            "high",
            {"chain_pairs": chain_pairs, "per_pair": per_pair, "candidate_counts": dict(candidate_counts)},
        )

    # Organism heuristic
    pdb_data_for_org = {p: v for p, v in pdb_data.items() if p in {x[0] for x in chain_pairs}}
    organism_scores = defaultdict(int)
    for pdb, chain in chain_pairs:
        for eid, info in pdb_data_for_org.get(pdb.upper(), {}).items():
            auth_chains = [c.upper() for c in info.get("auth_asym_ids", [])]
            if chain.upper() in auth_chains:
                for u in info.get("uniprots", []):
                    if u in candidate_counts:
                        for org in info.get("organisms", []):
                            ol = org.lower()
                            if "homo sapiens" in ol:
                                organism_scores[(u, "human")] += 1
                            elif "enterobacteria phage" in ol or "synthetic" in ol:
                                organism_scores[(u, "phage")] += 1
                            elif "escherichia coli" in ol:
                                organism_scores[(u, "ecoli")] += 1
                            else:
                                organism_scores[(u, "other")] += 1
    org_priority = {"human": 4, "other": 3, "ecoli": 2, "phage": 1}
    scores = {}
    for u in candidate_counts:
        s = 0
        for (uni, ot), c in organism_scores.items():
            if uni == u:
                s += org_priority.get(ot, 2) * c
        scores[u] = s
    if len(scores) >= 2 and max(scores.values()) != min(scores.values()):
        winner = max(scores, key=scores.get)
        return (
            [winner],
            "medium",
            {
                "chain_pairs": chain_pairs,
                "per_pair": per_pair,
                "candidate_counts": dict(candidate_counts),
                "organism_scores": dict(scores),
            },
        )

    return (
        None,
        "chain_ambiguous",
        {"chain_pairs": chain_pairs, "per_pair": per_pair, "candidate_counts": dict(candidate_counts)},
    )


def select_by_vote(pdb_ids, pdb_data):
    """Fallback: majority-vote Uniprot across all PDBs.

    Same algorithm as before — handles proteins without PDBTM chain data.
    """
    votes = Counter()
    pdb_uniprots = {}

    for pdb in pdb_ids:
        entities = pdb_data.get(pdb, {})
        all_in_pdb = set()
        for eid, info in entities.items():
            all_in_pdb.update(info.get("uniprots", []))
        pdb_uniprots[pdb] = all_in_pdb
        for u in all_in_pdb:
            votes[u] += 1

    if not votes:
        return None, "no_mapping", {"n_pdbs": len(pdb_ids), "details": pdb_uniprots}

    ranked = votes.most_common()

    if len(ranked) == 1:
        return [ranked[0][0]], "high", {"n_pdbs": len(pdb_ids), "votes": dict(votes), "pdb_uniprots": pdb_uniprots}

    if ranked[0][1] > ranked[1][1]:
        return [ranked[0][0]], "high", {"n_pdbs": len(pdb_ids), "votes": dict(votes), "pdb_uniprots": pdb_uniprots}

    # Tie: exclude fusion partners
    filtered = [(u, c) for u, c in ranked if u not in FUSION_PARTNERS]
    if len(filtered) == 1:
        return (
            [filtered[0][0]],
            "medium",
            {
                "n_pdbs": len(pdb_ids),
                "votes": dict(votes),
                "fusion_filtered": dict(filtered),
                "pdb_uniprots": pdb_uniprots,
            },
        )
    if len(filtered) >= 2 and filtered[0][1] > filtered[1][1]:
        return (
            [filtered[0][0]],
            "medium",
            {
                "n_pdbs": len(pdb_ids),
                "votes": dict(votes),
                "fusion_filtered": dict(filtered),
                "pdb_uniprots": pdb_uniprots,
            },
        )

    # Still tied: organism heuristic
    if len(filtered) >= 2 and filtered[0][1] == filtered[1][1]:
        organism_scores = defaultdict(int)
        for pdb in pdb_ids:
            for eid, info in pdb_data.get(pdb, {}).items():
                for u in info.get("uniprots", []):
                    if u in (filtered[0][0], filtered[1][0]):
                        for org in info.get("organisms", []):
                            ol = org.lower()
                            if "homo sapiens" in ol:
                                organism_scores[(u, "human")] += 1
                            elif "enterobacteria phage" in ol or "synthetic" in ol:
                                organism_scores[(u, "phage")] += 1
                            elif "escherichia coli" in ol:
                                organism_scores[(u, "ecoli")] += 1
                            else:
                                organism_scores[(u, "other")] += 1
        org_priority = {"human": 4, "other": 3, "ecoli": 2, "phage": 1}
        scores = {}
        for u in [filtered[0][0], filtered[1][0]]:
            s = 0
            for (uni, ot), c in organism_scores.items():
                if uni == u:
                    s += org_priority.get(ot, 2) * c
            scores[u] = s
        if scores[filtered[0][0]] != scores[filtered[1][0]]:
            winner = max(scores, key=scores.get)
            return (
                [winner],
                "medium",
                {
                    "n_pdbs": len(pdb_ids),
                    "votes": dict(votes),
                    "fusion_filtered": dict(filtered),
                    "organism_scores": scores,
                    "pdb_uniprots": pdb_uniprots,
                },
            )

    # Genuine tie → auto-pick first
    if filtered:
        return (
            [filtered[0][0]],
            "tie_auto",
            {
                "n_pdbs": len(pdb_ids),
                "votes": dict(votes),
                "options": [u for u, _ in filtered],
                "pdb_uniprots": pdb_uniprots,
            },
        )
    if ranked:
        return (
            [ranked[0][0]],
            "tie_auto",
            {
                "n_pdbs": len(pdb_ids),
                "votes": dict(votes),
                "options": [u for u, _ in ranked],
                "pdb_uniprots": pdb_uniprots,
            },
        )
    return None, "tie_fatal", {"n_pdbs": len(pdb_ids), "votes": dict(votes), "pdb_uniprots": pdb_uniprots}


# ═══════════════════════════════════════════════════════════════════
#  Phase 1d: YAML updater
# ═══════════════════════════════════════════════════════════════════


def update_yaml(yaml_path, uniprot_value, dry_run=True):
    """Add uniprot_id to a protein YAML file. Accepts str or list.

    Args:
        uniprot_value: str (single) or list (multiple) of Uniprot accessions.
    Returns: True if changed.
    """
    if not yaml_path.exists():
        print(f"  ERROR: YAML not found: {yaml_path}")
        return False
    original = yaml_path.read_text()
    data = yaml.safe_load(original)
    if not isinstance(data, dict):
        print(f"  ERROR: Invalid YAML: {yaml_path.name}")
        return False

    # Normalize to the storage value — list if >1, else single string
    if isinstance(uniprot_value, list) and len(uniprot_value) > 1:
        storage = sorted(set(uniprot_value))
    elif isinstance(uniprot_value, list):
        storage = uniprot_value[0] if uniprot_value else ""
    else:
        storage = uniprot_value

    existing = data.get("uniprot_id", "")
    if existing == storage:
        return False

    data["uniprot_id"] = storage
    data["updated"] = "2026-07-03"

    new_yaml = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    if dry_run:
        label = storage if isinstance(storage, str) else f"[{', '.join(storage)}]"
        print(f"  [DRY-RUN] Would update {yaml_path.name}: {existing or '(none)'} → {label}")
        return True

    yaml_path.write_text(new_yaml)
    verify = yaml.safe_load(yaml_path.read_text())
    if verify.get("uniprot_id", "") != storage:
        print(f"  ERROR: Write verification failed for {yaml_path.name}")
        return False
    label = storage if isinstance(storage, str) else f"[{', '.join(storage)}]"
    print(f"  Updated {yaml_path.name}: {existing or '(none)'} → {label}")
    return True


# ═══════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════


def main():
    parser = argparse.ArgumentParser(description="Enrich protein YAMLs with uniprot_id via RCSB PDB GraphQL API")
    parser.add_argument("--no-dry-run", action="store_true", help="Actually write changes (default is dry-run)")
    parser.add_argument("--dry-run", action="store_true", dest="force_dry", help="Force dry-run mode")
    parser.add_argument("--limit", type=int, default=0, help="Process only first N proteins")
    parser.add_argument("--cache-only", action="store_true", help="Use cached data only, skip API calls")
    parser.add_argument("--skip-existing", action="store_true", help="Skip proteins that already have uniprot_id")
    parser.add_argument("--batch-size", type=int, default=400, help="GraphQL batch size (default: 400)")
    parser.add_argument(
        "--method",
        choices=["auto", "chain", "vote"],
        default="auto",
        help="Selection method: auto (try chain first), chain-only, vote-only",
    )
    args = parser.parse_args()

    dry_run = not args.no_dry_run or args.force_dry
    GraphQLResolver.BATCH_SIZE = args.batch_size

    print("=" * 60)
    print(f"Uniprot Enrichment — {'DRY RUN' if dry_run else 'LIVE RUN'}")
    print(f"Selection method: {args.method}")
    print("=" * 60)

    # ── Step 1: Collect PDB IDs and chain pairs ─────────────
    print("\n[1/5] Collecting PDB IDs and chain pairs from YAMLs...")
    chain_proteins, vote_fallback_proteins, all_pdbs = collect_chain_pairs()
    print(f"  Proteins with PDBTM chains: {len(chain_proteins)}")
    print(f"  Proteins for vote fallback: {len(vote_fallback_proteins)}")
    print(f"  Unique PDB IDs: {len(all_pdbs)}")

    # ── Step 2: Resolve via GraphQL ──────────────────────────
    print("\n[2/5] Resolving Uniprot mappings via RCSB GraphQL...")
    resolver = GraphQLResolver(cache_only=args.cache_only)
    pdb_data = resolver.resolve(all_pdbs)
    resolved_count = sum(1 for v in pdb_data.values() if v)
    print(f"  PDBs resolved: {resolved_count} / {len(all_pdbs)}")

    # ── Step 3: Select Uniprot per protein ───────────────────
    method_label = {"chain": "PDBTM chain→entity", "vote": "majority vote", "auto": "chain→entity (fallback to vote)"}
    print(f"\n[3/5] Selecting Uniprot via {method_label[args.method]}...")

    results = {}
    summary_counts = Counter()
    method_counts = Counter()

    # Track which proteins each method handles
    processed = set()

    # Primary: chain-based selection
    if args.method in ("auto", "chain"):
        for protein_name in sorted(chain_proteins.keys()):
            if args.limit and len(results) >= args.limit:
                print(f"  (--limit {args.limit} reached)")
                break
            if args.skip_existing:
                yf = PROTEINS_DIR / f"{protein_name}.yaml"
                if yf.exists():
                    ed = yaml.safe_load(yf.read_text())
                    if isinstance(ed, dict) and ed.get("uniprot_id"):
                        results[protein_name] = {
                            "status": "skipped",
                            "uniprot_id": ed["uniprot_id"],
                            "method": "chain",
                            "reason": "already_has",
                        }
                        method_counts["chain_skipped"] += 1
                        continue

            chain_pairs = chain_proteins[protein_name]
            # Only use chain pairs whose PDBs are in the cache
            available = [(p, c) for p, c in chain_pairs if p in pdb_data]
            if not available:
                continue  # Will be handled by fallback

            uniprot_id, confidence, debug = select_by_chain(available, pdb_data)

            if uniprot_id:
                results[protein_name] = {
                    "status": "resolved",
                    "uniprot_id": uniprot_id,
                    "confidence": confidence,
                    "method": "chain",
                    "n_chain_pairs": len(available),
                }
                summary_counts[f"chain_{confidence}"] += 1
                method_counts["chain_ok"] += 1
            else:
                # Chain method failed — schedule for vote fallback
                continue

            processed.add(protein_name)

    # Fallback: majority vote for proteins without chain data or where chain failed
    if args.method in ("auto", "vote"):
        for protein_name in sorted(vote_fallback_proteins.keys()):
            if protein_name in processed:
                continue
            if args.limit and len(results) >= args.limit:
                print(f"  (--limit {args.limit} reached)")
                break
            if args.skip_existing:
                yf = PROTEINS_DIR / f"{protein_name}.yaml"
                if yf.exists():
                    ed = yaml.safe_load(yf.read_text())
                    if isinstance(ed, dict) and ed.get("uniprot_id"):
                        results[protein_name] = {
                            "status": "skipped",
                            "uniprot_id": ed["uniprot_id"],
                            "method": "vote",
                            "reason": "already_has",
                        }
                        method_counts["vote_skipped"] += 1
                        continue

            pdbs = vote_fallback_proteins[protein_name]
            available = [p for p in pdbs if p in pdb_data]
            if not available:
                results[protein_name] = {
                    "status": "failed",
                    "uniprot_id": None,
                    "reason": "no_pdb_mapping",
                    "method": "vote",
                    "n_pdbs": len(pdbs),
                }
                summary_counts["vote_no_mapping"] += 1
                continue

            uniprot_id, confidence, debug = select_by_vote(available, pdb_data)

            if uniprot_id:
                results[protein_name] = {
                    "status": "resolved",
                    "uniprot_id": uniprot_id,
                    "confidence": confidence,
                    "method": "vote",
                    "n_pdbs": len(available),
                }
                summary_counts[f"vote_{confidence}"] += 1
                method_counts["vote_ok"] += 1
            else:
                results[protein_name] = {
                    "status": "failed",
                    "uniprot_id": None,
                    "reason": confidence,
                    "method": "vote",
                    "n_pdbs": len(available),
                    "votes": debug.get("votes", {}),
                }
                summary_counts[f"vote_{confidence}"] += 1

    # Also try vote for proteins that had chain data but chain method failed
    if args.method == "auto":
        for protein_name in sorted(chain_proteins.keys()):
            if protein_name in results or protein_name in processed:
                continue
            if args.limit and len(results) >= args.limit:
                break

            # Try vote on the chain protein's structure PDBs
            pdbs = vote_fallback_proteins.get(protein_name, [])
            available = [p for p in pdbs if p in pdb_data]
            if not available:
                results[protein_name] = {
                    "status": "failed",
                    "uniprot_id": None,
                    "reason": "chain+vote_no_mapping",
                    "method": "chain_fallback_vote",
                    "n_pdbs": len(pdbs),
                }
                summary_counts["both_failed"] += 1
                continue

            uniprot_id, confidence, debug = select_by_vote(available, pdb_data)
            if uniprot_id:
                results[protein_name] = {
                    "status": "resolved",
                    "uniprot_id": uniprot_id,
                    "confidence": f"chain_fallback_{confidence}",
                    "method": "chain_fallback_vote",
                    "n_pdbs": len(available),
                }
                summary_counts[f"chain_fallback_{confidence}"] += 1
                method_counts["chain_fallback_ok"] += 1
            else:
                results[protein_name] = {
                    "status": "failed",
                    "uniprot_id": None,
                    "reason": confidence,
                    "method": "chain_fallback_vote",
                    "n_pdbs": len(available),
                    "votes": debug.get("votes", {}),
                }
                summary_counts[f"chain_fallback_{confidence}"] += 1

    # Print summary
    print("\n  Results:")
    for label, count in sorted(summary_counts.items()):
        print(f"    {label}: {count}")
    total_resolved = sum(1 for r in results.values() if r.get("status") == "resolved")
    print(f"  Total resolved: {total_resolved} / {len(results)}")
    print(
        f"  Methods: chain={method_counts.get('chain_ok', 0)}, "
        f"vote={method_counts.get('vote_ok', 0)}, "
        f"fallback={method_counts.get('chain_fallback_ok', 0)}"
    )

    # ── Step 4: Write to YAML files ──────────────────────────
    print("\n[4/5] Writing uniprot_id to YAML files...")
    written = 0
    skipped = 0
    for protein_name, info in sorted(results.items()):
        if info.get("status") != "resolved":
            continue
        yf = PROTEINS_DIR / f"{protein_name}.yaml"
        if update_yaml(yf, info["uniprot_id"], dry_run=dry_run):
            written += 1
        else:
            skipped += 1
    if dry_run:
        print(f"\n  DRY-RUN: Would update {written} files ({skipped} already correct)")
    else:
        print(f"\n  Written: {written} files ({skipped} already correct)")

    # ── Step 5: Audit report ─────────────────────────────────
    print("\n[5/5] Writing audit report...")
    report = {
        "run_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "dry_run": dry_run,
        "method": args.method,
        "total_proteins_with_chains": len(chain_proteins),
        "total_proteins_vote_fallback": len(vote_fallback_proteins),
        "unique_pdbs_total": len(all_pdbs),
        "unique_pdbs_resolved": resolved_count,
        "summary": dict(summary_counts),
        "total_resolved": total_resolved,
        "total_failed": len(results) - total_resolved,
        "methods": dict(method_counts),
        "proteins": results,
    }
    AUDIT_PATH.write_text(json.dumps(report, indent=2))
    print(f"  Audit report: {AUDIT_PATH}")
    print(f"\n{'=' * 60}")
    print(f"Done. {'DRY-RUN — use --no-dry-run to write' if dry_run else 'Changes written.'}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
