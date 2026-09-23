---
layout: archive-item
title: "NeoPlants-EU: Country-level first records and species characteristics of vascular plant neophytes in Europe"
short_title: "NeoPlants-EU dataset"
date: 2026-09-23
category: "Publication"
type: dataset
venue: "Zenodo"
category_url: "/publications/"
thumbnail: "/assets/images/content/neoplants-eu.jpg"
thumbnail_webp: "/assets/images/content/neoplants-eu.webp"
authors: "Colling G."
external_url: "https://doi.org/10.5281/zenodo.22127075"
tags: [dataset, invasive-species]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Research"
    url: "/research-archive/"
  - name: "Publications"
    url: "/publications/"
  - name: "NeoPlants-EU dataset"
---

Dataset on Zenodo, version 1.0, CC BY 4.0.

## About

NeoPlants-EU records vascular plant neophytes, taxa introduced to Europe after ca. 1492,
at the level of a taxon in a country. Each of the 7,158 records carries the earliest
documented occurrence of that taxon in that country, together with its life cycle, growth
form, dispersal mode and native source region on a standardised vocabulary. It covers
2,179 taxa across 55 countries and territories, with first-record years running from 1492
to 2020.

A first record is the earliest year across five sources: a GBIF occurrence download read
occurrence by occurrence, the Global Alien Species First-Record Database, the European
Vegetation Archive, national and regional alien plant lists, and the Austrian neophyte
checklist. The year each source gives for each row ships with the release, so any one of
them can be followed back.

I built the trait columns to carry their own provenance. Every life cycle and growth form
cites a page stating that value, as do 6,901 of the 7,038 recorded dispersal modes, and
the README gives a reason for each remaining gap. Names are matched against four
taxonomic checklists held at fixed versions, whose versions and checksums ship with the
data, so the taxonomy can be reproduced.

Version 1.0 is an independent release. Its taxonomy and first-record sources differ from
the 0.x pre-releases, so it is not a drop-in replacement for them.
