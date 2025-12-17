---
layout: chapter
title: "Project - Modelling the reintroduction of the harpy eagle (Harpia harpyja L. 1758) in southern Costa Rica"
permalink: /course-spattempdyn-project/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Spatial and Temporal Dynamics"
    url: "/course-spattempdyn/"
  - name: "Project"

prev_chapter:
  title: "Lecture 8"
  url: "/course-spattempdyn-lecture8/"

math: true
---

<div class="row">
  <div class="col">
    <div class="row">
      <div class="col align-self-center">
        <p class="text-lg-start">The harpy eagle (Harpia harpyja) is one of the most iconic apex predators in the Neotropics, primarily inhabiting the Amazon basin and parts of Central America. It plays an important role in maintaining the balance of tropical forest ecosystems. In Costa Rica, however, populations have become highly fragmented, and the species is now considered locally extinct in the south. The last confirmed sighting in that region was more than 20 years ago. Osa Conservation is preparing a reintroduction in the Osa Peninsula, an area known for its ecological richness and extensive forest cover. Successfully restoring a large raptor like the harpy eagle requires careful modelling, long-term planning, and a detailed understanding of how individuals might disperse, establish territories, and survive over time.<br><br>This project was originally part of a university course and developed in collaboration with Pablo Aycart Lazo and Markus Milchram. Since then, I have fully implemented and substantially expanded it, exploring different reintroduction strategies.</p>
      </div>
      <div class="col">
        <a href="https://news.mongabay.com/2022/09/harpy-eagles-return-to-costa-rica-means-rewildings-time-has-come-commentary/" target="_blank">
          <picture>
            <source type="image/webp" srcset="/assets/images/content/course_std_project_ref.webp">
            <img src="/assets/images/content/course_std_project_ref.jpg" class="img-fluid mx-auto d-block img-rd-md lazyload" alt="course_std_project_ref" width="628" height="419">
          </picture>
        </a>
      </div>
    </div>
  </div>
</div>

## Study Area

Spanning 2,835 km², the Osa Peninsula is home to 2.5% of the world's living species, including the famous Corcovado and Piedras Blancas National Parks. The harpy eagle, as a predator of arboreal mammals, plays an important role in shaping rainforest ecosystems, influencing nutrient distribution, and maintaining ecological balance.

<div class="row mb-4">
  <div class="col">
    <picture>
      <source type="image/webp" srcset="/assets/images/content/course_std_project_map_wide.webp">
      <img src="/assets/images/content/course_std_project_map_wide.jpg" class="img-fluid" alt="Study area map">
    </picture>
  </div>
</div>

Building the landscape, the model starts by generating a raster grid where each cell represents either suitable habitat (forest) or unsuitable land. Territories are precomputed by selecting random locations that meet habitat criteria while ensuring a minimum distance between them. A sea buffer is added around the landscape to prevent unrealistic dispersal beyond the peninsula.

## Research Questions

To better understand the feasibility and potential outcomes of a harpy eagle reintroduction, we explored the following:

- How many pairs should be released to ensure population establishment?
- How long would it take for the species to colonize the peninsula under different scenarios?
- How does release location (random vs. protected areas) affect dispersal success?

## Scenarios

Our individual-based model simulated different reintroduction scenarios:

- Number of released pairs (1, 3, or 5)
- Release locations (random vs. protected area)
- Mortality function (exponential vs. constant)
- Carrying capacity (100, 200 or 400 individuals) in the case of exponential mortality function

The model ran 10 simulations per scenario, tracking random movement, territory acquisition, breeding success, and mortality over a timespan of 167 years (2000 time steps, 1 month per step). Juveniles left the nest after two years, reaching maturity at 2.5 years old, while adults followed random-walk movement based on habitat suitability (forested vs. non-forested areas).

## Mortality

Mortality was modeled either as constant or density-dependent.

Under the constant scenarios, individuals experienced a fixed monthly death rate independent of population density. We began with baseline monthly mortality values representing minimal background mortality:

