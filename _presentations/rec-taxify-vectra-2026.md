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
description: "A short talk at the BioInvasions Research Exchange Club on two recurring frictions in ecological work: species names that will not match across datasets, and rasters and tables too large to hold in memory. The two R packages that take them on are taxify, resolving messy names to accepted names offline, and vectra, fitting models on data too big for memory."
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

Two problems come up often in my work: species name lists that are hard to match across datasets, and climate rasters and occurrence tables that can outgrow memory. taxify and vectra are the two R packages I build on the side to take those on, and the talk I gave at the BioInvasions Research Exchange Club on June 25, 2026 walked through both. The two handouts below reproduce the live examples; each is a single HTML file you can open in a browser, and both run offline against staged data so they work on any machine.

This semester our working group started a Research Exchange Club: a recurring meeting where one of us shows the others what they are working on. It came about as the BioInvasions and Biodiversity Dynamics and Conservation groups are merging, so a lot of each side's day-to-day work is easy to miss from the other. I presented taxify and vectra, since they sit close to work both groups run into.

A PhD fills up with work you did not pick, and Karasek (1979) tied job strain to that loss of control more than to the volume. So I keep Fridays open for projects I choose, and taxify and vectra came out of them. In February this year I went to [rainbowR](/rainbowr2026/), the inaugural LGBTQIA+ R conference. Everyone there, from PhD students to senior researchers, was building free and open-source software, and I came back wanting to do the same with these two. Both run on one engine, so the slot ran as two demos over one story: taxify matches names on the same C code vectra is built around.

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

Read a WorldClim stack of 19 bioclim layers, turn every cell into a point, merge it with occurrences, and fit a GLM, and R stops with `cannot allocate vector of size 6.3 Gb`. The whole table has to sit in memory at once, and copy-on-modify means editing a single column can copy the entire thing. vectra fits the same model on rasters and tables too big to load into memory.

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
