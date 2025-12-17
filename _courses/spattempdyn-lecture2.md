---
layout: chapter
title: "Lecture 2 - Single Species Models"
permalink: /course-spattempdyn-lecture2/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 2"

prev_chapter:
  title: "Lecture 1"
  url: "/course-spattempdyn-lecture1/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 3"
  url: "/course-spattempdyn-lecture3/"

math: true
---

In Lecture 2 we focused on single-species population models with an emphasis on exponential growth. The lecture began by revisiting the basic concepts of population dynamics in nature. A population is defined as a group of individuals of one species that live, reproduce, and interact within a particular area. Although real populations are affected by interactions with other species and environmental fluctuations, the simplest models assume that resources are unlimited and that the population is closed (ignoring immigration and emigration).

## Fundamentals of Population Dynamics

Population changes can be understood in terms of births and deaths. The population at the next time step is determined by the current population plus the number of births minus the number of deaths. This relationship is captured by the recursive equation:

$$ N_{t+1} = N_t + B - D $$

where $ N_t $ represents the population size at time $ t $, $ B $ is the number of births, and $ D $ is the number of deaths. The change in population size over time is

$$ N_{t+1} = N_t + B - D $$

Assuming that both births and deaths occur at rates proportional to the current population size,

$$B = b \cdot N$$
$$D = d \cdot N,$$

where $ b $ is the birth rate and $ d $ is the death rate.

## Exponential Growth Model

Substituting these assumptions into the equation for population change leads to a differential equation that describes continuous population change:

$$\frac{dN}{dt} = (b - d) \cdot N$$

The intrinsic growth rate is defined as

$$r = b - d$$

Thus, the exponential growth model is

$$\frac{dN}{dt} = r \cdot N$$

which has the well-known solution ($ \int dt$ on both sides)

$$N_t = N_0 \cdot e^{r t},$$

where $ N_0 $ is the initial population size. An important property of the exponential model is the doubling time, which describes the time required for the population to double in size. Setting $ N_t = 2N_0 $ in the exponential growth equation,

$$2N_0 = N_0 \cdot e^{r \cdot t_{\text{double}}}$$

Solving for $ t_{\text{double}} $ gives

$$t_{\text{double}} = \frac{\ln(2)}{r}$$

This expression provides a measure of how quickly a population can grow under ideal, density-independent conditions.

## Continuous vs. Discrete Time Models

Continuous time models use differential equations to describe population changes that occur at every instant. Many species, however, reproduce at specific intervals, making discrete time models more appropriate. In a discrete model, the population at the next time step is calculated using a difference equation:

$$N_{t+1} = N_t + (b - d) \cdot N_t + m,$$

where $ m $ represents net migration during the time step. This approach captures the life-cycle events that occur at distinct points in time rather than assuming continuous change.
