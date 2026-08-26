---
layout: default
title: "Presentations"
permalink: /presentations/
description: "Conference talks and presentations by Gilles Colling on ecology, alien species, and spatial statistics."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Research"
    url: "/research-archive/"
  - name: "Presentations"
---

<div class="section section-light" id="archive-header">
  <div class="container pad-sm pb-0">
    <div class="row">
      <div class="col-12">
        {% include breadcrumb.html items=page.breadcrumb %}
        <h1 class="text-bold mb-2">{{ page.title }}</h1>
        {% include type-filter.html types="talk:Talks,poster:Posters" %}
      </div>
    </div>
  </div>
</div>

<div class="section section-light background-gradient" id="archive-grid">
  <div class="container pad-sm pad-sm-md">
    <div class="row">
      <div class="text-start col-lg-12">
        <div class="blocs-grid-container writer-post-library">
          {% assign items = site.presentations | sort: 'date' | reverse %}
          {% for item in items %}
          {% include archive-card.html item=item category_url="/presentations/" %}
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>

<div class="section section-light" id="archive-list">
  <div class="container pad-sm pad-sm-md">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="text-bold mb-4">List</h2>
        {% assign items = site.presentations | sort: 'date' | reverse %}
        {% assign years = items | map: 'date' | map: 'year' %}
        {% assign current_year = "" %}
        <dl class="pres-list">
        {% for item in items %}
          {% assign year = item.date | date: "%Y" %}
          {% if year != current_year %}
            {% assign current_year = year %}
            <dt class="pres-list-year">{{ year }}</dt>
          {% endif %}
          <dd class="pres-list-item" data-type="{{ item.type | default: 'talk' }}">
            <span class="pres-list-date">{{ item.date | date: "%b %d" }}</span>
            <span class="pres-list-type post-label">{{ item.type | default: 'talk' | capitalize }}</span>
            <span class="pres-list-body">
              <a href="{{ item.url | relative_url }}" class="pres-list-title">{{ item.hero_title | default: item.title }}</a>
              {% if item.hero_title %}<span class="pres-list-venue tc-text-muted">{{ item.title }}</span>{% endif %}
              {% if item.downloads %}
              <span class="pres-list-downloads">
                {% for d in item.downloads %}<a href="{{ d.url | relative_url }}" target="_blank" rel="noopener">{{ d.name }}</a>{% endfor %}
              </span>
              {% endif %}
            </span>
          </dd>
        {% endfor %}
        </dl>
      </div>
    </div>
  </div>
</div>

