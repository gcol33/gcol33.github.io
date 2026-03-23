---
layout: workshop
title: "Thinking in R"
date: 2026-03-08
category: "Side Project"
category_url: "/side-projects/"
thumbnail: "/assets/images/content/thinking-in-r.jpg"
thumbnail_webp: "/assets/images/content/thinking-in-r.webp"
hero_bg_color: "#343739"
hero_combined: true
hero_container_class: "pad-md"
hero_label: "Published"
subtitle: "Mar 08, 2026"
description: "A free, open-source book that teaches R from scratch and explains why the language works the way it does."
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "Thinking in R"
---

<a href="https://gillescolling.com/thinking-in-r/" class="btn btn-lg btn-d button-01 mb-4">Read the Book</a>

## What is it

[Thinking in R](https://gillescolling.com/thinking-in-r/) is a free, open-source book that teaches R from zero. It covers the full path from first function call to metaprogramming and package development, organized in five parts and 33 chapters.

Why is everything in R a vector? Why are functions values you can pass around? Why does `x * 2` multiply an entire column without a loop? Why can `filter(df, x > 3)` read column names without quotes? Each chapter answers questions like these — *what* to type and *why* it works that way.

The five parts build on each other:

- **Foundations** (chapters 1--9): computation models, vectors, functions, logic, algorithms.
- **Working with data** (chapters 10--17): lists, data frames, strings, I/O, dplyr, tidy data, ggplot2.
- **Thinking functionally** (chapters 18--23): closures, map/reduce, function factories, recursion, lazy evaluation.
- **The type system** (chapters 24--27): S3/S7 objects, contracts and defensive code, metaprogramming, building a DSL.
- **Going further** (chapters 28--33): performance, R internals, connecting to C++/Rust/Python, packages, reproducibility.

No programming experience is assumed. By the end, you will have written real code, understood functional programming, and seen ideas that transfer to any language.

## Why I wrote it

I came to R from physics. When I started my PhD in ecology, R was the language everyone used, but I kept running into questions that none of the textbooks seemed to address. Why does assignment use `<-` instead of `=`? Why does `sapply()` sometimes return a matrix and sometimes a list? Why can you write `species` inside `filter()` without quoting it?

So I went looking. Every quirk had a reason, and the reasons turned out to be connected: choices made in the 1930s about what computation *is*, carried through decades of language design, all the way into the R you install today. Once I saw that chain, R stopped being a bag of functions and became a language I could reason about.

In 1936, two people independently proved that three rules are enough to compute anything a machine can compute. One of them used tapes. The other used only functions. R descends from the second one, and that descent explains things about R that most users never question.

## Why open source

In 1980, the AI Lab at MIT got a new Xerox laser printer. It jammed all the time, and print jobs would pile up with no one the wiser. With the old printer, Stallman had just modified the driver to send a notification whenever the paper jammed. But Xerox refused to release the source code for the new one, and a researcher at Carnegie Mellon who had access refused to share it because he had signed an NDA. Stallman was furious. Three years later he launched the GNU Project, and the free software movement was born. If something is broken, anyone should be able to fix it. Most of what I know about R comes from that same culture: other people's vignettes, blog posts, Stack Overflow answers, open-source textbooks. I like that anyone can contribute to something and make it better together.

A book on GitHub is a living document. Readers can open issues when something is wrong, submit pull requests when something could be better, and fork the whole thing if they want to take it in a different direction.

The book is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The source is on [GitHub](https://github.com/gcol33/thinking-in-r). If you find an error, open an issue. If you want to contribute, open a pull request.

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). Thinking in R: A Free, Open-Source Introduction to R Programming. https://gillescolling.com/thinking-in-r/</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
