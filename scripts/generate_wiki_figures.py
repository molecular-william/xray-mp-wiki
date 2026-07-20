"""Generate insight figures from aggregate_stats.json.

Usage: python3 scripts/generate_wiki_figures.py

Output: xray-mp-wiki/assets/fig-*.png
"""

import json
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DATA = Path("references/stats/aggregate_stats.json")
OUT = Path("xray-mp-wiki/assets")
OUT.mkdir(parents=True, exist_ok=True)

with open(DATA) as f:
    D = json.load(f)

# ponytail: helper shared by detergent + buffer heatmaps
_SHORT_FAM = {
    "g protein coupled receptors: class a": "GPCR Class A",
    "channels: potassium, sodium, & proton ion selective": "K/Na/H channels",
    "atp binding cassette (abc) transporters": "ABC transporters",
    "bacterial, algal, viral, and unusual rhodopsins": "Rhodopsins",
    "major facilitator superfamily (mfs) transporters": "MFS transporters",
    "multi drug efflux transporters": "MDR efflux",
    "solute carrier (slc) transporter superfamily": "SLC transporters",
    "channels: other ion channels": "Other ion channels",
    "channels: aquaporins and glyceroporins": "Aquaporins",
    "f type atpase": "F-type ATPase",
    "intramembrane proteases": "Intramembrane proteases",
    "oxidoreductases": "Oxidoreductases",
    "sec, translocase, and insertase proteins": "Sec/translocase",
    "p type atpase": "P-type ATPase",
    "cys loop receptor family": "Cys-loop receptors",
}


def _heatmap(data, row_labels, col_labels, xlabel, ylabel, title, cbar_label, out_name, figsize=(8, 7)):
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(data, aspect="auto", cmap="YlOrRd")
    ax.set_xticks(range(len(col_labels)))
    ax.set_xticklabels(col_labels, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(len(row_labels)))
    ax.set_yticklabels(row_labels, fontsize=7)
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_title(title, fontsize=10, fontweight="bold")
    fig.colorbar(im, ax=ax, label=cbar_label, shrink=0.7)
    fig.tight_layout()
    path = OUT / out_name
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved {path}")


# ── Figure 1: Detergent × Family heatmap ──────────────────────────
def fig_detergent_heatmap():
    matrix = D["detergent_matrix"]
    # Top 15 families by protein count
    families = sorted(D["family_coverage"], key=D["family_coverage"].get, reverse=True)[:15]
    # Top 10 detergents across these families
    det_totals = {}
    for fam in families:
        for det, cnt in matrix.get(fam, {}).items():
            det_totals[det] = det_totals.get(det, 0) + cnt
    detergents = sorted(det_totals, key=det_totals.get, reverse=True)[:10]

    data = np.zeros((len(families), len(detergents)))
    for i, fam in enumerate(families):
        n_proteins = D["family_coverage"].get(fam, 1)
        for j, det in enumerate(detergents):
            data[i, j] = matrix.get(fam, {}).get(det, 0) / n_proteins

    # Shorten long family names
    short = {
        "g protein coupled receptors: class a": "GPCR Class A",
        "channels: potassium, sodium, & proton ion selective": "K/Na/H channels",
        "atp binding cassette (abc) transporters": "ABC transporters",
        "bacterial, algal, viral, and unusual rhodopsins": "Rhodopsins",
        "major facilitator superfamily (mfs) transporters": "MFS transporters",
        "multi drug efflux transporters": "MDR efflux",
        "solute carrier (slc) transporter superfamily": "SLC transporters",
        "channels: other ion channels": "Other ion channels",
        "channels: aquaporins and glyceroporins": "Aquaporins",
        "f type atpase": "F-type ATPase",
        "intramembrane proteases": "Intramembrane proteases",
        "oxidoreductases": "Oxidoreductases",
        "sec, translocase, and insertase proteins": "Sec/translocase",
        "p type atpase": "P-type ATPase",
        "cys loop receptor family": "Cys-loop receptors",
    }

    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(data, aspect="auto", cmap="YlOrRd")
    ax.set_xticks(range(len(detergents)))
    ax.set_xticklabels(detergents, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(len(families)))
    ax.set_yticklabels([short.get(f, f[:30]) for f in families], fontsize=7)
    ax.set_xlabel("Detergent", fontsize=9)
    ax.set_ylabel("Protein family", fontsize=9)
    ax.set_title("Detergent preference by family (mentions per protein)", fontsize=10, fontweight="bold")
    fig.colorbar(im, ax=ax, label="Mentions per protein", shrink=0.7)
    fig.tight_layout()
    path = OUT / "fig-detergent-heatmap.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved {path}")


