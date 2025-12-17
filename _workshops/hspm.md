---
layout: workshop
title: "Hierarchical Spatial Modelling"
date: 2024-06-24
category: "Education"
category_url: "/education/"
description: "From June 24 to 27, 2024, Jeff Doser and Marc Kéry led a workshop on hierarchical Bayesian spatial models at the Swiss Ornithological Institute in Sempach, Switzerland. Participants brought their own laptops with R, using the `spOccupancy` and `spAbundance` packages throughout the sessions. While the course didn't require prior experience with Bayesian or spatial statistics, a solid understanding of regression models in R was expected. All course materials, including lectures and code, were made available via GitHub."
thumbnail: "/assets/images/content/hspm_ws_bg.jpg"
thumbnail_webp: "/assets/images/content/hspm_ws_bg.webp"
hero_bg_class: "bg-hspm-ws-bg"
texture_class: "texture-darken-strong"
hero_title: "Course Highlights"
hero_content: "The course combined theoretical background with hands-on implementation, with about 70 percent of the time dedicated to lectures and the remaining 30 percent to exercises. It began with an overview of hierarchical modelling and spatial statistics, then moved into scalable modelling techniques using `spOccupancy` and `spAbundance`. Over four packed days, participants worked through topics including single- and multi-species occupancy models, joint species distribution models with imperfect detection, and multi-season models. Later sessions focused on modelling count data using spatial GLMMs, N-mixture models, and hierarchical distance sampling. Real-world applications, such as analyses of Swiss bird data, anchored the exercises in practice. Each day ran from 9:00 to around 17:30, with generous breaks and time set aside for questions and discussion."
math: true
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Hierarchical spatial modelling"
---

## Introduction to Hierarchical Models for Distribution and Abundance

The opening session of the workshop set the foundation of hierarchical modelling by introducing the concept of HMs (hierarchical models) and explaining how they help us answer core ecological questions. These questions include: How many individuals are there? Where are they? How do abundance and distribution vary across space and time? And what environmental or demographic factors drive these patterns?

At the heart of this framework lies the idea of *point patterns*. In theory, the most fundamental way to describe a population or community is as a realization of a stochastic point process. A point pattern consists of a set of spatial coordinates, with each point representing an individual organism. This can be modeled using a homogeneous or inhomogeneous point process,, depending on whether intensity (expected density of individuals) varies across space.

However, real-world data rarely take this ideal form. It's difficult to record exact locations for every individual, and spatially continuous models require mathematical tools like integrals that biologists often avoid. Moreover, data often come in aggregated formats, counts per site, presence/absence in grid cells, or summaries by administrative region. So instead of modeling point patterns directly, we summarize them into two main quantities:

<ul>
<li><p>Abundance (N): The number of individuals per site or unit area.</p></li>
<li><p>Distribution (z or ψ): Presence/absence or the probability of occurrence.</p></li>
</ul>

The lecture emphasized that distribution is not an independent quantity: It is a *deterministic function of abundance*. In particular, if abundance follows a Poisson distribution with rate \\( \lambda \\), then occupancy probability is given by:

\\[\psi = 1 - e^{-\lambda}\\]

This makes distribution a lower-information summary of abundance. It's useful when abundance data are unavailable or detection is very low, but it cannot reveal much once all sites are saturated (i.e., when \\( \psi \to 1 \\)).

The discussion also highlighted the scale dependence of both abundance and distribution. How we discretize space (how large our sampling units are) directly affects the interpretation of results. For instance, small units tend to have low occupancy (since many will contain zero individuals), while very large units may have occupancy close to one. This modifiable area unit problem complicates comparisons across studies and scales.

Another key theme was measurement error. While point patterns have three types of error (location error, false positives, and false negatives), abundance and distribution data typically deal with only two: missed detections and false positives. Accounting for these errors is essential to avoid biased inference.

The second half of the session introduced hierarchical models as the statistical framework best suited to deal with these complexities. A hierarchical model is a sequence of random processes, where each submodel represents a biological or observation process. For example:

<ul>
<li><p>Abundance model: \\( N_j \sim \text{Poisson}(\lambda_j) \\)</p></li>
<li><p>Observation model: \\( y_{j,k} \sim \text{Binomial}(N_j, p_{j,k}) \\)</p></li>
</ul>

Alternatively, for presence/absence:

