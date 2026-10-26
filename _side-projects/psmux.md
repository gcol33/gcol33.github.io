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

I think agentic LLMs, AI models that can use a computer on their own, are changing how people work. A few years ago it was normal to sit at a PC all day. More and more, I set up another way to work: I dictate into my phone, the text goes to an agent on my workstation over [Tailscale](https://tailscale.com), a private network between my own devices, and the agent runs the commands. I find that workflow cool in itself.

What holds it together is a terminal session that keeps running when I walk away. On Linux, tmux does that: the session lives on the machine, and I drop in and out of it from wherever I am. [psmux](https://github.com/psmux/psmux) brings the same to Windows, natively, written in Rust. With it I can close the laptop and pick up the same session on my phone, with everything still running.

One thing didn't work. psmux redraws the screen in place, so when I scrolled up in Termius, the SSH app I use on my phone, the earlier output wasn't there. For reading long logs, that is most of what I need. So I wrote a client mode that sends the pane's plain output to the terminal instead, and scrolling back works again:

```
psmux attach -f passthrough
```

I could have kept the fix on my own machine, and at first I did. Every psmux update overwrote it. In the project itself it works for everyone who uses psmux from a phone, and I stop maintaining a private copy. It's also the best way I know to learn: someone who knows the code far better than I do reads mine and tells me what they would do differently.

That is exactly what happened. I opened an issue and a pull request, and the next day the maintainer had picked it up. They rebased it themselves, tested it over a real SSH connection, fixed a bug I had missed, and wrote me a careful list of five things to improve, with kind words around it. As an open-source developer you mostly hear from people when something breaks, so a review like that really got to me. I worked through all five points in a follow-up ([#913](https://github.com/psmux/psmux/pull/913)). The feature itself is on psmux master ([#900](https://github.com/psmux/psmux/pull/900), from issue [#898](https://github.com/psmux/psmux/issues/898)).

I like small tools like this one: one sharp idea, a small team, something I use every day. Together with agentic tools, they are what make this way of working possible for me. They're also the projects where a single contribution still changes something, and where you get to talk to the person who built it.

In *Star Trek IV*, Scotty lands in the 1980s, picks up a computer mouse and talks into it: "Hello, computer." In 1986 that was a joke. When I dictate a task into my phone and watch my workstation carry it out, it feels like we are slowly getting to the version of that scene where the computer answers.
