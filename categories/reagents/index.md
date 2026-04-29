---
layout: default
title: Reagents
---

# Reagents

## Detergents
{% for reagent in site.reagents %}
{% if reagent.tags contains "detergent" or reagent.tags contains "detergent-" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}

## Buffers
{% for reagent in site.reagents %}
{% if reagent.tags contains "buffer" or reagent.tags contains "buffer-" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}

## Additives
{% for reagent in site.reagents %}
{% if reagent.tags contains "additive" or reagent.tags contains "additive-" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}

## Lipids
{% for reagent in site.reagents %}
{% if reagent.tags contains "lipid" or reagent.tags contains "lipid-" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}

## Ligands
{% for reagent in site.reagents %}
{% if reagent.tags contains "ligand" or reagent.tags contains "ligand-" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}

## Protein Tags
{% for reagent in site.reagents %}
{% if reagent.tags contains "tag" or reagent.tags contains "protein-tag" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}

## Antibodies
{% for reagent in site.reagents %}
{% if reagent.tags contains "antibody" or reagent.tags contains "nanobody" or reagent.tags contains "fab" or reagent.tags contains "scfv" %}
- [{{ reagent.title }}]({{ reagent.url | relative_url }})
{% endif %}
{% endfor %}
