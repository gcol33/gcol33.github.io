---
layout: workshop
title: "vectra"
date: 2026-06-26
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/vectra.jpg"
thumbnail_webp: "/assets/images/content/vectra.webp"
hero_combined: true
subtitle: "Jun 26, 2026"
description: "A columnar query engine for larger-than-RAM data in R. dplyr-style verbs backed by a pull-based C11 engine, with native raster and vector support."
tags: [r-package, data]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "vectra"
---

<p class="mb-4"><a href="https://gillescolling.com/vectra/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

The [vectra](https://gillescolling.com/vectra/) package runs `dplyr`-style queries on datasets larger than RAM. It is backed by a pull-based columnar execution engine written in C11, so a query streams through the data one batch at a time and peak memory stays bounded regardless of how large the file on disk is.

The familiar verbs are all there: **filter()**, **select()**, **mutate()**, **group_by()**, and **summarise()**, along with the **left_join()**, **inner_join()**, and **fuzzy_join()** family, **arrange()**, the **slice_*()** helpers, and window functions such as **row_number()**, **rank()**, **lag()**, **cumsum()**, and **ntile()**. Execution is lazy: verbs build a plan that **explain()** can print, and **collect()** or **collect_chunked()** pulls the result when you ask for it.

Data lives in a custom on-disk columnar format (`.vtr`). vectra also reads and writes GeoTIFF, including tiled and BigTIFF layouts, and a tiled raster format (`.vec`) with overview pyramids and time cubes for larger-than-RAM raster work. Vector operations including spatial transforms, point-in-polygon and nearest-feature joins, select-by-location, clip, erase, dissolve, rasterization, polygonization, and contouring stream through `sf`. Raster operations including zonal statistics, focal windows, terrain derivatives, warp resampling and reprojection, polygon masking, map algebra, and mosaicking run in native C over the tiled format, one tile at a time.

Available on CRAN under MIT license.

```r
install.packages("vectra")
```

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). vectra: Columnar Query Engine for Larger-than-RAM Data. doi:10.32614/CRAN.package.vectra</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
