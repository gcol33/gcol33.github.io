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
        <div class="pres-filter mt-3" role="group" aria-label="Filter by type">
          <button type="button" class="pres-filter-btn active" data-filter="all">All</button>
          <button type="button" class="pres-filter-btn" data-filter="talk">Talks</button>
          <button type="button" class="pres-filter-btn" data-filter="poster">Posters</button>
        </div>
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
          <div class="writer-posts" data-type="{{ item.type | default: 'talk' }}">
            <div>
              <a href="{{ item.url | relative_url }}">
                <picture>
                  <source type="image/webp" srcset="{{ '/assets/images/lazyload-ph.png' | relative_url }}" data-srcset="{{ item.thumbnail_webp | relative_url }}">
                  <img src="{{ '/assets/images/lazyload-ph.png' | relative_url }}" data-src="{{ item.thumbnail | relative_url }}" class="img-fluid mx-auto d-block writer-post-image img-rd-md lazyload" alt="{{ item.title }}" width="398" height="265" loading="lazy">
                </picture>
              </a>
              <div class="mt-3 writer-post-group mb-3">
                <p class="mb-0 p-sm">{{ item.date | date: "%b %d, %Y" }}</p>
                <a href="{{ item.category_url | default: '/presentations/' | relative_url }}" class="a-btn post-label">{{ item.type | default: 'talk' | capitalize }}</a>
              </div>
              <a href="{{ item.url | relative_url }}" class="a-btn a-block title-post mt-0 mb-2">{{ item.short_title | default: item.title }}</a>
            </div>
          </div>
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

<script>
(function () {
  var buttons = document.querySelectorAll('.pres-filter-btn');
  var items = document.querySelectorAll('[data-type]');
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.getAttribute('data-filter');
      buttons.forEach(function (b) { b.classList.toggle('active', b === btn); });
      items.forEach(function (el) {
        el.hidden = f !== 'all' && el.getAttribute('data-type') !== f;
      });
      document.querySelectorAll('.pres-list-year').forEach(function (yr) {
        var n = yr.nextElementSibling, any = false;
        while (n && n.tagName === 'DD') { if (!n.hidden) any = true; n = n.nextElementSibling; }
        yr.hidden = !any;
      });
    });
  });
})();
</script>
