---
layout: workshop
title: "taxify"
date: 2026-06-26
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/taxify.jpg"
thumbnail_webp: "/assets/images/content/taxify.webp"
hero_combined: true
subtitle: "Jun 26, 2026"
description: "Offline taxonomic name matching against local Darwin Core backbones. Hand it a column of messy species names and get one standardized data.frame."
tags: [r-package, ecology]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "taxify"
---

<p class="mb-4"><a href="https://gillescolling.com/taxify/" class="btn btn-lg btn-d button-01">View Package Documentation</a></p>

The [taxify](https://gillescolling.com/taxify/) package matches taxonomic names against Darwin Core backbones stored on your own disk. Hand it a column of messy species names and **taxify()** cleans them, matches them against the backbone, resolves synonyms to accepted names, detects hybrids, and returns one standardized data.frame. Every step runs locally against a versioned snapshot, so a list of thousands resolves in seconds, there are no API calls or rate limits, and the same input gives the same output on any machine.

The package ships ten backbones as compressed local snapshots, downloaded once and matched against in C: **WFO**, **COL**, **GBIF**, **ITIS**, **NCBI Taxonomy**, **Open Tree of Life**, **WoRMS**, **Species Fungorum**, and **AlgaeBase**. Pass several and they form a fallback chain, where a name unmatched by the first backbone cascades to the next. Matching is fuzzy or exact, with a unified output schema across all sources.

Beyond name resolution, a family of join verbs enriches the matched table from local trait and status databases: **add_conservation_status()** for IUCN Red List, **add_invasive_status()** for invasion data, **add_woodiness()**, **add_eive()** for ecological indicator values, **add_fishbase()** and **add_fish_traits()** for fish morphology and ecology, and **add_data()** for custom user-provided datasets. All heavy computation runs in the [vectra](/side-projects/vectra/) C11 columnar engine.

Install the development version from GitHub:

```r
install.packages("pak")
pak::pak("gcol33/taxify")
```

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). taxify: Offline Taxonomic Name Matching Against Local Darwin Core Snapshots. R package. https://github.com/gcol33/taxify</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
