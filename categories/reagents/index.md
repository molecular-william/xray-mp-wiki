---
layout: default
title: Reagents
---

# Reagents

## Detergents
{% assign detergents = site.reagents | where_exp: "item", "item.tags contains 'detergent' or item.tags contains 'detergent-' %}
{% for reagent in detergents %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}

## Buffers
{% assign buffers = site.reagents | where_exp: "item", "item.tags contains 'buffer' or item.tags contains 'buffer-' %}
{% for reagent in buffers %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}

## Additives
{% assign additives = site.reagents | where_exp: "item", "item.tags contains 'additive' or item.tags contains 'additive-' %}
{% for reagent in additives %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}

## Lipids
{% assign lipids = site.reagents | where_exp: "item", "item.tags contains 'lipid' or item.tags contains 'lipid-' %}
{% for reagent in lipids %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}

## Ligands
{% assign ligands = site.reagents | where_exp: "item", "item.tags contains 'ligand' or item.tags contains 'ligand-' %}
{% for reagent in ligands %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}

## Protein Tags
{% assign tags = site.reagents | where_exp: "item", "item.tags contains 'tag' or item.tags contains 'protein-tag' %}
{% for reagent in tags %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}

## Antibodies
{% assign antibodies = site.reagents | where_exp: "item", "item.tags contains 'antibody' or item.tags contains 'nanobody' or item.tags contains 'fab' or item.tags contains 'scfv' %}
{% for reagent in antibodies %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endfor %}