# ── Figure 5: Buffer composition × Family heatmap ──────────────────
def fig_buffer_heatmap():
    """Count buffer reagent mentions per family from YAML buffer_details."""
    import yaml

    W = Path("xray-mp-wiki")
    buf_fam = Counter()
    fam_counter = Counter()
    yf_list = sorted((W / "proteins_yaml").glob("*.yaml"))
    # ponytail: slug → label for known buffer reagents
    _SHORT_BUF = {
        "tris": "Tris",
        "hepes": "HEPES",
        "mes": "MES",
        "mops": "MOPS",
        "sodium-citrate": "Na-citrate",
        "sodium-phosphate": "Na-phosphate",
        "bis-tris": "Bis-Tris",
        "caps": "CAPS",
        "pbs": "PBS",
        "tbs": "TBS",
        "potassium-phosphate": "K-phosphate",
        "imidazole": "Imidazole",
        "citrate": "Citrate",
        "tricine": "Tricine",
        "acetate": "Acetate",
        "sodium-acetate": "Na-acetate",
        "bicine": "Bicine",
        "glycine": "Glycine",
        "hbs": "HBS",
    }
    for yf in yf_list:
        try:
            data = yaml.safe_load(yf.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        # ponytail: family from mpstruc_classification.subgroup (matches aggregate_stats.py)
        fam = data.get("mpstruc_classification", {}).get("subgroup", "")
        fam = fam.lower().replace("-", " ").strip() if fam else ""
        if not fam or fam == "unknown":
            continue
        purif_sources = list(data.get("purifications", []) or [])
        for pub in data.get("publications", []) or []:
            if isinstance(pub, dict):
                purif_sources.extend(pub.get("purifications", []) or [])
        # Count proteins per family once
        fam_counter[fam] += 1
        bufs_seen = set()
        for p in purif_sources:
            if not isinstance(p, dict):
                continue
            for s in p.get("steps", []) or []:
                if not isinstance(s, dict):
                    continue
                for comp in s.get("buffer_details", []) or []:
                    if not isinstance(comp, dict):
                        continue
                    r = comp.get("reagent", "") or ""
                    if "/buffers/" not in r:
                        continue
                    slug = r.rstrip("/").rsplit("/", 1)[-1]
                    if slug not in bufs_seen:
                        bufs_seen.add(slug)
                        buf_fam[(fam, slug)] += 1

    # Build matrix: top 10 buffers, top 15 families
    buf_totals = Counter()
    for (fam, slug), cnt in buf_fam.items():
        buf_totals[slug] += cnt
    top_bufs = [s for s, _ in buf_totals.most_common(10)]
    top_fams = sorted(fam_counter, key=fam_counter.get, reverse=True)[:15]

    data = np.zeros((len(top_fams), len(top_bufs)))
    for i, fam in enumerate(top_fams):
        n = fam_counter.get(fam, 1)
        for j, slug in enumerate(top_bufs):
            data[i, j] = buf_fam.get((fam, slug), 0) / n

    _heatmap(
        data,
        row_labels=[_SHORT_FAM.get(f, f[:30]) for f in top_fams],
        col_labels=[_SHORT_BUF.get(s, s) for s in top_bufs],
        xlabel="Buffer",
        ylabel="Protein family",
        title="Buffer composition preference by family",
        cbar_label="Mentions per protein",
        out_name="fig-buffer-heatmap.png",
        figsize=(7, 7),
    )


# ── Figure 2: Expression system bar ─────────────────────────────────
def fig_expression_systems():
    expr = D["expression_systems"]
    labels = list(expr.keys())
    values = list(expr.values())
    short = {
        "e-coli": "E. coli",
        "sf9": "Sf9",
        "native-tissue": "Native",
        "pichia-pastoris": "P. pastoris",
        "hek293": "HEK293",
        "not-specified": "Unspecified",
        "other-bacterial": "Other bacteria",
        "saccharomyces-cerevisiae": "S. cerevisiae",
        "other-eukaryotic": "Other euk.",
        "hi5": "Hi5",
        "cell-free": "Cell-free",
        "lexsy": "LEXSY",
    }
    colors = plt.cm.tab20(np.linspace(0, 1, len(labels)))

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.barh(range(len(labels)), values, color=colors, edgecolor="white")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels([short.get(label, label) for label in labels], fontsize=8)
    ax.set_xlabel("Proteins", fontsize=9)
    ax.set_title("Expression systems in membrane protein structures", fontsize=10, fontweight="bold")
    for bar, v in zip(bars, values):
        ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height() / 2, str(v), va="center", fontsize=7)
    ax.margins(x=0.15)
    fig.tight_layout()
    path = OUT / "fig-expression-systems.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved {path}")


