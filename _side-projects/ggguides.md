---
layout: workshop
title: "ggguides"
date: 2025-12-17
category: "Side Project"
type: package
category_url: "/side-projects/"
thumbnail: "/assets/images/content/ggguides.jpg"
thumbnail_webp: "/assets/images/content/ggguides.webp"
hero_combined: true
subtitle: "Dec 17, 2025"
description: "Simplified legend and guide alignment for ggplot2. One-liner functions for common legend operations."
tags: [r-package, visualization]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "ggguides"
---

<p class="mb-4"><a href="https://gillescolling.com/ggguides/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

I kept forgetting the commands to put a ggplot2 legend on the left, right, top or bottom, and looking them up again and again annoyed me. So I wrote [ggguides](https://gillescolling.com/ggguides/), where `legend_left()` puts the legend on the left.

The package covers five kinds of legend work: **positioning** with functions like `legend_left()`, `legend_right()`, `legend_top()`, and `legend_bottom()`; **direction** control via `legend_horizontal()` and `legend_vertical()`; **styling** options for font size, family, wrapping, reversing, and reordering; tools for **multiple legends** including hiding, selecting, and managing guides; and **multi-panel integration** supporting patchwork and cowplot workflows.

Available on CRAN under MIT license.

```r
install.packages("ggguides")
```

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2025). ggguides: Simplified Legend and Guide Alignment for ggplot2. doi:10.32614/CRAN.package.ggguides</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