<div class="row mb-4">
  <div class="col-md-6">
    <picture>
      <source type="image/webp" srcset="/assets/images/content/Mortality_Constant.webp">
      <img src="/assets/images/content/Mortality_Constant.jpg" class="img-fluid" alt="Constant mortality">
    </picture>
  </div>
  <div class="col-md-6">
    <picture>
      <source type="image/webp" srcset="/assets/images/content/Mortality_Exponential.webp">
      <img src="/assets/images/content/Mortality_Exponential.jpg" class="img-fluid" alt="Exponential mortality">
    </picture>
  </div>
</div>

- Low baseline: 0.0008 per month (approx. 99% annual survival)
- Medium baseline: 0.0016 per month (approx. 98% annual survival)
- High baseline: 0.0032 per month (approx. 96% annual survival)

These values were derived from plausible survival rates reported in the literature, particularly for juvenile harpy eagles, which tend to face higher mortality than adults. However, because these baseline values led to unrealistically high survival across the full lifespan, we applied a uniform multiplier of 2.12, resulting in more realistic annual mortality cutoffs (~2%, 4%, and 8%).

<div class="mb-4">
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Scenario</th>
        <th>Baseline Monthly Mortality</th>
        <th>Adjusted Monthly Mortality</th>
        <th>Annual Mortality</th>
        <th>Expected Lifespan</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Low</td>
        <td>0.0008</td>
        <td>0.001696</td>
        <td>~2%</td>
        <td>~49 years</td>
      </tr>
      <tr>
        <td>Medium</td>
        <td>0.0016</td>
        <td>0.003392</td>
        <td>~4%</td>
        <td>~25 years</td>
      </tr>
      <tr>
        <td>High</td>
        <td>0.0032</td>
        <td>0.006784</td>
        <td>~8%</td>
        <td>~12 years</td>
      </tr>
    </tbody>
  </table>
</div>

This approach assumes mortality is constant for all individuals, regardless of population density. In an effort to make the model more realistic, we can use an exponential mortality function to simulate density-dependent survival. This function starts at the same baseline values used above, but increases smoothly with population size, reaching a maximum monthly mortality of 0.2094 at the carrying capacity (K).

This upper bound corresponds to 97.5% annual mortality under extreme crowding, and was chosen to reflect a strong ecological limit on population size. The value was guided by statistical reasoning: according to the Central Limit Theorem, population sizes across many simulations approximate a normal distribution, and the two sigma rule tells us that around 95% of values fall within two standard deviations of the mean.

Since this range is symmetrical, only 2.5% of population sizes are expected to exceed two standard deviations above the mean. By placing the carrying capacity at this upper 2.5% threshold and assigning it a very high mortality rate, the model ensures that population growth is only strongly limited under rare, overcrowded conditions, while remaining lenient under typical densities.

## Simulating Harpy Eagle Reintroduction

For individual movement and behavior, each eagle in the simulation follows a random walk model but with constraints based on habitat suitability. Eagles move 2 km per month in forests and 4 km per month in open areas. Individuals search for a mate once they reach maturity at 25 years and occupy an available territory of 25 km². If one member of a pair dies, the surviving partner may return to random movement.

Breeding and population growth dynamics ensure that once paired, eagles remain territorial, producing one juvenile every two years. Juveniles stay in the nest for two years before dispersing. Breeding success is limited by the number of available territories rather than the carrying capacity alone.

Mortality and survival functions are included in the model with two types of mortality. Linear mortality increases gradually with population size, while exponential mortality rises sharply as the population nears carrying capacity, set at either 100 or 200 individuals, simulating density dependence.

## Implementation

Simulating the harpy eagle reintroduction requires careful thought to handle the scale of movement, territory assignment, and population dynamics. A naïve approach, where every eagle evaluates its movement options, searches for a mate, and checks for available territories in real time, would quickly become computationally infeasible.

One of the biggest inefficiencies in the simulations comes from recalculating the same values repeatedly. Rather than dynamically determining which locations an eagle can move to at every time step, the model precomputes movement options for every possible location in the landscape. This means that when an eagle needs to move, it simply looks up precomputed options rather than recalculating them from scratch. The same principle applies to territories, rather than scanning the entire landscape to find available nesting sites, the model keeps an up-to-date list of what is occupied and what is available. This dramatically reduced our computation time.

