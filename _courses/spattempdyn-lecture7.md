---
layout: chapter
title: "Lecture 7 - Random Walks for Population Movement"
permalink: /course-spattempdyn-lecture7/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 7"

prev_chapter:
  title: "Lecture 6"
  url: "/course-spattempdyn-lecture6/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 8"
  url: "/course-spattempdyn-lecture8/"

math: true
---

Lecture 7 continued the discussion on random walks by integrating movement simulations with spatially explicit raster grids. Instead of modeling dispersal in continuous space, random-walk processes can be efficiently implemented on discrete raster environments. Working with rasters involves defining a spatially explicit grid characterized by:

- Extent: the geographic area represented by the raster.
- Resolution: the size of each raster cell, determining spatial precision.

When simulating dispersal on a raster, the movement rules had to be adapted. Rather than recording each intermediate step in a random walk, only the final position mattered for population updates. Thus, the original random walk function was adjusted to return only final displacement coordinates, significantly enhancing computational efficiency. This was particularly important when simulating dispersal for large numbers of individuals over multiple time steps. By overlaying dispersal models onto a raster, movement becomes discrete, meaning that individuals transition from one cell to another rather than moving freely in continuous space.

#### Random Walks on a Raster Grid

Instead of recording every intermediate step of an individual's movement, only the final displacement matteres for updating population distributions. This significantly improves computational efficiency, especially when simulating dispersal across large landscapes. To determine dispersal:

1. Calculate the relative movement of individuals.
2. Identifying the new location based on the movement.
3. Determinie the number of dispersing individuals.
4. Assigning dispersers to the new cell.
5. Assigning non-dispersers to the original cell.

This shift in approach reduces computational complexity by eliminating unnecessary calculations while preserving realistic dispersal dynamics.

#### Dispersal Kernels

A dispersal kernel defines the probability that an individual moves a certain distance from its starting location. Instead of tracking stepwise movement, individuals disperse according to a predefined probability distribution. The kernel is typically represented as a probability matrix, where the center represents the original location, and surrounding cells represent potential destinations.

A 3×3 dispersal kernel represents movement probabilities for an individual starting in a central cell with eight neighboring cells. Each cell in the kernel is assigned a probability, determining how likely it is for an individual to move there. For example, if dispersal is mostly local, a higher fraction of individuals will remain in the center, with smaller fractions moving outward. If most of individuals stay in place and the remaining disperse, the probabilities might be:

- The center cell retains most individuals (for example, 60% stay in place).
- The eight surrounding cells each receive 40% of dispersers (for example, 5% per neighboring cell).

The sum of all probabilities must be one to ensure population conservation (meaning no individuals are lost or artificially created).

Different kernel shapes control the dispersal process:

- Gaussian kernels: Most individuals disperse over short distances.
- Fat-tailed kernels: Allow for rare long-distance dispersal events, crucial for modeling species invasions.
- 2Dt kernels: Frequently used for invasive species spread, emphasizing extreme dispersal events.
- ...

This replaces the need for tracking individual movement, instead allowing population updates based on spatial probabilities. To apply the kernel to raster dispersion, in each time step, we loops through all raster cells:

1. Check if the cell contains individuals and skip if empty
2. Apply the dispersal kernel
    - The population in each cell is multiplied by the movement probabilities defined in the dispersal kernel. If $ N(x,y,t) $ represents the number of individuals in cell $ (x,y) $ at time $t$, and $ p(i,j) $ is the probability of moving to a neighboring cell $ (i,j) $, then the expected number of dispersers to each adjacent cell is given by:

$$N(i,j,t+1) = \sum_{x,y} p(i-x, j-y) \cdot N(x,y,t)$$

3. Update population values in a new raster
    - Each individual is assigned a new location according to the dispersal probabilities, and the population values are recorded in a new raster layer.

4. Handle edge effects
    - If dispersers reach the boundary of the raster, adjustments are made to prevent artificial loss. One approach is to reflect individuals back into the grid, while another is to allow movement beyond the boundary in an open system.

By applying this probabilistic update at each time step, dispersal models represent realistic population redistribution across a landscape. To track dispersal over time, the process is repeated for multiple time steps

1. Store the initial population raster
2. Iteratively apply the dispersal function
    - For each time step $t$, the dispersal equation is applied, updating the raster according to:

$$N(x,y,t+1) = \sum_{i,j} p(i,j) \cdot N(i,j,t),$$

where, dispersal is modeled as a convolution of the dispersal kernel with the current population distribution.

3. Track population spread over time up storing each update as a new layer on the stack.

#### A few words on efficiency

Simulating large-scale dispersal events requires several optimizations to ensure the model runs efficiently:

- Skipping empty cells, if  $ N(x,y,t) = 0 $, the cell is ignored to avoid unnecessary computations
- Using cumulative sum functions, matrix operations efficiently track dispersal in a single step
