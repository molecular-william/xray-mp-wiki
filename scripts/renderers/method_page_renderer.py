#!/usr/bin/env python3
"""
Shared rendering logic for method wiki pages.

Used by generate_method_page.py to render complete pages from YAML data.
"""

import os
import re
import sys

# Ensure scripts/ is on path
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from _base import render_frontmatter as _base_render_frontmatter


def format_frontmatter(yaml_data: dict) -> str:
    """Render YAML frontmatter. Delegates to shared _base.render_frontmatter."""
    return _base_render_frontmatter(yaml_data, "method", "methods")


def format_overview(overview):
    """Render Overview section."""
    lines = ["## Overview", "", overview.strip()]
    return "\n".join(lines)


def format_principle(principle):
    """Render Principle section."""
    lines = ["## Principle", "", principle.strip()]
    return "\n".join(lines)


def format_protocol(protocol):
    """Render Protocol section with subsections."""
    lines = ["## Protocol", ""]

    if "reagents" in protocol and protocol["reagents"]:
        lines.append("### Reagents and Materials")
        lines.append("")
        for item in protocol["reagents"]:
            lines.append(f"- {item}")
        lines.append("")

    if "steps" in protocol and protocol["steps"]:
        lines.append("### Steps")
        lines.append("")
        for i, step in enumerate(protocol["steps"], 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    if "conditions" in protocol and protocol["conditions"]:
        lines.append("### Typical Conditions")
        lines.append("")
        for key, value in protocol["conditions"].items():
            lines.append(f"- **{key}**: {value}")
        lines.append("")

    return "\n".join(lines)


def format_advantages_disadvantages(advantages, disadvantages):
    """Render Advantages and Disadvantages sections."""
    lines = []

    if advantages:
        lines.append("## Advantages")
        lines.append("")
        for item in advantages:
            lines.append(f"- {item}")
        lines.append("")

    if disadvantages:
        lines.append("## Disadvantages")
        lines.append("")
        for item in disadvantages:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)


def format_proteins_table(proteins):
    """Render Proteins Using This Method as a table."""
    if not proteins:
        return ""

    lines = ["## Proteins Using This Method", ""]
    lines.append("| Protein | Resolution | PDB | Notes |")
    lines.append("|---|---|---|---|")

    for p in proteins:
        protein_name = p.get("protein", "")
        resolution = p.get("resolution", "—")
        pdb = p.get("pdb", "—")
        notes = p.get("notes", "")

        # Format protein as wikilink
        if "/" in protein_name:
            # Already a wikilink
            protein_link = protein_name
        elif protein_name:
            protein_link = f"[{protein_name}](/xray-mp-wiki/proteins/{protein_name}/)"
        else:
            protein_link = ""

        lines.append(f"| {protein_link} | {resolution} | {pdb} | {notes} |")

    lines.append("")
    return "\n".join(lines)


def _format_related(heading, items):
    """Render Related X section with markdown links."""
    if not items:
        return ""
    lines = [f"## {heading}", ""]
    for item in items:
        path = item.get("path", "")
        title = item.get("title", "")
        reason = item.get("reason", "")
        if path and title:
            line = f"- [{title}]({path})"
            if reason:
                line += f" — {reason}"
            lines.append(line)
    lines.append("")
    return "\n".join(lines)


def format_related_methods(related):
    """Render Related Methods section. Delegates to shared _format_related."""
    return _format_related("Related Methods", related)


def format_related_reagents(related):
    """Render Related Reagents section. Delegates to shared _format_related."""
    return _format_related("Related Reagents", related)


