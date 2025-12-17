---
layout: workshop
title: "Corrselect"
date: 2025-08-05
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/corrselect.jpg"
thumbnail_webp: "/assets/images/content/corrselect.webp"
hero_bg_image: "/assets/images/content/corrselect.jpg"
hero_combined: true
hero_label: "Released"
subtitle: "Aug 05, 2025"
description: "Predictor pruning using association-based and model-based approaches. Fast, deterministic solutions with minimal code."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "Corrselect"
---

<p class="mb-4"><a href="https://gillescolling.com/corrselect/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

The [corrselect](https://gillescolling.com/corrselect/) package is an R tool designed for predictor pruning using association-based and model-based approaches. It addresses the admissible set problem by selecting maximal variable subsets where pairwise associations remain below user-defined thresholds.

## Core Functions

### corrPrune() - Association-Based Pruning

Association-based variable reduction operating on raw data without requiring model specification. It offers exact mode for optimal solutions (recommended when p ≤ 100) and greedy mode for larger datasets. The function supports automatic metric selection and includes a `force_in` parameter to protect key variables.

### modelPrune() - Model-Based Pruning

Model-dependent pruning using VIF (Variance Inflation Factor) methodology. It accommodates multiple engines including `lm`, `glm`, `lme4`, and `glmmTMB`, with extensibility for custom modeling packages like INLA, mgcv, or brms. This approach iteratively removes predictors while refitting models.

## Key Features

The package implements exhaustive subset enumeration via graph algorithms (Eppstein–Löffler–Strash and Bron–Kerbosch methods). It supports multiple association metrics: Pearson, Spearman, Kendall correlations; specialized measures like bicor and cramersv for mixed data; and energy distance calculations.

Advanced functionality includes `assocSelect()` for mixed-type data handling and `MatSelect()` for precomputed correlation matrices. Deterministic tie-breaking ensures reproducibility across analyses.

## Applicable Domains

The package benefits ecological modeling, trait-based species selection, and interpretable machine learning workflows.

## Installation

Available via CRAN or development installation through GitHub. Distributed under MIT license.

```r
install.packages("corrselect")
```
