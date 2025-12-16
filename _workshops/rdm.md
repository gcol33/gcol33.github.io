---
layout: workshop
title: "Research Data Management"
date: 2024-10-23
category: "Education"
category_url: "/education/"
description: "This workshop on research data management in the life sciences was developed at the University of Vienna and delivered in an interactive format using LiaScript. It introduced the principles and practices of handling research data across the entire research cycle, with the goal of making data FAIR: Findable, Accessible, Interoperable, and Reusable. Rather than treating data management as an afterthought, the course framed it as a foundation of good scientific practice. Each module combined theory, case studies, and practical exercises to highlight both the opportunities and the responsibilities that come with managing research data in the life sciences."
thumbnail: "/assets/images/content/data_cycle2.png"
thumbnail_webp: "/assets/images/content/data_cycle2.webp"
hero_bg_class: "bg-data-cycle2"
hero_title: "Take aways"
hero_content: "The workshop showed that research data management is not a bureaucratic add-on but a core part of scientific practice. Good RDM strengthens reproducibility, supports collaboration, and extends the impact of projects beyond their immediate lifetime. Clear organization and documentation reduce the risk of data loss and make results easier to verify. What first appears as administration is in fact a practical tool for better science."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Education"
    url: "/education/"
  - name: "Research Data Management"
---

## Core Topics

The course framed RDM within the entire research cycle. Data are not just a by-product of analysis but a resource that lives through multiple stages, from project planning to archiving and eventual reuse. One of the first themes was planning. A data management plan anticipates what kinds of data will be produced, how they will be structured, and where they will be stored. This planning step is often mandated by funders, but even without external requirements it prevents confusion, protects sensitive information, and ensures that collaborators have a common framework.

Documentation and metadata received special attention. The workshop showed how datasets quickly lose value if the context is not preserved. Metadata provide the context: what a dataset contains, how it was collected, when, where, and by whom. Standardized vocabularies and formats allow others to interpret data without relying on insider knowledge. Data dictionaries listing each variable, its unit, and its type transform raw tables into usable information.

Another core theme was storage and security. Data must be protected not only from technical failure but also from accidental deletion or unauthorized access. The workshop discussed the "3-2-1" rule: keep three copies of the data, on two different types of storage, with one stored off-site. Sensitive datasets require secure servers, encryption, and restricted access. These strategies prevent both catastrophic loss and misuse.

The final layer was preservation and sharing. The course encouraged the use of non-proprietary formats such as CSV or TIFF to ensure long-term readability. Checksums and other verification methods maintain data integrity. Trusted repositories such as Zenodo or Dryad give datasets persistent identifiers and stable access. Together, these practices align with the FAIR principles: making data findable, accessible, interoperable, and reusable. Licensing was tied directly to this step, since it defines how the data may be reused by others.

## Practical Skills

Alongside the conceptual framework, the workshop provided concrete habits for daily work. File naming and directory structure were presented as deceptively simple tools with large impact. A directory might separate raw, processed, and external datasets, scripts for analysis, and outputs such as figures and tables. File names that include dates, versions, and clear descriptors make it immediately obvious what a file contains. Instead of searching through folders or relying on memory, one can understand at a glance whether a file is raw input, a cleaned version, or an output ready for publication.

We also practiced writing data management plans. These documents translate abstract principles into step-by-step planning for specific projects. They specify file formats, naming conventions, metadata standards, storage methods, and sharing strategies. The exercise showed that planning clarifies responsibilities within a team, ensures funder compliance, and prevents ad hoc decisions later in the project.

Version control was another practical tool. The course introduced systems such as Git, which record the history of changes to code or data, making it possible to recover earlier versions or understand how results were produced. This links directly to reproducibility: by showing every modification, version control creates transparency and trust in analyses.

Finally, the workshop addressed repositories and licensing. We examined how to choose appropriate repositories for different types of data and how to assign licenses that encourage reuse while protecting credit. For example, a dataset deposited in Zenodo with a CC-BY license makes it discoverable, citable, and usable by others while ensuring attribution.

## Ethics and Standards

A major concern was the handling of sensitive information. Personal data, medical records, or the locations of endangered species require protection. Anonymization, controlled access, and secure storage were presented as ways to balance usefulness with responsibility. Ethical practice extends beyond legal compliance. It includes fairness in attribution, clarity in ownership, and accountability in collaborative projects.

The legal dimension is equally important. National regulations, institutional policies, and funder mandates all shape what can be shared and under what conditions. The workshop showed how these frameworks interact with practical choices about storage, sharing, and licensing. Researchers must be able to interpret them to avoid both accidental violations and unnecessary restrictions.

## Licensing

Licensing was treated as part of RDM rather than as an afterthought. The choice of license determines whether data and code remain locked away or become resources for the broader community. For code, permissive licenses such as MIT allow wide reuse, while copyleft licenses such as GPL ensure that derivatives remain open. For data, Creative Commons licenses provide a spectrum of options, from fully open (CC0) to attribution-required (CC-BY) to more restrictive forms.

The workshop worked through scenarios to show how licenses matter in practice. A researcher reusing GitHub code must respect the license under which it was shared. A dataset deposited with CC-BY can be reused commercially, but credit must be given. Teaching materials can be shared under licenses that encourage adaptation while still requiring attribution. These examples showed that licensing shapes visibility, collaboration, and impact.

The final lesson was that licensing should be built into project planning. Choosing the right license from the start ensures that outputs can be shared openly and used responsibly, aligning individual projects with the wider goals of open and reproducible science.

### License Comparison

| License Type | License | Modification | Distribution | Patent Use | License Notice | Must Share Changes | Closed-Source Allowed | Attribution Required |
|--------------|---------|--------------|--------------|------------|----------------|-------------------|----------------------|---------------------|
| Permissive | MIT | Yes | Yes | No | Yes | No | Yes | No |
| Permissive | Apache 2.0 | Yes | Yes | Yes | Yes | No | Yes | No |
| Permissive | BSD 3-Clause | Yes | Yes | No | Yes | No | Yes | No |
| Permissive | BSD 2-Clause | Yes | Yes | No | Yes | No | Yes | No |
| Permissive | CC0 | Yes | Yes | No | No | No | Yes | No |
| Copyleft | GPL v3 | Yes | Yes | No | Yes | Yes | No | No |
| Copyleft | LGPL v3 | Yes | Yes | No | Yes | Yes | Yes | No |
| Copyleft | AGPL v3 | Yes | Yes | No | Yes | Yes | No | No |
| Copyleft | EUPL 1.2 | Yes | Yes | No | Yes | Yes | No | No |
| Copyleft | CC-BY-SA 4.0 | Yes | Yes | No | No | Yes | Yes | Yes |
