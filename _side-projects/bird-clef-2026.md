---
layout: workshop
title: "BirdCLEF+ 2026"
date: 2026-06-15
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/bird-clef-2026.jpg"
thumbnail_webp: "/assets/images/content/bird-clef-2026.webp"
hero_combined: true
subtitle: "June 15, 2026"
description: "Single-author entry to the BirdCLEF+ 2026 multi-taxon acoustic species identification challenge (LifeCLEF Lab, CLEF 2026): a public acoustic baseline rank-blended with soundscape-tuned CNNs, plus a leaderboard-free evaluation harness. 0.932 public / 0.917 private macro-AUC across 4,092 teams."
tags: [bioacoustics, audio-classification, sound-event-detection, clef, kaggle, machine-learning]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "BirdCLEF+ 2026"
---

## The challenge

[BirdCLEF+ 2026](https://www.imageclef.org/BirdCLEF2026), the acoustic species identification task at the LifeCLEF Lab of [CLEF 2026](https://clef2026.clef-initiative.eu/), concluded on 3 June 2026 and drew 4,092 teams. Competitors must identify which of 234 species vocalise in continuous field recordings from the Pantanal of South America. The 2026 edition is multi-taxon: the classes span birds, amphibians, insects, and reptiles, so one model has to separate calls with very different structure. The task is framed as multi-label detection over 5-second windows, scored by macro-averaged ROC-AUC over the classes that carry a positive label in the hidden soundscape test set.

Two properties shape any entry. Training audio is clip-level focal recordings of single vocalising individuals, while scoring is window-level on continuous soundscapes with overlapping species and long silences, a distribution shift between training and evaluation audio. And inference runs on a CPU-only Kaggle kernel under a wall-clock budget, which caps how large and how numerous the models in an ensemble can be.

## Result

**0.932 macro-AUC on the [public leaderboard](https://www.kaggle.com/competitions/birdclef-2026/leaderboard) (1968th of 4092 teams) and 0.917 on the private leaderboard (2415th).** Most of that score comes from a publicly shared baseline used unchanged; the soundscape-tuned models trained for this entry add a small, consistent correction on top. The two leaderboards did not rank the submissions in the same order, and the entry's more transferable outputs are two pieces of method: a leaderboard-free evaluation harness built on the released soundscapes, and a documented public-to-private generalisation gap.

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-lg-8 col-md-10">
<picture>
  <source type="image/webp" srcset="/assets/images/content/bird-clef-2026.webp">
  <img src="/assets/images/content/bird-clef-2026.jpg" class="img-fluid mx-auto d-block img-rd-md zoomable" alt="System diagram for the BirdCLEF+ 2026 entry" loading="lazy" style="padding: 2.5%;" data-zoom-src="/assets/images/content/bird-clef-2026-zoom.jpg">
</picture>
</div>
</div>

## The pipeline

The submitted system is an ensemble of two parts, combined only at the very end. Every model resamples audio to 32 kHz mono, cuts it into 5-second windows, and turns each window into a 128-band log-mel spectrogram before scoring all 234 classes.

The first part is a publicly shared community baseline, used unchanged: an embedding branch built on the [Perch](https://arxiv.org/abs/2307.06292) bird-vocalisation model with a probe-classifier head, blended with a five-fold [EfficientNet](https://arxiv.org/abs/1905.11946) sound-event-detection ensemble. The second part is the contribution trained here, a weighted triplet of convolutional networks fine-tuned on the released soundscape recordings: an EfficientNet-B3, a pseudo-label-refined B3, and a [ConvNeXt](https://arxiv.org/abs/2201.03545)-Small, all taken from [timm](https://github.com/huggingface/pytorch-image-models) with single-channel input stems and trained with an [asymmetric loss](https://arxiv.org/abs/2009.14119). The triplet is rank-blended onto the baseline at a small weight (alpha = 0.10): the baseline carries most of the ranking, and the soundscape-tuned models supply a correction that helps only in small doses, degrading the score when allowed to dominate.

Each daily leaderboard slot tests only one idea, so the most useful piece of infrastructure was an offline evaluation harness. It scores any model or blend on the 66 labelled soundscape recordings released with the competition, restricts the macro-average to the 75 species that actually carry positive labels there, and reads out differences of a few thousandths in under a second. That moved hypothesis testing off the daily leaderboard slot. Its one blind spot is the embedding branch, which trains on those same 66 files and so cannot be held out cleanly. The public-to-private gap (the configuration that topped the public board was not the best on the private split) traces to exactly that: the part of the blend carrying most of the score is the part the harness cannot estimate independently.

## Artefacts

- **Working note:** submitted to CLEF 2026 (LifeCLEF / BirdCLEF track); CEUR-WS proceedings forthcoming.
- **Code:** [github.com/gcol33/bird-clef-2026](https://github.com/gcol33/bird-clef-2026) (MIT licence)
- **Trained weights:** [huggingface.co/gcol33/bird-clef-2026](https://huggingface.co/gcol33/bird-clef-2026) (CC BY 4.0, subject to upstream dataset restrictions)
- **Competition page:** [kaggle.com/competitions/birdclef-2026](https://www.kaggle.com/competitions/birdclef-2026)
- **Official challenge:** [imageclef.org/BirdCLEF2026](https://www.imageclef.org/BirdCLEF2026) · [CLEF 2026](https://clef2026.clef-initiative.eu/) (21–24 September, Jena)

The peer-reviewed CEUR-WS proceedings version will appear after the conference.

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
      open(img.dataset.zoomSrc || img.currentSrc || img.src, img.alt);
    });
    img.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(img.dataset.zoomSrc || img.currentSrc || img.src, img.alt); }
    });
  });

  overlay.addEventListener('click', close);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) close();
  });
})();
</script>
