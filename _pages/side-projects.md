---
layout: default
title: "Side Projects"
permalink: /side-projects/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
---

<div class="bloc l-bloc" id="archive-header">
  <div class="container bloc-md bloc-sm-lg">
    <div class="row">
      <div class="col-12">
        {% include breadcrumb.html items=page.breadcrumb %}
        <h1 class="text-bold mb-4">{{ page.title }}</h1>
      </div>
    </div>
  </div>
</div>

<div class="bloc l-bloc background-blocs" id="archive-grid">
  <div class="container bloc-sm bloc-sm-md">
    <div class="row">
      <div class="text-start col-lg-12">
        <div class="blocs-grid-container writer-post-library">
          {% assign items = site.side-projects | sort: 'date' | reverse %}
          {% for item in items %}
          <div class="writer-posts">
            <div>
              <a href="{{ item.url | relative_url }}">
                <picture>
                  <source type="image/webp" srcset="{{ '/assets/images/lazyload-ph.png' | relative_url }}" data-srcset="{{ item.thumbnail_webp | relative_url }}">
                  <img src="{{ '/assets/images/lazyload-ph.png' | relative_url }}" data-src="{{ item.thumbnail | relative_url }}" class="img-fluid mx-auto d-block writer-post-image img-rd-md lazyload" alt="{{ item.title }}" width="398" height="265">
                </picture>
              </a>
              <div class="mt-3 writer-post-group mb-3">
                <p class="mb-0 p-sm">{{ item.date | date: "%b %d, %Y" }}</p>
                <span class="post-label">{{ item.category }}</span>
              </div>
              <a href="{{ item.url | relative_url }}" class="a-btn a-block tital-post mt-0 mb-2">{{ item.title }}</a>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>
