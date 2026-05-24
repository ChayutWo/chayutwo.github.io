---
layout: page
title: Projects
---

This page highlights selected AI engineering, machine learning, research, and data science projects.

## Selected Projects

{% for project in site.data.projects %}
<section class="border rounded p-4 mb-4">
  <h3 class="mt-0">{{ project.title }}</h3>
  <p>{{ project.summary }}</p>

  <div class="mb-3">
    {% for tag in project.tags %}
      <span class="badge badge-secondary mr-1">{{ tag }}</span>
    {% endfor %}
  </div>

  <p class="mb-1"><strong>Methods:</strong> {{ project.methods | join: ", " }}</p>
  <p class="mb-2"><strong>Stack:</strong> {{ project.stack | join: ", " }}</p>

  <p class="small text-muted mb-0">
    <strong>Visibility:</strong> {{ project.visibility }} ·
    <strong>Status:</strong> {{ project.status }}
  </p>
</section>
{% endfor %}
