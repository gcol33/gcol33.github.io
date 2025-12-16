---
layout: workshop
title: "Vegetation Plot Workshop"
date: 2025-03-13
category: "Education"
category_url: "/education/"
description: "The Vegetation Plot Data Workshop took place at the Department at Rennweg, bringing together in house researchers working with vegetation plot data to discuss shared challenges and develop a more efficient and reproducible workflow. Organized by Michael Glaser and Bernd Lenzner, the one-day workshop provided an informal and interactive space to exchange experiences, identify common hurdles, and explore solutions for handling, standardizing, and analyzing plot data."
thumbnail: "/assets/images/content/plots_ws.jpg"
thumbnail_webp: "/assets/images/content/plots_ws.webp"
hero_bg_class: "bg-workshop-pd-bg"
hero_title: "Take aways"
hero_content: "We chose three common struggles when working with plot based data: data cleaning and standardization, taxonomic harmonization, and linking to other data sources. As for the output of the workshop: we made a table for common data sources and tools people want to combine with their plot data and additionally a table of common issues and pitfalls and suggestions on how to tackle these issues.<br><br>More generally we had a discussion about a checklist of common errors, such as duplicate plots and different abundance scales. Maybe this can be followed up with a short paper on how to deal with large plot databases."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Vegetation Plot Workshop"
---

## Morning

### A short round of introductions

Many of us work with plot data, yet we often do so in isolation, reinventing the wheel rather than building on existing solutions. This became clear during a recent workshop where researchers from different backgrounds shared their experiences with plot data and its challenges, pitfalls, and best practices. Long-time experts and newcomers, everyone at the workshop had his own perspective on working with plot data.

<ul>
<li><p>Michael has been working with EVA and resurvey data for years and has the experience to handle many challenges.</p></li>
<li><p>Andy encounters plot data occasionally and is interested in workflow best practices, though data format inconsistencies remain a hurdle.</p></li>
<li><p>Bernd has limited experience but is now involved in projects that rely on plot data, making it important to understand its challenges.</p></li>
<li><p>Me (Gilles) sees over- and under-sampling as the biggest hurdles when working with plot data.</p></li>
<li><p>Ekin struggles with understanding column definitions and what they actually represent but plans to rely on colleagues like Michael and Joni to overcome these issues.</p></li>
<li><p>Wolfgang works extensively with relevees, contributing to the Austrian Vegetation Database (75,000 relevees) and EVA. Managing this data optimally would be a full-time job, but he does it in his spare time. Missing coordinates, incomplete records, and taxonomic standardization are major bottlenecks.</p></li>
<li><p>Joni builds species distribution models (SDMs) using EVA data but finds taxonomic harmonization a persistent issue. EVA is not fully harmonized, requiring manual checks with external sources like POWO.</p></li>
<li><p>Daijun has used forest plot data since his PhD and plans to work with sPlot data in the future. Geographic bias and inconsistencies in plot size remain challenges.</p></li>
<li><p>Elias is just beginning to compile and format plot data for his PhD, finding the process of preparing data to be a major hurdle.</p></li>
<li><p>Karl has worked with plot data to varying degrees of success. Data quality and distribution issues have sometimes been insurmountable, leading him to circumvent rather than resolve certain challenges.</p></li>
</ul>

### Results of the questionnaire

<div class="row mb-lg-2">
<div class="col-lg-6">
<picture>
<source type="image/webp" srcset="/assets/images/content/workshop_pd_morning2.webp">
<img src="/assets/images/content/workshop_pd_morning2.jpg" class="img-fluid mx-auto d-block img-rd-md lazyload" alt="workshop_pd_morning" width="628" height="419">
</picture>
</div>
<div class="col">
<picture>
<source type="image/webp" srcset="/assets/images/content/workshop_pd_pie.webp">
<img src="/assets/images/content/workshop_pd_pie.png" class="img-fluid mx-auto d-block img-workshop-pd-p-style mb-lg-2 lazyload" alt="workshop_pd_pie" width="605" height="298">
</picture>
<p class="p-bloc-32-style text-justify">The majority of respondents (61.5%) plan to work with plot data in the future, with a smaller portion uncertain (30.8%) and only one person indicating they won't. This confirms that plot data will remain an important component for our group, making discussions around best practices still relevant.</p>
</div>
</div>

