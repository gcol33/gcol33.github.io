---
layout: workshop
title: "Species Accumulation Curves"
short_title: "Species Accumulation"
date: 2026-01-26
category: "Education"
category_url: "/education/"
thumbnail: "/assets/images/content/workshop_liams_stay.jpg"
thumbnail_webp: "/assets/images/content/workshop_liams_stay.webp"
hero_bg_class: "bg-workshop-liams-stay"
hero_combined: true
description: "A two-day ecology workshop designed for a visiting school student, introducing biodiversity sampling, species accumulation curves, and spatial algorithms through hands-on R programming exercises."
hero_title: "How Do We Count Species We Can't See?"
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Species Accumulation Curves"
---

On January 26 and 27, 2026, I mentored a school student, Liam, during a two-day visit to the Division of BioInvasions, Global Change & Macroecology at the University of Vienna. The goal was to introduce him to ecological research through a hands-on workshop on species accumulation curves, a fundamental concept in biodiversity science. The workshop was bilingual (English and German) and combined theory with practical R programming exercises.

## Day 1: Concepts and First Steps in R

The first day focused on foundational concepts. We started with what biodiversity means and why it is difficult to measure directly. From there, we moved into sampling theory: how ecologists collect data in the field, why complete censuses are rarely possible, and how accumulation curves allow us to estimate total species richness from incomplete samples. The concept of asymptotes was introduced as the theoretical limit a curve approaches, representing the total number of species in an area.

In the practical session, Liam worked through eight exercises that progressed from basic R syntax to his first real data analysis. Starting with simple operations and data structures, the exercises gradually built up to loading ecological datasets, computing species counts, and plotting his first accumulation curve. By the end of the day, he had written working R code that visualized how species richness increases with sampling effort.

## Day 2: Algorithms and a Research Project

The second day shifted to more advanced topics. The theory session covered spatial ordering of samples, nearest-neighbor algorithms, and the concept of multiple seeds for generating different accumulation curve trajectories from the same dataset. These ideas are directly relevant to my own R package work and gave Liam a glimpse into how algorithmic choices affect ecological conclusions.

The practical session consisted of seven exercises structured as a mini research project. Liam explored uncertainty in accumulation curves by running multiple randomizations, learned how to produce publication-quality figures, and drew his own conclusions from the data. The exercises culminated in a final analysis where he had to interpret results and communicate findings, mirroring the workflow of an actual research project.

## Workshop Materials

The full workshop materials, including theory slides and interactive exercises for both days, are available as a <a href="/liams_stay/" target="_blank">standalone bilingual web application</a>.
