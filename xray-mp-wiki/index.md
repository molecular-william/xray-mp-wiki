---
title: X-ray MP Wiki
---

This is a wiki on reagents and procedures for X-ray crystallography of membrane proteins.

## At a Glance

{% if site.data.stats %}
| Metric | Value |
|--------|-------|
| Total pages | {{ site.data.stats.entities.total_pages }} |
| Protein entries | {{ site.data.stats.entities.proteins }} |
| Reagent entries | {{ site.data.stats.entities.reagents }} |
| Method entries | {{ site.data.stats.entities.methods }} |
| Concept entries | {{ site.data.stats.entities.concepts }} |
| Total distinct structures | {{ site.data.stats.entities.total_structures }} |
| Mean resolution | {{ site.data.stats.resolution.mean }} Å |
| Median resolution | {{ site.data.stats.resolution.median }} Å |

### Top 10 Detergents

| Detergent | Proteins using it |
|-----------|------------------|
{% for d in site.data.stats.top_detergents -%}
| {{ d.name }} | {{ d.count }} |
{% endfor %}

### Top 10 Protein Families

| Family | Structures |
|--------|-----------|
{% for f in site.data.stats.top_families -%}
| {{ f.name }} | {{ f.count }} |
{% endfor %}

### Most Common Expression Systems

| System | Proteins |
|--------|---------|
{% for e in site.data.stats.top_expressions -%}
| {{ e.name }} | {{ e.count }} |
{% endfor %}
{% endif %}

## Browse by Category

- [Proteins](/xray-mp-wiki/categories/proteins/) — 800 entries across 16 families (GPCRs, transporters, channels, enzymes, and more)
- [Reagents](/xray-mp-wiki/categories/reagents/) — 815 entries: detergents, buffers, additives, lipids, ligands, tags, antibodies
- [Methods](/xray-mp-wiki/categories/methods/) — 70 entries: crystallization, purification, expression systems, structure determination
- [Concepts](/xray-mp-wiki/categories/concepts/) — 483 entries: transport mechanisms, structural motifs, protein families, signaling
- [📊 Knowledge Graph](/xray-mp-wiki/graph/) — Interactive network of all 2,100+ entities with 9,600+ relationships
- [🔍 Search](/xray-mp-wiki/search/) — Full-text search across all entities

## Getting Started

- **Crystallizing a GPCR?** → Browse the [GPCR category](/xray-mp-wiki/proteins/gpcr/). Most GPCRs use **DDM** or **LMNG** with **LCP crystallization**. Common additives: CHS, BRIL fusion.
- **Crystallizing a transporter?** → Browse the [ABC transporters](/xray-mp-wiki/proteins/abc-transporters/), [MFS transporters](/xray-mp-wiki/proteins/mfs-transporters/), or [SLC transporters](/xray-mp-wiki/proteins/slc-transporters/). These often use **DM**, **UDM**, or **DDM** with **vapor diffusion**.
- **Choosing a detergent?** → Check the [detergents list](/xray-mp-wiki/reagents/detergents/). DDM is most common ({{ site.data.stats.top_detergents[0].count }} proteins), followed by CHS ({{ site.data.stats.top_detergents[1].count }}), DM ({{ site.data.stats.top_detergents[2].count }}), and LMNG ({{ site.data.stats.top_detergents[3].count }}).

## Recently Updated

{% assign recent = site.pages | where_exp:"p","p.updated" | sort:"updated" | reverse | limit:10 %}
{% for p in recent %}
- [{{ p.title }}]({{ p.url }}) — updated {{ p.updated }}
{% endfor %}

## Health

Last built: {{ site.time | date: "%Y-%m-%d %H:%M" }}

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

## Documentation

- [Wiki Reference](https://github.com/molecular-william/xray-mp-wiki/blob/main/references/WIKI-REFERENCE.md) — Domain, conventions, directory structure, entity page structures, tag taxonomy, correction policy, source-truth verification
- [Wiki Workflow](https://github.com/molecular-william/xray-mp-wiki/blob/main/references/WIKI-WORKFLOW.md) — Complete per-entity workflows: YAML schemas, generate/update commands, merge rules, pitfalls
- [Wiki Scripts](https://github.com/molecular-william/xray-mp-wiki/blob/main/references/WIKI-SCRIPTS.md) — Script inventory, usage, architecture, testing

<!-- WIKI CATALOG -->
{% for page in site.pages %}{% if page.path contains '.md' and page.path contains '/proteins/' or page.path contains '/reagents/' or page.path contains '/methods/' or page.path contains '/concepts/' %}| {{ page.path }} | {{ page.title }} |
{% endif %}{% endfor %}