In the survey, participants ranked common challenges in working with plot data. After applying some fancy math*, we came up with the following ranking:

<ol>
<li><p>Data cleaning</p></li>
<li><p>Reproducible reports</p></li>
<li><p>Taxonomic harmonization</p></li>
<li><p>Linking to other data sources</p></li>
<li><p>Metadata issues and feedback</p></li>
<li><p>Plot level metrics</p></li>
</ol>

<div class="blockquote">
<p class="p-234-style">*The ranking was calculated using Likert scaling, where topics were scored from -3 (not relevant) to +3 (highly relevant) and weighted by the number of votes. Other ranking methods produced similar results, reinforcing these as priority areas for the community. Ultimately, people can decide what they find relevant.</p>
</div>

### Forming break out groups

<div class="row mb-lg-2">
<div class="col">
<picture>
<source type="image/webp" srcset="/assets/images/content/workshop_pd_morning4.webp">
<img src="/assets/images/content/workshop_pd_morning4.jpg" class="img-fluid mx-auto d-block img-rd-md lazyload" alt="workshop_pd_morning2" width="628" height="419">
</picture>
</div>
<div class="col">
<picture>
<source type="image/webp" srcset="/assets/images/content/workshop_pd_morning3.webp">
<img src="/assets/images/content/workshop_pd_morning3.jpg" class="img-fluid mx-auto d-block img-rd-md lazyload" alt="workshop_pd_morning3" width="628" height="419">
</picture>
</div>
</div>

During the morning breakout session, we split into three groups to focus on topics 1, 3 and 4 as these gathered the most interest. Each group discussed common challenges, shared experiences, and possible solutions. The output should be a sharable document to be used by new people or people already working with the data as a guideline.

#### Group 1: Topic 1 - Data cleaning (and beyond)

*Participants: Andi, Elias, Karl (+Emma joining later)*

Group 1 focused on data cleaning and standardization, though the discussion extended to broader topics. They identified the need for a unified format for data analysis, as inconsistencies persist even within the same project. Terms like Taxon, Species, and PlantName are not always used consistently, highlighting a necessity of establishing project-wide and *department-wide standards*, ideally with some level of automation or data standards everyone should follow.

Karl has a personal list of data sources that he considers when starting new projects, which could be useful for others as well. The group discussed how different sources are used inconsistently across projects and how a more unified approach could improve data handling. They also explored how to integrate data into department-wide standards and debated naming conventions for plot IDs, weighing the benefits of composite vs. free-standing primary keys and the need to define a normal form for structuring data. As the discussion got sidetracked they tried to refocus by working backward from the goal of what they want.

The group saw value in creating checklists and workflows, potentially including code snippets, but saw challenges in how to store, share, and especially maintain these resources to keep them up to date. While the discussion was not highly structured, important points were raised.

#### Group 2: Topic 3 - Taxonomic standardization

*Participants: Joni, Ekin, Wolfgang*

The group discussed the challenges of taxonomic harmonization and how to approach it effectively. One key takeaway was the importance of clarifying needs before starting:

<ul>
<li><p>Small-scale studies → Manual verification may be manageable.</p></li>
<li><p>Large-scale datasets → Automation is necessary</p></li>
</ul>

They also considered the scope of harmonization, emphasizing the need to avoid unnecessary complexity. A major question that should always be asked is whether subspecies and varieties need to be included, as this can significantly increase the workload. These are the main R packages people are using:

