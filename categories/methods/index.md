---
layout: default
title: Methods
---

# Methods

{% assign methods = site.methods %}
{% for method in methods %}
- [{{ method.title }}]({{ method.url | relative_url }})
{% endfor %}
