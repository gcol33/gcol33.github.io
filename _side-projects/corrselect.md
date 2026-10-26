---
layout: workshop
title: "corrselect"
date: 2025-08-05
category: "Side Project"
type: package
category_url: "/side-projects/"
thumbnail: "/assets/images/content/corrselect.jpg"
thumbnail_webp: "/assets/images/content/corrselect.webp"
hero_combined: true
subtitle: "Aug 05, 2025"
description: "Predictor pruning using association-based and model-based approaches. Fast, deterministic solutions with minimal code."
tags: [r-package, statistics]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "corrselect"
---

<p class="mb-4"><a href="https://gillescolling.com/corrselect/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

Many tools that remove correlated predictors pick one subset for you. In practice I saw many scientists choose their predictors by hand instead, by trial and error, until the correlations looked acceptable. I wanted to see all the choices.

[corrselect](https://gillescolling.com/corrselect/) lists every maximal subset of variables in which no pair exceeds a correlation threshold you set, so you can pick the subset that fits your question.

The package offers two main approaches: **corrPrune()** for association-based pruning that operates model-free on raw data, and **modelPrune()** for VIF-based iterative removal compatible with `lm`, `glm`, `lme4`, and `glmmTMB` engines. Both functions support a `force_in` parameter to protect important variables from removal.

Under the hood, corrselect implements exhaustive subset enumeration via graph algorithms (Eppstein–Löffler–Strash and Bron–Kerbosch methods). It supports multiple association metrics including Pearson, Spearman, Kendall correlations, as well as specialized measures like bicor, Cramér's V, eta, and energy distance for mixed-type data. Deterministic tie-breaking ensures reproducibility across analyses.

The package benefits ecological and bioclimatic modeling, trait-based species selection, and interpretable machine learning workflows. Available on CRAN under MIT license.

```r
install.packages("corrselect")
```

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2025). corrselect: Fast and Flexible Predictor Pruning. doi:10.32614/CRAN.package.corrselect</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