<ul>
<li><p>WFO (World Flora Online) is the main reference people are using right now</p></li>
<li><p>rWCVP (Royal Botanic Gardens, Kew's World Checklist of Vascular Plants)</p></li>
<li><p>taxize (allows matching across multiple sources, including WFO, GBIF, and ITIS)</p></li>
</ul>

The group noted that The Plant List has been discontinued, requiring users to rely on more current tools. But also with these tools challenges remain. One such issue is fuzzy matching, which is not always reliable and should be used cautiously. Difficulties also arise when standardizing aggregates, varieties, and hybrids, as they do not always fit neatly into existing frameworks. The group suggested that a list of known issues could help prevent recurring problems and provide clearer guidelines for future users.

#### Group 3: Topic 4 - Linking to other Data Sources

*Participants: Gilles (me), Daijun, Michi, Bernd*

My group focused on the challenges and strategies for integrating external data sources into plot-based research. We discussed how different datasets can be linked, common pitfalls, and potential solutions. We came up with a table to summarize the information:

##### Data sources

<table class="base-table collapsible-table">
<thead>
<tr><th>Type</th><th>Connection</th><th>Sources</th><th>Tools</th></tr>
</thead>
<tbody>
<tr><td>Biogeographic status</td><td>Species, Region</td><td><a href="https://glonaf.org/">GloNAF</a>, <a href="https://gift.uni-goettingen.de/home">GIFT</a>, <a href="https://powo.science.kew.org/">POWO</a>, <a href="https://www.preslia.cz/article/11566">Kalusová et al. (2024)</a></td><td><a href="https://doi.org/10.3897/neobiota.74.81082">DASCO</a>, <a href="https://github.com/EduardoArle/bRacatus">bRacatus</a> (R packages)</td></tr>
<tr><td>Traits</td><td>Species</td><td><a href="https://www.try-db.org/">TRY</a>, <a href="https://gift.uni-goettingen.de/home">GIFT</a>, <a href="https://bien.nceas.ucsb.edu/bien/">BIEN</a>, <a href="https://groot-database.github.io/GRooT/">GRooT</a>, <a href="https://kew.iro.bl.uk/concern/datasets/7243d727-e28d-419d-a8f7-9ebef5b9e03e">WCUPS</a></td><td></td></tr>
<tr><td>Phylogeny</td><td>Species</td><td><a href="https://doi.org/10.1093/jpe/rtv047">Qiang & Jin (2016)</a></td><td><a href="https://doi.org/10.1016/j.pld.2022.12.007">PhyloMaker</a> (R package)</td></tr>
<tr><td>Threats</td><td>Species, Region</td><td><a href="https://www.iucnredlist.org/">IUCN Red List</a></td><td></td></tr>
<tr><td>Ecological Indicator values</td><td>Species</td><td><a href="https://doi.org/10.1111/jvs.13168">Tichý et al. (2023)</a>, <a href="https://doi.org/10.3897/VCS.98324">Dengler et al. (2023)</a></td><td></td></tr>
<tr><td>First Records</td><td>Species</td><td><a href="https://zenodo.org/records/3690742">Seebens et al. (2023)</a></td><td></td></tr>
<tr><td>Biogeographic Region</td><td>Coordinates</td><td><a href="https://www.tdwg.org/">TDWG</a></td><td></td></tr>
<tr><td>Biomes / Ecoregion</td><td>Coordinates</td><td>TEOW (<a href="https://doi.org/10.1641/0006-3568(2001)051%5B0933:TEOTWA%5D2.0.CO;2">Olson et al., 2001</a>), Global Ecoregions (<a href="https://doi.org/10.1093/biosci/bix014">Dinerstein et al., 2017</a>), Anthromes (<a href="https://doi.org/10.1890/070062">Ellis et al., 2010</a>)</td><td></td></tr>
<tr><td>Political Region</td><td>Region</td><td><a href="https://www.iso.org/iso-3166-country-codes.html">ISO</a>, <a href="https://www.tdwg.org/">TDWG</a></td><td></td></tr>
<tr><td>Landcover</td><td>Coordinates, Time</td><td><a href="https://land.copernicus.eu/en/products/corine-land-cover">CORINE</a>, <a href="https://luh.umd.edu/">LUH</a>, <a href="https://www.pbl.nl/en/hyde-history-database-of-the-global-environment">HYDE</a>, <a href="https://landchange.imk-ifu.kit.edu/hilda">HILDA+</a></td><td></td></tr>
<tr><td>Climate</td><td>Coordinates, Time</td><td><a href="https://www.worldclim.org/">WorldClim</a>, <a href="https://chelsa-climate.org/">CHELSA</a></td><td></td></tr>
<tr><td>Socio-economic indicators (countries)</td><td>Country, Time</td><td><a href="https://hdr.undp.org/data-center/documentation-and-downloads">HDI</a>, <a href="https://data.worldbank.org/indicator/">GDP</a></td><td></td></tr>
<tr><td>Socio-economic indicators (explicit)</td><td>Coordinates, Time</td><td><a href="https://data.worldbank.org/indicator/">GDP</a>, <a href="https://www.earthdata.nasa.gov/data/catalog/sedac-ciesin-sedac-hanpp-percent-1.00">HANPP</a>, <a href="https://www.openstreetmap.org/">OSM</a></td><td></td></tr>
<tr><td>Research Intensity</td><td>Coordinates, Time</td><td><a href="https://www.nature.com/articles/ncomms9221">Meyer et al. 2015</a></td><td></td></tr>
</tbody>
</table>

## Afternoon

### Breakout Group Discussions

In the afternoon, Groups 1 and 2 combined to continue their general discussions on guidelines for handling plot data. Group 3 focused on improving the framework for linking external data sources, with Ekin joining the discussion. The shift in structure aimed to refine the morning's ideas. Group 3 continued their work on the tables and Group 1 & 2 had some issues to define a clear outcome, leading to a more open-ended discussion.

<div class="row mb-lg-3">
<div class="col">
<picture>
<source type="image/webp" srcset="/assets/images/content/workshop_pd_afternoon2.webp">
<img src="/assets/images/content/workshop_pd_afternoon2.jpg" class="img-fluid mx-auto d-block img-rd-md lazyload" alt="workshop_pd_afternoon2" width="628" height="419">
</picture>
</div>
<div class="col">
<picture>
<source type="image/webp" srcset="/assets/images/content/workshop_pd_afternoon.webp">
<img src="/assets/images/content/workshop_pd_afternoon.jpg" class="img-fluid mx-auto d-block img-rd-md lazyload" alt="workshop_pd_afternoon" width="628" height="419">
</picture>
</div>
</div>

#### Group 1 & 2: Defining Common Guidelines

*Participants: Joni, Ekin, Wolfgang, Andi, Karl, Emma, Elias*

The merged group explored different aspects of data standardization and taxonomic harmonization, leading to a broad discussion of recurring challenges. They started a table listing common issues encountered when working with large plot datasets, including:

<ul>
<li><p>Duplicate plots</p></li>
<li><p>Differences in abundance scales</p></li>
<li><p>Other known inconsistencies that can impact data integrity</p></li>
</ul>

The idea of a checklist of common errors was voiced. This should be available to the whole department.

#### Group 3: Expanding Linking Data Sources

*Participants: Ekin, Bernd, Michi, Gilles (me)*

My group continued refining the approach to linking external data sources. We identified two main categories of problems:

<ol>
<li><p>Limitations of the data itself (e.g., missing information, outdated classifications).</p></li>
<li><p>Challenges in linking different sources (e.g., inconsistencies in geographic or taxonomic definitions).</p></li>
</ol>

They discussed sharing the table as an online document for broader accessibility, potentially integrating it into the BioInvasion Wiki to serve as a community resource. The table was structured into two parts: 1) A table of data sources (which datasets to use for specific attributes) and 2) A table of issues (common pitfalls and how to address them).

