---
layout: page
title: Research and Publication
---

<style>
.post-heading h1 {
  font-size: 3.5rem;
  line-height: 1.1;
}
</style>

{% for publication in site.data.publications %}
{% assign publication_type = publication.type %}
{% if publication.type == "article" %}
  {% assign publication_type = "Journal Article" %}
{% elsif publication.type == "inproceedings" %}
  {% assign publication_type = "Conference Paper" %}
{% elsif publication.type == "misc" %}
  {% assign publication_type = "Preprint" %}
{% endif %}
<section class="border rounded px-3 py-2 mb-3">
  {% if publication.year %}
    <p class="small text-muted mb-1">{{ publication.year }}</p>
  {% endif %}
  <h3 class="mt-0 mb-1">
    {% if publication.url %}
      <a href="{{ publication.url }}" style="font-size: 1.05rem; line-height: 1.3; font-weight: 700; color: #333; text-decoration: none;">{{ publication.title }}</a>
    {% else %}
      <span style="font-size: 1.05rem; line-height: 1.3; font-weight: 700; color: #333; text-decoration: none;">{{ publication.title }}</span>
    {% endif %}
  </h3>
  <p class="mb-1" style="font-size: 0.95rem;">{{ publication.authors }}</p>
  <p class="mb-1" style="font-size: 0.95rem;"><em>{{ publication.venue }}</em></p>
  <div class="small mb-0">
    <span class="badge mr-2" style="background-color: #e8f0fe; color: #000; font-size: 0.8rem; padding: 0.35em 0.55em;">{{ publication_type }}</span>
    {% if publication.doi %}
      <a class="mr-2" href="https://doi.org/{{ publication.doi }}">DOI</a>
    {% endif %}
    {% if publication.url %}
      <a href="{{ publication.url }}">Link</a>
    {% endif %}
  </div>
</section>
{% endfor %}
