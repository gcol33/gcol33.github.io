---
layout: workshop
title: "Visualize your Science — Spring 2026"
short_title: "Visualize your Science"
date: 2026-05-06
category: "Education"
category_url: "/education/"
thumbnail: "/assets/images/content/vys_2026_poster.jpg"
thumbnail_webp: "/assets/images/content/vys_2026_poster.webp"
thumbnail_zoom: true
hero_combined: true
description: "A three-week PhD course on scientific communication and visual design, producing a graphical abstract and a scientific poster for the RESOLVE project."
hero_title: "Visualize your Science — Spring 2026"
tags: [scientific-communication, poster-design, data-visualization, phd-training, resolve]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Visualize your Science 2026"
downloads:
  - name: "Diploma (PDF)"
    url: "/assets/downloads/vys_2026_diploma.pdf"
---

[Visualize your Science](https://www.visualizeyourscience.com) is an online PhD course by Andreas Dahlin on scientific communication and visual design, equivalent to four ECTS credits. The Spring 2026 edition ran from 10 March to 8 May 2026 and was structured around 22 video modules, four graded assignments with individual feedback meetings, and optional live drawing workshops.

## What the course covers

The foundational modules covered how images function in science: file formats, colour theory, typography, layout, composition, and image ethics. A module on data visualisation addressed representing quantitative information without distortion. The poster-specific modules moved into harder design problems: building hierarchy in a dense layout, getting content density and legibility to coexist, and making the whole thing read as one visual argument.

The production half introduced vector drawing from scratch in Affinity Designer (with Illustrator and Inkscape as alternatives): basic shapes and clip art, gradient drawing, tracing techniques, and document setup for A0 print. The final section covered poster presentation: pitching the work in under two minutes and using the poster as a visual aid during conversation.

## Assignment 1 — learning to draw

The first assignment was to draw a favourite research item or kitchen appliance in vector graphics. I drew a golden spatula.

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-6 col-md-3 col-lg-2">
<img src="/assets/images/content/vys_2026_spatula.svg" class="img-fluid d-block mx-auto zoomable" alt="Vector drawing of a golden spatula — Assignment 1 for Visualize your Science">
<p class="text-center mt-2"><i>Assignment 1 — golden spatula</i></p>
</div>
</div>

## Graphical abstract

The second assignment asked for a graphical abstract summarising a current research project. I made one for RESOLVE, the multi-layer perceptron I train on European vegetation data to recover environmental context from species lists. The abstract reduces the model to its essential logic: species composition, taxonomy, and plot covariates flow in; area, slope, altitude, habitat type, and geographic location come out.

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-10 col-md-8 col-lg-6">
<picture>
<source type="image/webp" srcset="/assets/images/content/vys_2026_graphical_abstract.webp">
<img src="/assets/images/content/vys_2026_graphical_abstract.jpg" class="img-fluid d-block img-rd-md mx-auto zoomable" alt="Graphical abstract: Decoding environment from plant community data — species, taxonomy, and covariates feed into an MLP that outputs area, slope, altitude, habitat, and location">
</picture>
<p class="text-center mt-2"><i>Assignment 2 — graphical abstract: Decoding environment from plant community data</i></p>
</div>
</div>

## Scientific poster

The final assignment was a scientific poster. I put together a conference-ready RESOLVE poster, under the title *Neural networks reconstruct landscape properties from plant species composition*, co-authored with B. Lenzner, M. Glaser, H. Seebens, the EVA data contributors, S. Dullinger, and F. Essl.

The poster runs across four panels. The first covers the dataset (1.9 million vegetation plots from the European Vegetation Archive) and RESOLVE's prediction performance across seven targets: year of recording, EUNIS habitat type, aspect, slope, area, altitude, and geographic location, with altitude reaching R² = 0.96 and habitat classification reaching 91.5% accuracy. The second reports an ablation: species composition alone accounts for 50–75% of the full model's performance, with taxonomy having the largest marginal impact on altitude prediction. The third compares RESOLVE against Random Forest, XGBoost, and spatial k-NN baselines. The fourth shows that model performance saturates at roughly 25% of the training set (~180k plots), with even 5% of the data achieving half the peak accuracy.

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-12 col-md-10" style="max-width:80%;">
<picture>
<source type="image/webp" srcset="/assets/images/content/vys_2026_poster_full.webp">
<img src="/assets/images/content/vys_2026_poster_full.jpg" class="img-fluid d-block mx-auto no-rd zoomable" alt="Scientific poster: Neural networks reconstruct landscape properties from plant species composition">
</picture>
<p class="text-center mt-2"><i>Final poster: Neural networks reconstruct landscape properties from plant species composition</i></p>
</div>
</div>

The design uses the course's two-tier structure: a visually accessible top section communicating the core idea at a glance (vegetation plots sampled, landscapes reconstructed) and a lower section with the technical detail. The instructor noted the contrast between the two tiers as effective.

## Diploma

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-10 col-md-6 col-lg-4">
<picture>
<source type="image/webp" srcset="/assets/images/content/vys_2026_diploma.webp">
<img src="/assets/images/content/vys_2026_diploma.jpg" class="img-fluid d-block img-rd-md mx-auto zoomable" alt="Certificate of completion — Visualize your Science, Gilles Colling, 4 ECTS, May 2026">
</picture>
</div>
</div>

<script>
(function () {
  var imgs = document.querySelectorAll('.zoomable');
  if (!imgs.length) return;

  var overlay = document.createElement('div');
  overlay.className = 'photo-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('aria-label', 'Photo viewer');
  overlay.innerHTML = '<button type="button" class="photo-overlay-close" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></svg></button><img alt="">';
  document.body.appendChild(overlay);

  var overlayImg = overlay.querySelector('img');

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

  imgs.forEach(function (img) {
    img.setAttribute('role', 'button');
    img.setAttribute('tabindex', '0');
    img.addEventListener('click', function () {
      open(img.currentSrc || img.src, img.alt);
    });
    img.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(img.currentSrc || img.src, img.alt); }
    });
  });

  overlay.addEventListener('click', close);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) close();
  });
})();
</script>
