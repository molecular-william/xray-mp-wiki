---
layout: default
title: Concepts
---

# Concepts

{% assign concepts_sorted = site.pages | sort: 'path' %}
{% assign current_subdir = "" %}

{% for c in concepts_sorted %}
{% if c.path contains "concepts/" and c.path != "categories/concepts/index.md" %}
{% assign path_parts = c.path | split: "/" %}
{% assign concept_subdir = path_parts[1] %}

{% case concept_subdir %}
{% when 'transport-mechanisms' %}{% assign display = 'Transport Mechanisms' %}
{% when 'signaling-receptors' %}{% assign display = 'Signaling & Receptors' %}
{% when 'structural-mechanisms' %}{% assign display = 'Structural Mechanisms' %}
{% when 'protein-families' %}{% assign display = 'Protein Families' %}
{% when 'enzyme-mechanisms' %}{% assign display = 'Enzyme & Catalytic Mechanisms' %}
{% when 'rhodopsin-mechanisms' %}{% assign display = 'Rhodopsin Mechanisms' %}
{% when 'membrane-mimetics' %}{% assign display = 'Membrane Mimetics' %}
{% when 'methods-techniques' %}{% assign display = 'Methods & Techniques' %}
{% when 'construct-design' %}{% assign display = 'Construct Design' %}
{% when 'miscellaneous' %}{% assign display = 'Miscellaneous' %}
{% else %}{% assign display = concept_subdir %}
{% endcase %}

{% if concept_subdir != current_subdir %}
{% if current_subdir != "" %}</ul>{% endif %}
<h2>{{ display }}</h2>
<ul>
{% endif %}
{% assign current_subdir = concept_subdir %}
<li><a href="/xray-mp-wiki{{ c.url }}">{{ c.title }}</a></li>
{% endif %}
{% endfor %}
{% if current_subdir != "" %}</ul>{% endif %}