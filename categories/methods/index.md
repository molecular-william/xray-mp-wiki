---
layout: default
title: Methods
---

# Methods

{% assign methods = site.pages | where:"type", "method" %}
{% for method in methods %}
- [{{ method.title }}]({{ method.url | relative_url }})
{% endfor %}