##### Limitations and Resolutions

<table class="base-table collapsible-table">
<thead>
<tr><th>Type</th><th>Limitations of Data</th><th>Limitations of Linking Data</th><th>Approach to Address These Limitations</th></tr>
</thead>
<tbody>
<tr><td rowspan="4">Biogeographic status</td><td></td><td>Mismatch GloNaf and GIFT</td><td>Use GloNAF as the authority for alien species classification since it specializes in alien species.</td></tr>
<tr><td>Spatial status mismatch (alien in part of region, native in other part)</td><td></td><td>Cross-check the age and source of biogeographic data. Use multiple sources as a tie-breaker (e.g., regional floras, expert assessments).</td></tr>
<tr><td>Data Gaps</td><td></td><td>Use complementary sources (e.g., national databases, regional species checklists) to fill gaps.</td></tr>
<tr><td>Classifying archaeophytes vs. neophytes</td><td></td><td></td></tr>
<tr><td rowspan="3">Climate*</td><td>Spatial uncertainty in climate datasets</td><td></td><td></td></tr>
<tr><td>Extreme years in climate records</td><td></td><td>Apply rolling averages (e.g., past 10–30 years) to smooth outlier years</td></tr>
<tr><td></td><td>Broad range of available future climate projections</td><td>Use multiple global circulation models (GCMs), including region-specific models, and ensemble averaging to capture projection uncertainties.</td></tr>
<tr><td rowspan="2">First Records</td><td>Resolution is often at the country level (adequate for continental but not fine-scale analyses)</td><td></td><td>Infer finer-scale estimates using surrounding country data, species' median residence times, or expert-verified local records.</td></tr>
<tr><td>Uncertainty in first record data (earliest record ≠ actual first establishment)</td><td></td><td>Validate with additional sources (e.g., GBIF occurrence data, herbarium records) and apply probabilistic approaches to estimate introduction timing.</td></tr>
<tr><td rowspan="2">Land Cover*</td><td></td><td>Mismatch between plot-level habitat classification and land cover datasets</td><td></td></tr>
<tr><td>Accounting for gross vs. net land use change (e.g., what changes to what)</td><td></td><td>Track specific land use transitions over time</td></tr>
<tr><td>Political region</td><td></td><td>Changes in political boundaries affecting spatial data</td><td>Apply standardized disaggregation methods for boundary changes or use historical boundaries when necessary.</td></tr>
<tr><td rowspan="2">Research intensity</td><td>Uneven representation of taxonomic groups</td><td></td><td>Apply sampling corrections (e.g., rarefaction) and account for taxonomic biases in analysis.</td></tr>
<tr><td>Uneven regional contributions to datasets</td><td></td><td>Use methodological controls (e.g., weighting by sampling effort) and acknowledge source biases.</td></tr>
<tr><td>Socio-economic data (countries)</td><td>Differences in socio-economic indicator definitions between countries and across time</td><td></td><td>Harmonize indicators by aligning definitions and adjusting for temporal shifts.</td></tr>
<tr><td>Socio-economic data (explicit indicators)*</td><td>Incomplete reporting or gaps in indicator-specific data</td><td></td><td>Use interpolation cautiously; validate interpolated values with alternative socio-economic datasets.</td></tr>
<tr><td>Threats</td><td>Outdated region-level species lists</td><td></td><td></td></tr>
<tr><td rowspan="3">Traits</td><td>Data Gaps</td><td></td><td>Impute missing trait values based on phylogenetic or ecological similarity. Validate imputed values and consider using CSR mapping instead</td></tr>
<tr><td>Differences in measurement source (e.g., in situ vs. lab; different life stages; native vs. invaded ranges; experimental vs. natural conditions)</td><td></td><td></td></tr>
<tr><td>Environmental plasticity in trait expression</td><td></td><td>Use summary statistics (minimum, maximum, average) and analyze the range width to capture variability for robust comparisons.</td></tr>
<tr><td>Traits, EIVs, Phylogeny</td><td></td><td>Taxonomic resolution differences (e.g., subspecies vs. varieties)</td><td>Harmonize taxonomic levels when integrating data</td></tr>
</tbody>
</table>

