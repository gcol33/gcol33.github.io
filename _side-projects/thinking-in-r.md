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
hero_label: "In Progress"
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

<p class="mb-4">
  <a href="https://gcol33.github.io/functional-r/" class="btn btn-lg btn-d button-01">Read the Book</a>
  <a href="https://github.com/gcol33/functional-r" class="btn btn-lg btn-outline-dark ms-2">Source on GitHub</a>
</p>

## What is it

[Thinking in R](https://gcol33.github.io/functional-r/) is a free, open-source book that teaches R from zero. It covers the full path from first function call to metaprogramming and package development, organized in five parts and 33 chapters.

The book is different from most R introductions in one specific way: it treats R as a language with a design, not a collection of tricks to memorize. R descends from the lambda calculus, through Lisp, Scheme, and S. That lineage explains why everything in R is a vector, why functions are values you can pass around, why `x * 2` multiplies an entire column without a loop, and why `filter(df, x > 3)` can read column names without quotes. Most R books teach *what* to type. This one also explains *why* it works, because understanding the design makes everything else easier to learn.

The five parts build on each other:

- **Foundations** (chapters 1--9): computation models, vectors, functions, logic, algorithms.
- **Working with data** (chapters 10--17): lists, data frames, strings, I/O, dplyr, tidy data, ggplot2.
- **Thinking functionally** (chapters 18--23): closures, map/reduce, function factories, recursion, lazy evaluation.
- **The type system** (chapters 24--27): S3/S7 objects, contracts and defensive code, metaprogramming, building a DSL.
- **Going further** (chapters 28--33): performance, R internals, connecting to C++/Rust/Python, packages, reproducibility.

No programming experience is assumed. By the end, you will have written real code, understood functional programming, and seen ideas that transfer to any language.

## Why I wrote it

I came to R from physics. When I started my PhD in ecology, R was the language everyone used, and nobody could tell me why it worked the way it did. Why does assignment use `<-` instead of `=`? Why does `sapply()` sometimes return a matrix and sometimes a list? Why can you write `species` inside `filter()` without quoting it? The answers I got were "that's just how R is" or "don't worry about it."

I did worry about it. I went looking and found that every quirk has a reason, and the reasons form a coherent story: Church's lambda calculus (1936), McCarthy's Lisp (1958), Sussman and Steele's Scheme (1975), Chambers' S at Bell Labs (1976), and Ihaka and Gentleman's R in Auckland (1993). Once I understood that chain, R stopped being a bag of functions and became a language I could reason about. I wanted to write the book I wish I'd had when I started.

There is also something deeper. Lambda calculus is extraordinarily elegant: three rules---variables, abstraction, application---and nothing else. No numbers, no loops, no data structures. Yet from those three rules you can build arithmetic, recursion, and any computation a machine can perform. That last part still strikes me as remarkable. In 1936, Turing defined computation with tapes and state machines; Church defined it with pure function application. The two models look nothing alike, yet they turned out to be exactly equivalent. Any function you can compute on a Turing machine, you can compute with lambdas, and vice versa. That equivalence is one of the most surprising results in the foundations of mathematics, and it means that functional programming is not a style or a preference---it is a complete model of computation. R inherits from that lineage, and I wanted to write a book that lets the reader feel it.

The other motivation is simpler. The best R books are already free: Hadley Wickham's R for Data Science, Advanced R, R Packages. Geocomputation with R. STAT 545. They proved that open-source books work: they reach more people, they get community contributions, and they stay up to date. I wanted to contribute to that ecosystem rather than compete with it. Thinking in R fills a gap between "here's how to use dplyr" and "here's the formal theory of R's evaluation model." It's the middle layer: practical enough to teach a beginner, principled enough that the knowledge compounds.

The book is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The source is on [GitHub](https://github.com/gcol33/functional-r). If you find an error, open an issue. If you want to contribute, open a pull request.
