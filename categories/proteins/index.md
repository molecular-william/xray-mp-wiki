---
layout: default
title: Proteins
---

# Proteins

{% assign proteins_sorted = site.pages | sort: 'title' %}
{% for p in proteins_sorted %}
{% if p.path contains "proteins/" and p.path != "categories/proteins/index.md" %}
- [{{ p.title }}](/xray-mp-wiki{{ p.url }})
{% endif %}
{% endfor %}