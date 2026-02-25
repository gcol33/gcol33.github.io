---
layout: workshop
title: "couplr"
date: 2026-01-21
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/couplr.jpg"
thumbnail_webp: "/assets/images/content/couplr.webp"
hero_bg_color: "#343739"
hero_combined: true
hero_container_class: "pad-md"
hero_label: "Released"
subtitle: "Jan 21, 2026"
description: "Optimal one-to-one matching for causal inference and experimental design. High-level matching with balance diagnostics and 18 LAP algorithms."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "couplr"
---

<p class="mb-4"><a href="https://gillescolling.com/couplr/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

The [couplr](https://gillescolling.com/couplr/) package provides high-level functions for optimal one-to-one matching between two groups in R. It addresses direct covariate matching without requiring intermediate propensity score modeling, making it useful for causal inference, experimental design, resource allocation, and image processing tasks.

The package offers two main matching functions: **match_couples()** for optimal matching with automatic preprocessing, multiple scaling methods, distance constraints, and blocking support; and **greedy_couples()** for fast approximate matching using sorted, row-best, or priority queue strategies (10-100x faster for large datasets). Use `match_couples()` for n < 5,000 where guaranteed optimality matters; switch to `greedy_couples()` for larger datasets prioritizing speed.

Balance diagnostics are built-in via **balance_diagnostics()** for assessing covariate balance using standardized differences, variance ratios, and KS tests, along with **balance_table()** for publication-ready output. For lower-level control, **lap_solve()** provides an interface to 18 linear assignment algorithms with automatic method selection, plus batch solving and K-best solutions via Murty's algorithm.

Available on CRAN under MIT license.

```r
install.packages("couplr")
```

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). couplr: Linear Assignment Problem Solver for Optimal Matching. doi:10.32614/CRAN.package.couplr</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