<ul>
<li><p>State model: \\( z_j \sim \text{Bernoulli}(\psi_j) \\)</p></li>
<li><p>Observation model: \\( y_{j,k} \sim \text{Bernoulli}(z_j \cdot p_{j,k}) \\)</p></li>
</ul>

These models can incorporate covariates and spatial effects using generalized linear model (GLM) formulations. For instance:

\\[\log(\lambda_j) = \beta_0 + \beta_1 x_j + w_j,\\]

where \\( w_j \\) is a spatial random effect.

The benefit of this structure is twofold: First, it separates the ecological signal from the observation noise; second, it allows for flexible and realistic modeling of complex datasets, across space, time, and species.

The takeaway message was clear: Hierarchical models are not just statistical tools, but conceptual frameworks that match the layered nature of ecological data. Whether we are modeling occupancy, abundance, detection, or their spatial and temporal patterns, hierarchical models allow us to describe the world more realistically and to account for the uncertainty that pervades all ecological observations.

## Foundations & Core Spatial Concepts

The first lecture of the occupancy modeling workshop, led by Jeffrey Doser, introduced the fundamental concepts behind species distribution models that account for imperfect detection. The problem is simple in theory but difficult in practice: when studying a species' presence or absence across a landscape, how do we separate biological truth from observation error? This is particularly important in ecology, where even skilled observers may miss a species that is present, and absences may reflect limitations of detection rather than true absence.

To set the stage, the lecture began by discussing the kinds of questions ecologists often want to answer. These include understanding where species live, how effective conservation efforts have been, whether management changes influence entire communities, and how distributions shift over time. Each of these depends on having accurate knowledge of species occurrence, but our observations are always partial, noisy, and incomplete. Occupancy models were designed to deal with this reality.

