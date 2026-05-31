---
layout: page
title: Research and Publication
---

{% for publication in site.data.publications %}
{% assign publication_type = publication.type %}
{% if publication.type == "article" %}
  {% assign publication_type = "Journal Article" %}
{% elsif publication.type == "inproceedings" %}
  {% assign publication_type = "Conference Paper" %}
{% elsif publication.type == "misc" %}
  {% assign publication_type = "Preprint" %}
{% endif %}
<section class="border rounded p-4 mb-4">
  {% if publication.year %}
    <p class="small text-muted mb-1">{{ publication.year }}</p>
  {% endif %}
  <h3 class="h4 mt-0 mb-2">
    {% if publication.url %}
      <a href="{{ publication.url }}">{{ publication.title }}</a>
    {% else %}
      {{ publication.title }}
    {% endif %}
  </h3>
  <p class="mb-2">{{ publication.authors }}</p>
  <p class="mb-2"><em>{{ publication.venue }}</em></p>
  <div class="small mb-0">
    <span class="badge mr-2" style="background-color: #e8f0fe; color: #000;">{{ publication_type }}</span>
    {% if publication.doi %}
      <a class="mr-2" href="https://doi.org/{{ publication.doi }}">DOI</a>
    {% endif %}
    {% if publication.url %}
      <a href="{{ publication.url }}">Link</a>
    {% endif %}
  </div>
</section>
{% endfor %}
