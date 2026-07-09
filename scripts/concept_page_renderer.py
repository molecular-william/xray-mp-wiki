#!/usr/bin/env python3
"""
Shared rendering functions for concept wiki pages.

Used by generate_concept_page.py to render complete pages from YAML data.
"""

from _base import render_frontmatter as _base_render_frontmatter


def render_link(path, title):
    """Render a markdown link with absolute path."""
    return f"[{title}]({path})"


def render_frontmatter(data: dict) -> str:
    """Render YAML frontmatter. Delegates to shared _base.render_frontmatter."""
    return _base_render_frontmatter(data, "concept", "concepts")


def _bullet_list(items, fmt):
    """Format a list of items into markdown bullets using format function fmt."""
    if not items:
        return ""
    return "\n".join(f"- {fmt(item)}" for item in items)


def generate_page(yaml_data: dict) -> str:
    """
    Generate a new concept page from YAML metadata.

    The YAML contains structured data (overview, mechanism, examples,
    related_concepts, cross_references) with prose written directly into
    YAML fields. This function renders them into markdown sections.
    """
    frontmatter = render_frontmatter(yaml_data)

    # Convert cross_references[] list to markdown link list
    cross_refs = yaml_data.get("cross_references", [])
    cross_refs_text = _bullet_list(cross_refs, lambda cr: f"[{cr.get('title', '')}]({cr.get('path', '')}) — {cr.get('reason', '')}")
    if not cross_refs_text:
        cross_refs_text = yaml_data.get("cross_refs_text", "")

    # Render examples[] list to markdown bullets
    examples = yaml_data.get("examples", [])
    examples_text = _bullet_list(examples, lambda ex: f"{ex.get('protein', '')} — {ex.get('context', '')}")
    if not examples_text:
        examples_text = yaml_data.get("examples_text", "")

    # Render related_concepts[] list to markdown bullets
    related = yaml_data.get("related_concepts", [])
    def _fmt_rc(rc):
        if isinstance(rc, dict):
            return f"[{rc.get('name', '')}]({rc.get('path', '')}) — {rc.get('relationship', '')}"
        return str(rc)
    related_text = _bullet_list(related, _fmt_rc)
    if not related_text:
        related_text = yaml_data.get("related_concepts_text", "")

    content = f"""{frontmatter}

# {yaml_data["title"]}

## Overview
{yaml_data.get("overview", "")}

## Mechanism/Details
{yaml_data.get("details", yaml_data.get("mechanism", ""))}

## Examples in Membrane Protein Work
{examples_text}

## Related Concepts
{related_text}

## Cross-References
{cross_refs_text}
"""
    return content
