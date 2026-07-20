#!/usr/bin/env python3
"""Rendering functions for protein wiki pages (publications-based)."""

from typing import Optional

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from _base import normalize_hosts
from _base import render_frontmatter as _base_render_frontmatter


def render_link(path: str, title: str) -> str:
    return f'<a href="{path}">{title}</a>'


def render_pdb_link(pdb_id: str) -> str:
    """Render a PDB ID as a clickable link to RCSB."""
    if not pdb_id:
        return ""
    return f'<a class="pdb-link" href="https://www.rcsb.org/structure/{pdb_id.lower()}">{pdb_id.upper()}</a>'


def md_link_to_html(text):
    """Convert markdown links [text](url) to HTML <a> tags inline."""
    import re

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)


def render_html_table(headers: Optional[list[str]], rows: list[list[str]], css_class: str = "wiki-table") -> str:
    """Render a table as HTML with CSS class. Converts markdown links to HTML."""
    lines = [f'<table class="{css_class}">']
    if headers:
        lines.append("  <thead><tr>")
        for h in headers:
            lines.append(f"    <th>{h}</th>")
        lines.append("  </tr></thead>")
    lines.append("  <tbody>")
    for row in rows:
        lines.append("    <tr>")
        for cell in row:
            lines.append(f"      <td>{md_link_to_html(str(cell))}</td>")
        lines.append("    </tr>")
    lines.append("  </tbody>")
    lines.append("</table>")
    return "\n".join(lines)


def render_table(headers, rows):
    return render_html_table(headers, rows)


def render_frontmatter(data: dict) -> str:
    return _base_render_frontmatter(data, "protein", "proteins")


def render_publication_structures(structures):
    if not structures:
        return ""
    headers = ["PDB ID", "Resolution", "Space Group", "Construct", "Ligand/Co-factor"]
    rows = []
    for s in structures:
        rows.append(
            [
                render_pdb_link(s.get("pdb_id", "")),
                s.get("resolution", ""),
                s.get("space_group", "\u2014"),
                s.get("construct", ""),
                s.get("ligand", ""),
            ]
        )
    blocks = ["**Structures:**", "", render_table(headers, rows)]
    notes = []
    for s in structures:
        note_parts = []
        if "refinement" in s:
            r = s["refinement"]
            note_parts.append(f"R-work {r.get('r_work', '')}%, R-free {r.get('r_free', '')}%")
        if "atoms" in s:
            note_parts.append(f"Atoms: {s['atoms']}")
        if "data_collection" in s:
            note_parts.append(f"Data collection: {s['data_collection']}")
        if note_parts:
            notes.append(" - " + "; ".join(note_parts))
    if notes:
        blocks.extend(notes)
    return "\n".join(blocks)


def render_publication_purifications(purifications):
    if not purifications:
        return ""
    blocks = ["**Purification:**", ""]
    for p in purifications:
        if p.get("expression_system"):
            blocks.append(f"- **Expression system**: {p['expression_system']}")
        if p.get("expression_construct"):
            blocks.append(f"- **Expression construct**: {p['expression_construct']}")
        if p.get("tag_info"):
            blocks.append(f"- **Tag info**: {p['tag_info']}")
        if blocks[-1] != "":
            blocks.append("")

        headers = ["Step", "Method", "Resin / Column", "Buffer + Detergent", "Notes"]
        rows = []
        for i, step in enumerate(p.get("steps", []), 1):
            step_label = step.get("step", f"Step {i}")
            buf = step.get("buffer", "")
            det = step.get("detergent", "")
            buf_det = f"{buf} + {det}" if buf and det else (buf or det or "")
            rows.append(
                [step_label, step.get("method", ""), step.get("resin", "\u2014"), buf_det, step.get("notes", "")]
            )
        blocks.append(render_table(headers, rows))

        if p.get("final_sample"):
            blocks.append(f"**Final sample**: {p['final_sample']}")
        if p.get("yield"):
            blocks.append(f"**Yield**: {p['yield']}")
        if p.get("purity"):
            blocks.append(f"**Purity**: {p['purity']}")
        blocks.append("")
    return "\n".join(blocks)


def render_crystallization_table(c):
    rows = []
    if c.get("method"):
        rows.append(("Method", c["method"]))
    if c.get("protein_sample"):
        rows.append(("Protein sample", c["protein_sample"]))
    is_lcp = "cubic phase" in c.get("method", "").lower() or "lcp" in c.get("method", "").lower()
    if is_lcp:
        if c.get("lipid"):
            rows.append(("Lipid", c["lipid"]))
        if c.get("protein_to_lipid_ratio"):
            rows.append(("Protein-to-lipid ratio", c["protein_to_lipid_ratio"]))
    else:
        if c.get("reservoir"):
            rows.append(("Reservoir", c["reservoir"]))
        if c.get("mixing_ratio"):
            rows.append(("Mixing ratio", c["mixing_ratio"]))
    if c.get("temperature"):
        rows.append(("Temperature", c["temperature"]))
    if c.get("growth_time"):
        rows.append(("Growth time", c["growth_time"]))
    if c.get("cryoprotection"):
        rows.append(("Cryoprotection", c["cryoprotection"]))
    if c.get("notes"):
        rows.append(("Notes", c["notes"]))
    if not rows:
        return ""
    return render_html_table(None, rows, "wiki-kv-table")


