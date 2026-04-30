---
layout: default
title: Methods
---

# Methods

{% assign methods_sorted = site.pages | sort: 'title' %}
{% assign current_subdir = "" %}

{% for method in methods_sorted %}
{% if method.path contains "methods/" and method.path != "categories/methods/index.md" %}
{% assign path_parts = method.path | split: "/" %}
{% assign method_subdir = path_parts[1] %}

{% case method_subdir %}
{% when 'cell-lysis' %}{% assign method_subdir = 'Cell Lysis' %}
{% when 'crystallization' %}{% assign method_subdir = 'Crystallization' %}
{% when 'expression-systems' %}{% assign method_subdir = 'Expression Systems' %}
{% when 'purification' %}{% assign method_subdir = 'Purification' %}
{% when 'quality-assessment' %}{% assign method_subdir = 'Quality Assessment' %}
{% when 'solubilization' %}{% assign method_subdir = 'Solubilization' %}
{% when 'structure-determination' %}{% assign method_subdir = 'Structure Determination' %}
{% endcase %}

{% if method_subdir != current_subdir %}
{% if current_subdir != "" %}</ul>{% endif %}
<h2>{{ method_subdir }}</h2>
<ul>
{% endif %}
{% assign current_subdir = method_subdir %}
<li><a href="/xray-mp-wiki{{ method.url }}">{{ method.title }}</a></li>
{% endif %}
{% endfor %}
{% if current_subdir != "" %}</ul>{% endif %}
