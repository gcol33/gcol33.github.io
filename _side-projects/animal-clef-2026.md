---
layout: workshop
title: "AnimalCLEF 2026"
date: 2026-05-06
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/animal-clef-2026.jpg"
thumbnail_webp: "/assets/images/content/animal-clef-2026.webp"
hero_combined: true
subtitle: "May 06, 2026"
description: "Entry to the AnimalCLEF 2026 individual animal re-identification challenge (LifeCLEF Lab, CLEF 2026). Final rank: 6/230 on the private leaderboard, top solo team."
tags: [computer-vision, re-identification, clef, kaggle, machine-learning]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "AnimalCLEF 2026"
---

## The challenge

[AnimalCLEF 2026](https://www.imageclef.org/AnimalCLEF2026), the individual animal re-identification task at the LifeCLEF Lab of [CLEF 2026](https://clef2026.clef-initiative.eu/), ran from 1 February to 7 May 2026 and drew 230 teams. Competitors must assign every test image to an identity cluster across four species: Eurasian lynx, fire salamander, loggerhead sea turtle, and Texas horned lizard. The test set mixes known training individuals with completely unseen ones; submissions are scored by Adjusted Rand Index (ARI), which measures pairwise cluster consistency against hidden ground-truth identities. Both false merges and missed merges hurt, and novel individuals must be assigned to a cluster; the scoring gives no credit for leaving them isolated.

Each species demands something different. Lynx coat patterns and turtle scute arrangements separate cleanly on global appearance descriptors; salamander spot patterns and lizard ventral markings need local feature matching to tell individuals apart at fine scale. The test set spans 2,409 images (946 lynx, 689 salamander, 500 sea turtle, 274 horned lizard); the mix of known and novel individuals varies by species, which shapes the pipeline design for each.

## Result

**[6th of 230 teams](https://www.kaggle.com/competitions/animal-clef-2026/leaderboard) on the private leaderboard, first place among solo entries.** Final scores: 0.61741 ARI public / 0.57038 ARI private, producing 833 predicted clusters across 2,409 test images.

<div class="row mt-4 mb-4 justify-content-center">
<div class="col-12 img-constrained-md">
<picture>
  <source type="image/webp" srcset="/assets/images/content/animal-clef-2026.webp">
  <img src="/assets/images/content/animal-clef-2026.jpg" class="img-fluid mx-auto d-block img-rd-md zoomable" alt="System diagram for the AnimalCLEF 2026 entry" loading="lazy" style="padding: 2.5%;" data-zoom-src="/assets/images/content/animal-clef-2026-zoom.jpg">
</picture>
</div>
</div>

## The pipeline

Every pair of test images gets a score. The score encodes how likely those two images depict the same individual, derived from neural network embeddings and local feature matches. Those scores become edge weights in an undirected graph, one node per image; draw an edge wherever the weight exceeds a threshold, and the connected components are the clusters.

Two signals feed each weight. Global descriptors compare the whole frame: coat pattern, scute arrangement, overall silhouette. Local keypoint matchers work at finer scale, anchoring on specific marks and finding correspondences patch by patch. Lynx and sea turtles separate cleanly on global appearance alone; salamanders and horned lizards, whose identifying marks are small and inconsistent across photographs, need the local signal. Which signal dominates, and at what threshold, is decided per species. Set the threshold too tight and the same individual fragments into separate clusters; too loose and strangers merge.

The system runs one anchored graph-clustering pipeline per species. Global similarity comes from two pretrained re-identification encoders: [MiewID](https://huggingface.co/conservationxlabs/miewid-msv3) (used off-the-shelf) and [MegaDescriptor-L-384](https://huggingface.co/BVRA/MegaDescriptor-L-384), with two species-specific MegaDescriptor checkpoints fine-tuned with ArcFace heads on the competition's Lynx and Sea Turtle training splits. [LightGlue](https://github.com/cvg/LightGlue) + [SuperPoint](https://arxiv.org/abs/1712.07629) local feature matching provides a complementary score. The two signals are blended into a per-species similarity, thresholded, and turned into edges in an undirected graph; connected components become the predicted clusters.

The system then anchors the graph through the labelled training set: when a test image's nearest training neighbour exceeds the species threshold, the test image inherits that individual's identity, and all test images sharing an anchor merge automatically. For Salamander and Horned Lizard, an [XGBoost](https://github.com/dmlc/xgboost) pair classifier scores every test–test pair from LightGlue match statistics and descriptor cosines; pairs above the species threshold contribute must-link edges. The Salamander classifier draws on embeddings from a [LoRA](https://arxiv.org/abs/2106.09685)-finetuned [DINOv2-S](https://github.com/facebookresearch/dinov2) adapter (rank 8, trained on ~7,800 hand-labelled spot-correspondence pairs); the Horned Lizard classifier additionally uses [DINOv3](https://arxiv.org/abs/2508.10104) patch features. MegaDescriptor fine-tunes use [ArcFace](https://arxiv.org/abs/1801.07698) heads.

## Artefacts

- **Working note (preprint, DOI):** [10.5281/zenodo.20055000](https://doi.org/10.5281/zenodo.20055000)
- **Code:** [github.com/gcol33/animal-clef-2026](https://github.com/gcol33/animal-clef-2026) (MIT licence)
- **Trained weights:** [huggingface.co/gcol33/animal-clef-2026](https://huggingface.co/gcol33/animal-clef-2026) (CC BY 4.0, subject to upstream dataset restrictions)
- **Competition page:** [kaggle.com/competitions/animal-clef-2026](https://www.kaggle.com/competitions/animal-clef-2026)
- **Official challenge:** [imageclef.org/AnimalCLEF2026](https://www.imageclef.org/AnimalCLEF2026) · [CLEF 2026](https://clef2026.clef-initiative.eu/) (21–24 September, Jena)

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
