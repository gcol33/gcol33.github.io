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
hero_title: "Taming big data and bad names"
description: "A short talk at the BioInvasions Research Exchange Club on why I keep a day a week for software, and on the two R packages that came out of it: taxify, for resolving messy species names to accepted names offline; and vectra, for fitting models on rasters and tables too large to hold in memory."
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

On June 25, 2026, I gave a short talk at the BioInvasions Research Exchange Club on two R packages I build in my spare time, and on why I make the time at all. Both grew out of recurring friction in our own work: cleaning species name lists, and running analyses on climate rasters and occurrence tables that outgrow memory. The two handouts below reproduce the live examples; each is a single HTML file you can open in a browser, and both run offline against staged data so they work on any machine.

## Why I keep a day a week for this

A PhD starts wide open and ends as a long list of things you have to do. I wanted to hold on to the part I enjoy, so I set a rule early: about a fifth of my time, roughly one day a week, stays on projects I choose, and taxify and vectra are that fifth. There is a line in the work-stress literature behind the rule. Karasek's demand-control model (1979) finds that what wears people down is less the sheer volume of work and more how little of it they get to decide; a day a week of chosen work is a small lever on the control side.

The spark came from rainbowR 2026, the inaugural LGBTQIA+ R conference, which a colleague suggested. The room ran from PhD students to senior researchers, all building free and open-source software, and I left thinking I could do this too. The two packages are released as free software for the same reason. As Richard Stallman, who started the free software movement and wrote the GPL, put it: "To be able to choose between proprietary software packages is to be able to choose your master. Freedom means not having a master."

The two packages share one engine: taxify matches names on the same C engine that vectra is built around. The slot was one story with two demos on top, so the two halves below are how the talk ran.

## taxify

taxify resolves a column of species names to accepted names, offline. It cleans messy strings, catches typos, follows synonyms, and returns one standardized table. From there it joins published trait, status, and alien-species layers onto the result, drawing on open databases from across the tree of life (woodiness, EIVE, Diaz traits, AVONET, FishBase, and more). Matching runs in C against a name backbone kept on disk, so the same input gives the same output on any machine. The package is in active development.

In the talk's demo, a fuzzy match of 1,000 names resolved in about a second on the local backbone, against roughly half an hour for the usual route over web services.

Install with `install.packages("pak")`, then `pak::pak("gcol33/taxify")`; the first call downloads the name backbone once.

- **Handout:** [handout_taxify.html](/assets/downloads/handout_taxify.html)
- **Documentation:** [gillescolling.com/taxify](https://gillescolling.com/taxify)
- **Code:** [github.com/gcol33/taxify](https://github.com/gcol33/taxify)

## vectra

vectra fits models on rasters and tables too big to load into memory. It streams the data off disk in chunks with the usual dplyr verbs, keeping peak memory small at any file size, as a plain R package. It is on CRAN, and sf support for spatial work is in progress.

In the talk's demo, a GLM fit over a 6.26 GB table held about 0.48 GB in memory by folding one chunk at a time, the same fit either way.

Install with `install.packages("vectra")`.

- **Handout:** [handout_vectra.html](/assets/downloads/handout_vectra.html)
- **Documentation:** [gillescolling.com/vectra](https://gillescolling.com/vectra)
- **CRAN:** [CRAN.R-project.org/package=vectra](https://cran.r-project.org/package=vectra)
