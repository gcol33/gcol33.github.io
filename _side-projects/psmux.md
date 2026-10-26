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

tmux is my favourite tool for working from my phone. It keeps the terminal session running on the machine itself, so I can resume where I left off. Phones drop their connection from time to time, and without tmux I would have to start over each time.

Windows never had that. tmux needs the terminal interface of Unix systems, which Windows lacks, so on Windows it only runs inside WSL, a Linux system running inside Windows.

Then I found [psmux](https://github.com/psmux/psmux), a tmux for Windows written in Rust. It runs natively and takes the same commands as tmux.

I like it because of how I work now. A few years ago it was normal to sit at a PC all day, and agentic LLMs are changing that: more and more, I dictate into my phone, the text goes to an agent on my workstation over [Tailscale](https://tailscale.com), a private network between my own devices, and the agent runs the commands. I find that workflow cool in itself. The agent runs inside psmux, so when I SSH in from my phone I land in the same session it is working in, and when I put the phone away it keeps going.

But when I scrolled up in Termius, the SSH app I use on my phone, the earlier output wasn't there, because psmux redraws the screen in place. I couldn't read back what the agent had done. I wrote a client mode that sends the pane's plain output to the terminal instead, and scrolling back works again:

```
psmux attach -f passthrough
```

I sent the fix to psmux ([#900](https://github.com/psmux/psmux/pull/900)). The next day the maintainer had added it, tested it over SSH, fixed a bug I had missed, thanked me and sent a list of five things to improve. As an open-source developer you mostly hear from people when something breaks, so a review like that really got to me. I worked through all five in a follow-up ([#913](https://github.com/psmux/psmux/pull/913)).

My setup is a stack of small tools: Tailscale, Termius, psmux and the agent. When one of them is missing a piece, I can add it.

In *Star Trek IV*, Scotty lands in the 1980s, picks up a computer mouse and talks into it: "Hello, computer." In 1986 that was a joke. When I dictate a task into my phone and watch my workstation carry it out, it feels like we are slowly getting to the version of that scene where the computer answers.