Many of our operations, such as calculating movement possibilities or assigning territories, can be done simultaneously rather than sequentially. By distributing these tasks across multiple CPU cores, the model speeds up operations that would otherwise slow down the simulation. Instead of iterating over every eagle one by one, groups of individuals are processed in parallel per time step, reducing the bottleneck of handling large populations.

Finding mates in a simulation is a challenge. Instead of iterating over every possible pair (which would be computationally expensive), the model:

<ol><li><p>Filters for mature males and females separately.</p></li><li><p>Iterates through available males and checks if they are in proximity to available females.</p></li><li><p>Checks available territories that both individuals can access before confirming a pair.</p></li></ol>

This avoids an exhaustive $$\mathcal{O}(n^2)$$ complexity for pairwise comparisons.

Instead of dynamically expanding lists or recalculating movement at every step, the model preallocates space for individuals, their movement history, and population statistics. We aimed to keep the simulation realistic without adding unnecessary complexity. This led to the choice of fixing territories in advance rather than assigning them dynamically. Density-dependent mortality was left out to avoid slowdowns. Similarly, once a pair occupies a territory, they remain there until one of them dies.

<div class="row">
  <div class="col-md-4">
    <div style="position: relative; aspect-ratio: 712 / 650; width: 100%; margin-top: 20px; background: url('assets/backgrounds/scenario-bg.jpg') center/cover no-repeat;">
      <video id="scenarioVideo" autoplay loop muted playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: block;">
        <source id="videoSource" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
  </div>
  <div class="col-md-4">
    <div style="position: relative; aspect-ratio: 712 / 650; width: 100%; margin-top: 20px;">
      <img id="scenarioImage" alt="Scenario Plot" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; display: block;">
    </div>
  </div>
  <div class="col-md-4">
    <div>
      <div style="margin-bottom: 20px;">
        <label>Pairs Released: <span id="pairs_val">1</span></label><br>
        <input type="range" id="pairs" min="1" max="5" step="2" value="1" oninput="updateValue(this, 'pairs_val'); updateMedia();">
      </div>
      <div style="margin-bottom: 20px;">
        <label>Mortality Rate: <span id="mortality_label_val">low</span></label><br>
        <input type="range" id="mortality_label" min="0" max="2" step="1" value="0" oninput="updateMortalityLabel(this); updateMedia();">
      </div>
      <div style="margin-bottom: 20px;">
        <label><strong>Release Location:</strong></label><br>
        <label style="margin-right: 15px;">
          <input type="radio" name="release_location" value="0" checked onchange="setBinary('location', this.value)">
          Random
        </label>
        <label>
          <input type="radio" name="release_location" value="1" onchange="setBinary('location', this.value)">
          Protected
        </label>
        <input type="hidden" id="location" value="0">
      </div>
      <div style="margin-bottom: 20px;">
        <label><strong>Mortality Function:</strong></label><br>
        <label style="margin-right: 15px;">
          <input type="radio" name="mortality_func" value="0" checked onchange="setBinary('mortality_func', this.value)">
          Constant
        </label>
        <label>
          <input type="radio" name="mortality_func" value="1" onchange="setBinary('mortality_func', this.value)">
          Exponential
        </label>
        <input type="hidden" id="mortality_func" value="0">
      </div>
      <div id="capacityContainer" style="margin-bottom: 20px;">
        <label><strong>Carrying Capacity:</strong></label><br>
        <label style="margin-right: 15px;">
          <input type="radio" name="carrying_capacity" value="100" checked onchange="setBinary('capacity', this.value)">
          100
        </label>
        <label style="margin-right: 15px;">
          <input type="radio" name="carrying_capacity" value="200" onchange="setBinary('capacity', this.value)">
          200
        </label>
        <label>
          <input type="radio" name="carrying_capacity" value="400" onchange="setBinary('capacity', this.value)">
          400
        </label>
        <input type="hidden" id="capacity" value="100">
      </div>
    </div>
  </div>
</div>

<script src="/assets/js/scenarioController.js"></script>
