---
layout: default
title: Buffers
---

# Buffers

{% assign buffers = site.pages | where:"type", "buffer" %}
{% for buffer in buffers %}
- [{{ buffer.title }}]({{ buffer.url | relative_url }})
{% endfor %}
