# gillescolling.com: current state

Updated 2026-08-20. Read this first, then `todo.md` for the prioritized work.

## What happened this session

A full review of the site: repo read, local build, and a live audit of the
deployed pages. **No code was changed.** Every finding below was verified, not
inferred from a grep. The working tree is clean and `HEAD` is `99878e7`.

## Environment that worked

- `bundle exec jekyll build` completes with zero Liquid or Jekyll warnings.
  Ruby 4.0 with bundler 2.6.9, Jekyll 4.4.1. The bundler-vs-rubygems
  "already initialized constant Gem::Platform" warnings on stderr are noise and
  do not affect the build.
- Build to a scratch dir for inspection: `bundle exec jekyll build --quiet
  --destination /tmp/jbuild`.
- Live-site auditing used Playwright for Python, which is installed and works.
  Edge headless screenshots gave a misleading mobile render (text appeared
  clipped at 390px when it is not); use Playwright with an explicit viewport
  instead.
- ImageMagick `magick` is on PATH, used for `identify` and cropping.

## Facts established about the deployment

- Repo is `gcol33/gcol33.github.io`, **public**, description "Source for
  gillescolling.com". It is a GitHub user site, deployed by
  `.github/workflows/jekyll.yml` as a Pages artifact.
- Because it is a user site, the pkgdown project repos are served under the same
  domain. Verified 200 on the live site: `/corrselect/`, `/hexify/`,
  `/ggguides/`, `/couplr/`, `/taxify/`, `/vectra/`, `/thinking-in-r/`,
  `/resolve`, `/blog`.
- Case variants do **not** resolve: `/CorrSelect/`, `/Hexify/`, `/GGguides/`,
  `/Taxify/` all 404.
- The seven packages named in the `404.html` redirect table (BiHeat,
  texanshootR, INLAocc, tulpaMesh, restrictR, SIMP, areaOfEffect) all 404. That
  table currently covers nothing that exists.
- The SubmitJSON key is injected from a repo secret at build time, so it is not
  committed. It is still readable in the deployed page, which is inherent to a
  client-side form.

## What is solid, and should not be "fixed"

Recorded so a later session does not spend time re-deriving or breaking these.

- Collection architecture: six collections with per-type `defaults` in
  `_config.yml`. Adding a publication or workshop needs front matter only.
- Dark mode: 137 `[data-bs-theme="dark"]` rules in `custom.css`, plus the
  pre-paint script at `_includes/head.html:4` so there is no flash of the wrong
  theme.
- Accessibility basics: skip link, exactly one `<h1>` per page (verified on 5
  pages), `aria-label` on every icon button, `<nav aria-label="Breadcrumb">`,
  `role="dialog"` on the search modal.
- `related-content.html` does genuine two-pass tag-overlap scoring, first for
  items sharing at least 2 tags, then at least 1. All 35 content items carry
  tags, so it has real data.
- 70 of 77 declared thumbnails are exactly 2400x1600.
- CI does not commit a key.

## Checked and found NOT broken

These looked like defects and are not. Do not re-open them.

- **Mobile layout is fine.** At 390, 768 and 1280 px, `scrollWidth` equals
  `clientWidth` on `/`, `/publications/`, `/workshops/bart/`,
  `/course-spattempdyn-lecture5/` and `/contact/`. The hamburger
  (`#nav-toggle`) is visible below xl and hidden at 1280. Hero text wraps
  correctly.
- **KaTeX display math is fine on mobile.** `.katex-display` carries
  `overflow-x: auto` and its `scrollWidth` equals its `clientWidth` at 390px.
  Equations render at full width and legibly.
- The elements that a naive overflow scan reports as escaping the viewport on
  math pages (`semantics`, `mrow`, `msub`, `mtable`) are KaTeX's hidden MathML
  accessibility copy. False positive.
