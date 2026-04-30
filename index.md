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

| Category | Pages |
|----------|-------|
| Proteins | {{ site.pages | where_exp: "p", "p.path contains 'proteins/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/proteins/index.md' and p.path != 'SCHEMA.md'" | size }} |
| Reagents | {{ site.pages | where_exp: "p", "p.path contains 'reagents/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/reagents/index.md' and p.path != 'SCHEMA.md'" | size }} |
| Methods | {{ site.pages | where_exp: "p", "p.path contains 'methods/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/methods/index.md' and p.path != 'SCHEMA.md'" | size }} |
| Concepts | {{ site.pages | where_exp: "p", "p.path contains 'concepts/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/concepts/index.md' and p.path != 'SCHEMA.md'" | size }} |
| **Total** | **{{ site.pages | where_exp: "p", "p.path contains 'proteins/' or p.path contains 'reagents/' or p.path contains 'methods/' or p.path contains 'concepts/' | where_exp: "p", "p.path contains '.md' and p.path != 'categories/proteins/index.md' and p.path != 'categories/reagents/index.md' and p.path != 'categories/methods/index.md' and p.path != 'categories/concepts/index.md' and p.path != 'SCHEMA.md'" | size }}** |

{% assign stale_count = 0 %}
{% for page in site.pages %}
{% if page.path contains 'proteins/' or page.path contains 'reagents/' or page.path contains 'methods/' or page.path contains 'concepts/' %}
{% if page.path contains '.md' and page.path != 'SCHEMA.md' %}
{% if page.path contains 'index.md' == false %}
{% if page.updated %}
{% assign updated = page.updated | date: "%s" %}
{% assign now = "now" | date: "%s" %}
{% assign diff = now | minus: updated %}
{% if diff > 2592000 %}
{% assign stale_count = stale_count | plus: 1 %}
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}

**{{ stale_count }}** pages not updated in the last 30 days.

For a detailed audit: `python3 scripts/lint.py`