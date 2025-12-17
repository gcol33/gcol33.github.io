---
layout: workshop
title: "ggguides"
date: 2025-12-17
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/corrselect.jpg"
thumbnail_webp: "/assets/images/content/corrselect.webp"
hero_bg_color: "#343739"
hero_combined: true
hero_container_class: "bloc-md"
hero_label: "Released"
subtitle: "Dec 17, 2025"
description: "Simplified legend and guide alignment for ggplot2. One-liner functions for common legend operations."
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

The [ggguides](https://gillescolling.com/ggguides/) package provides streamlined functions for managing legends in ggplot2 visualizations. It offers one-liner functions for common legend operations, reducing the boilerplate typically required for legend customization.

The package delivers five functional categories: **positioning** with functions like `legend_left()`, `legend_right()`, `legend_top()`, and `legend_bottom()`; **direction** control via `legend_horizontal()` and `legend_vertical()`; **styling** options for font size, family, wrapping, reversing, and reordering; tools for **multiple legends** including hiding, selecting, and managing guides; and **multi-panel integration** supporting patchwork and cowplot workflows.

Available on GitHub under MIT license.

```r
# install.packages("devtools")
devtools::install_github("gcol33/ggguides")
```
