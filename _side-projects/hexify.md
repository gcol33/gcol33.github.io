---
layout: workshop
title: "hexify"
date: 2026-02-04
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/hexify.jpg"
thumbnail_webp: "/assets/images/content/hexify.webp"
hero_bg_color: "#343739"
hero_combined: true
hero_container_class: "bloc-md"
hero_label: "Released"
subtitle: "Feb 04, 2026"
description: "Equal-area hexagonal grids on the Snyder ISEA icosahedron. Fast C++ core with sf/terra-compatible R wrappers."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "hexify"
---

<p class="mb-4"><a href="https://gillescolling.com/hexify/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

The [hexify](https://gillescolling.com/hexify/) package implements an equal-area hexagonal discrete global grid system (DGGS) using the Snyder ISEA projection in R. It provides a fast C++ core for projection and aperture quantization, with sf- and terra-compatible R wrappers for grid generation and coordinate assignment.

The package supports multiple grid resolutions through aperture quantization, allowing users to generate hexagonal grids at varying spatial scales. Core functions handle the conversion between geographic coordinates and hexagonal cell identifiers, making it straightforward to bin point data, aggregate raster values, or create gridded representations of spatial phenomena at any resolution.

Under the hood, hexify uses a C++ backend for the computationally intensive Snyder equal-area icosahedral projection, ensuring fast performance even for large datasets. The R interface integrates directly with the sf and terra ecosystems, so grids can be used seamlessly in spatial analysis workflows.

Available on CRAN under MIT license.

```r
install.packages("hexify")
```

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). hexify: Equal-Area Hex Grids on the Snyder ISEA Icosahedron. doi:10.32614/CRAN.package.hexify</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
