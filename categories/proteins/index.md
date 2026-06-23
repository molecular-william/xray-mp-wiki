---
layout: default
title: Proteins
---

# Proteins

{% assign proteins_sorted = site.pages | sort: 'path' %}
{% assign current_subdir = "" %}

{% for p in proteins_sorted %}
{% if p.path contains "proteins/" and p.path != "categories/proteins/index.md" %}
{% assign path_parts = p.path | split: "/" %}
{% assign protein_subdir = path_parts[1] %}

{% case protein_subdir %}
{% when 'gpcr' %}{% assign display = 'GPCRs' %}
{% when 'rhodopsins' %}{% assign display = 'Rhodopsins' %}
{% when 'voltage-gated-channels' %}{% assign display = 'Voltage-Gated Ion Channels' %}
{% when 'cys-loop-receptors' %}{% assign display = 'Cys-Loop Receptors' %}
{% when 'other-ion-channels' %}{% assign display = 'Other Ion Channels' %}
{% when 'abc-transporters' %}{% assign display = 'ABC Transporters' %}
{% when 'mfs-transporters' %}{% assign display = 'MFS Transporters' %}
{% when 'slc-transporters' %}{% assign display = 'SLC Family Transporters' %}
{% when 'pumps-atpases' %}{% assign display = 'Pumps & ATPases' %}
{% when 'secretion-translocon' %}{% assign display = 'Secretion & Translocon' %}
{% when 'photosynthesis' %}{% assign display = 'Photosynthesis' %}
{% when 'enzymes' %}{% assign display = 'Membrane Enzymes' %}
{% when 'structural-adhesion' %}{% assign display = 'Structural & Adhesion' %}
{% when 'toxins' %}{% assign display = 'Pore-Forming Toxins' %}
{% when 'receptors-signaling' %}{% assign display = 'Receptors & Signaling' %}
{% when 'miscellaneous' %}{% assign display = 'Miscellaneous' %}
{% else %}{% assign display = protein_subdir %}
{% endcase %}

{% if protein_subdir != current_subdir %}
{% if current_subdir != "" %}</ul>{% endif %}
<h2>{{ display }}</h2>
<ul>
{% endif %}
{% assign current_subdir = protein_subdir %}
<li><a href="/xray-mp-wiki{{ p.url }}">{{ p.title }}</a></li>
{% endif %}
{% endfor %}
{% if current_subdir != "" %}</ul>{% endif %}