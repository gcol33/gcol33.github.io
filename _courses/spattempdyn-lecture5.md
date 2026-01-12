---
layout: chapter
title: "Lecture 5 - Class-structured Population Models"
permalink: /course-spattempdyn-lecture5/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 5"

prev_chapter:
  title: "Lecture 4"
  url: "/course-spattempdyn-lecture4/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 6"
  url: "/course-spattempdyn-lecture6/"

math: true
---

Lecture 5 introduced class-structured population models, where individuals are categorized into different groups based on age, sex, developmental stage, or physiological condition. Unlike previous models that treated populations as homogeneous, class-structured models allow for more realistic representations of survival and reproduction patterns across different life stages. The lecture focused on age-structured models, particularly Leslie matrices, and included an application to whale populations.

#### Class-Structured Models

A class-structured model divides a population into different classes, each with distinct survival and reproductive characteristics. This contrasts with previous models where all individuals were assumed to reproduce immediately after birth and have the same birth and death rates.

Classes can be grouped by:

- Age (e.g., juveniles, adults, seniors)
- Sex (e.g., males, females)
- Developmental stage (e.g., larvae, pupae, adults)
- Physiological condition (e.g., breeding, non-breeding)
- ...

The general approach in these models is to track the number of individuals in each class over time and model how they transition between classes based on survival probabilities and fertility rates.

#### Age-Structured Population Models

Consider a species that lives for three years, where individuals reproduce once per year from their first year until death. The number of one-year-old individuals at the next time step is given by:

$$N_{1,t+1} = N_{1,t} F_1 + N_{2,t} F_2 + N_{3,t} F_3,$$

where $F_i$ represents the fertility rate of individuals aged $i$. The number of two-year-old individuals at the next time step depends on the survival of one-year-olds:

$$N_{2,t+1} = N_{1,t} S_1,$$

where $S_1$ is the survival probability of a one-year-old. The same logic applies to other age classes, repeating for each class in the population.

#### Leslie Matrix Models

A Leslie matrix is a discrete, age-structured model of population growth, developed by Patrick H. Leslie. It assumes:

- A closed population (no migration).
- Resource independence (no density effects).
- Only one sex (typically females) is considered.
- Individuals always transition to the next class without skipping stages.

The model is written in matrix notation as:

$$\begin{bmatrix}N_{1,t+1} \\\\ N_{2,t+1} \\\\ N_{3,t+1}\end{bmatrix}=\begin{bmatrix}F_1 & F_2 & F_3 \\\\ S_1 & 0 & 0 \\\\ 0 & S_2 & 0\end{bmatrix}\begin{bmatrix}N_{1,t} \\\\ N_{2,t} \\\\ N_{3,t}\end{bmatrix},$$

where $F_1, F_2, F_3$ are age-specific fertility rates, $S_1, S_2$ represent the fraction of individuals surviving to the next class, the first row represents births, and the subdiagonal entries represent survival to the next age class.

Population projections using the Leslie matrix require multiplying the matrix by the population vector at each time step:

$$N_{t+1} = A N_t,$$

where $A$ is the Leslie matrix and $N_t$ is the population vector. This multiplication gives the population size in each age class for the next time step.

#### Example: Whale Population Model

Let's consider whale populations divided into four classes:

- Calves ($n_C$)
- Immature ($n_I$)
- Mature ($n_M$)
- Reproductive ($n_R$)

Each class has specific transition probabilities:

$$\begin{bmatrix}n_{C,t+1} \\\\ n_{I,t+1} \\\\ n_{M,t+1} \\\\ n_{R,t+1}\end{bmatrix}=\begin{bmatrix}0 & 0 & 0 & F \\\\ S_{IC} & S_{II} & 0 & 0 \\\\ 0 & S_{MI} & S_{MM} & S_{MR} \\\\ 0 & S_{RI} & S_{RM} & S_{RR}\end{bmatrix}\begin{bmatrix}n_{C,t} \\\\ n_{I,t} \\\\ n_{M,t} \\\\ n_{R,t}\end{bmatrix},$$

where $S_{IC}, S_{MI}, S_{RI}$ represent transitions between classes, $S_{II}, S_{MM}, S_{RR}$ are within-class survival probabilities, and $F$ is the fertility rate of reproductive individuals.

#### Density Dependence in Class-Structured Models

Class-structured models can incorporate density dependence by modifying fertility or survival rates. To incorporate density dependence, we replace $N$ with $f(N)$ in the transition functions. Instead of assuming that all individuals experience fixed survival and fertility rates, we introduce functions that scale survival or reproduction rates based on population size. Two common approaches are:

1. Beverton-Holt (Compensatory Density Dependence), assumes population growth slows as density increases. It is defined as:

$$f(N) = N \cdot g(N) = \dfrac{N}{1 + bN},$$

where $b$ determines the strength of density dependence.

2. Ricker Model (Overcompensatory Density Dependence), predicts population overshooting followed by crashes. It is defined as:

$$f(N) = N \cdot g(N) = N e^{-bN},$$

where high $b$ values lead to large fluctuations.
