---
layout: page
title: Projects
---

This page highlights selected AI engineering, machine learning, research, and data science projects.

## Selected Projects

{% for project in site.data.projects %}
<section class="border rounded p-4 mb-4">
  <h3 class="mt-0 mb-1">{{ project.title }}</h3>
  <p class="small text-muted mb-2">{{ project.year }}</p>
  <p>{{ project.summary }}</p>

  <div class="mb-0">
    {% for method in project.methods %}
      <span class="badge badge-secondary mr-1">{{ method }}</span>
    {% endfor %}
  </div>
</section>
{% endfor %}
