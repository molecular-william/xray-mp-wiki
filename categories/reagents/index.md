---
layout: default
title: Reagents
---

# Reagents

{% assign reagents_sorted = site.pages | sort: 'path' %}
{% assign current_subdir = "" %}

{% for r in reagents_sorted %}
{% if r.path contains "reagents/" and r.path != "categories/reagents/index.md" %}
{% assign path_parts = r.path | split: "/" %}
{% assign reagent_subdir = path_parts[1] %}

{% if reagent_subdir != current_subdir %}
{% if current_subdir != "" %}</ul>{% endif %}
<h2>{{ reagent_subdir }}</h2>
<ul>
{% endif %}
{% assign current_subdir = reagent_subdir %}
<li><a href="/xray-mp-wiki{{ r.url }}">{{ r.title }}</a></li>
{% endif %}
{% endfor %}
{% if current_subdir != "" %}</ul>{% endif %}
