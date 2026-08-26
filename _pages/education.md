---
layout: default
title: "Education"
permalink: /education/
description: "Workshops, courses, and educational materials by Gilles Colling on ecology, R programming, and data science."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
---

<div class="section section-light" id="archive-header">
  <div class="container pad-sm pb-0">
    <div class="row">
      <div class="col-12">
        {% include breadcrumb.html items=page.breadcrumb %}
        <h1 class="text-bold mb-2">{{ page.title }}</h1>
        {% include type-filter.html types="workshop:Workshops,course:Courses" %}
      </div>
    </div>
  </div>
</div>

<div class="section section-light background-gradient" id="archive-grid">
  <div class="container pad-sm pad-sm-md">
    <div class="row">
      <div class="text-start col-lg-12">
        <div class="blocs-grid-container writer-post-library">
          {% assign course_overviews = site.courses | where: "layout", "course-overview" %}
          {% assign items = site.workshops | concat: course_overviews | sort: 'date' | reverse %}
          {% for item in items %}
          {% include archive-card.html item=item category_url="/education/" %}
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>