We started by comparing different types of species data: presence-only data (where we know only where a species has been seen), presence-absence data (which also record when a species wasn't observed), and count data (which record how many individuals were detected). The focus here was on presence-absence data collected through repeated surveys, what [MacKenzie et al. (2002)](https://www.researchgate.net/publication/228821155_Estimating_Site_Occupancy_Rates_When_Detection_Probabilities_Are_Less_Than_One) call *detection/nondetection* data. For example, at a given site, a species might be seen during the first and last visit, but missed in between. This type of dataset allows us to start modeling both the probability that a species is present and the probability that it is detected.

Occupancy models work by separating the biological process: Whether the species actually occupies the site, from the observation process, whether it was detected. Each site has a latent (unobserved) occupancy state \\( z_j \\), which equals 1 if the species is present and 0 if absent. At the same time, each survey \\( k \\) at site \\( j \\) yields an observation \\( y_{j,k} \\), which is a function of both occupancy and detection. Even if the species is present, it may not be detected.

The model is built around two parts. First, the *occupancy model*, which describes the true (but unobserved) state of nature. We define the probability of occupancy at site \\( j \\) as \\( \psi_j \\), and model this as

\\[z_j \sim \text{Bernoulli}(\psi_j)\\]

Often, occupancy is influenced by site-level environmental variables—say, elevation, vegetation cover, or land use. These are included through a logistic regression:

\\[\text{logit}(\psi_j) = \beta_0 + \beta_1 x_{1j} + \dots + \beta_R x_{Rj}\\]

Second, the *observation model*, which accounts for the fact that a species may go undetected even if it is present. If the species is at the site, we model detection using

\\[y_{j,k} \sim \text{Bernoulli}(p_{j,k}),\\]

where \\( p_{j,k} \\) is the detection probability, possibly depending on covariates like weather, observer skill, or time of day:

\\[\text{logit}(p_{j,k}) = \alpha_0 + \alpha_1 w_{1jk} + \dots + \alpha_Q w_{Qjk}\\]

Together, these two components form a hierarchical model that allows us to estimate both presence and detectability. This is powerful because it lets us distinguish a true absence from a non-detection.

Of course, the model depends on some assumptions. Most importantly, the occupancy state must remain constant during the survey period: This is the *closure assumption*. The model also assumes no false positives (i.e. if the species is detected, it is truly there), that detections are independent across surveys, and that all relevant variation in detection is explained by covariates.

Bayesian models provide full posterior distributions, making uncertainty transparent and interpretable. They are more flexible and more naturally handle latent variables and hierarchical structures, especially when extending to spatial or multi-species models. In practice, Bayesian occupancy models are estimated using MCMC (Markov Chain Monte Carlo), which iteratively samples from the posterior distribution of each parameter.

We briefly discussed how this works in practice. After specifying priors for each parameter, the MCMC sampler proposes new values, accepts or rejects them based on likelihood, and repeats this process thousands of times. The resulting samples can be summarized using posterior means, medians, or credible intervals. Diagnostics like trace plots and R-hat values help assess convergence.

The hands-on component of the lecture used the [`spOccupancy`](https://doserlab.com/files/spoccupancy-web/) R package, which simplifies fitting single-species, spatial, and multi-species occupancy models in a Bayesian framework. For this session, we worked with presence-absence data from the Swiss Breeding Bird Survey (MHB), focusing on the European goldfinch. Each site had multiple surveys, and the aim was to estimate occupancy across Switzerland while accounting for imperfect detection.

The next part of the workshop introduced spatial models. Many ecological datasets exhibit spatial autocorrelation, meaning that observations closer in space tend to be more similar than those further apart. If we ignore this dependence, we risk biased estimates and underestimated uncertainty. Spatial models incorporate coordinates directly into the analysis, allowing us to represent ecological processes that vary smoothly across the landscape.

The foundation is the spatial linear model. Suppose we observe a response \\( y_i \\) at each site \\( i \\). We model this as

\\[y_i = \mathbf{x}_i^\top \beta + w_i + \epsilon_i,\\]

where \\( \mathbf{x}_i \\) are covariates, \\( \beta \\) are regression coefficients, \\( w_i \\) is a spatial random effect, and \\( \epsilon_i \\) is independent error. The spatial random effect is modeled with a Gaussian process prior:

\\[\mathbf{w} \sim \text{MVN}(0, \mathbf{C}),\\]

where \\(\mathbf{C}\\) is a covariance matrix with entries determined by distances between sites. A common choice is the exponential covariance function,

\\[\text{Cov}(w_i, w_j) = \sigma^2 \exp(-\phi d_{ij}),\\]

where \\( \sigma^2 \\) is the variance, \\( d_{ij} \\) is the distance between sites \\( i \\) and \\( j \\), and \\( \phi \\) controls the rate at which correlation decays with distance. This structure allows nearby sites to share more information than distant ones.

Gaussian processes can be embedded in occupancy models by letting the occupancy probability at each site depend not only on covariates but also on a spatial random effect. This provides a flexible way to capture unmeasured spatial structure, such as habitat heterogeneity or dispersal processes. In practice, these models are fit using Bayesian methods, often implemented in packages like `spOccupancy`.

We explored how changing the parameters affects the spatial surface. Increasing \\( \sigma^2 \\) increases the overall variability in the spatial effect, while changing \\( \phi \\) alters the spatial scale of correlation. Small values of \\( \phi \\) yield long-range dependence, while large values yield short-range dependence. Visualizing these surfaces helps to understand what the model is capturing.

The key advantage of spatial models is that they reduce bias and improve inference by properly accounting for spatial dependence. However, this comes at a computational cost, since Gaussian process models require storing and inverting large covariance matrices.

The final part of the foundations addressed the computational challenges of fitting Gaussian process models when the number of locations becomes large. This is the so-called big-\\( n \\) problem. When we assign a Gaussian process prior to the spatial random effect, the covariance matrix \\(\mathbf{C}\\) is \\( J \times J \\), where \\( J \\) is the number of locations. For small \\( J \\), such as 5 or 10, inversion is trivial. But as \\( J \\) grows, the cost of storing and inverting \\(\mathbf{C}\\) scales as \\( O(J^2) \\) and \\( O(J^3) \\), respectively. For \\( J = 1000 \\), this already becomes infeasible, and with \\( J = 1600 \\), computation is prohibitively slow.

This difficulty arises because Gaussian processes require evaluating multivariate normal likelihoods, inverting dense matrices, and storing all pairwise distances. These demands quickly overwhelm both memory and processing time.

Several strategies have been developed to make Gaussian processes scalable:

<ul>
<li><p><strong>Low-rank methods</strong> approximate the full covariance structure using a smaller set of basis functions, reducing the dimensionality of the spatial surface.</p></li>
<li><p><strong>Sparse methods</strong> impose sparsity in the covariance or precision matrix, drastically reducing computational requirements.</p></li>
<li><p><strong>Nearest Neighbor Gaussian Processes (NNGPs)</strong> approximate dependencies locally, conditioning each site only on a subset of its nearest neighbors. This retains much of the spatial structure while making computation feasible for thousands of sites.</p></li>
</ul>

Among these, the lecture focused in detail on Nearest Neighbor Gaussian Processes (NNGPs), introduced by [Datta et al. (2016)](https://pubmed.ncbi.nlm.nih.gov/29720777/) and further developed by [Finley et al. (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6753955/). NNGPs offer a sparse and scalable approximation to full GPs, while retaining the same model structure and interpretation. That is, NNGPs have the same spatial parameters as GPs and generate similar spatial surfaces, but can be applied to much larger datasets.

The conceptual foundation of NNGPs is surprisingly intuitive. First, spatial locations are ordered, often just along the x-axis. Then, for each location, we define a set of its \\( m \\) nearest neighbors (subject to the ordering). The key idea is that the spatial random effect at each location is assumed to depend only on the values of these neighbors. This assumption introduces *conditional independence*, which is the heart of what makes the approach computationally efficient.

Instead of a dense \\( J \times J \\) covariance matrix, NNGPs produce a sparse matrix. Each entry depends only on a small set of nearby locations. As a result, the storage requirement drops to \\( O(Jm^2) \\), and computation scales as \\( O(Jm^3) \\). Because \\( m \ll J \\), the savings are substantial. And unlike low-rank methods, NNGPs preserve local variation and perform well in capturing short-range spatial structure.

In practical terms, the [`spOccupancy`](https://doserlab.com/files/spoccupancy-web/) and [`spAbundance`](https://doserlab.com/files/spabundance-web/) R packages implement NNGPs by ordering sites along the Easting coordinate and using default neighbor sizes like \\( m = 15 \\). Users can adjust this value and compare different options using criteria like the Widely Applicable Information Criterion (WAIC). Even relatively small neighbor sets tend to perform well, and increasing \\( m \\) improves accuracy at the cost of computation.

## Spatial Occupancy & Survey Design

The focus shifted to the implementation and interpretation of spatial occupancy models, specifically, how to fit and understand them using the [`spOccupancy`](https://doserlab.com/files/spoccupancy-web/) package. While previous lectures laid out the theory behind spatial processes and modeling frameworks like Gaussian processes and their scalable approximations, this lecture applied those tools directly to the occupancy context.

The foundation remains the same: the basic occupancy model consists of two components. The ecological or occupancy sub-model defines the true presence or absence of a species at each site, while the detection sub-model accounts for imperfect observations. These are combined in a hierarchical Bayesian framework, allowing uncertainty to be modeled explicitly.

This time, the motivation was framed using a real-world example: The European goldfinch in Switzerland. The goal was to determine whether including spatial structure improves model performance and produces a more realistic species distribution map. The short answer is yes: spatial models provide more accurate predictions, more realistic estimates of uncertainty, and deeper insight into unmeasured ecological processes.

But why is residual spatial autocorrelation so common in species distributions? First, because ecological drivers like habitat suitability or environmental gradients often have spatial structure, and many of these drivers are unmeasured or unknown. Second, because species themselves interact with space, through dispersal, conspecific attraction, and biotic interactions. As a result, nearby locations tend to be more similar than distant ones, even after accounting for known covariates.

The spatial occupancy model reflects this reality by extending the standard occupancy formulation. In its spatial form, the occupancy probability \\( \psi_j \\) at site \\( j \\) is given by:

\\[\text{logit}(\psi_j) = \mathbf{X}_j \boldsymbol{\beta} + w(s_j),\\]

where \\( \mathbf{X}_j \boldsymbol{\beta} \\) is the usual linear predictor based on covariates and \\( w(s_j) \\) is a spatial random effect evaluated at location \\( s_j \\). This term captures residual spatial variation. Detection remains modeled in the same way, typically as:

\\[\text{logit}(p_{j,k}) = \mathbf{W}_{j,k} \boldsymbol{\alpha}\\]

Together, these define a full spatial occupancy model that can be fitted either with a full Gaussian process or with the more scalable NNGP approach.

The lecture then moved on to discuss prior distributions, especially for the regression coefficients \\( \boldsymbol{\beta} \\). In traditional generalized linear models, it is common to assign Normal priors like \\( \text{Normal}(0, 1000) \\). But this turns out to be highly informative in logistic models like occupancy, because coefficients live on the logit scale. A large prior variance leads to probabilities near 0 or 1, which can bias estimation. Instead, a more appropriate default is:

\\[\boldsymbol{\beta} \sim \text{Normal}(0, 2.72)\\]

This choice places more uniform weight on the probability scale and avoids the overconfidence induced by broader priors.

For the spatial parameters, the same structure introduced in Lecture 2 applies. The spatial decay parameter \\( \phi \\) governs how quickly spatial correlation drops with distance, and the spatial variance \\( \sigma^2 \\) controls the magnitude of the random effect. These parameters are often weakly identifiable, especially \\( \phi \\), and the lecture introduced the *adaptive Metropolis algorithm* used by [`spOccupancy`](https://doserlab.com/files/spoccupancy-web/) to address this.

In contrast to a standard Metropolis algorithm, which uses a fixed proposal variance, the adaptive version adjusts the tuning variance throughout the MCMC run. This is done in batches, typically every 25 samples, and attempts to achieve a target acceptance rate of 0.43. Each batch provides feedback about how the chain is mixing, and the tuning variance is updated accordingly. This helps accelerate convergence, especially for parameters like \\( \phi \\), which are difficult to sample efficiently due to their strong influence on the shape of the spatial surface.

In practice, users of [`spOccupancy`](https://doserlab.com/files/spoccupancy-web/) need to specify four key values when using the adaptive Metropolis implementation:

1. `tuning`: The initial tuning variance.
2. `accept.rate`: The target acceptance rate.
3. `n.batch`: Number of MCMC batches.
4. `batch.length`: Number of MCMC samples per batch.

The total number of MCMC samples is the product of `n.batch` and `batch.length`.

The classic framework for occupancy studies uses a grid of \\( J \\) sites, each visited \\( K \\) times. These repeated surveys allow estimation of both the occupancy probability \\( \psi \\) and the detection probability \\( p \\), which are confounded in single-visit datasets. The observed detection histories, such as \\([1, 0, 0, 1]\\), are used to infer whether a species is truly present but missed, or genuinely absent.

Choosing the right number of sites and visits is nontrivial. It depends on your goals. Do you want to estimate occupancy with a given precision? Compare two habitats? Detect a trend over time? Evaluate a new detection method? Or model population dynamics? The optimal survey effort looks different for each objective.

For basic estimation of occupancy, the main concern is the cumulative detection probability, defined as:

\\[p^* = 1 - (1 - p)^K\\]

This represents the probability of detecting the species at least once across \\( K \\) visits, given that it is present and detection probability per visit is \\( p \\). To design your survey, you can define the total number of surveys \\( T = J \times K \\), and then optimize the allocation between sites and visits.

[MacKenzie & Royle (2005)](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2664.2005.01098.x) offer practical advice based on simulations. When detection is low (\\( p \ll 0.5 \\)), it is better to concentrate effort on fewer sites with more visits. When occupancy is low (\\( \psi \ll 0.5 \\)), the opposite holds: more sites with fewer visits yield more information. If detection is your main goal, prioritize repeated visits. If surveying new sites is costly, say, due to travel or access issues, it's again better to revisit fewer places.

In most cases, \\( K \geq 3 \\) is recommended to allow stable estimation of detection probabilities. When your study includes multiple species, it's often safest to design around the rarest or hardest-to-detect species. That design usually works for everything else.

The lecture then introduced alternative designs that deviate from the standard "\\( J \\) sites with \\( K \\) visits" format. The *removal design* stops visiting a site after the first detection. If a species is detected on the first visit, there's no need to return. This can save time and resources. It's particularly effective when occupancy is moderate to high (\\( \psi \geq 0.4 \\)). The removal design yields lower standard errors than the standard design under these conditions.

A second alternative is the *conditional design*, where every site is visited once, and only those with a detection are revisited. This approach was explored by Specht et al. (2017) and others. It is especially efficient for rare species with low detection probability, where many sites are likely to yield no detections at all. The first visit acts as a filter, identifying candidates for further effort.

A third hybrid is the *mixed design*, also known as "double sampling" or "fractional replication." Here, a subset of sites receives only one visit (\\( J_S \\)), while another subset (\\( J_R \\)) is visited \\( K \\) times. This design can reduce field costs when some data is already available or when resources are limited. However, single-visit data only help if the species is very easy to detect. Otherwise, their contribution to parameter estimation is marginal. Still, when combined with repeated visits, even a few single-visit data points can slightly improve inference, particularly when occupancy and detection are modeled using continuous covariates.
