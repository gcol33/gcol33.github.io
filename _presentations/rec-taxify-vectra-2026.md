---
layout: workshop
title: "Research Exchange Club 2026"
short_title: "Research Exchange Club"
date: 2026-06-25
category: "Presentation"
category_url: "/presentations/"
thumbnail: "/assets/images/content/presentation_rec_2026.jpg"
thumbnail_webp: "/assets/images/content/presentation_rec_2026.webp"
hero_combined: true
subtitle: "June 25, 2026"
hero_title: "taxify and vectra"
description: "A short talk at the BioInvasions Research Exchange Club on two R packages I build in my spare time: taxify, for resolving messy species names to accepted names offline and joining trait and status layers onto them; and vectra, for fitting models on rasters and tables too large to hold in memory."
tags: [r-package, taxonomy, spatial, software]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Research"
    url: "/research-archive/"
  - name: "Presentations"
    url: "/presentations/"
  - name: "Research Exchange Club 2026"
---

On June 25, 2026, I gave a short talk at the BioInvasions Research Exchange Club on two R packages I build in my spare time. Both grew out of recurring friction in our own work: cleaning species name lists, and running analyses on climate rasters and occurrence tables that outgrow memory. The two handouts below reproduce the live examples; each is a single HTML file you can open in a browser, and both run offline against staged data so they work on any machine.

## taxify

taxify resolves a column of species names to accepted names, offline. It cleans messy strings, catches typos, follows synonyms, and returns one standardized table. From there it joins published trait, status, and alien-species layers onto the result, drawing on open databases from across the tree of life (woodiness, EIVE, Diaz traits, AVONET, FishBase, and more). Matching runs in C against a name backbone kept on disk, so the same input gives the same output on any machine. The package is in active development.

Install with `install.packages("pak")`, then `pak::pak("gcol33/taxify")`; the first call downloads the name backbone once.

- **Handout:** [handout_taxify.html](/assets/downloads/handout_taxify.html)
- **Documentation:** [gillescolling.com/taxify](https://gillescolling.com/taxify)
- **Code:** [github.com/gcol33/taxify](https://github.com/gcol33/taxify)

## vectra

vectra fits models on rasters and tables too big to load into memory. It streams the data off disk in chunks with the usual dplyr verbs, keeping peak memory small at any file size, as a plain R package. It is on CRAN, and sf support for spatial work is in progress.

Install with `install.packages("vectra")`.

- **Handout:** [handout_vectra.html](/assets/downloads/handout_vectra.html)
- **Documentation:** [gillescolling.com/vectra](https://gillescolling.com/vectra)
- **CRAN:** [CRAN.R-project.org/package=vectra](https://cran.r-project.org/package=vectra)