def render_publication_crystallizations(crystallizations):
    if not crystallizations:
        return ""
    blocks = ["**Crystallization:**", ""]
    for c in crystallizations:
        blocks.append(render_crystallization_table(c))
    return "\n".join(blocks)


def render_colored_sequence(residues: str, topology: list[dict]) -> str:
    """Render sequence with topology-colored spans and position ruler.

    Returns inline HTML with ruler + colored sequence lines interleaved.
    Each chunk gets: <span class="topo-ruler">position numbers</span>
                     <span class="topo-line">colored residues</span>
    """
    if not residues:
        return ""

    # Build position → location mapping
    pos_loc = {}
    for reg in topology:
        loc = reg.get("location", "Unknown").lower()
        css_class = f"topo-{loc}"
        start = int(reg.get("begin", 1))
        end = int(reg.get("end", 1))
        for i in range(start, end + 1):
            pos_loc[i] = css_class

    def build_ruler(start_pos, length):
        """Build a ruler string where numbers appear right-aligned at every 10th position."""
        arr = [" "] * length
        for i in range(length):
            pos = start_pos + i
            if pos % 10 == 0:
                s = str(pos)
                for d, ch in enumerate(s):
                    idx = i - len(s) + 1 + d
                    if 0 <= idx < length:
                        arr[idx] = ch
        return "".join(arr)

    lines = []
    line_len = 120
    for start in range(0, len(residues), line_len):
        chunk = residues[start : start + line_len]
        global_start = start + 1  # 1-indexed

        # Ruler line (same monospace font, muted color)
        ruler = build_ruler(global_start, len(chunk))
        lines.append(f'<span class="topo-ruler">{ruler}</span>')

        # Sequence line
        seq_line = '<span class="topo-line">'
        i = 0
        while i < len(chunk):
            pos = global_start + i
            css = pos_loc.get(pos, "topo-unknown")
            j = i + 1
            while j < len(chunk) and pos_loc.get(global_start + j, "topo-unknown") == css:
                j += 1
            segment = chunk[i:j]
            seq_line += f'<span class="{css}">{segment}</span>'
            i = j
        seq_line += "</span>"
        lines.append(seq_line)

    return "\n".join(lines)


def render_sequence_block(sequences: list[dict]) -> str:
    """Render sequence + topology with colored TM regions."""
    if not sequences:
        return ""
    blocks = ['<div class="sequences" markdown="1">', "**Sequences (PDBTM):**", ""]
    for seq in sequences:
        chain = seq.get("chain", "?")
        tmd = seq.get("tmd", "?")
        pdb_id = seq.get("pdb_id", "")
        seq_type = seq.get("type", "")

        pdb_link = render_pdb_link(pdb_id) if pdb_id else pdb_id
        blocks.append('<div class="sequence-entry" markdown="1">')
        blocks.append(f"**PDB {pdb_link} — Chain {chain} ({tmd} TMs, {seq_type})**")
        blocks.append("")

        residues = seq.get("residues", "")
        topo = seq.get("topology", [])

        if residues:
            # Sequence display with monospace and line numbers
            blocks.append('<div class="sequence-display">')
            if topo:
                # Legend
                blocks.append('<div class="topo-legend">')
                blocks.append('<span class="topo-membrane-legend">&#9608; TM Helix</span>')
                blocks.append('<span class="topo-inside-legend">&#9608; Inside</span>')
                blocks.append('<span class="topo-outside-legend">&#9608; Outside</span>')
                blocks.append('<span class="topo-unknown-legend">&#9608; Unknown</span>')
                blocks.append("</div>")
            blocks.append('<div class="sequence-text">')

            if topo:
                colored = render_colored_sequence(residues, topo)
                blocks.append(colored)
                # Topology table (collapsed by default — ruler shows position context)
                topo_rows = []
                for r in topo:
                    topo_rows.append(
                        [
                            r.get("begin", ""),
                            r.get("end", ""),
                            r.get("pdb_begin", ""),
                            r.get("pdb_end", ""),
                            r.get("location", ""),
                        ]
                    )
                n_regions = len(topo_rows)
                blocks.append(
                    f'<details class="topo-details"><summary>Topology coordinates ({n_regions} regions)</summary>'
                )
                blocks.append(
                    render_html_table(
                        ["Begin", "End", "PDB Begin", "PDB End", "Location"], topo_rows, "wiki-mini-table"
                    )
                )
                blocks.append("</details>")
            else:
                for i in range(0, len(residues), 120):
                    blocks.append(residues[i : i + 120])

            blocks.append("</div>")
            blocks.append("</div>")

        blocks.append("</div>")
        blocks.append("")

    blocks.append("</div>")
    return "\n".join(blocks)


