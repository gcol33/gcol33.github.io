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

<a href="https://thinking-in-r.gillescolling.com/" class="btn btn-lg btn-d button-01 mb-4">Read the Book</a>

## What is it

[Thinking in R](https://thinking-in-r.gillescolling.com/) is a free, open-source book that teaches R from zero. It covers the full path from first function call to metaprogramming and package development, organized in five parts and 33 chapters.

The book treats R as a language with a design, not a collection of tricks to memorize. R descends from the lambda calculus, through Lisp, Scheme, and S. That lineage explains why everything in R is a vector, why functions are values you can pass around, why `x * 2` multiplies an entire column without a loop, and why `filter(df, x > 3)` can read column names without quotes. Traditionally, R is taught as *what* to type; this book also explains *why* it works, because understanding the design makes everything else easier to learn.

The five parts build on each other:

- **Foundations** (chapters 1--9): computation models, vectors, functions, logic, algorithms.
- **Working with data** (chapters 10--17): lists, data frames, strings, I/O, dplyr, tidy data, ggplot2.
- **Thinking functionally** (chapters 18--23): closures, map/reduce, function factories, recursion, lazy evaluation.
- **The type system** (chapters 24--27): S3/S7 objects, contracts and defensive code, metaprogramming, building a DSL.
- **Going further** (chapters 28--33): performance, R internals, connecting to C++/Rust/Python, packages, reproducibility.

No programming experience is assumed. By the end, you will have written real code, understood functional programming, and seen ideas that transfer to any language.

## Why I wrote it

I came to R from physics. When I started my PhD in ecology, R was the language everyone used, but the teaching materials rarely explained why it worked the way it did. Why does assignment use `<-` instead of `=`? Why does `sapply()` sometimes return a matrix and sometimes a list? Why can you write `species` inside `filter()` without quoting it? But the textbooks I found never explained why. They taught what to type, not why it worked, so I went looking. I found that every quirk has a reason, and the reasons form a coherent story: Church's lambda calculus (1936), McCarthy's Lisp (1958), Sussman and Steele's Scheme (1975), Chambers' S at Bell Labs (1976), and Ihaka and Gentleman's R in Auckland (1993). Once I understood that chain, R stopped being a bag of functions and became a language I could reason about.

There is also something deeper. Lambda calculus is extraordinarily elegant: three rules---variables, abstraction, application---and nothing else. No numbers, no loops, no data structures. Yet from those three rules you can build arithmetic, recursion, and any computation a machine can perform. That last part still strikes me as remarkable. In 1936, Turing defined computation with tapes and state machines; Church defined it with pure function application. The two models look nothing alike, yet they turned out to be exactly equivalent. Any function you can compute on a Turing machine, you can compute with lambdas, and vice versa. That equivalence is one of the most surprising results in the foundations of mathematics, and it means that functional programming is not a style or a preference---it is a complete model of computation. R inherits from that lineage, and I wanted to write a book that lets the reader feel it.

## Why open source

In 1980, the AI Lab at MIT got a new Xerox laser printer. It jammed all the time, and print jobs would pile up with no one the wiser. With the old printer, Stallman had just modified the driver to send a notification whenever the paper jammed. But Xerox refused to release the source code for the new one, and a researcher at Carnegie Mellon who had access refused to share it because he had signed an NDA. Stallman was furious. Three years later he launched the GNU Project, and the free software movement was born. I like the idea behind it: if something is broken, anyone should be able to fix it. Most of what I know about R comes from that same culture: other people's vignettes, blog posts, Stack Overflow answers, open-source textbooks. I like the idea that anyone can contribute to something and make it better together.

A book on GitHub is a living document. Readers can open issues when something is wrong, submit pull requests when something could be better, and fork the whole thing if they want to take it in a different direction.

The book is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The source is on [GitHub](https://github.com/gcol33/thinking-in-r). If you find an error, open an issue. If you want to contribute, open a pull request.

## Citation

<div class="citation-box">
  <p class="citation-text">Colling G (2026). Thinking in R: A Free, Open-Source Introduction to R Programming. https://thinking-in-r.gillescolling.com/</p>
  <button class="copy-btn" aria-label="Copy citation"><i class="far fa-copy"></i></button>
</div>
