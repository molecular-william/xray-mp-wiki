"""Fill year/pmid/journal/PDB Release/MW from RCSB GraphQL."""
import json, csv, time
from pathlib import Path
from urllib.request import Request, urlopen

CSV_PATH = Path("raw/datasets/wiki_dataset_v1.csv")
GRAPHQL = "https://data.rcsb.org/graphql"
BATCH_SIZE = 500
DELAY = 0.5

def query(pdb_ids):
    gql = '''{ entries(entry_ids: %s) { rcsb_id rcsb_primary_citation { year journal_abbrev pdbx_database_id_PubMed } rcsb_entry_info { molecular_weight } rcsb_accession_info { initial_release_date } } }'''
    body = json.dumps({"query": gql % json.dumps(pdb_ids)})
    req = Request(GRAPHQL, data=body.encode(), headers={"Content-Type": "application/json"})
    try:
        resp = json.loads(urlopen(req, timeout=30).read())
        return resp.get("data", {}).get("entries", [])
    except Exception as e:
        print(f"  Error batch of {len(pdb_ids)}: {e}")
        return []

# Read CSV
with open(CSV_PATH, newline="") as f:
    reader = list(csv.DictReader(f))

headers = list(reader[0].keys())
missing_pdbs = sorted({r["pdbCode"].lower() for r in reader if not r["year"]})
total_missing = len(missing_pdbs)
print(f"Rows: {len(reader)}, missing year: {total_missing} unique PDBs")

# Batch query
results = {}
for i in range(0, len(missing_pdbs), BATCH_SIZE):
    batch = missing_pdbs[i:i+BATCH_SIZE]
    print(f"  Batch {i//BATCH_SIZE + 1} ({len(batch)} PDBs)...")
    for entry in query(batch):
        pdb = entry["rcsb_id"].lower()
        cit = entry.get("rcsb_primary_citation") or {}
        info = entry.get("rcsb_entry_info") or {}
        acc = entry.get("rcsb_accession_info") or {}
        results[pdb] = {
            "year": str(cit.get("year") or ""),
            "journal": str(cit.get("journal_abbrev") or ""),
            "pmid": str(cit.get("pdbx_database_id_PubMed") or ""),
            "release": str(acc.get("initial_release_date", "")[:10] if acc.get("initial_release_date") else ""),
            "mw": str(round(info.get("molecular_weight", 0))) if info.get("molecular_weight") else "",
        }
    time.sleep(DELAY)

print(f"  Found {len(results)} PDBs")

# Apply
updated = 0
for row in reader:
    pdb = row["pdbCode"].lower()
    meta = results.get(pdb)
    if meta and not row["year"]:
        row["year"] = meta["year"]
        row["journal"] = meta["journal"]
        if meta["pmid"] and not row["pubMedId"]:
            row["pubMedId"] = meta["pmid"]
            row["PubMed Link"] = f"https://www.ncbi.nlm.nih.gov/pubmed/{meta['pmid']}"
        row["PDB Release"] = meta["release"]
        row["PDBStructure Weight"] = meta["mw"]
        updated += 1

with open(CSV_PATH, "w", newline="") as f:
    csv.DictWriter(f, fieldnames=headers).writeheader()
    csv.DictWriter(f, fieldnames=headers).writerows(reader)

print(f"\nUpdated {updated} rows")
print(f"Final:  year={sum(1 for r in reader if r['year'])}/{len(reader)}")
print(f"        release={sum(1 for r in reader if r['PDB Release'])}/{len(reader)}")
print(f"        mw={sum(1 for r in reader if r['PDBStructure Weight'])}/{len(reader)}")
