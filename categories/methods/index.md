---
layout: default
title: Methods
---

# Methods

{% assign methods_sorted = site.pages | sort: 'path' %}
{% assign current_subdir = "" %}

{% for method in methods_sorted %}
{% if method.path contains "methods/" and method.path != "categories/methods/index.md" %}
{% assign path_parts = method.path | split: "/" %}
{% assign method_subdir = path_parts[1] %}

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
