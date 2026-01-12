---
layout: chapter
title: "Lecture 8 - Population Growth and Dispersal"
permalink: /course-spattempdyn-lecture8/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 8"

prev_chapter:
  title: "Lecture 7"
  url: "/course-spattempdyn-lecture7/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Overview"
  url: "/course-spattempdyn/"

math: true
---

This lecture extended the concept of dispersal modeling by integrating population dynamics with spatially explicit dispersal kernels. The focus was on simulating how populations grow and spread across a raster landscape over multiple time steps. By combining population growth models with dispersal processes, the lecture demonstrated how species expand their range over time, influenced by both intrinsic demographic parameters and external dispersal constraints.

#### Passive Dispersal and the Importance of Long-Distance Movement

Dispersal is a critical ecological process, influencing species distributions, colonization, and invasion dynamics. Many organisms rely on passive dispersal, where movement is driven by external forces such as wind, water currents, or animal vectors. Examples include:

- Seeds carried by the wind.
- Pollen dispersed by insects.
- Marine larvae transported by ocean currents.

Measuring dispersal, especially over long distances, is challenging. However, long-distance dispersal events are essential in shaping ecological patterns. Many dispersal kernels exhibit fat tails, meaning that while most individuals disperse over short distances, some rare events lead to exceptionally long-distance dispersal. These rare events are critical for processes such as species invasions and range expansion.

#### Mathematical Definition

A dispersal kernel defines the probability distribution governing how individuals move away from their origin. Several dispersal kernels were introduced, each with different implications for movement behavior.

- Exponential kernel
    - Movement probability decreases exponentially with distance and is useful for short-distance dispersal. It is described by

$$p(x) = \frac{1}{2\pi a^2} \exp\left(-\frac{x}{a}\right)$$

- Gaussian kernel
    - Dispersal is centered around the origin, with most individuals remaining close and very few traveling long distances. This is typically used for local movement in stable environments. The function is given by

$$p(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{x^2}{2\sigma^2}\right)$$

- Fat-tailed 2Dt kernel
    - This kernel allows for rare but significant long-distance dispersal events, making it widely used in invasion and range expansion models. It is expressed as

$$p(x) = \frac{b-1}{\pi a^2} \left(1 + \frac{x^2}{a^2}\right)^{-b}$$

Each of these kernels captures different ecological dispersal processes and plays a key role in modeling how populations spread.

#### Dispersal Kernels in Raster-Based Models

The dispersal process can be implemented in a raster environment, where the landscape is represented as a grid of cells. Each raster cell holds population values, and dispersal occurs based on a probability matrix derived from a dispersal kernel.

The first step is to define the raster environment by structuring the landscape into a raster grid with a specified extent and resolution. Each cell represents a discrete spatial unit where individuals reside.

The dispersal kernel is applied by multiplying the population in each cell by a dispersal raster, which assigns movement probabilities. If $ N(x,y,t) $ represents the number of individuals in cell $ (x,y) $ at time $t$, and $ p(i,j) $ is the probability of movement to a neighboring cell $ (i,j) $, then the new population at time $ t+1 $ is computed as

$$N(i,j,t+1) = \sum_{x,y} p(i-x, j-y) \cdot N(x,y,t)$$

#### Population Growth

This lecture introduced population dynamics into the model. The growth of individuals within each raster cell was modeled using density-dependent growth equations.

The logistic growth model assumes that population growth slows as individuals compete for resources. It follows the equation

$$\frac{dN}{dt} = rN \left(1 - \frac{N}{K}\right)$$

where $r$ is the intrinsic growth rate and $K$ is the carrying capacity.

Discrete growth models are also possible. The Beverton-Holt model represents compensatory density dependence and is defined as

$$N_{t+1} = \frac{rN_t}{1 + \frac{(r-1)}{K} N_t}$$

The Ricker model captures overcompensatory density dependence, where population growth can lead to oscillations. It follows

$$N_{t+1} = N_t e^{r(1-N_t/K)}$$

Both models were implemented during the lecture in raster-based simulations, combining local population growth with spatial dispersal. To model long-term species spread, the process was repeated over multiple time steps.

The initial population raster was stored, defining the starting distribution of individuals. The dispersal function was then applied iteratively, updating the raster at each step according to

$$N(x,y,t+1) = \sum_{i,j} p(i,j) \cdot N(i,j,t) + rN_t \left(1 - \frac{N_t}{K}\right)$$

Combining dispersal kernels with density-dependent growth models showed how species expand over time, depending on movement patterns and local resource limits. Different dispersal kernels led to different outcomes. Exponential and Gaussian kernels resulted in localized spread, while fat-tailed kernels allowed for long-distance dispersal, which plays a key role in invasion dynamics.

Integrating population growth into the model made it possible to track how density dependence influences dispersal. The logistic model introduced carrying capacity limits, while the Beverton-Holt and Ricker models demonstrated different forms of competition and population regulation.

This approach makes it possible to simulate population expansion under various conditions, showing how species distributions emerge from the interaction between movement and reproduction.
