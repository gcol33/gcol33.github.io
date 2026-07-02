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

The package ships thirteen backbones as compressed local snapshots, downloaded once and matched against in C: **WFO**, **COL**, **GBIF**, **ITIS**, **NCBI Taxonomy**, **Open Tree of Life**, **WoRMS**, **Euro+Med**, **Species Fungorum**, **AlgaeBase**, **FishBase**, **SeaLifeBase**, and **Reptile Database**. Pass several and they form a fallback chain, where a name unmatched by the first backbone cascades to the next. Matching is fuzzy or exact, with a unified output schema across all sources.

Beyond name resolution, more than sixty enrichment layers join local trait and status databases onto the accepted name: **add_iucn()** for IUCN Red List status, **add_griis()** for GRIIS invasion records, **add_zanne()** for woodiness, **add_eive()** for ecological indicator values, **add_fishbase()** and **add_fishmorph()** for fish ecology and morphology, **add_trait()** to gather one trait across every source that carries it, and **add_data()** for custom user-provided datasets. All heavy computation runs in the [vectra](/side-projects/vectra/) C11 columnar engine.

To check a list before trusting it, **inspect()** returns only the names that look wrong, each labelled with what stands out and the name to use instead, and a `region` or `coords` argument steers fuzzy correction toward species that actually occur where you work.

Install from CRAN:

```r
install.packages("taxify")
```

Or the development version from GitHub (vectra is installed automatically):

```r
install.packages("pak")
pak::pak("gcol33/taxify")
```

Source and issues: [github.com/gcol33/taxify](https://github.com/gcol33/taxify).

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). taxify: Offline Taxonomic Name Matching Against Local Darwin Core Snapshots. doi:10.32614/CRAN.package.taxify</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
