#!/usr/bin/env python3
"""
Aggregate statistics from existing structured wiki data.

Computes: resolution by family, detergent usage matrix, detergent concentration
ranges, step-type pipeline profiles, detergent exchange prevalence, expression
system distribution, and expression×resolution correlation.

Output: structured report to stdout, plus JSON at references/stats/ for
reuse in visualisations.
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from scripts._base import fast_load_str

BASE = Path(__file__).resolve().parent.parent.parent
W = BASE / "xray-mp-wiki"
OUT = BASE / "references" / "stats"
OUT.mkdir(exist_ok=True)

# ── Helpers ──────────────────────────────────────────────────────────

LINK_EXTRACT = re.compile(r"\[([^\]]+)\]\([^)]+/reagents/detergents/([^/)]+)/?\)")
CONC_PATTERN = re.compile(r"([\d.]+)\s*(%\s*\(w/v\)|%|mM|μM|mM|M|m?M)\s*")

# Build auto-detergent name map from YAML directory
DETERGENT_NAME_MAP = {}  # lowercase name/alias → slug
DETERGENT_SLUGS = set()  # all known detergent slugs

rd = BASE / "xray-mp-wiki" / "reagents_yaml"
for yf in rd.glob("*.yaml"):
    slug = yf.stem
    try:
        data = fast_load_str(yf.read_text())
        if not isinstance(data, dict):
            continue
        tags = data.get("tags", []) or []
        if not any("detergent" in (t or "") for t in tags):
            continue
        title = data.get("title", slug)
        DETERGENT_SLUGS.add(slug)
        # Index full title (lowercased)
        DETERGENT_NAME_MAP[title.lower().strip()] = slug
        # Index parenthetical abbreviations: "n-Dodecyl (DDM)" → ddm
        m = re.search(r"\(([^)]+)\)", title)
        if m:
            abbr = m.group(1).strip().lower()
            # Only index if not colliding with an existing slug key
            if abbr and abbr != slug and abbr not in DETERGENT_SLUGS:
                DETERGENT_NAME_MAP[abbr] = slug
        # Index the slug itself as a fallback (highest priority)
        DETERGENT_NAME_MAP[slug.lower()] = slug
    except Exception:
        continue


def split_detergent_text(raw):
    """Split compound detergent field like '0.5% DDM/0.1% CHS' into parts."""
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", str(raw))  # strip wikilinks
    parts = re.split(r"\s*[/+;]\s*", text)
    result = []
    for p in parts:
        p = p.strip()
        if p:
            result.append(p)
    return result


def resolve_detergent_slug(part):
    """Try to resolve a raw detergent string fragment to a slug."""
    p = part.lower().strip()
    # Direct name map lookup
    if p in DETERGENT_NAME_MAP:
        result = DETERGENT_NAME_MAP[p]
        return result
    # Remove concentration prefix: "0.5% ddm" → "ddm"
    p_clean = re.sub(r"^[\d.,\s%μµm/()w/v]+", "", p).strip()
    if p_clean and p_clean in DETERGENT_NAME_MAP:
        result = DETERGENT_NAME_MAP[p_clean]
        return result
    # Try stripping common suffixes
    for suffix in ["(w/v)", "w/v", "anatrace", "anagrade"]:
        p_clean = p.replace(suffix, "").strip()
        if p_clean and p_clean in DETERGENT_NAME_MAP:
            result = DETERGENT_NAME_MAP[p_clean]
            return result
    # Check if the part itself is in slug set (e.g. raw "ddm")
    if p in DETERGENT_SLUGS:
        return p
    # Fuzzy: check if any known name contains this fragment
    if len(p) < 2:
        return None
    for name, slug in DETERGENT_NAME_MAP.items():
        if p in name or name in p:
            return slug
    return None


def extract_detergent(step):
    """Return [(detergent_slug, conc_val, conc_unit), ...] or []."""
    raw = step.get("detergent", "") or ""
    if isinstance(raw, list):
        det_text = " ".join(str(x) for x in raw)
    else:
        det_text = str(raw)
    if not det_text.strip():
        return []

    # Primary path: extract wikilinks directly
    results = []
    seen_slugs = set()
    for m in LINK_EXTRACT.finditer(det_text):
        slug = m.group(2).lower().strip()
        if slug not in seen_slugs:
            results.append((slug, extract_conc(det_text)))
            seen_slugs.add(slug)

    # Secondary path: resolve raw text fragments → slugs
    for part in split_detergent_text(det_text):
        if not part:
            continue
        slug = resolve_detergent_slug(part)
        if slug and slug not in seen_slugs:
            results.append((slug, extract_conc(part)))
            seen_slugs.add(slug)

    return results


def extract_conc(text):
    m = CONC_PATTERN.search(text)
    if m:
        val = float(m.group(1))
        unit = m.group(2).replace("(w/v)", "").strip()
        if unit.startswith("%"):
            unit = "%"
        return val, unit
    return None


def family_label(subgroup):
    """Short readable family label."""
    if not subgroup:
        return "unknown"
    s = subgroup.lower().replace("-", " ")
    return s.strip()


# ── Collection ───────────────────────────────────────────────────────

records = []  # list of dicts, one per protein
step_db = []  # list of dicts, one per step
family_count = Counter()
resolution_data = []  # (family, resolution)
expr_data = []  # (title, expr_system_or_class) for expression×resolution correlation
detergent_data = []  # (family, detergent_slug, conc_val, conc_unit, step_type)

# ── Parallel-load all protein YAMLs once ─────────────────────────────
from scripts._base import parallel_load_yamls
_all_proteins = {}
for path, data in parallel_load_yamls(sorted((W / "proteins_yaml").glob("*.yaml"))):
    if isinstance(data, dict):
        _all_proteins[path.stem] = data

# ── Process loaded data ──────────────────────────────────────────────
for slug, data in sorted(_all_proteins.items()):

    title = data.get("title", slug)
    family = family_label(data.get("mpstruc_classification", {}).get("subgroup", ""))
    family_count[family] += 1

    # Expression system — use canonical class if available, fallback to raw
    expr = data.get("expression", {}) or {}
    expr_class = (expr.get("class", "") or "").strip()
    if expr_class:
        expr_data.append((title, expr_class))
    else:
        expr_sys = (expr.get("system", "") or "").strip()
        if expr_sys:
            expr_data.append((title, expr_sys))

    # Structures → resolution
    for pub in data.get("publications", []) or []:
        if not isinstance(pub, dict):
            continue
        for s in pub.get("structures", []) or []:
            if isinstance(s, dict):
                res = s.get("resolution")
                if res:
                    try:
                        r = float(str(res).replace("\u00c5", "").strip())
                        resolution_data.append((family, r, title, s.get("pdb_id", "")))
                    except ValueError:
                        pass

        # Steps
        purifs = list(pub.get("purifications", []) or [])
        for p in purifs:
            if not isinstance(p, dict):
                continue
            for step in p.get("steps", []) or []:
                if not isinstance(step, dict):
                    continue
                st = step.get("step_type", "")
                dt = step.get("detergent", "") or ""
                step_db.append(
                    {
                        "protein": title,
                        "family": family,
                        "step_type": st,
                        "detergent_raw": dt,
                        "buffer": step.get("buffer", "") or "",
                    }
                )
                for det in extract_detergent(step):
                    slug, conc = det
                    conc_val = conc[0] if conc else None
                    conc_unit = conc[1] if conc else None
                    detergent_data.append((family, slug, conc_val, conc_unit, st))


# ── Analysis Functions ───────────────────────────────────────────────


def resolution_stats():
    """Resolution distribution by family."""
    families = defaultdict(list)
    for fam, res, _, _ in resolution_data:
        families[fam].append(res)
    rows = []
    for fam, vals in sorted(families.items(), key=lambda x: -len(x[1])):
        vals_s = sorted(vals)
        n = len(vals_s)
        mean = sum(vals_s) / n
        med = vals_s[n // 2]
        rows.append((fam, n, mean, med, vals_s[0], vals_s[-1]))
    return rows


def detergent_matrix():
    """Detergent usage matrix: (family × detergent) → count."""
    rows = defaultdict(Counter)
    for fam, slug, _, _, _ in detergent_data:
        rows[fam][slug] += 1
    return rows


def detergent_conc_ranges():
    """Concentration ranges per (family, detergent)."""
    ranges = defaultdict(list)
    for fam, slug, conc_val, conc_unit, _ in detergent_data:
        if conc_val:
            ranges[(fam, slug, conc_unit)].append(conc_val)
    result = {}
    for key, vals in sorted(ranges.items()):
        fam, slug, unit = key
        vals_s = sorted(vals)
        n = len(vals_s)
        result[f"{fam}/{slug}/{unit}"] = {
            "n": n,
            "min": vals_s[0],
            "max": vals_s[-1],
            "mean": sum(vals_s) / n,
            "median": vals_s[n // 2],
        }
    return result


def step_type_profiles():
    """Pipeline profile: which step_types appear per family."""
    profiles = defaultdict(Counter)
    for rec in step_db:
        if rec["step_type"]:
            profiles[rec["family"]][rec["step_type"]] += 1
    return profiles


def exchange_analysis():
    """Detergent exchange: proteins where detergent changes between steps."""
    exchanges = []
    exchange_count = Counter()
    for slug, data in sorted(_all_proteins.items()):
        title = data.get("title", slug)
        fam = family_label(data.get("mpstruc_classification", {}).get("subgroup", ""))
        environments = []  # list of frozensets, one per step
        for pub in data.get("publications", []) or []:
            if not isinstance(pub, dict):
                continue
            for p in pub.get("purifications", []) or []:
                if not isinstance(p, dict):
                    continue
                for step in p.get("steps", []):
                    if not isinstance(step, dict):
                        continue
                    slugs = frozenset(d[0] for d in extract_detergent(step) if d[0])
                    if slugs and (not environments or slugs != environments[-1]):
                        environments.append(slugs)
        if len(set(environments)) > 1:
            env_list = [sorted(e) for e in environments]
            exchanges.append((title, fam, env_list))
            key = " → ".join("+".join(e) for e in env_list[:3])
            exchange_count[key] += 1
    return exchanges, exchange_count


def expression_analysis():
    """Expression system distribution + resolution correlation."""
    sys_count = Counter(s for _, s in expr_data)
    # Resolution by expression system
    sys_res = defaultdict(list)
    for fam, res, title, pdb in resolution_data:
        # Find expression system for this protein from expr_data
        for ti, syst in expr_data:
            if ti == title:
                sys_res[syst].append(res)
                break
    sys_res_stats = {}
    for syst, vals in sorted(sys_res.items()):
        vals_s = sorted(vals)
        n = len(vals_s)
        sys_res_stats[syst] = {
            "n": n,
            "mean": sum(vals_s) / n,
            "median": vals_s[n // 2],
            "min": vals_s[0],
            "max": vals_s[-1],
        }
    return sys_count, sys_res_stats


def resolution_by_step_type():
    """Does step count or specific steps correlate with resolution?"""
    # Count step types per protein
    step_counts = defaultdict(Counter)
    for rec in step_db:
        if rec["step_type"]:
            step_counts[rec["protein"]][rec["step_type"]] += 1
    # Pair with resolution
    step_res = defaultdict(list)
    for fam, res, title, pdb in resolution_data:
        sc = step_counts.get(title, {})
        for st, cnt in sc.items():
            step_res[st].append(res)
    result = {}
    for st, vals in sorted(step_res.items()):
        if len(vals) < 3:
            continue
        vals_s = sorted(vals)
        n = len(vals_s)
        result[st] = {"n": n, "mean": sum(vals_s) / n, "median": vals_s[n // 2]}
    return result


# ── Generate Report ──────────────────────────────────────────────────


def fmt(v, precision=2):
    if isinstance(v, float):
        return f"{v:.{precision}f}"
    return str(v)


lines = []
lines.append("# Aggregate Statistics — X-ray MP Wiki")
lines.append("")
lines.append("**Generated:** 2026-07-06")
lines.append(f"**Proteins scanned:** {len(family_count)} families, {sum(family_count.values())} proteins")
lines.append(f"**Steps scanned:** {len(step_db)}")
lines.append(f"**Resolutions scanned:** {len(resolution_data)}")
lines.append("")

# ── 1. Family coverage ──
lines.append("---")
lines.append("## 1. Family Coverage")
lines.append("")
lines.append("| Family | Proteins | Structures | Avg. resolution | Median resolution |")
lines.append("|--------|----------|------------|-----------------|-------------------|")
res_rows = resolution_stats()
res_by_fam = {r[0]: r for r in res_rows}
for fam, count in family_count.most_common():
    rr = res_by_fam.get(fam, None)
    if rr:
        _, n, mean, med, lo, hi = rr
        lines.append(f"| {fam} | {count} | {n} | {fmt(mean)}Å | {fmt(med)}Å |")
    else:
        lines.append(f"| {fam} | {count} | 0 | — | — |")
lines.append("")

# ── 2. Resolution distribution ──
lines.append("---")
lines.append("## 2. Resolution Distribution")
lines.append("")
all_res = sorted(r for _, r, _, _ in resolution_data)
if all_res:
    lines.append(f"- **Overall mean:** {fmt(sum(all_res) / len(all_res))}Å")
    lines.append(f"- **Overall median:** {fmt(all_res[len(all_res) // 2])}Å")
    lines.append(f"- **Best:** {fmt(all_res[0])}Å ({resolution_data[all_res.index(all_res[0])][2]})")
    lines.append(f"- **Worst:** {fmt(all_res[-1])}Å")
    # Distribution bands
    bands = [(2.0, 2.5), (2.5, 3.0), (3.0, 3.5), (3.5, 4.0), (4.0, 100)]
    for lo, hi in bands:
        c = sum(1 for r in all_res if lo <= r < hi)
        pct = c / len(all_res) * 100
        label = f"{fmt(lo)}–{fmt(hi)}Å" if hi < 100 else f">{fmt(lo)}Å"
        lines.append(f"- **{label}:** {c} ({fmt(pct, 1)}%)")
lines.append("")

# ── 3. Detergent usage matrix ──
lines.append("---")
lines.append("## 3. Detergent Usage by Family")
lines.append("")
det_matrix = detergent_matrix()
# Top 15 detergents
all_detergents = Counter()
for fam, dets in det_matrix.items():
    all_detergents.update(dets)
top_dets = [d for d, _ in all_detergents.most_common(20)]
top_fams = [f for f, _ in family_count.most_common(15)]

# Header
header = "| Detergent | " + " | ".join(f[:16] for f in top_fams) + " | Total |"
sep = "|-----------|" + "|".join("---" for _ in top_fams) + "|-------|"
lines.append(header)
lines.append(sep)
for det in top_dets:
    totals = sum(det_matrix[f].get(det, 0) for f in top_fams)
    # Check all families
    total = sum(det_matrix[f].get(det, 0) for f in det_matrix)
    cells = [str(det_matrix[f].get(det, 0) or "") for f in top_fams]
    lines.append(f"| {det} | {' | '.join(cells)} | {total} |")
lines.append("")

# ── 4. Detergent concentration ranges ──
lines.append("---")
lines.append("## 4. Detergent Concentration Ranges (notable)")
lines.append("")
conc_data = detergent_conc_ranges()
for key, stats in sorted(conc_data.items()):
    if stats["n"] >= 5:
        lines.append(f"- **{key}** — n={stats['n']}, range {stats['min']}–{stats['max']}, median {stats['median']}")
lines.append("")

# ── 5. Step-type pipeline profiles ──
lines.append("---")
lines.append("## 5. Step-Type Pipeline Profiles by Family")
lines.append("")
profiles = step_type_profiles()
all_step_types = sorted(set(st for fam, c in profiles.items() for st in c))
for fam in sorted(profiles.keys()):
    p = profiles[fam]
    total = sum(p.values())
    if total < 10:
        continue
    parts = []
    for st in all_step_types:
        if p.get(st, 0) > 0:
            pct = p[st] / total * 100
            if pct >= 5:
                parts.append(f"{st}({fmt(pct, 0)}%)")
    lines.append(f"- **{fam}** ({total} steps): {', '.join(parts)}")
lines.append("")

# ── 6. Detergent exchange ──
lines.append("---")
lines.append("## 6. Detergent Exchange Analysis")
lines.append("")
exchanges, exchange_count = exchange_analysis()
lines.append(
    f"- **Proteins with detergent exchange:** {len(exchanges)} / {sum(family_count.values())} ({fmt(100 * len(exchanges) / sum(family_count.values()), 1)}%)"
)
lines.append("")
lines.append("### Most common exchange patterns")
for pattern, count in exchange_count.most_common(10):
    lines.append(f"- **{pattern}** ({count} proteins)")
lines.append("")

# ── 7. Expression system ──
lines.append("---")
lines.append("## 7. Expression System Distribution")
lines.append("")
sys_count, sys_res = expression_analysis()
lines.append("| System | Proteins | % | Mean Res. | Median Res. |")
lines.append("|--------|----------|---|-----------|-------------|")
total_proteins = sum(sys_count.values())
for system, count in sys_count.most_common():
    pct = count / total_proteins * 100
    rs = sys_res.get(system, {})
    mean_r = fmt(rs["mean"]) if rs.get("mean") else "—"
    med_r = fmt(rs["median"]) if rs.get("median") else "—"
    lines.append(f"| {system} | {count} | {fmt(pct, 1)}% | {mean_r}Å | {med_r}Å |")
lines.append("")

# ── 8. Resolution by step type ──
lines.append("---")
lines.append("## 8. Resolution by Step-Type Presence")
lines.append("")
st_res = resolution_by_step_type()
lines.append("| Step type | Proteins | Mean Res. | Median Res. |")
lines.append("|-----------|----------|-----------|-------------|")
for st in sorted(st_res.keys(), key=lambda s: -st_res[s]["n"]):
    d = st_res[st]
    lines.append(f"| {st} | {d['n']} | {fmt(d['mean'])}Å | {fmt(d['median'])}Å |")
lines.append("")

print("\n".join(lines))

# ── Save JSON for reuse ──
stats_out = {
    "family_coverage": {f: c for f, c in family_count.most_common()},
    "resolution_distribution": {
        "overall_mean": round(sum(all_res) / len(all_res), 2),
        "overall_median": round(all_res[len(all_res) // 2], 2),
    }
    if all_res
    else {},
    "detergent_matrix": {f: dict(d) for f, d in det_matrix.items()},
    "detergent_conc_ranges": conc_data,
    "step_profiles": {f: dict(c) for f, c in profiles.items()},
    "exchanges": [(t, f, d) for t, f, d in exchanges],
    "expression_systems": dict(sys_count),
    "resolution_by_step_type": st_res,
}
(OUT / "aggregate_stats.json").write_text(json.dumps(stats_out, indent=2))
print(f"\n(JSON saved to {OUT / 'aggregate_stats.json'})")
