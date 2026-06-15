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
description: "A single-author BirdCLEF+ 2026 entry built mostly on a public baseline (LifeCLEF Lab, CLEF 2026). The parts that are mine: a leaderboard-free evaluation harness, an honest account of what did not work, and a diagnosed public-to-private generalisation gap."
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

Every team started from the same strong public baseline, so an entry came down to small additions of my own on top of it, and the public leaderboard returned a score only a few times a day. I built an offline evaluator on the 66 labelled soundscape recordings the organisers released: it scores any blend of my models in under a second, over the 75 species that carry labels there. That let me rank tens of configurations in an evening instead of one per leaderboard submission. The evaluator could not score the component that carried most of the prediction, the public embedding branch, because that branch trains on the same 66 recordings. The result turned on that blind spot: the blend that led the public leaderboard fell on the private split.

## The challenge

[BirdCLEF+ 2026](https://www.imageclef.org/BirdCLEF2026), the acoustic species identification task at the LifeCLEF Lab of [CLEF 2026](https://clef2026.clef-initiative.eu/), concluded on 3 June 2026 and drew 4,092 teams. Competitors identify which of 234 species vocalise in continuous field recordings from the Pantanal of South America. The 2026 edition is multi-taxon, so one model has to separate birds, amphibians, insects, and reptiles, whose calls share almost nothing. Submissions are scored by macro-averaged ROC-AUC over the classes that carry a positive label in the hidden soundscape test set.

That setup is harder than a leaderboard position makes it look. Training audio is clip-level focal recordings of a single calling individual, while the test audio is continuous soundscape with overlapping species and long silences, so a model is scored on a distribution it never trained on. Because the metric averages over classes, a handful of rare species move the score as much as the common ones, and the room to improve sits in the worst-scoring classes rather than the easy majority. Inference runs CPU-only under a wall-clock cap, which rules out large or numerous models. And the field is dense: a shared public baseline already reaches about 0.927, and from there the leaderboard is decided in the third decimal place, so a mid-pack finish among 4,092 teams sits only a few thousandths off the top.

## What I added

Two things, and neither is the leaderboard position.

The first is a **way to evaluate without the leaderboard**. A solo competitor gets only a few public-board reads a day, which is a slow way to choose between ideas. The competition released 66 soundscape recordings with window-level labels, so I built an evaluator on them: it scores any model or blend in under a second, restricts the macro-average to the 75 species that actually carry a label there, and cross-validates across the files. A daily leaderboard slot became tens of offline comparisons in an evening.

The second is a **public-to-private gap I can explain**. The blend that topped my public score was not the best on the private split. The cause is specific: the component carrying most of the prediction is the public embedding branch, and it trains on the same 66 soundscapes my harness uses, so there is no clean way to hold it out and measure it. The harness could rank everything except the part that mattered most, which is precisely where the two boards disagreed.

The scores themselves are mid-pack: **0.932 macro-AUC on the [public leaderboard](https://www.kaggle.com/competitions/birdclef-2026/leaderboard) (1968th of 4092 teams), 0.917 on the private leaderboard (2415th)**, most of it carried by the public baseline.

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-lg-8 col-md-10">
<picture>
  <source type="image/webp" srcset="/assets/images/content/bird-clef-2026.webp">
  <img src="/assets/images/content/bird-clef-2026.jpg" class="img-fluid mx-auto d-block img-rd-md zoomable" alt="System diagram for the BirdCLEF+ 2026 entry" loading="lazy" style="padding: 2.5%;" data-zoom-src="/assets/images/content/bird-clef-2026-zoom.jpg">
</picture>
</div>
</div>

## What I tried that didn't work

Most of the effort went into directions that did not improve the score.

On the modelling side, single-class (argmax) pseudo-labels plateaued below the best blend, so I switched to frame-level multi-hot pseudo-targets that keep the overlapping-species structure of real soundscapes. Distilling a seven-model teacher into one student to save runtime scored worse than the teacher and worse than the small triplet, losing more than the budget it saved. Fusing the models by a geometric mean of probabilities, instead of by rank, also lost, because the models are not calibrated to a shared scale. And my soundscape-tuned models helped only at a low weight; above a small share of the blend they made the score worse.

The inference budget killed others outright. A seven-model ensemble timed out on the hidden test set. A ConvNeXt-Base that scored well locally projected to nearly two hours of CPU inference and was shelved. Two attempts to make heavier models fit, INT8 quantisation and float16 conversion, either ran slower than the original or disagreed with it almost completely, an interaction with the depthwise convolutions. The entry that shipped is the best one that fit the budget; my best local model never did.

The most ambitious thread, a deeper data pipeline with cross-year pretraining on previous editions and several rounds of pseudo-labelling, was only partly finished by the deadline. It is the route the strongest published solutions take, and the part I would start earlier next time, because it does not fit into a final week. Finishing it would take more than an earlier start: the full multi-backbone, multi-seed version outgrows the two personal machines I trained on, a 16 GB RTX 5080 and an M4 Pro Mac mini.

## The pipeline

The submitted system is an ensemble of two parts, combined only at the very end. Every model resamples audio to 32 kHz mono, cuts it into 5-second windows, and turns each window into a 128-band log-mel spectrogram before scoring all 234 classes.

The first part is a publicly shared community baseline, used unchanged: an embedding branch built on the [Perch](https://arxiv.org/abs/2307.06292) bird-vocalisation model with a probe-classifier head, blended with a five-fold [EfficientNet](https://arxiv.org/abs/1905.11946) sound-event-detection ensemble. The second part is mine: a weighted triplet of convolutional networks I fine-tuned on the released soundscape recordings, an EfficientNet-B3, a pseudo-label-refined B3, and a [ConvNeXt](https://arxiv.org/abs/2201.03545)-Small, all taken from [timm](https://github.com/huggingface/pytorch-image-models) with single-channel input stems and trained with an [asymmetric loss](https://arxiv.org/abs/2009.14119). The triplet is rank-blended onto the baseline at a small weight (alpha = 0.10): the baseline carries most of the ranking, and the soundscape-tuned models supply a small correction on top.

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
