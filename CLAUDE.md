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
| workshops | `/workshops/:name/` | workshop |
| courses | `/courses/:name/` | course-overview |
| side-projects | `/side-projects/:name/` | workshop |
| projects | `/projects/:name/` | workshop |

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

Custom CSS variables in `assets/css/style.css` `:root`:
- `--color-text-primary`: Dark text (#212121)
- `--color-text-secondary`: Medium gray (#5e5e5e)
- `--color-white`: White
- `--color-black`: Black
- `--color-bg-secondary`: Light gray background
- `--color-accent-tan`: Tan/beige accent
- `--color-accent-cream`: Cream accent
- `--color-border`: Border color

Dark mode variables in `assets/css/custom.css`:
- `--dm-bg-primary`, `--dm-bg-secondary`, `--dm-bg-tertiary`: Background tiers
- `--dm-text-primary`, `--dm-text-secondary`: Text colors
- `--dm-accent`, `--dm-border`, `--dm-code-color`: Accent/border/code

## CSS Naming Conventions

### Section structure

| CSS Class | Purpose |
|-----------|---------|
| `section` | Full-width section wrapper (flex, background cover) |
| `section-light` | Light-background section (dark text) |
| `section-dark` | Dark-background section (light text, used with hero banners) |
| `bg-texture` | Background texture overlay (use with `texture-darken` etc.) |
| `background-gradient` | Tan/cream gradient background |

### Padding utilities

| CSS Class | Padding |
|-----------|---------|
| `pad-lg` | 100px vertical |
| `pad-md` | 50px vertical |
| `pad-sm` | 20px vertical |
| `pad-none` | 0px vertical |
| `pad-{size}-{bp}` | Responsive variant (e.g. `pad-lg-lg` = 100px at >=992px) |

### Text and color utilities

| CSS Class | Purpose |
|-----------|---------|
| `tc-text-primary` | Dark text color |
| `tc-text-dark` | Black text color |
| `tc-text-light` | White text color (hero sections) |
| `tc-text-muted` | Secondary/muted text color |
| `bg-surface` | Light gray background |
| `hero-title-link` | Hero section title styling |
| `hero-separator` | Hero section separator dash |
| `title-post` | Post title link styling |

## Thumbnails for Side Projects

Side project pages (R packages, etc.) use screenshots of their pkgdown sites as thumbnails. To create a thumbnail:

```python
from playwright.sync_api import sync_playwright
from pathlib import Path

output_dir = Path(r"C:\Users\Gilles Colling\Documents\website\assets\images\content")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 2400, "height": 1600}, device_scale_factor=1)
    page.goto('https://gillescolling.com/PACKAGE_NAME/')
    page.wait_for_load_state('networkidle')
    page.screenshot(path=str(output_dir / "PACKAGE_NAME.png"))
    browser.close()
```

Then convert to JPG and WebP:
```bash
cd assets/images/content
magick PACKAGE_NAME.png PACKAGE_NAME.jpg
magick PACKAGE_NAME.png PACKAGE_NAME.webp
rm PACKAGE_NAME.png
```

Required size: **2400x1600** pixels.

## Deployment

Push to `main` branch to deploy via GitHub Pages. Jekyll builds automatically.

## Migration Notes

The site is being migrated from Blocs (static HTML) to Jekyll. Old static HTML files remain in the repo temporarily for reference. The `_site/` directory is generated output.