# ── Figure 3: Top detergent exchange patterns ──────────────────────
def fig_exchange_patterns():
    ex = D.get("exchanges", [])
    if not ex:
        print("  No exchange data")
        return
    from collections import Counter

    pattern_counts = Counter()
    for name, fam, chain in ex:
        # Normalize to a pattern key
        key = " → ".join(chain)
        pattern_counts[key] += 1

    top = pattern_counts.most_common(8)
    if not top:
        print("  No exchange patterns")
        return

    labels = [t[0] for t in top]
    values = [t[1] for t in top]

    fig, ax = plt.subplots(figsize=(8, 3.5))
    bars = ax.barh(range(len(labels)), values, color="steelblue", edgecolor="white")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=7)
    ax.set_xlabel("Proteins", fontsize=9)
    ax.set_title("Top detergent exchange patterns", fontsize=10, fontweight="bold")
    for bar, v in zip(bars, values):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2, str(v), va="center", fontsize=8)
    ax.margins(x=0.15)
    fig.tight_layout()
    path = OUT / "fig-exchange-patterns.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved {path}")


# ── Figure 4: Resolution by step type ──────────────────────────────
def fig_resolution_by_step():
    step = D["resolution_by_step_type"]
    # Filter to step types with n >= 20
    items = [(k, v) for k, v in step.items() if v["n"] >= 20]
    items.sort(key=lambda x: x[1]["n"], reverse=True)

    labels = [it[0].replace("_", " ").title() for it in items]
    means = [it[1]["mean"] for it in items]

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.barh(range(len(labels)), means, color="darkorange", edgecolor="white")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Mean resolution (Å)", fontsize=9)
    ax.set_title("Resolution by step-type presence", fontsize=10, fontweight="bold")
    ax.invert_xaxis()  # lower = better = on top
    for bar, v in zip(bars, means):
        n = [it[1]["n"] for it in items][bars.index(bar)]
        ax.text(
            bar.get_width() + 0.02, bar.get_y() + bar.get_height() / 2, f"{v:.2f}Å (n={n})", va="center", fontsize=7
        )
    ax.margins(x=0.2)
    fig.tight_layout()
    path = OUT / "fig-resolution-by-step.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved {path}")


if __name__ == "__main__":
    print("Generating insight figures…")
    fig_detergent_heatmap()
    fig_buffer_heatmap()
    fig_expression_systems()
    fig_exchange_patterns()
    fig_resolution_by_step()
    print("Done.")
