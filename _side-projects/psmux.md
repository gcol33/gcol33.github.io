---
layout: workshop
title: "psmux"
date: 2026-10-25
category: "Side Project"
type: contribution
category_url: "/side-projects/"
thumbnail: "/assets/images/content/psmux.jpg"
thumbnail_webp: "/assets/images/content/psmux.webp"
hero_combined: true
subtitle: "Oct 25, 2026"
description: "A client mode for psmux, tmux for Windows, that keeps the terminal's own scrollback over SSH. Landed on psmux master."
tags: [open-source, rust, terminal]
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Engagement"
    url: "/engagement-archive/"
  - name: "Side Projects"
    url: "/side-projects/"
  - name: "psmux"
---

<p class="mb-4"><a href="https://github.com/psmux/psmux/commit/39a9bf87" class="btn btn-lg btn-d button-01">View the Commit on psmux</a></p>

[psmux](https://github.com/psmux/psmux) is tmux for Windows, written in Rust. tmux keeps terminal sessions running on a machine, so you can disconnect and pick up where you left off. I use it to work on my Windows workstation over SSH from my phone.

psmux redraws the screen in place, so I couldn't scroll up on my phone. I added a client mode that sends the active pane's plain output to the terminal instead, so scrolling back works again:

```
psmux attach -f passthrough
```

It landed on psmux master in October 2026 ([#900](https://github.com/psmux/psmux/pull/900), from issue [#898](https://github.com/psmux/psmux/issues/898)). A follow-up with the maintainer's suggestions is in review ([#913](https://github.com/psmux/psmux/pull/913)): it renames the flag to `-f scrollback`, lets the server enforce read-only clients, and lets the client leave the window size to other clients.

Source and issues: [github.com/psmux/psmux](https://github.com/psmux/psmux).
