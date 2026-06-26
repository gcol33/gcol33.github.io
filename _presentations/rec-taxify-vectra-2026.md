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

## Why I keep Fridays free

I keep Fridays open to play with whatever idea is in front of me, no roadmap, no goal for where it lands. taxify and vectra are two of the things that have come together over those Fridays. The talk mentioned the demand-control idea (Karasek 1979): having some say over your work eases the strain we all feel, and a free day is a small way to get a little of that back. Somewhere along those Fridays an interest in free software grew too.

A nudge came from rainbowR 2026, the inaugural LGBTQIA+ R conference, which a colleague suggested. It drew everyone from PhD students to senior researchers, all building free and open-source software, and I came away thinking I might be able to do this too. The two packages are free software for that reason. As Richard Stallman, who started the free software movement and wrote the GPL, put it: "To be able to choose between proprietary software packages is to be able to choose your master. Freedom means not having a master."

The two packages share one engine: taxify matches names on the same C engine that vectra is built around. The slot was one story with two demos on top, so the two halves below are how the talk ran.

## taxify

A lot of ecological work starts by unifying taxonomy, and the names never quite match. The same species arrives as `Quercus robur L.` carrying its authorship, as `Pinus cf. sylvestris` with a qualifier, as the hybrid `Nothofagus x alpina`, as a synonym (`Pinus abies` is `Picea abies`), or as a plain typo (`Quercus robus`). The talk walked through the three common routes for resolving a name list and where each one strains: WorldFlora loads the WFO backbone into memory and runs its fuzzy pass name by name; taxize calls out to around twenty web services, so it is tied to the network, rate limits, and answers that can shift between runs; taxadb keeps local snapshots but queries them in SQL and matches exact names, so typos and synonyms slip through.

taxify does the same job locally, in C. Hand it a column of messy names and one call returns accepted names, with the cleaning, synonym following, and fuzzy matching done against a name backbone kept on disk, so the same input gives the same output on any machine.

```r
taxify(c(
  "Quercus robur",
  "Pinus abies",          # synonym -> Picea abies
  "Quercus robus",        # typo    -> Quercus robur
  "Taraxacum officinale"
), backend = "wfo")
```

In the talk's demo, the same 1,000 plant names matched in about a second on the local backbone, against roughly half an hour over web services.

Once names are resolved, trait and status layers join on the accepted name: IUCN Red List status, GRIIS invasion status by country, EIVE indicator values, woodiness, FishBase ecology, and your own tables, drawing on published databases for plants, animals, fungi, and algae.

```r
taxify(plant_names, backend = "wfo") |>
  add_conservation_status() |>   # IUCN Red List
  add_invasive_status("AT") |>   # GRIIS, Austria
  add_eive() |>                  # EIVE indicator values
  add_data("TRY_traits.csv")     # your own table
```

The package is in active development.

Install with `install.packages("pak")`, then `pak::pak("gcol33/taxify")`; the first call downloads the name backbone once.

- **Handout:** [handout_taxify.html](/assets/downloads/handout_taxify.html)
- **Documentation:** [gillescolling.com/taxify](https://gillescolling.com/taxify)
- **Code:** [github.com/gcol33/taxify](https://github.com/gcol33/taxify)

## vectra

vectra fits models on rasters and tables too big to load into memory. The talk opened on a routine task that breaks: read a WorldClim stack of 19 bioclim layers, turn every cell into a point, merge it with occurrences, and fit a GLM. R answers with `cannot allocate vector of size 6.3 Gb`, because the whole table has to sit in memory at once, and R's copy-on-modify means editing a single column can copy the entire thing.

Existing engines solve this at a price: Arrow brings a new memory format to build around, DuckDB is a full in-process SQL database, and Spark is a distributed cluster driven through a JVM. vectra stays inside plain R. Underneath it leans on one idea: read one chunk, fold it into a running result, and keep only that chunk in memory. Sums, counts, means, and even a regression's normal equations combine this way, so the same dplyr verbs you already write stream off disk and `collect()` pulls the result in pieces.

```r
tbl_tiff("stack.tif") |>
  mutate(warm = band1 > 10) |>
  select(x, y, warm) |>
  collect()
```

For models, `bigglm` folds a GLM chunk by chunk off disk through a chunk feeder. For fits that cannot fold, such as a GAM that needs all its rows at once, `offload` maps over groups and spills them to disk one group at a time.

In the talk's demo, the GLM that peaked at 6.26 GB held about 0.48 GB in memory when folded a chunk at a time, the same fit either way.

vectra is on CRAN, and sf support for spatial work is in progress.

Install with `install.packages("vectra")`.

- **Handout:** [handout_vectra.html](/assets/downloads/handout_vectra.html)
- **Documentation:** [gillescolling.com/vectra](https://gillescolling.com/vectra)
- **CRAN:** [CRAN.R-project.org/package=vectra](https://cran.r-project.org/package=vectra)