- `site.side-projects` in Liquid resolves correctly despite the hyphen. Both
  that form and `site["side-projects"]` are in use and both work.
- All 35 content items have `category_url` in front matter, so the archive pages
  that omit a `| default:` fallback do not currently emit an empty `href`.
- The case-insensitive redirect logic inside `404.html` is correct in itself.
  Its package list is what is stale.
- `assets/js/scenarioController.js` is vanilla JS with no jQuery dependency and
  is genuinely used by `_courses/spattempdyn-project.md`. Keep it.

## Findings

Six live bugs, eight content and design gaps, four dead-code items, two
performance items, two infrastructure items. All of them, with file and line
references, evidence and the fix, are in `todo.md`.

The two that cost the most for the least effort:

1. Two 404s fire on every single page load (`scrollFX.js` and
   `pageload-spinner.gif`, both referenced and both absent).
2. The RSS feed is 100% course chapters, all stamped with the build time, so
   every rebuild re-publishes 20 "new" items to subscribers.

The one that silently corrupts content is `_plugins/katex_protect.rb`: its
`gsub` uses a String replacement, so Ruby interprets escapes in the replacement
text. Proven with a standalone Ruby repro this session:

| source math | current output | with block-form gsub |
|---|---|---|
| `A \\ B` | `A \ B` | `A \\ B` |
| `x \& y` | `x KATEXDISPLAY0XETAKEND y` | `x \& y` |

`_courses/spattempdyn-lecture5.md:70` and `_courses/spattempdyn-lecture6.md:48`
already contain four backslashes per matrix row break. That is content written
around the bug, so fixing the plugin means normalizing those two files in the
same commit.

## Asset weight

- ~90 MB in `assets/` is referenced by nothing. The single largest item is
  `assets/images/content/conference_neobiota2024_dance.gif` at 56.4 MB;
  `_presentations/neobiota2024.md:224` serves an mp4 and a separate 110 KB webp
  for that content, so the GIF is history. The `liams_workshop_*.pdf` set adds
  24.9 MB.
- The git pack is 207 MB, largely because of these. Deleting from HEAD shrinks
  the working tree and the Pages artifact immediately. Shrinking `.git` needs a
  history rewrite, which is a separate decision and has not been taken.
- `assets/fonts/` is 3.8 MB, of which 2.5 MB is `.eot` and `.svg` webfont
  formats that no current browser requests.

## Working tree

On `main`. Clean after the handoff commit, which carries this file plus three
lines added to `exclude` in `_config.yml` (`current.md`, `todo.md`,
`dev_notes`), so working notes are not served from the public site.

That commit sits on top of `99878e7` ("auto: 2026-08-09 00:00") and is **not
pushed**. `origin/main` is still at `99878e7`. Pushing triggers the Pages
deploy, and this repo is public, so the decision to publish these notes was left
open deliberately.

No site code was touched. Nothing in `_layouts`, `_includes`, `_pages`,
`_plugins`, `assets` or any collection has changed, so the deployed site is
byte-identical to what `99878e7` produced apart from the two files above being
excluded from the build.

`todo.md` does not appear in `git status` and is not in the commit. The global
ignore at `~/.config/git/ignore:58-63` lists `todo.md` and `TODO.md`, matching
the pattern used across the other projects, where `current.md` is tracked and
`todo.md` is not. It exists on disk next to this file. Use `git add -f todo.md`
if it should ever be tracked.

`Gemfile.lock` exists locally and is gitignored (`.gitignore:11`), so CI resolves
gems fresh on every deploy. See P3 in `todo.md`.

Ignored-but-present at root: `_site/`, `.jekyll-cache/`, `.jekyll-serve.log`,
`.playwright-mcp/`, `.code-review-graph/`, `dev_notes/`.

`current.md` and `todo.md` are excluded from the Jekyll build in `_config.yml`
alongside `CLAUDE.md`, so they are not served from the public site. Keep them
there if either file is renamed.
