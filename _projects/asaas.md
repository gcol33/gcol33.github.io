---
layout: workshop
title: "ASAAS – Alien Species Accumulation Across Scales"
short_title: "ASAAS"
date: 2022-01-01
category: "Project"
category_url: "/projects/"
thumbnail: "/assets/images/content/project_asaas_field.jpg"
thumbnail_webp: "/assets/images/content/project_asaas_field.webp"
hero_combined: true
hero_title: "Alien Species Accumulation Across Scales"
hero_label: "Project"
hero_separator: true
subtitle: "Currently running"
tags: [invasive-species, asaas, vegetation-plots]
description: "Humans have transported thousands of species across the globe, often with long-lasting consequences for ecosystems. While the number of alien species in regional species pools such as countries or islands is steadily increasing, their actual presence in local communities remains surprisingly low. My PhD project, ASAAS (Alien Species Accumulation Across Scales), explores this mismatch between regional accumulation and local representation."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Projects"
---

## The puzzle

Regional lists of alien species keep growing. First-record curves for most countries show no sign of flattening. Walk into an average vegetation plot in that same country and you find one or two alien species, often none. Regional accumulation and local presence are moving on very different scales, and the gap between them is the question my PhD is built around.

## What would explain it

Two explanations are on the table, and they lead to very different futures.

The first is time. Spread takes decades. A species recorded once at a port needs generations to reach a meadow 300 km inland, so a large regional pool may simply be a pool of species that have not arrived yet. Under this reading, local alien richness will catch up, and the current gap is invasion debt waiting to be paid.

The second is constraint. Most alien species may never leave the ruderal and man-made habitats they arrived in, because the climate, soil, or competition in semi-natural communities keeps them out. Under this reading, regional lists overstate what ecosystems will experience, and the gap is permanent.

The two are not exclusive, and which one dominates probably differs between taxa and habitats. Separating them requires following the same species through both scales over long periods.

## The data

Regional accumulation comes from GloNAF (global naturalized alien flora) and the Alien Species First Record Database, which together give the year each alien species was first recorded in each region. Local presence comes from vegetation plot archives: the European Vegetation Archive (EVA), sPlot, and BioTime, which record which species were found in which plot in which year. PREDICTS adds local community data across further taxa. AgriWeedClim, a database our group compiled, contributes more than 32,000 arable field records from central Europe spanning the last century, one of the few sources deep enough in time to follow local dynamics directly.

The project covers plants first, with vertebrates and selected invertebrates as comparison groups.

## How I test it

Each species carries a residence time, the number of years since its first regional record. If time lags dominate, residence time should predict local presence strongly, and the relationship should look the same across habitat types. If constraints dominate, the relationship should saturate, and it should differ sharply between man-made and semi-natural habitats.

I fit these relationships with Bayesian hurdle models with country-level random effects across residence-time classes and EUNIS habitat types, and compare the habitat associations of recently arrived and long-established species. Habitat transition analysis then reveals which habitats serve as entry points and which are reached later. Projections under land-use and climate scenarios follow from the fitted models.

## What we have found so far

In central European arable fields, ninety years of plot data show neophytes (species introduced after 1500) increasing steadily at both the regional and the local scale, while archaeophytes (earlier arrivals) followed a flat trajectory. The lag between the two scales is visible in the data and has not closed.

Across 835,891 EVA plots (1930–2023, 53 European countries and regions), I compared 1,357 alien plants introduced after 1492 by their minimum residence time, the years since the first record in each country. A species counts as overrepresented in a habitat when it occurs there more often than the local habitat mix would predict. The probability of overrepresentation in more than one habitat rises from 21% for species resident up to 20 years to 62% for species resident over 200 years, and the expected habitat count from 1.31 to 2.17. Ruderal habitats increase most steeply (9% to 40%), followed by arable land (15% to 24%), while alpine and nutrient-poor habitats stay rarely overrepresented. Species are usually first recorded as overrepresented in man-made habitats, and then most often in dry and mesic grasslands. Each species has one date per country, so this compares recent and long-established species and does not follow any single species over time. The pattern suggests that anthropogenic habitats act as entry points, and that the aliens already here could still reach the natural habitats that remain largely free of them today. This work received the Best Poster award at the [VDSEE Symposium 2026](/presentations/vdsee2026/).

<picture>
<source type="image/webp" srcset="/assets/images/content/asaas_residence_time_fig1.webp">
<img src="/assets/images/content/asaas_residence_time_fig1.jpg" class="img-fluid d-block img-rd-md mt-4 mb-4" alt="Probability of multi-habitat overrepresentation, expected habitat count and observed habitat-count distributions by residence-time class" width="1200" height="667" loading="lazy">
</picture>

A side product of the arable work is a species distribution model of emerging agricultural weeds under climate change, produced through a master's thesis I co-supervised.

## Papers

- [Ninety years of alien plant species accumulation across regional and local scales in central European fields](/publications/arable-alien-plant-trends/)
- [Projected range shifts of emerging agricultural weeds under climate change in central Europe](/publications/agricultural-weed-range-shifts/)
- [The neglected importance of managing biological invasions for sustainable development](/publications/invasions-sustainable-development/)

ASAAS is supervised by Franz Essl and Stefan Dullinger at the Division of BioInvasions, Global Change & Macroecology, University of Vienna, and funded by the Luxembourg National Research Fund (FNR). The [AgriWeedClim](/projects/agriweed/) project page describes the arable database in more detail.
