---
layout: default
title: "Side Projects"
permalink: /side-projects/
description: "R packages, open-source tools, and side projects by Gilles Colling — corrselect, hexify, ggguides, and more."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
---

<div class="section section-light" id="archive-header">
  <div class="container pad-sm pb-0">
    <div class="row">
      <div class="col-12">
        {% include breadcrumb.html items=page.breadcrumb %}
        <h1 class="text-bold mb-2">{{ page.title }}</h1>
        {% include type-filter.html types="package:R packages,competition:Competitions,book:Books" %}
      </div>
    </div>
  </div>
</div>

<div class="section section-light background-gradient" id="archive-grid">
  <div class="container pad-sm pad-sm-md">
    <div class="row">
      <div class="text-start col-lg-12">
        <div class="blocs-grid-container writer-post-library">
          {% assign items = site.side-projects | sort: 'date' | reverse %}
          {% for item in items %}
          {% include archive-card.html item=item category_url="/side-projects/" %}
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>
