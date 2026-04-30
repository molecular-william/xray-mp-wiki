---
layout: default
title: Wiki Health
---

# Wiki Health

Last updated: {{ site.time | date: "%Y-%m-%d" }}

## Page Counts

| Category | Pages |
|----------|-------|
| Proteins | {{ site.pages | where_exp: "p", "p.path contains 'proteins/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/proteins/index.md' and p.path != 'SCHEMA.md'" | size }} |
| Reagents | {{ site.pages | where_exp: "p", "p.path contains 'reagents/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/reagents/index.md' and p.path != 'SCHEMA.md'" | size }} |
| Methods | {{ site.pages | where_exp: "p", "p.path contains 'methods/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/methods/index.md' and p.path != 'SCHEMA.md'" | size }} |
| Concepts | {{ site.pages | where_exp: "p", "p.path contains 'concepts/' and p.path contains '.md'" | where_exp: "p", "p.path != 'categories/concepts/index.md' and p.path != 'SCHEMA.md'" | size }} |
| **Total** | **{{ site.pages | where_exp: "p", "p.path contains 'proteins/' or p.path contains 'reagents/' or p.path contains 'methods/' or p.path contains 'concepts/' | where_exp: "p", "p.path contains '.md' and p.path != 'categories/proteins/index.md' and p.path != 'categories/reagents/index.md' and p.path != 'categories/methods/index.md' and p.path != 'categories/concepts/index.md' and p.path != 'SCHEMA.md'" | size }}** |

## Type Breakdown

| Type | Pages |
|------|-------|
| Protein | {{ site.pages | where_exp: "p", "p.type == 'protein'" | size }} |
| Reagent | {{ site.pages | where_exp: "p", "p.type == 'reagent'" | size }} |
| Method | {{ site.pages | where_exp: "p", "p.type == 'method'" | size }} |
| Concept | {{ site.pages | where_exp: "p", "p.type == 'concept'" | size }} |

## Issues

### Stale Pages (>30 days since update)

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

**{{ stale_count }}** pages not updated in the last 30 days

### Pages Missing Layout

{% assign layout_issues = 0 %}
{% for page in site.pages %}
{% if page.path contains 'proteins/' or page.path contains 'reagents/' or page.path contains 'methods/' or page.path contains 'concepts/' %}
{% if page.path contains '.md' and page.path != 'SCHEMA.md' %}
{% if page.path contains 'index.md' == false %}
{% unless page.layout == 'default' %}
{% assign layout_issues = layout_issues | plus: 1 %}
{% endunless %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}

**{{ layout_issues }}** pages missing `layout: default`

### Other Checks

- **Orphan pages** — run `python3 scripts/lint.py`
- **Duplicate sections** — run `python3 scripts/lint.py`
- **Low outbound links** — run `python3 scripts/lint.py`
- **Frontmatter consistency** — run `python3 scripts/lint.py`
- **Broken links** — run `python3 scripts/lint.py`

---

*For a detailed audit, run: `python3 scripts/lint.py` from the project root.*