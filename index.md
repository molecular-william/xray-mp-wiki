---
title: X-ray MP Wiki
---

This is a wiki on reagents and procedures for X-ray crystallography of membrane proteins.

## Categories

- [Proteins](/xray-mp-wiki/categories/proteins/) - All protein pages
- [Reagents](/xray-mp-wiki/categories/reagents/) - Detergents, buffers, additives, lipids, ligands
- [Methods](/xray-mp-wiki/categories/methods/) - Crystallization, purification, expression systems
- [Concepts](/xray-mp-wiki/categories/concepts/) - Scientific concepts and mechanisms

## Content

This wiki contains pages organized into the categories above. Browse the category pages to find content on specific topics.

## Documentation

See [SCHEMA.md](/xray-mp-wiki/SCHEMA.md) for the wiki structure and schema.

## Health

Last updated: {{ site.time | date: "%Y-%m-%d" }}

{% assign protein_count = 0 %}
{% assign reagent_count = 0 %}
{% assign method_count = 0 %}
{% assign concept_count = 0 %}
{% assign total_count = 0 %}

{% for page in site.pages %}
{% if page.path contains '.md' %}
{% unless page.path contains 'index.md' %}
{% unless page.path contains 'SCHEMA' %}
{% assign total_count = total_count | plus: 1 %}
{% if page.path contains 'proteins/' %}
{% assign protein_count = protein_count | plus: 1 %}
{% elsif page.path contains 'reagents/' %}
{% assign reagent_count = reagent_count | plus: 1 %}
{% elsif page.path contains 'methods/' %}
{% assign method_count = method_count | plus: 1 %}
{% elsif page.path contains 'concepts/' %}
{% assign concept_count = concept_count | plus: 1 %}
{% endif %}
{% endunless %}
{% endunless %}
{% endif %}
{% endfor %}

| Category | Pages |
|----------|-------|
| Proteins | {{ protein_count }} |
| Reagents | {{ reagent_count }} |
| Methods | {{ method_count }} |
| Concepts | {{ concept_count }} |
| **Total** | **{{ total_count }}** |

{% assign stale_count = 0 %}
{% for page in site.pages %}
{% if page.path contains 'proteins/' or page.path contains 'reagents/' or page.path contains 'methods/' or page.path contains 'concepts/' %}
{% if page.path contains '.md' %}
{% unless page.path contains 'index.md' %}
{% unless page.path contains 'SCHEMA' %}
{% if page.updated %}
{% assign updated = page.updated | date: "%s" %}
{% assign now = "now" | date: "%s" %}
{% assign diff = now | minus: updated %}
{% if diff > 2592000 %}
{% assign stale_count = stale_count | plus: 1 %}
{% endif %}
{% endif %}
{% endunless %}
{% endunless %}
{% endif %}
{% endif %}
{% endfor %}

**{{ stale_count }}** pages not updated in the last 30 days.

For a detailed audit: `python3 ~/Desktop/Research/coding_projects/xray-mp-wiki/scripts/lint.py`