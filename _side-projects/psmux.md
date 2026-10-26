---
layout: workshop
title: "Contribution to psmux"
date: 2026-10-25
category: "Side Project"
type: contribution
category_url: "/side-projects/"
thumbnail: "/assets/images/content/psmux.jpg"
thumbnail_webp: "/assets/images/content/psmux.webp"
hero_combined: true
subtitle: "Oct 25, 2026"
description: "A feature I added to psmux, an open-source tmux for Windows: a client mode that keeps the terminal's own scrollback over SSH."
tags: [open-source, rust, terminal]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "Contribution to psmux"
---

<p class="mb-4"><a href="https://github.com/psmux/psmux/commit/39a9bf87" class="btn btn-lg btn-d button-01">View the Commit on psmux</a></p>

I think agentic LLMs are changing how people work. A few years ago it was normal to sit at a PC all day. More and more, I set up another way to work: I dictate into my phone, the text goes to an agent on my workstation over [Tailscale](https://tailscale.com), a private network between my own devices, and the agent runs the commands. I find that workflow cool in itself.

The agent runs inside [psmux](https://github.com/psmux/psmux), a tmux for Windows written in Rust. When I SSH into my workstation from my phone, I land in the same session the agent is working in. When I put the phone away, the agent keeps going.

One thing didn't work. psmux redraws the screen in place, so when I scrolled up in Termius, the SSH app I use on my phone, the earlier output wasn't there and I couldn't read back what the agent had done. I wrote a client mode that sends the pane's plain output to the terminal instead, and scrolling back works again:

```
psmux attach -f passthrough
```

I could have kept the fix on my own machine, and at first I did. Every psmux update overwrote it. In the project itself it works for everyone who uses psmux from a phone, and I stop maintaining a private copy.

I opened an issue and a pull request, and the next day the maintainer had picked it up. They rebased it themselves, tested it over a real SSH connection, fixed a bug I had missed, and wrote me a careful list of five things to improve, with kind words around it. One of them I would never have found alone: `passthrough` already means something else in tmux. As an open-source developer you mostly hear from people when something breaks, so a review like that really got to me. I worked through all five points in a follow-up ([#913](https://github.com/psmux/psmux/pull/913)). The feature itself is on psmux master ([#900](https://github.com/psmux/psmux/pull/900), from issue [#898](https://github.com/psmux/psmux/issues/898)).

My setup is a stack of small tools: Tailscale, Termius, psmux and the agent. Each does one job, and when one of them is missing a piece, I can add it, as I did here. In a project this size, the person who built it reads your code the next day.

In *Star Trek IV*, Scotty lands in the 1980s, picks up a computer mouse and talks into it: "Hello, computer." In 1986 that was a joke. When I dictate a task into my phone and watch my workstation carry it out, it feels like we are slowly getting to the version of that scene where the computer answers.
