#!/usr/bin/env python3
"""
rebuild_graph.py — Build wiki knowledge graph from YAML files.

Output:
  xray-mp-wiki/assets/graph.json — node/edge data for Cytoscape.js
  xray-mp-wiki/assets/graph-hubs.png — static PNG of top-100 hubs

Run after any batch of YAML changes to keep the graph in sync.

Usage:
  python3 scripts/rebuild_graph.py
  python3 scripts/rebuild_graph.py --image-only   # skip JSON, update PNG
  python3 scripts/rebuild_graph.py --png   # generate high-res PNG
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from scripts._base import fast_load_str

BASE = Path(__file__).resolve().parent.parent
W = BASE / "xray-mp-wiki"


def parse_sources(data):
    src = data.get("sources", []) or []
    if isinstance(src, str):
        src = [src]
    return sum(1 for s in src if isinstance(s, str))


def parse_structures(data):
    structs = data.get("structures", []) or []
    return sum(1 for s in structs if isinstance(s, dict) and s.get("pdb_id", "") not in (None, "", "--"))


def parse_insights(data):
    return len(data.get("biological_insights", []) or [])


def main():
    nodes = {}
    edge_reasons = defaultdict(list)
    node_degree = Counter()

    for yaml_dir, etype in [
        ("proteins_yaml", "proteins"),
        ("reagents_yaml", "reagents"),
        ("concepts_yaml", "concepts"),
        ("methods_yaml", "methods"),
    ]:
        for yf in sorted((W / yaml_dir).rglob("*.yaml")):
            try:
                data = fast_load_str(yf.read_text())
            except Exception:
                continue
            if not isinstance(data, dict):
                continue

            name = yf.stem
            title = data.get("title", name)[:80]
            mp = data.get("mpstruc_classification", {}) or {}
            subgroup = mp.get("subgroup", "")[:60] if isinstance(mp, dict) else ""
            tags = data.get("tags", []) or []
            if isinstance(tags, str):
                tags = [tags]

            nodes[name] = {
                "id": name,
                "type": etype,
                "title": title,
                "subgroup": subgroup,
                "tags": tags[:10],
                "sources": parse_sources(data),
                "pdbs": parse_structures(data),
                "insights": parse_insights(data),
            }

            xrefs = data.get("cross_references", []) or []
            for xr in xrefs:
                path = xr.get("path", "")
                target = path.rstrip("/").split("/")[-1] if path else ""
                if target and target != name:
                    reason = xr.get("reason", "related")[:60]
                    edge_reasons[(name, target)].append(reason)

    # Degree
    for (s, t), _ in edge_reasons.items():
        if s in nodes:
            node_degree[s] += 1
        if t in nodes:
            node_degree[t] += 1

    max_deg = max(node_degree.values()) if node_degree else 1
    for nid, node in nodes.items():
        deg = node_degree.get(nid, 0)
        node["degree"] = deg
        node["importance"] = round(
            (deg / max_deg) * 0.4
            + min(node["sources"] / 20, 1) * 0.25
            + min(node["pdbs"] / 10, 1) * 0.2
            + min(node["insights"] / 15, 1) * 0.15,
            3,
        )
        node["radius"] = max(5, min(30, 5 + int(node["importance"] * 35)))

    # Edges
    edges = []
    for (src, tgt), reasons in edge_reasons.items():
        if src not in nodes or tgt not in nodes:
            continue
        rt = " ".join(reasons).lower()
        if any(w in rt for w in ["homolog", "ortholog", "paralog", "identity", "similar", "sequence"]):
            etype, base_w = "homolog", 5
        elif any(w in rt for w in ["detergent", "ligand", "buffer", "lipid", "additive", "reagent"]):
            etype, base_w = "reagent", 4
        elif any(w in rt for w in ["family", "member", "subfamily", "subgroup"]):
            etype, base_w = "family", 3
        elif any(w in rt for w in ["method", "technique", "protocol"]):
            etype, base_w = "method", 2
        elif any(w in rt for w in ["concept", "mechanism", "principle"]):
            etype, base_w = "concept", 2
        else:
            etype, base_w = "general", 1

        mult = min(len(reasons), 5)
        bi = (tgt, src) in edge_reasons
        weight = base_w * (1 + mult * 0.15) * (1.5 if bi else 1.0)

        edges.append(
            {
                "source": src,
                "target": tgt,
                "type": etype,
                "reasons": reasons[:3],
                "weight": round(weight, 1),
                "multiplicity": mult,
                "bidirectional": bi,
            }
        )

    max_w = max(e["weight"] for e in edges) if edges else 1
    for e in edges:
        e["opacity"] = round(max(0.05, min(1.0, e["weight"] / max_w * 0.9 + 0.1)), 2)

    # ponytail: trim low-importance nodes — full graph is 2.8MB, too slow
    # upgrade: remove filter when server-side pagination/level-of-detail is added
    IMPORTANCE_MIN = 0.07
    filtered_ids = {n["id"] for n in nodes.values() if n["importance"] >= IMPORTANCE_MIN}
    nodes = {k: v for k, v in nodes.items() if k in filtered_ids}
    edges = [e for e in edges if e["source"] in filtered_ids and e["target"] in filtered_ids]

    graph = {
        "meta": {"total_nodes": len(nodes), "total_edges": len(edges)},
        "nodes": sorted(nodes.values(), key=lambda n: -n["importance"]),
        "edges": edges,
    }

    out_path = W / "assets" / "graph.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(graph, indent=2))
    print(f"Graph: {len(nodes)} nodes, {len(edges)} edges → {out_path}")

    # Static PNG (top 100 hubs)
    if "--image-only" not in sys.argv:
        _render_png(graph, W / "assets" / "graph-hubs.png")


def _render_png(graph, out_path):
    """Render a static PNG of the top-100 hub nodes."""
    try:
        import matplotlib
        import networkx as nx

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  Skipping PNG (networkx/matplotlib not available)")
        return

    top = graph["nodes"][:100]
    top_ids = {n["id"] for n in top}
    edges = [e for e in graph["edges"] if e["source"] in top_ids and e["target"] in top_ids]

    NXG = nx.Graph()
    for n in top:
        NXG.add_node(n["id"])
    for e in edges:
        NXG.add_edge(e["source"], e["target"])

    pos = nx.spring_layout(NXG, k=2.5, iterations=80, seed=42)

    fig, ax = plt.subplots(1, 1, figsize=(24, 20))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#1a1a2e")

    tc = {"proteins": "#4e79a7", "reagents": "#f28e2b", "concepts": "#59a14f", "methods": "#e15759"}
    ec = {
        "homolog": "#4e79a7",
        "reagent": "#f28e2b",
        "method": "#e15759",
        "concept": "#59a14f",
        "family": "#af7aa1",
        "general": "#555555",
    }

    for e in sorted(edges, key=lambda x: x["weight"]):
        if e["source"] not in pos or e["target"] not in pos:
            continue
        x1, y1 = pos[e["source"]]
        x2, y2 = pos[e["target"]]
        ax.plot(
            [x1, x2],
            [y1, y2],
            color=ec.get(e["type"], "#555"),
            alpha=max(0.08, min(0.8, e["opacity"] * 0.8)),
            linewidth=max(0.5, min(4, e["weight"] / 3)),
            zorder=1,
        )

    for n in top:
        if n["id"] not in pos:
            continue
        x, y = pos[n["id"]]
        r = max(4, min(35, n["radius"]))
        c = tc.get(n["type"], "#888")
        if n["importance"] > 0.5:
            ax.scatter(x, y, s=(r * 3) ** 2, c=c, alpha=0.12, zorder=2, edgecolors="none")
        ax.scatter(x, y, s=r**2, c=c, alpha=0.85, zorder=3, edgecolors="white", linewidth=0.5)
        if n["importance"] > 0.4 or n["degree"] > 10:
            ax.annotate(
                n["title"][:35],
                (x, y),
                fontsize=6,
                ha="center",
                va="bottom",
                color="white",
                alpha=0.9,
                zorder=4,
                bbox=dict(boxstyle="round,pad=0.1", fc="#1a1a2e", ec="none", alpha=0.7),
            )

    ax.set_title(
        "X-ray MP Wiki — Knowledge Graph (Top 100 Entities)", fontsize=18, color="white", pad=20, fontweight="bold"
    )
    sub = f"{graph['meta']['total_nodes']} entities · {graph['meta']['total_edges']} connections · Hubs sized by importance"
    ax.text(0.5, 0.97, sub, transform=ax.transAxes, fontsize=10, color="#888888", ha="center", va="top")
    for i, (t, c) in enumerate(tc.items()):
        ax.plot([0.02], [0.92 - i * 0.025], "o", color=c, markersize=10, transform=ax.transAxes, clip_on=False)
        ax.text(0.035, 0.92 - i * 0.025, t.capitalize(), color="white", fontsize=9, transform=ax.transAxes, va="center")

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.axis("off")
    fig.savefig(str(out_path), dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print(f"  PNG: {out_path}")


if __name__ == "__main__":
    main()
