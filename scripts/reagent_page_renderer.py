#!/usr/bin/env python3
"""
Shared rendering functions for reagent wiki pages.

Used by generate_reagent_page.py to render complete pages from YAML data.
"""

from _base import render_frontmatter as _base_render_frontmatter


def render_link(path, title):
    """Render a markdown link with absolute path."""
    return f"[{title}]({path})"


def render_table(headers, rows):
    """Render a Kramdown table."""
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_frontmatter(data: dict) -> str:
    """Render YAML frontmatter. Delegates to shared _base.render_frontmatter."""
    return _base_render_frontmatter(data, "reagent", "reagents")


def render_properties(data):
    """Render Properties section with type-specific fields."""
    lines = ["## Properties", ""]

    # Common fields
    common_fields = [
        ("Chemical name", "chemical_name"),
        ("Chemical formula", "chemical_formula"),
        ("Molecular weight", "molecular_weight"),
        ("Class", "class"),
    ]

    for label, key in common_fields:
        val = data.get(key)
        if val:
            lines.append(f"- **{label}**: {val}")

    # Type-specific fields
    reagent_type = data.get("type", "").lower()

    if reagent_type in ("buffer", "buffers"):
        for label, key in [
            ("pKa", "pka"),
            ("pH range", "ph_range"),
            ("Concentration range", "concentration_range"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    elif reagent_type in ("detergent", "detergents"):
        for label, key in [
            ("CMC", "cmc"),
            ("HLB", "hlb"),
            ("Transition temperature", "transition_temp"),
            ("Head group", "head_group"),
            ("Tail length", "tail_length"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    elif reagent_type in ("lipid", "lipids"):
        for label, key in [
            ("Acyl chain composition", "acyl_chain"),
            ("Phase transition temperature", "phase_transition"),
            ("Class", "class"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    elif reagent_type in ("additive", "additives"):
        for label, key in [
            ("Function", "function"),
            ("Solubility", "solubility"),
            ("Typical concentration", "typical_concentration"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    elif reagent_type in ("ligand", "ligands"):
        for label, key in [
            ("Kd/Ki", "kd_ki"),
            ("Clinical status", "clinical_status"),
            ("Scaffold", "scaffold"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    elif reagent_type in ("protein-tag", "protein-tags"):
        for label, key in [
            ("Source organism", "source_organism"),
            ("Fusion strategy", "fusion_strategy"),
            ("Size", "size"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    elif reagent_type in ("antibody", "antibodies"):
        for label, key in [
            ("Target", "target"),
            ("Format", "format"),
            ("Epitope", "epitope"),
            ("Isotype", "isotype"),
        ]:
            val = data.get(key)
            if val:
                lines.append(f"- **{label}**: {val}")

    # If no properties found, add placeholder
    if len(lines) == 1:
        lines.append("No properties recorded.")

    lines.append("")
    return "\n".join(lines)


def render_use_in_work(uses):
    """Render 'Use in Membrane Protein Work' section."""
    lines = ["## Use in Membrane Protein Work", ""]

    if not uses:
        lines.append("No specific use cases documented.")
        return "\n".join(lines)

    for use in uses:
        if use.get("title"):
            lines.append(f"### {use['title']}")
            lines.append("")
        content = use.get("content", "")
        content = content.rstrip("\n") + "\n"
        lines.append(content)
        lines.append("")

    return "\n".join(lines)


def render_examples_table(examples):
    """Render 'Examples from This Wiki' table."""
    lines = ["## Examples from This Wiki", ""]

    if not examples:
        lines.append("No examples from this wiki.")
        return "\n".join(lines)

    headers = ["Protein", "Concentration", "Context", "Result"]
    rows = []
    for ex in examples:
        protein = ex.get("protein", "")
        concentration = ex.get("concentration", "")
        context = ex.get("context", "")
        result = ex.get("result", "")
        rows.append([protein, concentration, context, result])

    lines.append(render_table(headers, rows))
    lines.append("")
    return "\n".join(lines)


def render_binding_mode(binding):
    """Render 'Binding Mode' section (ligands only)."""
    lines = ["## Binding Mode", ""]

    if not binding:
        lines.append("No binding mode data available.")
        return "\n".join(lines)

    if isinstance(binding, dict):
        # Single binding entry
        if binding.get("target"):
            lines.append(f"### Binding to {binding['target']}")
            lines.append("")
        content = binding.get("interactions", "")
        if content:
            if isinstance(content, list):
                content = "\n".join(f"- {item}" for item in content)
            lines.append(content.rstrip("\n") + "\n")
        if binding.get("pocket_volume"):
            lines.append(f"- **Pocket volume**: {binding['pocket_volume']}")
        if binding.get("key_residues"):
            lines.append(f"- **Key residues**: {binding['key_residues']}")
    elif isinstance(binding, list):
        # Multiple binding entries
        for entry in binding:
            if entry.get("target"):
                lines.append(f"### Binding to {entry['target']}")
                lines.append("")
            content = entry.get("interactions", "")
            if content:
                if isinstance(content, list):
                    content = "\n".join(f"- {item}" for item in content)
                lines.append(content.rstrip("\n") + "\n")
            if entry.get("pocket_volume"):
                lines.append(f"- **Pocket volume**: {entry['pocket_volume']}")
            lines.append("")

    lines.append("")
    return "\n".join(lines)


def render_advantages_disadvantages(data):
    """Render 'Advantages and Disadvantages' section."""
    lines = ["## Advantages and Disadvantages", ""]

    advantages = data.get("advantages", [])
    disadvantages = data.get("disadvantages", [])

    if advantages:
        lines.append("### Advantages")
        lines.append("")
        for adv in advantages:
            lines.append(f"- {adv}")
        lines.append("")

    if disadvantages:
        lines.append("### Disadvantages")
        lines.append("")
        for dis in disadvantages:
            lines.append(f"- {dis}")
        lines.append("")

    if not advantages and not disadvantages:
        lines.append("No advantages/disadvantages recorded.")
        lines.append("")

    return "\n".join(lines)


def render_comparison_table(comparison):
    """Render 'Comparison with Related Reagents' table."""
    lines = ["## Comparison with Related Reagents", ""]

    if not comparison:
        lines.append("No comparison data available.")
        lines.append("")
        return "\n".join(lines)

    if isinstance(comparison, dict):
        headers = list(comparison.keys())
        if not headers:
            lines.append("No comparison data available.")
            lines.append("")
            return "\n".join(lines)
        rows = [[str(comparison.get(h, "")) for h in headers]]
        lines.append(render_table(headers, rows))
    elif isinstance(comparison, list):
        if comparison:
            headers = list(comparison[0].keys())
            rows = [[str(entry.get(h, "")) for h in headers] for entry in comparison]
            lines.append(render_table(headers, rows))
        else:
            lines.append("No comparison data available.")
    lines.append("")
    return "\n".join(lines)


def render_cross_references(references: list[dict]) -> str:
    """Render Cross-References section."""
    lines = ["## Cross-References", ""]

    if not references:
        return "\n".join(lines)

    for ref in references:
        link = render_link(ref["path"], ref["title"])
        lines.append(f"- {link} \u2014 {ref['reason']}")

    lines.append("")
    return "\n".join(lines)


def generate_page(data: dict) -> str:
    """Generate a complete reagent wiki page from data dict."""
    sections = []
    sections.append(render_frontmatter(data))
    sections.append("")
    sections.append(f"# {data['title']}")
    sections.append("")
    sections.append("## Overview")
    sections.append("")
    sections.append(data.get("overview", ""))
    sections.append("")
    sections.append(render_properties(data))
    sections.append(render_use_in_work(data.get("uses", [])))
    sections.append(render_examples_table(data.get("examples", [])))

    # Binding mode (ligands only)
    if data.get("binding") or data.get("binding_mode"):
        sections.append(render_binding_mode(data.get("binding") or data.get("binding_mode")))

    sections.append(render_advantages_disadvantages(data))
    sections.append(render_comparison_table(data.get("comparison", [])))
    sections.append(render_cross_references(data.get("cross_references", [])))

    return "\n".join(sections)
