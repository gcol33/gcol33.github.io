---
layout: archive-item
title: "Colling 2026"
date: 2026-02-25
category: "Publication"
category_url: "/publications/"
thumbnail: "/assets/images/content/corrselect.jpg"
thumbnail_webp: "/assets/images/content/corrselect.webp"
authors: "Colling G."
external_url: "https://doi.org/10.21105/joss.09539"
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Research"
    url: "/research-archive/"
  - name: "Publications"
    url: "/publications/"
  - name: "Colling 2026"
---

Publication in Journal of Open Source Software, 11(118), 9539.

## Abstract

corrselect is an R package for reducing multicollinearity and redundancy in predictor sets. It provides two complementary approaches: high-level pruning functions that return a single optimal subset, and exhaustive enumeration of all maximal admissible subsets. The package accommodates both numeric and mixed-type data, permits forced inclusion of essential predictors, and works with standard R modeling workflows including mixed-effects models. Version 3.0 introduces `corrPrune()` for association-based pruning and `modelPrune()` for VIF-based model pruning, while maintaining the original exhaustive enumeration functions (`corrSelect()`, `assocSelect()`, `MatSelect()`). A fast C++ greedy algorithm enables efficient pruning for large predictor sets (p > 100), while exact graph-theoretic algorithms guarantee complete enumeration when exhaustive search is feasible.
