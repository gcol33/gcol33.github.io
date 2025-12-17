---
layout: workshop
title: "Corrselect"
date: 2025-08-05
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/corrselect.jpg"
thumbnail_webp: "/assets/images/content/corrselect.webp"
hero_bg_image: "/assets/images/content/corrselect.jpg"
hero_combined: true
hero_label: "Released"
subtitle: "Aug 05, 2025"
description: "The corrselect package automatically identifies all maximal subsets of variables in your data whose pairwise correlations or associations remain below a user-defined threshold."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "Corrselect"
---

The [corrselect](https://gillescolling.com/corrselect/) package automatically identifies all maximal subsets of variables in your data whose pairwise correlations or associations remain below a user-defined threshold. This helps reduce multicollinearity and redundancy while retaining interpretability. The method is model-agnostic, making it applicable to regression, clustering, ecological modeling, and other workflows.

<h1 class="mb-4 text-lg-center mt-lg-4 mb-lg-3">Overview</h1>

I started working on corrselect as a side project in the summer of 2025 and first submitted it on August 5. The idea came from working with bioclimatic variables, where many predictors are strongly correlated, and I wanted a way to define multiple maximal subsets without discarding more than necessary. The package provides a systematic way to select subsets where no pair of variables exceeds a chosen correlation or association threshold. At its core, it tackles the admissible set problem, which is about finding all maximal subsets of predictors that remain below a user-defined threshold. My goal was to make something practical for reducing multicollinearity while keeping models interpretable, and to design it so it could slot into many different workflows, from regression and clustering to trait-based selection and interpretable machine learning.

<h1 class="mb-4 text-lg-center mt-lg-4 mb-lg-3">Core Functionality</h1>

The methods I implemented are graph based. corrselect uses two algorithms, the ELS method by Eppstein, Löffler, and Strash, and the Bron-Kerbosch algorithm with optional pivoting. Both can enumerate all maximal subsets that satisfy a threshold. I wanted an approach that was exhaustive rather than heuristic, so users would not miss valid combinations that greedy filters might skip.

To make it useful beyond purely numeric datasets, I added support for multiple correlation and association measures. Alongside Pearson, Spearman, Kendall, and biweight midcorrelation, the package includes distance correlation, maximal information coefficient, eta, and Cramér's V. With [`assocSelect()`](https://gillescolling.com/corrselect/reference/assocSelect.html) the package automatically chooses the right measure depending on variable types, which makes it possible to handle mixed datasets with both numerical and categorical predictors.

For usability, I built in options to work directly with data frames ([`corrSelect()`](https://gillescolling.com/corrselect/reference/corrSelect.html) and [`assocSelect()`](https://gillescolling.com/corrselect/reference/assocSelect.html)) or with precomputed matrices ([`MatSelect()`](https://gillescolling.com/corrselect/reference/MatSelect.html)). Users can also force specific variables into every subset when these are required by design. The results are returned as S4 objects of class [`CorrCombo`](https://gillescolling.com/corrselect/reference/CorrCombo.html), with summary methods for quick inspection and easy conversion into tidy data frames.

<h1 class="mb-4 text-lg-center mt-lg-4 mb-lg-3">Development</h1>

I built corrselect because I wanted a complete solution for correlation-based variable selection. Most existing approaches rely on heuristics or greedy filtering, which often miss valid combinations. By using graph algorithms, corrselect guarantees that all maximal subsets are returned, which makes the process transparent and reproducible.

What excites me about this project is how flexible it turned out to be. It works across different kinds of datasets, not just numeric ones, and it is independent of any specific modeling framework. That makes it useful for regression, clustering, trait-based analyses, or machine learning where interpretability is important. In the end, it was also just a fun project to build an R package from scratch, to see the algorithms come together, and to release something that others can use in their own work.
