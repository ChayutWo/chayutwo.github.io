---
layout: page
title: Projects
---

This page highlights selected AI engineering, machine learning, research, and data science projects.

## Selected Projects

{% for project in site.data.projects %}
<section>
  <h3>{{ project.title }}</h3>
  <p>{{ project.summary }}</p>

  <p><strong>Tags:</strong> {{ project.tags | join: ", " }}</p>
  <p><strong>Methods:</strong> {{ project.methods | join: ", " }}</p>
  <p><strong>Stack:</strong> {{ project.stack | join: ", " }}</p>
  <p><strong>Visibility:</strong> {{ project.visibility }}</p>
  <p><strong>Status:</strong> {{ project.status }}</p>
</section>
{% endfor %}
