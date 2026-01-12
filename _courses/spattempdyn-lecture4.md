---
layout: chapter
title: "Lecture 4 - Predator-Prey Models"
permalink: /course-spattempdyn-lecture4/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 4"

prev_chapter:
  title: "Lecture 3"
  url: "/course-spattempdyn-lecture3/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 5"
  url: "/course-spattempdyn-lecture5/"

math: true
---

Lecture 4 introduced predator-prey models, focusing on the Lotka-Volterra equations and extensions like the Rosenzweig-MacArthur model. We also covered functional responses, which describe how predator feeding rates change with prey density. These models help us understand how populations cycle and how predators and prey influence each other's abundance.

## Lotka-Volterra Predator-Prey Model

The Lotka-Volterra model describes the interaction between a predator and its prey using a system of first-order nonlinear differential equations:

$$\frac{dx}{dt} = r x - a x y$$
$$\frac{dy}{dt} = -d y + c x y,$$

where $x$ is the prey population, $y$ is the predator population, $r$ is the intrinsic growth rate of the prey, $d$ is the predator's death rate, $a$ is the predation efficiency (rate at which predators capture prey), and $c$ is the conversion efficiency (rate at which consumed prey contributes to predator reproduction).

This model assumes that:

- The prey population has unlimited food.
- The predator depends entirely on the prey for survival.
- The rate of encounters between predators and prey is proportional to both populations.
- The environment remains constant.
- There is no spatial structure or density dependence.

Solving for equilibrium points involves setting both differential equations to zero:

$$r x - a x y = 0$$
$$- d y + c x y = 0$$

This gives two equilibrium points:

1. $ x = 0, y = 0 $ (extinction of both species)

2. $ x = \frac{d}{c}, y = \frac{r}{a} $ (coexistence equilibrium)

The second equilibrium point is not stable (in the sense that small perturbations do not lead to convergence but rather to oscillations).

## Rosenzweig-MacArthur Model: Adding Density Dependence

The Lotka-Volterra model assumes that prey populations grow exponentially when predators are absent. In reality, prey populations experience resource limitations. The Rosenzweig-MacArthur model introduces density dependence in the prey equation:

$$\frac{dx}{dt} = r x \left( 1 - \frac{x}{K} \right) - a y h(x)$$
$$\frac{dy}{dt} = -d y + c y h(x),$$

where $K$ is the carrying capacity of the prey, and $h(x)$ represents the functional response (how prey consumption depends on prey density). This modification prevents unrealistic exponential growth and provides more biologically realistic population dynamics.

## Functional Responses

The functional response describes how the number of prey consumed per predator changes with prey density. Holling (1959) classified three types:

| Type | Equation $\mathbf{h(x)}$ = | Characteristics | Examples |
|------|------------------------------|-----------------|----------|
| Type I (Linear Response) | $s \cdot x$ | Consumption rate increases linearly with prey density. Assumes no handling time limitations. | Passive predators like spiders. |
| Type II (Saturating Response, Holling's Disk Equation) | $\dfrac{ax}{1 + T_h ax}$ | Consumption rate increases at a decelerating rate due to prey handling time limitations. | Damselfly nymphs preying on Daphnia. |
| Type III (Sigmoidal Response) | $\dfrac{a x^2}{1 + T_h a x^2}$ | Slow increase at low prey densities, then rapid acceleration before leveling off. Occurs when predators switch to abundant prey or improve hunting efficiency. | Predators responding to chemical cues from prey. |

Here, $T_h$ (handling time) represents the time a predator spends processing each prey item, reducing its ability to consume additional prey as prey density increases. This is a key factor in Type II and III responses which introduces stabilizing mechanisms, preventing predator-prey systems from extreme oscillations.

## Implications of Predator-Prey Models

These models show that predator-prey dynamics are inherently cyclic, with feedback loops driven by food availability and predation pressure. While the Lotka-Volterra model predicts oscillations without dampening, real-world systems include stabilizing factors such as prey refuge, alternative food sources, and adaptive predator behavior. The Rosenzweig-MacArthur model and functional response modifications provide more realistic population regulation.

This lecture introduced key predator-prey models, highlighting how they predict population cycles and how density dependence and functional responses modify these interactions. Future lectures will extend these ideas by incorporating spatial effects and stochasticity into ecological models.
