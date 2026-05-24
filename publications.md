---
layout: page
title: Research and Publication
---

{% for publication in site.data.publications %}
<section class="mb-4">
  <h3 class="mb-1">
    {% if publication.url %}
      <a href="{{ publication.url }}">{{ publication.title }}</a>
    {% else %}
      {{ publication.title }}
    {% endif %}
  </h3>
  <p class="mb-1">{{ publication.authors }}</p>
  <p class="mb-1">
    <em>{{ publication.venue }}</em>{% if publication.year %}, {{ publication.year }}{% endif %}
  </p>
  <p class="small text-muted mb-0">
    {{ publication.type }}{% if publication.doi %} | DOI: {{ publication.doi }}{% endif %}
  </p>
</section>
{% endfor %}
