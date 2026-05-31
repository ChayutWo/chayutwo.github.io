---
layout: page
title: Projects
---

{% for project in site.data.projects %}
<section class="border rounded p-4 mb-4">
  <h3 class="mt-0 mb-1">{{ project.title }}</h3>
  <p class="small text-muted mb-2">{{ project.year }}</p>
  <p>{{ project.summary }}</p>

  <div class="mb-0">
    {% for method in project.methods %}
      <span class="badge mr-1" style="background-color: #e8f0fe; color: #000;">{{ method }}</span>
    {% endfor %}
  </div>
</section>
{% endfor %}
