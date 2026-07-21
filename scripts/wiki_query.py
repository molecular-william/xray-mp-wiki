import argparse
import json
import re
import sys
import textwrap
from collections import Counter, defaultdict

from _base import BASE_DIR, HOST_MAP, fast_load_str, normalize_host

BASE = BASE_DIR
INDEX_PATH = BASE / "references" / "entity_index.json"


class WikiQuery:
    """xray-mp-wiki query engine. Loads data lazily."""

    def __init__(self, rebuild=False):
        self._catalog = None
        self._graph = None
        self._adj = None
        self._yamls = {}
        self._indices = {}
        self._loaded = False
        self._load_catalog()
        self._load_graph()
        if rebuild:
            self._load_yamls()
        else:
            self._try_load_index()

    def _load_catalog(self):
        p = BASE / "references" / "entity_catalog.json"
        self._catalog = json.loads(p.read_text()) if p.exists() else {}

    def _load_graph(self):
        p = BASE / "xray-mp-wiki" / "assets" / "graph.json"
        if p.exists():
            g = json.loads(p.read_text())
            self._graph = g
            self._adj = defaultdict(dict)
            for e in g.get("edges", []):
                s, t = e["source"], e["target"]
                self._adj[s][t] = {
                    "type": e.get("type", "general"),
                    "weight": e.get("weight", 1),
                    "reasons": e.get("reasons", []),
                }
                if e.get("bidirectional", True):
                    self._adj[t][s] = {
                        "type": e.get("type", "general"),
                        "weight": e.get("weight", 1),
                        "reasons": e.get("reasons", []),
                    }
        else:
            self._graph = {"nodes": [], "edges": []}
            self._adj = defaultdict(dict)

    def _try_load_index(self):
        """Load precomputed index if fresh enough. Returns True on success."""
        if not INDEX_PATH.exists():
            self._indices = {}
            return False
        # Check freshness: index must be newer than all YAML dirs
        index_mtime = INDEX_PATH.stat().st_mtime
        for d in ["proteins_yaml", "reagents_yaml", "methods_yaml", "concepts_yaml"]:
            yaml_dir = BASE / "xray-mp-wiki" / d
            if yaml_dir.exists():
                # Check if any YAML file is newer than index
                for f in yaml_dir.rglob("*.yaml"):
                    if f.stat().st_mtime > index_mtime + 1:  # 1s grace
                        self._indices = {}
                        return False
        try:
            with open(INDEX_PATH) as f:
                self._indices = json.load(f)
            # Restore defaultdicts
            for k in [
                "by_tag",
                "by_family",
                "by_detergent",
                "by_pdb",
                "by_expression",
                "by_uniprot",
                "by_organism",
                "by_subdir",
                "by_reagent_prop",
            ]:
                if k in self._indices:
                    self._indices[k] = defaultdict(list, self._indices[k])
            self._loaded = True
            return True
        except Exception:
            self._indices = {}
            return False

    def _save_index(self):
        """Save current indices to disk for fast reload."""
        try:
            serializable = {}
            for k, v in self._indices.items():
                if isinstance(v, defaultdict):
                    serializable[k] = dict(v)
                elif isinstance(v, dict):
                    serializable[k] = v
                else:
                    serializable[k] = v
            with open(INDEX_PATH, "w") as f:
                json.dump(serializable, f, indent=2, default=str)
        except Exception:
            pass  # Non-critical, fail silently

    def _load_yamls(self):
        if self._loaded:
            return

        for t in ["proteins", "reagents", "methods", "concepts"]:
            self._yamls[t] = {}
            d = BASE / "xray-mp-wiki" / f"{t}_yaml"
            if not d.exists():
                continue
            for f in sorted(d.glob("*.yaml")):
                try:
                    data = fast_load_str(f.read_text())
                    if data and isinstance(data, dict):
                        self._yamls[t][f.stem] = data
                except Exception:
                    pass
        self._build_indices()
        self._loaded = True
        self._save_index()

    def _build_indices(self):
        idx = {
            "by_tag": defaultdict(list),
            "by_subdir": defaultdict(list),
            "by_family": defaultdict(list),
            "by_detergent": defaultdict(list),
            "by_pdb": defaultdict(list),
            "by_expression": defaultdict(list),
            "by_uniprot": defaultdict(list),
            "by_organism": defaultdict(list),
            "by_reagent_prop": defaultdict(list),
            "by_resolution": {},
            "reagent_by_subdir": defaultdict(list),
            "protein_meta": {},  # name → {family, pdb_count, best_resolution, tags, verified}
            "reagent_meta": {},  # name → {tags, cmc, molecular_weight, class, uses_count, examples_count}
        }
        known_detergents = {}
        for rname, rinfo in (self._catalog or {}).items():
            if rinfo.get("type") == "reagents":
                known_detergents[rname.lower()] = rname
                known_detergents[rname.lower().replace("-", "")] = rname
        for name, data in self._yamls.get("proteins", {}).items():
            tags_list = data.get("tags", [])
            for t in tags_list:
                idx["by_tag"][t].append(name)
            m = data.get("mpstruc_classification", {})
            family = m.get("subgroup", "") if m else ""
            if family:
                idx["by_family"][family.split(":")[0].strip()].append(name)
            e = data.get("expression", {})
            if e and e.get("system"):
                idx["by_expression"][self._normalize_host(e["system"].lower())].append(name)
            res_list, det_list, pdb_count = [], [], 0
            for pub in data.get("publications", []):
                if not isinstance(pub, dict):
                    continue
                for s in pub.get("structures", []):
                    pdb_id = s.get("pdb_id", "")
                    if pdb_id:
                        idx["by_pdb"][pdb_id.upper()].append(name)
                        pdb_count += 1
                    r = s.get("resolution", "")
                    if r:
                        m2 = re.search(r"([\d.]+)", str(r))
                        if m2:
                            res_list.append(float(m2.group(1)))
                for p in pub.get("purifications", []):
                    for step in p.get("steps", []):
                        det = step.get("detergent", "")
                        dets = self._extract_detergents(str(det), known_detergents)
                        det_list.extend(dets)
            if res_list:
                idx["by_resolution"][name] = res_list
            for d in set(det_list):
                idx["by_detergent"][d].append(name)
            uniprot_id = data.get("uniprot_id", "") or ""
            if isinstance(uniprot_id, list):
                for u in uniprot_id:
                    if u:
                        idx["by_uniprot"][u].append(name)
                uniprot_id_str = ", ".join(uniprot_id)
            elif uniprot_id:
                idx["by_uniprot"][uniprot_id].append(name)
                uniprot_id_str = uniprot_id
            else:
                uniprot_id_str = ""
            idx["protein_meta"][name] = {
                "family": family,
                "pdb_count": pdb_count,
                "best_resolution": self._fmt_resolution(res_list),
                "tags": tags_list,
                "verified": data.get("verified", False),
                "uniprot_id": uniprot_id_str,
            }
            organism = data.get("organism", "") or ""
            if organism:
                idx["by_organism"][organism].append(name)
        for name, data in self._yamls.get("reagents", {}).items():
            tags_list = data.get("tags", [])
            for t in tags_list:
                idx["by_tag"][t].append(name)
                if t.startswith("subdirectory-"):
                    s = t.replace("subdirectory-", "")
                    idx["by_subdir"][s].append(name)
                    idx["reagent_by_subdir"][s].append(name)
            for prop in [
                "cmc",
                "hlb",
                "molecular_weight",
                "pka",
                "kd_ki",
                "chemical_formula",
                "head_group",
                "tail_length",
                "class",
            ]:
                val = data.get(prop)
                if val:
                    idx["by_reagent_prop"][prop].append((name, str(val)))
            idx["reagent_meta"][name] = {
                "tags": tags_list,
                "cmc": data.get("cmc"),
                "molecular_weight": data.get("molecular_weight"),
                "kd_ki": data.get("kd_ki"),
                "class": data.get("class"),
                "uses_count": len(data.get("uses", [])),
                "examples_count": len(data.get("examples", [])),
            }
        for t in ["methods", "concepts"]:
            for name, data in self._yamls.get(t, {}).items():
                for tag in data.get("tags", []):
                    idx["by_tag"][tag].append(name)
                    if tag.startswith("subdirectory-"):
                        idx["by_subdir"][tag.replace("subdirectory-", "")].append(name)
        self._indices = idx

    _HOST_MAP = HOST_MAP  # type: ignore[assignment]

    @staticmethod
    def _normalize_host(sys_str):
        return normalize_host(sys_str)

    @staticmethod
    def _extract_detergents(det_str, known_detergents):
        results = set()
        dl = det_str.lower()
        for kname, rname in known_detergents.items():
            if kname in dl:
                results.add(rname)
        for m in re.finditer(r"\(/xray-mp-wiki/reagents/detergents/([^/]+)/\)", det_str):
            results.add(m.group(1))
        for m in re.finditer(r"\[([^\]]+)\]\(/xray-mp-wiki/reagents/detergents/([^/]+)/\)", det_str):
            results.add(m.group(2))
        return results

    @staticmethod
    def _parse_cmc(s):
        m = re.search(r"([\d.]+)", str(s))
        return float(m.group(1)) if m else None

    @staticmethod
    def _parse_mw(s):
        m = re.search(r"([\d.]+)", str(s))
        return float(m.group(1)) if m else None

    @staticmethod
    def _fmt_resolution(res_list):
        return f"{min(res_list):.1f}" if res_list else "—"

    def _ensure_loaded(self):
        if not self._loaded:
            self._load_yamls()

    def _cat_entry(self, name):
        for n in [name, name.lower(), name.replace("_", "-")]:
            if n in (self._catalog or {}):
                return self._catalog[n]
        return None

    # ─── Queries ───

    def get(self, name):
        entry = self._cat_entry(name)
        if entry:
            return {
                "name": name,
                "type": entry.get("type", "?"),
                "title": entry.get("title", name),
                "path": entry.get("filename", f"{name}.md"),
            }
        return None

    def entities(self, etype=None, tag=None, subdir=None, limit=None, offset=0, sort=None):
        results = []
        for name, info in (self._catalog or {}).items():
            if etype and info.get("type") != etype:
                continue
            results.append(
                {
                    "name": name,
                    "type": info.get("type", "?"),
                    "title": info.get("title", name),
                    "path": info.get("filename", f"{name}.md"),
                }
            )
        if tag or subdir:
            # Use index for tag/subdir filtering (fast, no YAML load)
            if not self._loaded and self._indices.get("by_tag"):
                filtered = []
                for r in results:
                    meta = self._indices.get("protein_meta", {}).get(r["name"]) or self._indices.get(
                        "reagent_meta", {}
                    ).get(r["name"])
                    if not meta:
                        continue
                    if tag and tag not in meta.get("tags", []):
                        continue
                    if subdir and f"subdirectory-{subdir}" not in meta.get("tags", []):
                        continue
                    filtered.append(r)
                results = filtered
            else:
                self._ensure_loaded()
                filtered = []
                for r in results:
                    data = self._yamls.get(r["type"], {}).get(r["name"])
                    if not data:
                        continue
                    if tag and tag not in data.get("tags", []):
                        continue
                    if subdir:
                        if not any(
                            s.replace("subdirectory-", "") == subdir
                            for s in data.get("tags", [])
                            if s.startswith("subdirectory-")
                        ):
                            if (
                                r["type"] != "proteins"
                                or subdir not in data.get("mpstruc_classification", {}).get("subgroup", "").lower()
                            ):
                                continue
                    filtered.append(r)
                results = filtered
        if sort:
            results.sort(key=lambda x: x.get(sort, ""))
        if offset:
            results = results[offset:]
        if limit:
            results = results[:limit]
        return results

    def proteins(
        self,
        family=None,
        detergent=None,
        resolution_max=None,
        expression=None,
        pdb=None,
        tag=None,
        uniprot=None,
        limit=None,
    ):
        # Use indices + protein_meta when available (no YAML load)
        if self._indices.get("protein_meta"):
            results = list(self._indices["protein_meta"].keys())
            if family:
                results = [
                    n for n in results if family.lower() in self._indices["protein_meta"][n].get("family", "").lower()
                ]
            if tag:
                results = [n for n in results if tag in self._indices["protein_meta"][n].get("tags", [])]
            if detergent:
                det_set = set(self._indices.get("by_detergent", {}).get(detergent.lower(), []))
                results = [n for n in results if n in det_set]
            if expression:
                expr_set = set(self._indices.get("by_expression", {}).get(self._normalize_host(expression.lower()), []))
                results = [n for n in results if n in expr_set]
            if pdb:
                pdb_set = set(self._indices.get("by_pdb", {}).get(pdb.upper(), []))
                results = [n for n in results if n in pdb_set]
            if uniprot:
                uniprot_set = set(self._indices.get("by_uniprot", {}).get(uniprot.upper(), []))
                results = [n for n in results if n in uniprot_set]
            if resolution_max is not None:
                results = [
                    n
                    for n in results
                    if self._indices.get("by_resolution", {}).get(n, [])
                    and min(self._indices["by_resolution"][n]) <= resolution_max
                ]
            if limit:
                results = results[:limit]
            out = []
            for name in results:
                m = self._indices["protein_meta"][name]
                entry = self._cat_entry(name) or {}
                out.append(
                    {
                        "name": name,
                        "title": entry.get("title", name),
                        "family": m["family"],
                        "pdb_count": m["pdb_count"],
                        "best_resolution": m["best_resolution"],
                        "tags": m["tags"],
                        "verified": m["verified"],
                        "uniprot_id": m.get("uniprot_id", ""),
                    }
                )
            return out

        # Fallback: full YAML load
        self._ensure_loaded()
        results = []
        for name, data in self._yamls.get("proteins", {}).items():
            if family:
                m = data.get("mpstruc_classification", {})
                if not m or family.lower() not in (m.get("subgroup", "") or "").lower():
                    continue
            if tag and tag not in data.get("tags", []):
                continue
            if detergent and name not in self._indices.get("by_detergent", {}).get(detergent.lower(), []):
                found = False
                for pub in data.get("publications", []):
                    for p in pub.get("purifications", []):
                        for step in p.get("steps", []):
                            if detergent.lower() in str(step.get("detergent", "")).lower():
                                found = True
                                break
                if not found:
                    continue
            if expression and expression.lower() not in str(data.get("expression", {}).get("system", "")).lower():
                continue
            if pdb:
                found = False
                for pub in data.get("publications", []):
                    for s in pub.get("structures", []):
                        if s.get("pdb_id", "").upper() == pdb.upper():
                            found = True
                            break
                if not found:
                    continue
            if resolution_max is not None:
                rl = self._indices.get("by_resolution", {}).get(name, [])
                if not rl or min(rl) > resolution_max:
                    continue
            results.append(name)
        if limit:
            results = results[:limit]
        return [
            {
                "name": n,
                "title": self._yamls["proteins"][n].get("title", n),
                "family": (self._yamls["proteins"][n].get("mpstruc_classification", {}) or {}).get("subgroup", ""),
                "pdb_count": sum(
                    1 for pub in self._yamls["proteins"][n].get("publications", []) for s in pub.get("structures", [])
                ),
                "best_resolution": self._fmt_resolution(self._indices.get("by_resolution", {}).get(n, [])),
                "tags": self._yamls["proteins"][n].get("tags", []),
                "verified": self._yamls["proteins"][n].get("verified", False),
            }
            for n in results
        ]

    def reagents(
        self, subdir=None, cmc_max=None, cmc_min=None, mw_max=None, mw_min=None, tag=None, has_property=None, limit=None
    ):
        # Use indices + reagent_meta when available
        if self._indices.get("reagent_meta"):
            results = list(self._indices["reagent_meta"].keys())
            if subdir:
                results = [
                    n for n in results if f"subdirectory-{subdir}" in self._indices["reagent_meta"][n].get("tags", [])
                ]
            if tag:
                results = [n for n in results if tag in self._indices["reagent_meta"][n].get("tags", [])]
            if has_property:
                prop_set = {p[0] for p in self._indices.get("by_reagent_prop", {}).get(has_property, [])}
                results = [n for n in results if n in prop_set]
            if cmc_max is not None or cmc_min is not None or mw_max is not None or mw_min is not None:
                # Need value comparison — fall back to full YAML load
                self._ensure_loaded()
                return self._reagents_yaml(results, subdir, cmc_max, cmc_min, mw_max, mw_min, tag, has_property, limit)
            if limit:
                results = results[:limit]
            out = []
            for name in results:
                m = self._indices["reagent_meta"][name]
                entry = self._cat_entry(name) or {}
                out.append(
                    {
                        "name": name,
                        "title": entry.get("title", name),
                        "tags": m["tags"],
                        "cmc": m["cmc"],
                        "molecular_weight": m["molecular_weight"],
                        "kd_ki": m["kd_ki"],
                        "class": m["class"],
                        "uses_count": m["uses_count"],
                        "examples_count": m["examples_count"],
                    }
                )
            return out

        self._ensure_loaded()
        return self._reagents_yaml(
            list(self._yamls.get("reagents", {}).keys()),
            subdir,
            cmc_max,
            cmc_min,
            mw_max,
            mw_min,
            tag,
            has_property,
            limit,
        )

    def _reagents_yaml(self, names, subdir, cmc_max, cmc_min, mw_max, mw_min, tag, has_property, limit):
        """Filter reagents using full YAML data (for property value comparisons)."""
        results = []
        for name in names:
            data = self._yamls.get("reagents", {}).get(name, {})
            if not data:
                continue
            if subdir and f"subdirectory-{subdir}" not in data.get("tags", []):
                continue
            if tag and tag not in data.get("tags", []):
                continue
            if has_property and not data.get(has_property):
                continue
            if cmc_max is not None or cmc_min is not None:
                c = data.get("cmc")
                cv = self._parse_cmc(c) if c else None
                if cv is None:
                    continue
                if cmc_max is not None and cv > cmc_max:
                    continue
                if cmc_min is not None and cv < cmc_min:
                    continue
            if mw_max is not None or mw_min is not None:
                m = data.get("molecular_weight")
                mv = self._parse_mw(m) if m else None
                if mv is None:
                    continue
                if mw_max is not None and mv > mw_max:
                    continue
                if mw_min is not None and mv < mw_min:
                    continue
            results.append(name)
        if limit:
            results = results[:limit]
        return [
            {
                "name": n,
                "title": (self._yamls.get("reagents", {}).get(n, {}) or {}).get("title", n),
                "tags": (self._yamls.get("reagents", {}).get(n, {}) or {}).get("tags", []),
                "cmc": (self._yamls.get("reagents", {}).get(n, {}) or {}).get("cmc"),
                "molecular_weight": (self._yamls.get("reagents", {}).get(n, {}) or {}).get("molecular_weight"),
                "kd_ki": (self._yamls.get("reagents", {}).get(n, {}) or {}).get("kd_ki"),
                "class": (self._yamls.get("reagents", {}).get(n, {}) or {}).get("class"),
                "uses_count": len((self._yamls.get("reagents", {}).get(n, {}) or {}).get("uses", [])),
                "examples_count": len((self._yamls.get("reagents", {}).get(n, {}) or {}).get("examples", [])),
            }
            for n in results
        ]

    def methods(self, tag=None, limit=None):
        if self._indices.get("by_tag"):
            results = [n for n in (self._catalog or {}) if (self._catalog or {}).get(n, {}).get("type") == "methods"]
            if tag:
                results = [n for n in results if tag in self._indices.get("by_tag", {}).get(tag, [])]
            if limit:
                results = results[:limit]
            return [{"name": n, "title": (self._catalog or {}).get(n, {}).get("title", n), "tags": []} for n in results]
        self._ensure_loaded()
        results = [n for n, d in self._yamls.get("methods", {}).items() if not tag or tag in d.get("tags", [])]
        if limit:
            results = results[:limit]
        return [
            {
                "name": n,
                "title": self._yamls["methods"][n].get("title", n),
                "tags": self._yamls["methods"][n].get("tags", []),
            }
            for n in results
        ]

    def concepts(self, tag=None, limit=None):
        if self._indices.get("by_tag"):
            results = [n for n in (self._catalog or {}) if (self._catalog or {}).get(n, {}).get("type") == "concepts"]
            if tag:
                results = [n for n in results if tag in self._indices.get("by_tag", {}).get(tag, [])]
            if limit:
                results = results[:limit]
            return [{"name": n, "title": (self._catalog or {}).get(n, {}).get("title", n), "tags": []} for n in results]
        self._ensure_loaded()
        results = [n for n, d in self._yamls.get("concepts", {}).items() if not tag or tag in d.get("tags", [])]
        if limit:
            results = results[:limit]
        return [
            {
                "name": n,
                "title": self._yamls["concepts"][n].get("title", n),
                "tags": self._yamls["concepts"][n].get("tags", []),
            }
            for n in results
        ]

    def search(self, query, etype=None, limit=None):
        """Title search fast (catalog). Overview search triggers full YAML load."""
        q = query.lower()
        results = []
        for name, info in (self._catalog or {}).items():
            if etype and info.get("type") != etype:
                continue
            if q in info.get("title", "").lower():
                results.append(
                    {
                        "name": name,
                        "type": info.get("type", "?"),
                        "title": info.get("title", name),
                        "match_field": "title",
                    }
                )
        if limit and len(results) >= limit:
            return results[:limit]
        self._ensure_loaded()
        existing = {r["name"] for r in results}
        for t, yamls in self._yamls.items():
            if etype and t != etype:
                continue
            for name, data in yamls.items():
                if name in existing:
                    continue
                ov = (data.get("overview", "") or "").lower()
                if q in ov:
                    results.append(
                        {"name": name, "type": t, "title": data.get("title", name), "match_field": "overview"}
                    )
                    if limit and len(results) >= limit:
                        return results[:limit]
        if limit:
            results = results[:limit]
        return results

    def connections(self, name, depth=1, direction="both", limit=None):
        if not self._adj:
            return []
        visited = {name: 0}
        queue = [name]
        while queue:
            cur = queue.pop(0)
            cd = visited.get(cur, 0)
            if cd >= depth:
                continue
            for nbr in self._adj.get(cur, {}):
                if nbr not in visited:
                    visited[nbr] = cd + 1
                    queue.append(nbr)
        visited.pop(name, None)
        results = []
        for n, dist in sorted(visited.items(), key=lambda x: (x[1], x[0])):
            entry = self._cat_entry(n)
            ei = self._adj.get(name, {}).get(n) or self._adj.get(n, {}).get(name, {})
            results.append(
                {
                    "name": n,
                    "distance": dist,
                    "title": (entry or {}).get("title", n),
                    "type": (entry or {}).get("type", "?"),
                    "edge_type": ei.get("type", "general"),
                    "reasons": ei.get("reasons", []),
                }
            )
        if limit:
            results = results[:limit]
        return results

    def path(self, source, target):
        if not self._adj or source not in self._adj:
            return None
        visited, parent = {source}, {source: None}
        queue = [source]
        while queue:
            cur = queue.pop(0)
            if cur == target:
                path = []
                while cur:
                    entry = self._cat_entry(cur)
                    path.append(
                        {"name": cur, "title": (entry or {}).get("title", cur), "type": (entry or {}).get("type", "?")}
                    )
                    cur = parent[cur]
                path.reverse()
                return path
            for nbr in self._adj.get(cur, {}):
                if nbr not in visited:
                    visited.add(nbr)
                    parent[nbr] = cur
                    queue.append(nbr)
        return None

    def counts(self, by="type"):
        if by == "type":
            c = Counter()
            for info in (self._catalog or {}).values():
                c[info.get("type", "?")] += 1
            return dict(c)
        # For index-dependent queries, ensure data is available
        if not self._indices.get("protein_meta") and not self._indices.get("by_tag"):
            self._ensure_loaded()
        if by == "family":
            if self._indices.get("protein_meta"):
                fams = Counter()
                for meta in self._indices["protein_meta"].values():
                    f = meta.get("family", "Unknown").split(":")[0].strip() if meta.get("family") else "Unknown"
                    if f:
                        fams[f] += 1
                return dict(fams.most_common(20))
            return {
                f: len(ns)
                for f, ns in sorted(self._indices.get("by_family", {}).items(), key=lambda x: -len(x[1]))[:20]
            }
        elif by == "tag":
            tc = Counter()
            for t, ns in self._indices.get("by_tag", {}).items():
                tc[t] = len(ns)
            return dict(tc.most_common(30))
        elif by == "detergent":
            return {
                d: len(ps)
                for d, ps in sorted(self._indices.get("by_detergent", {}).items(), key=lambda x: -len(x[1]))[:20]
            }
        elif by == "subdir":
            return {
                s: len(ns) for s, ns in sorted(self._indices.get("by_subdir", {}).items(), key=lambda x: -len(x[1]))
            }
        elif by == "expression":
            return {
                h: len(ps)
                for h, ps in sorted(self._indices.get("by_expression", {}).items(), key=lambda x: -len(x[1]))[:15]
            }
        return {}

    def resolution_stats(self, family=None):
        if self._indices.get("protein_meta"):
            by_family = defaultdict(list)
            for name, meta in self._indices["protein_meta"].items():
                fam = meta.get("family", "Unknown").split(":")[0].strip() if meta.get("family") else "Unknown"
                if family and family.lower() not in fam.lower():
                    continue
                res_list = self._indices.get("by_resolution", {}).get(name, [])
                if res_list:
                    by_family[fam].extend(res_list)
            results = []
            for fam, vals in sorted(by_family.items(), key=lambda x: -len(x[1])):
                vals.sort()
                results.append(
                    {
                        "family": fam,
                        "count": len(vals),
                        "min": round(vals[0], 2),
                        "max": round(vals[-1], 2),
                        "median": round(vals[len(vals) // 2], 2),
                        "mean": round(sum(vals) / len(vals), 2),
                    }
                )
            return results

        self._ensure_loaded()
        by_family = defaultdict(list)
        for name, res_list in self._indices.get("by_resolution", {}).items():
            data = self._yamls.get("proteins", {}).get(name, {})
            m = data.get("mpstruc_classification", {})
            fam = m.get("subgroup", "").split(":")[0].strip() if m else "Unknown"
            if family and family.lower() not in fam.lower():
                continue
            by_family[fam].extend(res_list)
        results = []
        for fam, vals in sorted(by_family.items(), key=lambda x: -len(x[1])):
            vals.sort()
            results.append(
                {
                    "family": fam,
                    "count": len(vals),
                    "min": round(vals[0], 2),
                    "max": round(vals[-1], 2),
                    "median": round(vals[len(vals) // 2], 2),
                    "mean": round(sum(vals) / len(vals), 2),
                }
            )
        return results

    def stats(self):
        c = Counter()
        for info in (self._catalog or {}).values():
            c[info.get("type", "?")] += 1
        return {
            "total_entities": len(self._catalog or {}),
            "by_type": dict(c),
            "total_cross_ref_edges": len(self._graph.get("edges", [])),
            "graph_nodes": len(self._graph.get("nodes", [])),
            "note": "Use 'proteins --limit N' or 'reagents --limit N' for deeper stats (loads YAMLs)",
        }

    def suggest(self, name=None, tags=None, family=None, etype=None, limit=15):
        """Suggest cross-references for an entity based on graph analysis.

        Mode A (entity in graph): Return ranked neighbors.
        Mode B (new entity): Aggregate connections of similar entities by tags/family.
        """
        candidates = Counter()

        if name and self._adj and name in self._adj:
            # Mode A: entity already in graph
            for nbr, info in self._adj[name].items():
                entry = self._cat_entry(nbr) or {}
                candidates[nbr] = info.get("weight", 1) * (1 + 0.5 * (entry.get("type") != "proteins"))

        elif family or tags:
            # Mode B: find similar entities and aggregate their connections
            similar = []
            fam_lower = family.lower() if family else ""
            # Common family abbreviations
            fam_aliases = {
                "gpcr": "g protein-coupled receptor",
                "abc": "abc transporter",
                "mfs": "major facilitator",
                "slc": "solute carrier",
            }
            fam_patterns = [fam_lower]
            for abbr, full in fam_aliases.items():
                if abbr in fam_lower or fam_lower in abbr:
                    fam_patterns.append(full)
            if family:
                if self._indices.get("protein_meta"):
                    for ent, meta in self._indices["protein_meta"].items():
                        mf = (meta.get("family", "") or "").lower()
                        if any(p in mf for p in fam_patterns):
                            similar.append(ent)
                else:
                    for ent, info in (self._catalog or {}).items():
                        if info.get("type") != "proteins":
                            continue
                        if self._adj and ent in self._adj:
                            for nbr, einfo in self._adj[ent].items():
                                if einfo.get("type") in ("homolog", "family") or any(
                                    p in str(einfo.get("reasons", "")).lower() for p in fam_patterns
                                ):
                                    similar.append(ent)
                                    break
            # Also match by tag when family is an abbreviation
            if tags:
                for t in [t.strip() for t in tags.split(",")]:
                    similar.extend(self._indices.get("by_tag", {}).get(t, []))
            elif family and not tags:
                # Try matching the family abbreviation as a tag
                if fam_lower in ("gpcr", "abc", "mfs", "slc"):
                    similar.extend(self._indices.get("by_tag", {}).get(fam_lower, []))

            # Aggregate connections from similar entities
            if self._adj:
                for s in set(similar):
                    for nbr, info in self._adj.get(s, {}).items():
                        if nbr != name:
                            candidates[nbr] += info.get("weight", 1)

        # Remove self and boost relevant types
        if name:
            candidates.pop(name, None)

        # Rank and return
        results = []
        for ent, score in candidates.most_common(limit * 2):
            entry = self._cat_entry(ent) or {}
            etype_label = entry.get("type", "?").replace("proteins", "protein").replace("reagents", "reagent")
            # Build reason from edge type or catalog info
            reason = f"Related {etype_label}"
            if self._adj and name and ent in self._adj.get(name, {}):
                ei = self._adj[name][ent]
                if ei.get("reasons"):
                    reason = ei["reasons"][0][:80]
                elif ei.get("type") != "general":
                    reason = f"Edge type: {ei['type']}"
            results.append(
                {
                    "name": ent,
                    "type": etype_label,
                    "title": entry.get("title", ent),
                    "score": round(score, 2),
                    "reason": reason,
                }
            )
            if len(results) >= limit:
                break

        return results

    # ─── Output ───

    @staticmethod
    def render(data, fmt="json"):
        if fmt == "json":
            return json.dumps(data, indent=2, default=str)
        elif fmt == "table":
            return WikiQuery._table(data)
        elif fmt == "csv":
            return WikiQuery._csv(data)
        return str(data)

    @staticmethod
    def _table(data):
        if not data:
            return "(empty)"
        if isinstance(data, dict):
            if any(k in data for k in ("family", "best_resolution", "pdb_count")):
                data = [data]
            else:
                return "\n".join(f"  {k}: {v}" for k, v in data.items())
        if not isinstance(data, list) or not data:
            return str(data)
        keys = [k for k in data[0].keys() if k not in ("tags", "reasons")]
        cw = {}
        for k in keys:
            cw[k] = max(len(k), min(max(len(str(r.get(k, ""))) for r in data), 40))
        sep = "+" + "+".join("-" * (cw[k] + 2) for k in keys) + "+"
        head = "|" + "|".join(f" {k:<{cw[k]}} " for k in keys) + "|"
        body = []
        for row in data:
            body.append("|" + "|".join(f" {str(row.get(k, '')): <{cw[k]}} " for k in keys)[: cw[k] + 2] + "|")
        return "\n".join([sep, head, sep.replace("-", "=")] + body + [sep])

    @staticmethod
    def _csv(data):
        if not data:
            return ""
        if isinstance(data, dict):
            data = [data]
        if not isinstance(data, list):
            return str(data)
        keys = list(data[0].keys())
        lines = [",".join(keys)]
        for row in data:
            lines.append(",".join(f'"{str(row.get(k, "")).replace(chr(34), chr(34) + chr(34))}"' for k in keys))
        return "\n".join(lines)


# ─── CLI ───


def _add_format(parser):
    parser.add_argument("--format", choices=["json", "table", "csv"], default="json", help="Output format")


def main():
    p = argparse.ArgumentParser(
        description="xray-mp-wiki query tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              wiki_query.py entities --type protein --limit 5
              wiki_query.py proteins --tag gpcr --limit 10 --format table
              wiki_query.py proteins --detergent ddm --limit 5
              wiki_query.py reagents --subdir detergents --cmc-max 1.0 --has-property cmc
              wiki_query.py search adenosine --limit 5
              wiki_query.py connections ddm --depth 2
              wiki_query.py path ddm kcsa
              wiki_query.py stats --format table
              wiki_query.py resolution-stats
              wiki_query.py counts --by family
        """),
    )
    sub = p.add_subparsers(dest="command")

    for name, help_text in [
        ("entities", "List entities"),
        ("get", "Get single entity"),
        ("proteins", "Query proteins"),
        ("reagents", "Query reagents"),
        ("methods", "Query methods"),
        ("concepts", "Query concepts"),
        ("search", "Full-text search"),
        ("connections", "Graph connections"),
        ("path", "Shortest path"),
        ("counts", "Count entities"),
        ("resolution-stats", "Resolution statistics"),
        ("stats", "Wiki summary"),
        ("rebuild", "Rebuild precomputed index from YAMLs (~30s)"),
        ("suggest", "Suggest cross-references from knowledge graph"),
    ]:
        sp = sub.add_parser(name, help=help_text)
        _add_format(sp)

    # Per-command args
    sub.choices["entities"].add_argument("--type", choices=["proteins", "reagents", "methods", "concepts"])
    sub.choices["entities"].add_argument("--tag")
    sub.choices["entities"].add_argument("--subdir")
    sub.choices["entities"].add_argument("--limit", type=int)
    sub.choices["entities"].add_argument("--offset", type=int, default=0)
    sub.choices["entities"].add_argument("--sort", choices=["name", "title"])

    sub.choices["get"].add_argument("name")
    sub.choices["get"].add_argument("--full", action="store_true", help="Load YAML for full details")

    sub.choices["proteins"].add_argument("--family")
    sub.choices["proteins"].add_argument("--detergent")
    sub.choices["proteins"].add_argument("--resolution-max", type=float)
    sub.choices["proteins"].add_argument("--expression")
    sub.choices["proteins"].add_argument("--pdb")
    sub.choices["proteins"].add_argument("--tag")
    sub.choices["proteins"].add_argument("--limit", type=int)

    sub.choices["reagents"].add_argument("--subdir")
    sub.choices["reagents"].add_argument("--cmc-max", type=float)
    sub.choices["reagents"].add_argument("--cmc-min", type=float)
    sub.choices["reagents"].add_argument("--mw-max", type=float)
    sub.choices["reagents"].add_argument("--mw-min", type=float)
    sub.choices["reagents"].add_argument("--tag")
    sub.choices["reagents"].add_argument("--has-property")
    sub.choices["reagents"].add_argument("--limit", type=int)

    sub.choices["methods"].add_argument("--tag")
    sub.choices["methods"].add_argument("--limit", type=int)
    sub.choices["concepts"].add_argument("--tag")
    sub.choices["concepts"].add_argument("--limit", type=int)

    sub.choices["search"].add_argument("query")
    sub.choices["search"].add_argument("--type", choices=["proteins", "reagents", "methods", "concepts"])
    sub.choices["search"].add_argument("--limit", type=int)

    sub.choices["connections"].add_argument("name")
    sub.choices["connections"].add_argument("--depth", type=int, default=1)
    sub.choices["connections"].add_argument("--direction", choices=["both", "out", "in"], default="both")
    sub.choices["connections"].add_argument("--limit", type=int)

    sub.choices["path"].add_argument("source")
    sub.choices["path"].add_argument("target")
    sub.choices["counts"].add_argument(
        "--by", choices=["type", "family", "tag", "detergent", "subdir", "expression"], default="type"
    )
    sub.choices["resolution-stats"].add_argument("--family")

    sub.choices["suggest"].add_argument("name", nargs="?", help="Entity name (omit for tag/family-based suggestions)")
    sub.choices["suggest"].add_argument(
        "--tags", help="Comma-separated tags for new entity (e.g., 'gpcr,membrane-protein')"
    )
    sub.choices["suggest"].add_argument("--family", help="Protein family for new entity (e.g., 'GPCR')")
    sub.choices["suggest"].add_argument("--limit", type=int, default=15)

    args = p.parse_args()
    if not args.command:
        p.print_help()
        sys.exit(1)

    q = WikiQuery()
    fmt = args.format

    if args.command == "get":
        result = q.get(args.name)
        if result is None:
            print(f"Not found: {args.name}", file=sys.stderr)
            sys.exit(1)
        out = result
    elif args.command == "entities":
        result = q.entities(
            etype=args.type, tag=args.tag, subdir=args.subdir, limit=args.limit, offset=args.offset, sort=args.sort
        )
        out = {"query": "entities", "count": len(result), "results": result}
    elif args.command == "proteins":
        result = q.proteins(
            family=args.family,
            detergent=args.detergent,
            resolution_max=args.resolution_max,
            expression=args.expression,
            pdb=args.pdb,
            tag=args.tag,
            limit=args.limit,
        )
        out = {"query": "proteins", "count": len(result), "results": result}
    elif args.command == "reagents":
        result = q.reagents(
            subdir=args.subdir,
            cmc_max=args.cmc_max,
            cmc_min=args.cmc_min,
            mw_max=args.mw_max,
            mw_min=args.mw_min,
            tag=args.tag,
            has_property=args.has_property,
            limit=args.limit,
        )
        out = {"query": "reagents", "count": len(result), "results": result}
    elif args.command == "methods":
        result = q.methods(tag=args.tag, limit=args.limit)
        out = {"query": "methods", "count": len(result), "results": result}
    elif args.command == "concepts":
        result = q.concepts(tag=args.tag, limit=args.limit)
        out = {"query": "concepts", "count": len(result), "results": result}
    elif args.command == "search":
        result = q.search(args.query, etype=args.type, limit=args.limit)
        out = {"query": args.query, "count": len(result), "results": result}
    elif args.command == "connections":
        result = q.connections(args.name, depth=args.depth, direction=args.direction, limit=args.limit)
        out = {"query": f"connections({args.name})", "count": len(result), "results": result}
    elif args.command == "path":
        result = q.path(args.source, args.target)
        if result is None:
            print("No path found", file=sys.stderr)
            sys.exit(1)
        if fmt == "table":
            print(q.render(result, "table"))
            return
        out = {"query": f"path({args.source}→{args.target})", "hops": len(result) - 1, "path": result}
    elif args.command == "counts":
        result = q.counts(by=args.by)
        out = {"query": f"counts(by={args.by})", "counts": result}
    elif args.command == "resolution-stats":
        result = q.resolution_stats(family=args.family)
        out = {"query": "resolution-stats", "results": result}
    elif args.command == "stats":
        out = q.stats()
    elif args.command == "suggest":
        if not args.name and not args.tags and not args.family:
            print("suggest requires a name, --tags, or --family", file=sys.stderr)
            sys.exit(1)
        result = q.suggest(name=args.name, tags=args.tags, family=args.family, limit=args.limit)
        out = {
            "query": f"suggest({args.name or 'tags=' + (args.tags or '') + ' family=' + (args.family or '')})",
            "count": len(result),
            "results": result,
        }
    elif args.command == "rebuild":
        q = WikiQuery(rebuild=True)
        idx_size = len(json.dumps(q._indices, default=str))
        print(
            json.dumps({"status": "rebuilt", "index_bytes": idx_size, "entity_count": len(q._catalog or {})}, indent=2)
        )
        return
    else:
        p.print_help()
        sys.exit(1)

    print(q.render(out, fmt))


if __name__ == "__main__":
    main()