def render_method_page(yaml_data):
    """Render a complete method page from YAML data.

    Supports two modes:
    1. Specific method page: has principle, protocol, advantages, disadvantages, proteins
    2. Overview/parent page: has methods_list, workflow, comparison

    Detection: if 'methods_list' is present, render as overview page.
    """
    parts = []

    # Always start with frontmatter
    parts.append(format_frontmatter(yaml_data))
    parts.append("")

    # Title
    title = yaml_data.get("title", "Method")
    parts.append(f"# {title}")
    parts.append("")

    # Check if this is an overview/parent page
    is_overview = "methods_list" in yaml_data

    if is_overview:
        # Overview page structure
        if "overview" in yaml_data:
            parts.append(format_overview(yaml_data["overview"]))
            parts.append("")

        if "methods_list" in yaml_data:
            parts.append("## Methods")
            parts.append("")
            for item in yaml_data["methods_list"]:
                path = item.get("path", "")
                title_text = item.get("title", "")
                description = item.get("description", "")
                best_for = item.get("best_for", "")

                if path and title_text:
                    line = f"- [{title_text}]({path})"
                    if description:
                        line += f" — {description}"
                    if best_for:
                        line += f". Best for {best_for}."
                    parts.append(line)
            parts.append("")

        if "workflow" in yaml_data:
            parts.append("## Workflow Overview")
            parts.append("")
            parts.append(yaml_data["workflow"].strip())
            parts.append("")

        if "comparison" in yaml_data:
            parts.append("## Comparison of Methods")
            parts.append("")
            headers = yaml_data["comparison"].get("headers", [])
            rows = yaml_data["comparison"].get("rows", [])

            if headers:
                parts.append("| " + " | ".join(headers) + " |")
                parts.append("|" + "|".join(["---"] * len(headers)) + "|")
                for row in rows:
                    parts.append("| " + " | ".join(str(c) for c in row) + " |")
            parts.append("")

        if "related_resources" in yaml_data:
            parts.append("## Related Resources")
            parts.append("")
            for item in yaml_data["related_resources"]:
                path = item.get("path", "")
                title_text = item.get("title", "")
                reason = item.get("reason", "")

                if path and title_text:
                    line = f"- [{title_text}]({path})"
                    if reason:
                        line += f" — {reason}"
                    parts.append(line)
            parts.append("")
    else:
        # Specific method page structure
        if "overview" in yaml_data:
            parts.append(format_overview(yaml_data["overview"]))
            parts.append("")

        if "principle" in yaml_data:
            parts.append(format_principle(yaml_data["principle"]))
            parts.append("")

        if "protocol" in yaml_data:
            parts.append(format_protocol(yaml_data["protocol"]))
            parts.append("")

        if "advantages" in yaml_data or "disadvantages" in yaml_data:
            adv = yaml_data.get("advantages", [])
            dis = yaml_data.get("disadvantages", [])
            parts.append(format_advantages_disadvantages(adv, dis))

        if "proteins_using" in yaml_data:
            parts.append(format_proteins_table(yaml_data["proteins_using"]))

        related_methods = yaml_data.get("related_methods", [])
        related_reagents = yaml_data.get("related_reagents", [])

        if related_methods:
            parts.append(format_related_methods(related_methods))

        if related_reagents:
            parts.append(format_related_reagents(related_reagents))

    return "\n".join(parts)


def parse_existing_page(page_content):
    """Parse an existing method page and extract sections.

    Returns a dict with keys: frontmatter, overview, principle, protocol,
    advantages, disadvantages, proteins_table, related_methods, related_reagents
    """
    result = {
        "frontmatter": {},
        "overview": "",
        "principle": "",
        "protocol": "",
        "advantages": [],
        "disadvantages": [],
        "proteins_table": [],
        "related_methods": [],
        "related_reagents": [],
    }

    # Extract frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", page_content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        for line in fm_text.split("\n"):
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip()
                result["frontmatter"][key] = val

    # Remove frontmatter for section parsing
    body = re.sub(r"^---\n.*?\n---", "", page_content, flags=re.DOTALL).strip()

    # Split by ## headings
    sections = re.split(r"^## ", body, flags=re.MULTILINE)

    for section in sections:
        lines = section.strip().split("\n")
        if not lines:
            continue

        heading = lines[0].strip()
        content = "\n".join(lines[1:]).strip()

        if heading == "Overview":
            result["overview"] = content
        elif heading == "Principle":
            result["principle"] = content
        elif heading == "Protocol":
            result["protocol"] = content
        elif heading == "Advantages":
            result["advantages"] = [
                line.lstrip("- ").strip() for line in content.split("\n") if line.strip().startswith("- ")
            ]
        elif heading == "Disadvantages":
            result["disadvantages"] = [
                line.lstrip("- ").strip() for line in content.split("\n") if line.strip().startswith("- ")
            ]
        elif heading == "Proteins Using This Method":
            # Parse table rows
            result["proteins_table"] = _parse_protein_table(content)
        elif heading == "Related Methods":
            result["related_methods"] = _parse_related(content, "/xray-mp-wiki/methods/")
        elif heading == "Related Reagents":
            result["related_reagents"] = _parse_related(content, "/xray-mp-wiki/reagents/")

    return result


def _parse_protein_table(table_text):
    """Parse markdown table into list of dicts."""
    proteins = []
    lines = table_text.strip().split("\n")

    for line in lines:
        line = line.strip()
        if line.startswith("|") and "---" not in line and line != "| Protein | Resolution | PDB | Notes |":
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 4:
                protein_link = cells[0]
                # Extract protein name from wikilink
                name_match = re.search(r"\[([^\]]+)\]", protein_link)
                protein_name = name_match.group(1) if name_match else protein_link
                # Remove trailing slash from path
                protein_name = protein_name.rstrip("/")

                proteins.append(
                    {
                        "protein": protein_name,
                        "resolution": cells[1],
                        "pdb": cells[2],
                        "notes": cells[3],
                    }
                )

    return proteins


def _parse_related(text, base_path):
    """Parse related links section."""
    related = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if line.startswith("- "):
            line = line[2:]
            # Extract [title](path) — reason
            match = re.match(r"\[([^\]]+)\]\(([^)]+)\)\s*(?:—\s*(.*))?", line)
            if match:
                related.append(
                    {
                        "title": match.group(1),
                        "path": match.group(2),
                        "reason": match.group(3) or "",
                    }
                )
    return related


def generate_page(yaml_data: dict) -> str:
    """Generate a complete method page from YAML data.

    This is the public API function imported by generate_method_page.py.
    """
    return render_method_page(yaml_data)
