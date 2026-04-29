---
layout: default
title: Methods
---

# Methods

{% for method in site.methods %}
- [{{ method.title }}]({{ method.url | relative_url }})
{% endfor %}
