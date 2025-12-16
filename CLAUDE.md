# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Jekyll-based static website** for gillescolling.com, deployed via GitHub Pages.

## Build Commands

```bash
# Install dependencies
bundle install

# Build site
bundle exec jekyll build

# Serve locally with live reload
bundle exec jekyll serve
```

## Architecture

- **Static Site Generator**: Jekyll 4.x
- **Hosting**: GitHub Pages (custom domain: gillescolling.com)
- **Framework**: Bootstrap 5 with custom CSS
- **Content**: Markdown files with YAML front matter

### Directory Structure

```
_layouts/           # Page templates
  default.html      # Base layout (navbar, footer, scripts)
  home.html         # Homepage with hero + recent posts grid
  workshop.html     # Workshop/event/presentation pages
  archive.html      # Grid listing pages
  archive-item.html # Individual publication/item pages
  course-overview.html  # Course landing with chapter grid
  chapter.html      # Course chapter with prev/next nav

_includes/          # Reusable components
  head.html         # Meta tags, CSS links
  navbar.html       # Site navigation
  footer.html       # Footer
  breadcrumb.html   # Breadcrumb navigation
  social-icons.html # Social media icons
  scripts.html      # JS includes

_pages/             # Static pages (index, archive, etc.)

# Collections (content types)
_publications/      # Academic publications
_presentations/     # Conference presentations
_workshops/         # Workshops and educational events
_courses/           # Course overview pages
_side-projects/     # Side projects
_projects/          # Main research projects

assets/
  css/              # Stylesheets
  js/               # JavaScript
  images/
    hero/           # Hero section images
    thumbnails/     # Post thumbnails
    content/        # Inline content images
    logos/          # Logo files
  fonts/            # Custom fonts
  downloads/        # PDFs and downloadable files
```

### Collections

Each content type is a Jekyll collection with its own permalink pattern:

| Collection | Permalink | Layout |
|------------|-----------|--------|
| publications | `/publications/:name/` | archive-item |
| presentations | `/presentations/:name/` | workshop |
| workshops | `/workshop-:name/` | workshop |
| courses | `/course-:name/` | course-overview |
| side-projects | `/project-:name/` | workshop |
| projects | `/proj:name/` | workshop |

### Front Matter Example

```yaml
---
layout: workshop
title: "Workshop Title"
date: 2025-01-15
category: "Education"
category_url: "/education/"
thumbnail: "/assets/images/content/image.jpg"
thumbnail_webp: "/assets/images/content/image.webp"
hero_image: "/assets/images/content/hero.jpg"
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Education"
    url: "/education/"
  - name: "Workshop Title"
---
```

## CSS Variables

Custom colors in `assets/css/style.css`:
- `--swatch-var-7020`: Dark text (#212121)
- `--swatch-var-7951`: Medium gray (#5e5e5e)
- `--swatch-var-4629`: White
- `--swatch-var-4819`: Light gray background
- `--swatch-var-684`: Tan/beige accent

## Deployment

Push to `main` branch to deploy via GitHub Pages. Jekyll builds automatically.

## Migration Notes

The site is being migrated from Blocs (static HTML) to Jekyll. Old static HTML files remain in the repo temporarily for reference. The `_site/` directory is generated output.
