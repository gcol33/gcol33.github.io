---
layout: chapter
title: "Lecture 6 - Random Walks"
permalink: /course-spattempdyn-lecture6/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 6"

prev_chapter:
  title: "Lecture 5"
  url: "/course-spattempdyn-lecture5/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 7"
  url: "/course-spattempdyn-lecture7/"

math: true
---

Lecture 6 introduced random walks as a fundamental model for dispersal, explaining how individuals move in space without a predefined direction. The lecture covered basic random walks, correlated random walks, and how to implement these models computationally. These concepts are widely used in animal movement ecology, invasive species spread, and diffusion models in ecology.

#### Dispersal and Movement in Ecology

Dispersal describes the movement of organisms from one location to another. Density-dependent dispersal can involve avoidance of overcrowded areas, reduced settlement in areas with high population densities, or carry-over effects, where individuals born in crowded areas develop different dispersal behaviors. Dispersal behaviour can be classified into two main types:

1. Passive (density-independent) dispersal.
2. Active (density-dependent) dispersal.

Passive dispersal occurs when movement is driven by external factors such as wind or water currents, as seen in seeds dispersed by wind, whereas active dispersal occurs when organisms move based on environmental conditions or population density, such as cane toads in Australia, which have increased dispersal distances over time due to selective pressures favoring more mobile individuals.

#### Random Walks and Brownian Motion

A random walk is a mathematical model where movement consists of a series of steps in randomly chosen directions. It was first described by Robert Brown, who observed the random motion of pollen grains in water due to molecular collisions.

The simplest form is Brownian motion, where each step is independent of the previous one. This can be modeled in two dimensions by allowing movement in any of the following directions:

$$\begin{array}{ccc}(+1,-1) & (+1,\pm0) & (+1,+1) \\\\ (\pm0,-1) & \bullet & (\pm0,+1) \\\\ (-1,-1) & (-1,\pm0) & (-1,+1)\end{array}$$

At each step, one of these movements is chosen randomly. A dispersal event consists of multiple steps. To simulate a basic random walk:

1. Identify all possible movements.
2. Build an array representing movement options, with one column for $x$ displacement and one for $y$ displacement.
3. Sample from these movements using a random selection process.
4. Sum the movements over time to get the final position.

The cumulative sum function is used to track position changes over multiple steps. For example, a simple random walk with four moves might follow this sequence:

$$\begin{array}{c|cc}\text{Step} & x \text{ movement} & y \text{ movement} \\\\ \hline 1 & 0 & +1 \\\\ 2 & -1 & +1 \\\\ 3 & -1 & +1 \\\\ 4 & +1 & -1\end{array}$$

Summing the columns gives the final position.

$$(x_{\text{final}}, y_{\text{final}}) = \left( 0 + (-1) + (-1) + 1, 1 + 1 + 1 + (-1) \right) = (-1, 2)$$

#### Correlated Random Walks

A correlated random walk introduces persistence, meaning an individual is more likely to continue moving in the same direction as the previous step. This models the tendency of animals to maintain direction over short distances rather than changing direction randomly. A basic implementation would be:

1. Compute the distance from all possible moves to the previous step.
2. Assign probabilities based on distance, using:

$$P_i = \frac{1}{\text{distance}_i + 1/\text{weight}},$$

where the weight determines the strength of persistence.

A small weight reduces directional bias, while a larger weight strongly favors continued movement in the same direction. For example, if an individual previously moved to the right ($+1,0$), the probability of continuing in that direction is increased, while the probability of reversing direction is decreased. To visualize directional bias, consider a matrix of possible moves:

$$\begin{array}{ccc}4 & 3 & 2 \\\\ 3 & 1 & 0 \\\\ 2 & 1 & 0\end{array}$$

Lower values indicate preferred directions. When calculating movement probabilities, these values are inverted and normalized to sum to 1, creating a biased movement pattern. If an individual previously moved upward, future moves upward will have a higher probability than lateral or downward moves. By adjusting weight, different movement behaviors emerge:

- Low weight → nearly random movement.
- High weight → strong directional persistence
