---
layout: chapter
title: "Lecture 3 - Density-Dependent Growth"
permalink: /course-spattempdyn-lecture3/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 3"

prev_chapter:
  title: "Lecture 2"
  url: "/course-spattempdyn-lecture2/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 4"
  url: "/course-spattempdyn-lecture4/"

math: true
---

Lecture 3 focused on density-dependent growth, introducing the logistic growth model as an extension of the exponential growth model covered in the previous lecture. The lecture examined how resource limitations affect population growth and how this leads to equilibrium population sizes. Additionally, concepts such as overcompensation, chaos, and bifurcation in discrete population models were introduced.

## Population Dynamics and Exponential Growth Recap

The exponential growth model assumes unlimited resources and constant birth and death rates. The basic differential equation is

$$\frac{dN}{dt} = rN,$$

where $ r $ is the intrinsic growth rate, defined as

$$r = b - d$$

with $ b $ as the birth rate and $ d $ as the death rate. The solution to this equation is

$$N_t = N_0 e^{rt}$$

In discrete time, the model is written as

$$N_{t+1} = N_t + rN_t$$

However, real populations do not grow indefinitely. Instead, they encounter resource limitations, leading to density-dependent effects that modify growth dynamics.

## Logistic Growth Model

When resources are limited, birth and death rates depend on the population size. In this case, population growth is no longer purely exponential. Instead, the differential equation for population growth includes density dependence:

$$\frac{dN}{dt} = b' N - d' N$$

where the effective birth and death rates, $ b'(N) $ and $ d'(N) $, are functions of population size. These are typically modeled as:

$$b'(N) = b - aN$$
$$d'(N) = d + cN$$

where $ a $ and $ c $ are constants that describe how birth and death rates change with population size. Substituting these into the differential equation gives:

$$\frac{dN}{dt} = (b - aN - d - cN) N$$

which simplifies to:

$$\frac{dN}{dt} = rN \left( 1 - \frac{a + c}{b - d} N \right)$$

Defining the carrying capacity $ K $ as

$$K = \frac{b - d}{a + c}$$

the equation is rewritten in its standard logistic form:

$$\frac{dN}{dt} = rN \left( 1 - \frac{N}{K} \right)$$

The logistic model introduces a self-regulating mechanism: when the population is small, growth is nearly exponential, but as $ N$ approaches $K$, the growth rate slows down. If $N > K$, the growth rate becomes negative, leading to a decline in population size.

## Equilibrium and Stability

Equilibria in population models are found by setting the growth rate to zero:

$$\frac{dN}{dt} = 0$$

For the logistic model:

$$rN \left( 1 - \frac{N}{K} \right) = 0$$

Solving for $ N $, the equilibria are:

$$N = 0 \quad \text{or} \quad N = K$$

The equilibrium at $ N = 0 $ is unstable, meaning that any small increase in population will lead to further growth. The equilibrium at $ N = K $ is stable, meaning if the population deviates slightly from $ K $, density dependence restores it to equilibrium.

In discrete-time models, large growth rates can lead to overcompensation, where the population overshoots the carrying capacity and then crashes. This creates oscillatory behavior instead of smooth convergence to equilibrium. The discrete logistic equation is:

$$N_{t+1} = N_t + rN_t \left( 1 - \frac{N_t}{K} \right)$$

For small $ r $, the population stabilizes at $ K $, but as $ r $ increases, the system begins oscillating between two or more values, leading to chaotic dynamics.

The simplest equation to exhibit chaos is the logistic growth equation. As $ r $ increases, bifurcations occur, meaning that the system transitions from stable equilibrium to periodic cycles, and eventually to chaotic fluctuations. This behavior is a hallmark of nonlinear population models.

At very high $ r $, small changes in initial conditions can lead to drastically different long-term outcomes. This is known as the butterfly effect, first described by Edward Lorenz in 1961.
