---
layout: workshop
title: "Photo Contest — Life Sciences Vienna"
date: 2026-04-09
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/ice-contest.jpg"
thumbnail_webp: "/assets/images/content/ice-contest.webp"
hero_combined: true
subtitle: "Apr 09, 2026"
description: "Glacier ice on black volcanic sand at Jökulsárlón, Iceland. Entry for the 'Diversity of Life' photo contest, Faculty of Life Sciences, University of Vienna."
tags: [photography, photo-contest]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "Photo Contest"
---

<h2 class="text-center fst-italic">Global Change</h2>

<picture>
  <source type="image/webp" srcset="/assets/images/content/ice-contest.webp">
  <img src="/assets/images/content/ice-contest.jpg" class="img-fluid mx-auto d-block img-rd-md photo-border photo-tile" alt="Ice fragment on black sand beach, Iceland" loading="lazy">
</picture>

> In the age of the Anthropocene, even small coastal scenes echo the planetary transformations reshaping ecosystems. My research examines these shifting patterns as life reorganizes across space and time. © 2026 Gilles Colling

This was taken on the black sand beach at Jökulsárlón, Iceland, where icebergs calved from the Breiðamerkurjökull glacier wash up, melt for a few hours, and disappear back into the sea. The piece of ice in the foreground had probably been on the beach for less than a day when I photographed it. The black sand is volcanic basalt. The ocean behind it is the North Atlantic.

Glacier ice that may have been compressed for centuries, sitting on volcanic sand, slowly returning to water. The whole scene lasts a few hours, then it is gone.

## The contest

The [Life Sciences Faculty photo contest](https://lifesciences.univie.ac.at/innovation-impact/photo-contest/), "Diversity of Life", asks students and staff for self-taken photos from research, fieldwork, or experimental settings. My research looks at how species distributions shift under global change: how life reorganizes across space and time as climate, land use, and disturbance reshape ecosystems.

Glacier retreat is one of the clearest signals of that reorganization. The beach at Jökulsárlón did not look like this fifty years ago. The glacier has retreated several kilometres since the 1930s; the lagoon it created (now the largest in Iceland) grows every decade. What looks like an otherworldly scene is also a record of that retreat.

<script>
(function () {
  var tiles = document.querySelectorAll('.photo-tile');
  if (!tiles.length) return;

  var overlay = document.createElement('div');
  overlay.className = 'photo-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('aria-label', 'Photo viewer');
  overlay.innerHTML = '<button type="button" class="photo-overlay-close" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></svg></button><img alt="">';
  document.body.appendChild(overlay);

  var overlayImg = overlay.querySelector('img');
  var closeBtn = overlay.querySelector('.photo-overlay-close');

  function open(src, alt) {
    overlayImg.src = src;
    overlayImg.alt = alt || '';
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function close() {
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
    overlayImg.src = '';
  }

  tiles.forEach(function (tile) {
    tile.setAttribute('role', 'button');
    tile.setAttribute('tabindex', '0');
    tile.addEventListener('click', function () {
      open(tile.currentSrc || tile.src, tile.alt);
    });
    tile.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        open(tile.currentSrc || tile.src, tile.alt);
      }
    });
  });

  overlay.addEventListener('click', function () {
    close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) close();
  });
})();
</script>
