---
layout: chapter
title: "Lecture 1 - What is a model?"
permalink: /course-spattempdyn-lecture1/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Lecture 1"

prev_chapter:
  title: "Overview"
  url: "/course-spattempdyn/"

course:
  name: "Spatial and Temporal Dynamics"
  url: "/course-spattempdyn/"

next_chapter:
  title: "Lecture 2"
  url: "/course-spattempdyn-lecture2/"

math: true
---

The lecture started with a basic but crucial question: What is a model? In the context of ecology, a model is a simplified representation of reality, designed to capture the essential processes of an ecological system while ignoring unnecessary complexity. This abstraction is necessary because ecological systems are highly complex, with countless interactions between organisms, their environment, and external influences. Models allow us to test hypotheses, explore scenarios, and make predictions by focusing on key processes rather than every possible detail.

A model must be built with a specific purpose in mind. This was illustrated through an example: How do invasive cats impact native bird populations on an island? The ecological system is complex, but by identifying key processes, i.e. birth, death, migration, and predation, we can construct a model that captures the core dynamics affecting bird populations. This process of simplification and structuring is at the heart of ecological modelling.

## The Modelling Cycle

A main takeaway from the lecture was the modelling cycle, which provides a structured approach to developing ecological models. The process follows six main steps:

1. Formulating the research question (Clearly defining what needs to be studied and what hypotheses should be tested)

2. Conceptualizing the model (Identifying relevant ecological processes and how they interact)

3. Implementing the model (Translating the conceptual framework into mathematical equations and computer code)

4. Analyzing model outputs (Examining whether the results align with expectations and ecological knowledge)

5. Communicating results (Interpreting findings in a meaningful way and considering ecological implications)

6. Refining the model (Adjusting assumptions, parameter values, or model structure based on new insights)

This iterative approach ensures that models evolve and improve over time. Many ecological models go through multiple cycles of refinement before they are considered useful for scientific interpretation.

## Mathematical Foundations

After covering some basic principles of modelling, we shifted toward the fundamental mathematical functions underlying ecological models. One can differentiate between continuous and discrete functions. Many natural processes, such as bacterial growth or nutrient cycling, occur continuously over time. These processes are often described by differential equations, which track the rate of change rather than absolute values at specific time points. In contrast, species with seasonal reproduction cycles or organisms that have distinct life stages (e.g., annual plants, insects with metamorphosis) are better represented using difference equations, which capture population sizes at fixed time intervals. Since unlimited growth is not realistic in most ecosystems, we also explored density-dependent growth, which introduces limitations such as resource availability, competition, or predation.

### Linear Growth

Linear growth describes a processes that change at a constant rate over time. The general form of a linear growth function is

$$f(x) = kx + d,$$

where $k$ is the slope and $d$ is the intercept. Linear models are simple but useful for representing basic ecological processes like constant reproduction rates or steady resource accumulation. An example discussed in the lecture was egg production in the European paper wasp (Polistes dominula). The model assumes that a queen produces an initial batch of 100 workers in spring and then lays a constant number of 35 eggs per day:

$$f(x) = 35x + 100$$

This type of growth is common in early-stage population expansion but does not capture resource limitations or density-dependent effects.

### Exponential Growth

Unlike linear growth, exponential growth describes a process where the rate of change is proportional to the current population size. The general form of exponential growth is:

$$\frac{dN}{dt} = rN$$

where $N$ is the population size, $r$ is the growth rate, and $t$ is time. The solution to this equation gives the classic exponential growth function:

$$N_t = N_0 e^{rt}$$

where $N_0$ is the initial population size. A well-known example is bacterial growth, where each bacterium divides every hour, doubling the population:

$$N_t = 2^t$$

After 24 hours, this leads to a massive population size:

$$N_{24} = 16,777,216$$

Of course, unlimited exponential growth is not realistic because resources eventually become limited, leading to constraints that require more advanced models like logistic growth.

### Quadratic Growth and Interaction Effects

Moving beyond exponential growth, we learned how interactions between individuals or species can lead to quadratic growth patterns. Unlike linear or exponential models, which assume independent individuals, quadratic models introduce density-dependent interactions, where the rate of change depends on how individuals interact with each other. One example is competition for resources, where the probability of two individuals encountering each other increases with population size. If resources are limited, the growth rate slows down as population density increases. This type of relationship is often represented using a quadratic term, which modifies the classic exponential growth equation.

The Law of Mass Action, describes how the rate of a process depends on the density of interacting individuals. This principle is widely used in epidemiological models to represent how diseases spread. The number of new infections per unit time is often proportional to the number of susceptible ($S$) and infected ($I$) individuals in a population, leading to a quadratic term:

$$\frac{dI}{dt} = \beta S I,$$

where $\beta$ is the transmission rate. This equation reflects the fact that as more individuals come into contact, the spread of infection accelerates. A similar principle applies to predator-prey models, where the encounter rate between predators and prey determines predation success.

Beyond disease dynamics, similar quadratic terms appear in other ecological processes. For instance, in predator-prey models, the rate at which predators consume prey depends on how often predators and prey encounter each other, leading to an interaction term of the form:

$$\frac{dN}{dt} = rN - cPN$$

$$\frac{dP}{dt} = ecPN - dP,$$

where $N$ is the prey population, $P$ is the predator population, $r$ is the prey intrinsic growth rate, $c$ is the predation rate coefficient, $e$ is the conversion efficiency of prey into predator offspring, and $d$ is the predator death rate.

These quadratic interactions consider that in many ecological systems, growth is not just a function of individual reproduction but also of species interactions. Whether it's competition, predation, or disease transmission, the processes that shape population dynamics cannot be captured by simple linear or exponential models.

### Logarithmic Growth

Some biological processes do not exhibit simple linear or exponential growth but instead follow a logarithmic pattern, where the rate of increase slows over time. One example is Dyar's rule, which describes larval growth in insects. Unlike continuous growth, insect larvae grow in discrete stages, molting between each stage. The size of the insect increases at a nearly constant ratio between molts:

$$\text{size}(t) = b \cdot 1.4^t,$$

where $b$ is the initial size and $t$ is the number of molts.

When plotted on a logarithmic scale, this function appears linear, simplifying the analysis of growth patterns. Logarithmic growth is also observed in resource-limited systems, where early growth is fast but slows as resources become scarce.

### Reciprocal Growth

Another ecological concept is predator dilution. Many species form large groups to reduce their individual probability of being attacked by predators. The probability of being eaten in a group of size $n$ follows a reciprocal function:

$$p(n) = \frac{1}{n}$$

This reflects a diminishing effect: as group size increases, predation risk approaches zero but never fully disappears. This explains why animals such as fish, birds, and ungulates form large aggregations - not only does it reduce the chance of predation, but it can also provide advantages in foraging and thermoregulation.
