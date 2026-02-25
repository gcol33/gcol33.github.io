# Jekyll Migration Verification & Fix

You are tasked with ensuring the Jekyll site matches the original Blocs-generated HTML site exactly. Work systematically through each page, compare against the original, and fix discrepancies until achieving a 1:1 visual match.

## Strategy

1. **Discovery Phase**: Identify all pages that need verification
2. **Comparison Phase**: For each page, compare Jekyll output vs original HTML
3. **Fix Phase**: Make necessary changes to layouts, includes, CSS, or content
4. **Verification Phase**: Confirm the fix works

## Page Mapping

Original HTML pages are in folders like:
- `workshop-plot-data/index.html` → Jekyll: `_workshops/plot-data.md`
- `workshop-writing/index.html` → Jekyll: `_workshops/writing.md`
- `presentations/vdsee2025/index.html` → Jekyll: `_presentations/vdsee2025.md`
- `projasaas/index.html` → Jekyll: `_projects/asaas.md`
- `projagriweed/index.html` → Jekyll: `_projects/agriweed.md`
- `course-spattempdyn/index.html` → Jekyll: `_courses/spattempdyn.md`
- `course-foundevotheo/index.html` → Jekyll: `_courses/foundevotheo.md`

## Checklist for Each Page

For each page, verify:
- [ ] Hero/banner section matches (background image, text overlay, positioning)
- [ ] Typography matches (fonts, sizes, colors, spacing)
- [ ] Tables render correctly (responsive, collapsible, styling)
- [ ] Images display properly (lazy loading, responsive, rounded corners)
- [ ] Links work correctly
- [ ] Navigation breadcrumbs match
- [ ] Footer matches
- [ ] Mobile responsiveness matches

## Key Files to Modify

- `_layouts/workshop.html` - Workshop/presentation page template
- `_layouts/course-overview.html` - Course landing pages
- `_layouts/chapter.html` - Course chapter pages
- `_includes/head.html` - CSS includes
- `_includes/scripts.html` - JS includes
- `_includes/navbar.html` - Navigation
- `_includes/footer.html` - Footer
- `assets/css/style.css` - Main styles (read-only, use for reference)
- `assets/css/tables.css` - Table styles

## Common Issues to Check

1. **Background images**: Use CSS classes (`hero_bg_class: "bg-workshop-pd-bg"`) not inline styles
2. **Texture overlay**: Add `bg-texture texture-darken section-dark` classes
3. **Tables**: Need `class="base-table collapsible-table"` and tables.js
4. **Images**: Use `<picture>` with webp source, add `lazyload` class
5. **Spacing**: Match `pad-lg`, `pad-md`, `pad-sm` padding classes
6. **Grid layouts**: Match Bootstrap column classes exactly

## Execution

Spawn parallel agents for efficiency:
1. One agent per page category (workshops, presentations, courses, projects)
2. Each agent reads original HTML, compares to Jekyll output, and fixes discrepancies
3. Report back with changes made and any remaining issues

## Success Criteria

The Jekyll page should be visually indistinguishable from the original HTML page when viewed in a browser at the same viewport size.

Start by listing all pages that exist in the original site but may not be fully migrated to Jekyll, then systematically work through them.