<p class="mb-4 mt-lg-2 mb-lg-1 text-lg-start tc-7951"><strong>*Considerations for Grid-Based Data</strong></p>

<table class="base-table">
<tbody>
<tr><th>Limitations</th><th>Solutions</th></tr>
<tr><td>Inconsistent spatial and temporal resolutions</td><td>Apply appropriate downscaling or upscaling techniques carefully</td></tr>
</tbody>
</table>

## Reflections on the Workshop

The workshop was a good effort in sharing common struggles and ideas. I liked the six topics we focused on. They covered most issues people face when working with plot data. There was, however, concern from people about where this would be shared. Without knowing where the outputs would go, some people were unsure what the outcome of the discussions would be.

That was especially noticeable in the afternoon session. Some lacked concrete goals, and without a clear output, discussions drifted. Having something specific (i.e a Word document, a structured table or a checklist) could have helped keep things more focused. Since I am not formally trained in ecology or even biology, I found the list of challenges and solutions really useful. It is not just relevant internally but could also help new PhD or master's students who are starting to work with plot data.

If I had one suggestion, it would have been good to have a clear output goal from the start. Otherwise, people just discuss and not much happens afterward. Bernd had a good idea of following up with a paper on dealing with plot data, perhaps something like "10 Common Pitfalls." That could be a good next step.