def render_publications(publications: list[dict], expression: dict) -> str:
    """Render all publication entries as collapsible details/summary sections."""
    lines = ["## Publications", ""]

    if not publications:
        lines.append("No publications.")
        return "\n".join(lines)

    too_many = len(publications) > 5

    for pub in publications:
        src = pub.get("source", "unknown")
        n_structs = len(pub.get("structures", []))
        n_seqs = len(pub.get("sequences", []))
        summary_label = f"{src} ({n_structs} structure{'s' if n_structs != 1 else ''}"
        if n_seqs:
            summary_label += f", {n_seqs} sequence{'s' if n_seqs != 1 else ''}"
        summary_label += ")"

        if too_many:
            lines.append('<details class="pub-entry" markdown="1">')
            lines.append(f"<summary><strong>{summary_label}</strong></summary>")
            lines.append("")
        else:
            lines.append(f"### {src}")
            lines.append("")

        # Structures
        struct_block = render_publication_structures(pub.get("structures", []))
        if struct_block:
            lines.append(struct_block)
            lines.append("")

        # Expression
        if expression and any(expression.values()):
            expr_lines = []
            if expression.get("system"):
                expr_lines.append(f"- **Expression system**: {expression['system']}")
            if expression.get("construct"):
                expr_lines.append(f"- **Construct**: {expression['construct']}")
            if expression.get("notes"):
                expr_lines.append(f"- **Notes**: {expression['notes']}")
            if expression.get("induction"):
                expr_lines.append(f"- **Induction**: {expression['induction']}")
            if expression.get("media"):
                expr_lines.append(f"- **Media**: {expression['media']}")
            if expr_lines:
                lines.append("**Expression:**")
                lines.append("")
                lines.extend(expr_lines)
                lines.append("")

        # Purifications
        purif_block = render_publication_purifications(pub.get("purifications", []))
        if purif_block:
            lines.append(purif_block)

        # Crystallizations
        xtal_block = render_publication_crystallizations(pub.get("crystallizations", []))
        if xtal_block:
            lines.append(xtal_block)

        # Sequences
        seq_block = render_sequence_block(pub.get("sequences", []))
        if seq_block:
            lines.append(seq_block)

        if too_many:
            lines.append("</details>")
            lines.append("")

    return "\n".join(lines)


def render_biological_insights(insights):
    lines = ["## Biological / Functional Insights", ""]
    if not insights:
        return "\n".join(lines)
    for ins in insights:
        if ins.get("title"):
            lines.append(f"### {ins['title']}")
            lines.append("")
        content = ins.get("content", "").rstrip("\n") + "\n"
        lines.append(content)
    return "\n".join(lines)


def render_expression_badges(expression):
    """Render expression system as color-coded badges.

    Parses expression.system, normalizes to canonical host, renders inline badges.
    """
    if not expression or not expression.get("system"):
        return ""

    sys_str = expression["system"]
    hosts = normalize_hosts(sys_str)
    if not hosts:
        return ""
    badges = " ".join(
        f'<span class="expr-badge expr-{host.lower().replace(" ", "-").replace(".", "")}">{host}</span>'
        for host in hosts
    )
    return f'<div class="expr-badges">{badges}</div>\n\n'


def render_cross_references(references: list[dict]) -> str:
    lines = ["## Cross-References", ""]
    if not references:
        return "\n".join(lines)
    for ref in references:
        link = render_link(ref["path"], ref["title"])
        lines.append(f"- {link} \u2014 {ref['reason']}")
    lines.append("")
    return "\n".join(lines)


def generate_page(data: dict) -> str:
    """Generate a complete protein wiki page from the restructured YAML data."""
    sections = []
    sections.append(render_frontmatter(data))
    sections.append("")
    sections.append(f"# {data['title']}")
    sections.append("")
    sections.append(render_expression_badges(data.get("expression", {})))
    uniprot = data.get("uniprot_id", "")
    if uniprot:
        if isinstance(uniprot, list) and uniprot:
            if isinstance(uniprot[0], dict):
                badges = " ".join(
                    f'<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/{u["accession"]}" title="{u.get("species", "")}">UniProt: {u["accession"]}</a>'
                    if u.get("accession")
                    else f'<span class="badge badge-uniprot badge-uniprot-none" title="{u.get("species", "")}">No UniProt</span>'
                    for u in uniprot
                )
            else:
                badges = " ".join(
                    f'<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/{u}">UniProt: {u}</a>'
                    for u in uniprot
                )
            sections.append(badges)
        else:
            sections.append(
                f'<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/{uniprot}">UniProt: {uniprot}</a>'
            )
        sections.append("")
    organism = data.get("organism", "")
    if organism:
        sections.append(f'<span class="expr-badge">{organism}</span>')
        sections.append("")
    sections.append("## Overview")
    sections.append("")
    sections.append(data.get("overview", ""))
    sections.append("")
    sections.append(render_publications(data.get("publications", []), data.get("expression", {})))
    sections.append("")
    sections.append(render_biological_insights(data.get("biological_insights", [])))
    sections.append("")
    sections.append(render_cross_references(data.get("cross_references", [])))

    return "\n".join(sections)
