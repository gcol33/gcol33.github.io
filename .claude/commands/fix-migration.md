# Auto-Fix Jekyll Migration

Compare each Jekyll page against its original HTML source and fix all discrepancies. Spawn parallel agents for different page categories.

## Instructions

1. First, enumerate all original HTML pages by running:
   ```
   find . -name "index.html" -path "*/workshop-*" -o -name "index.html" -path "*/course-*" -o -name "index.html" -path "*/proj*" -o -name "index.html" -path "*/presentations/*" | head -20
   ```

2. Spawn 4 parallel agents using the Task tool with subagent_type='general-purpose':

### Agent 1: Workshops
```
Compare and fix all workshop pages. For each workshop:
1. Read the original HTML file (e.g., workshop-plot-data/index.html)
2. Read the Jekyll markdown file (e.g., _workshops/plot-data.md)
3. Compare structure, classes, content
4. Fix the markdown file or layout to match

Key things to check:
- hero_bg_class matches the original CSS class (e.g., bg-workshop-pd-bg)
- hero_content contains the "Take aways" text from original
- Tables have class="base-table collapsible-table"
- Images use <picture> tags with webp sources
- All content sections are present

Files: _workshops/*.md, _layouts/workshop.html
```

### Agent 2: Presentations
```
Compare and fix all presentation pages. Same process as workshops.
Files: _presentations/*.md
```

### Agent 3: Courses
```
Compare and fix course pages. These use course-overview.html and chapter.html layouts.
Check: course-spattempdyn/, course-foundevotheo/
Files: _courses/*.md, _layouts/course-overview.html, _layouts/chapter.html
```

### Agent 4: Projects
```
Compare and fix project pages (projasaas, projagriweed).
Files: _projects/*.md
```

3. After agents complete, verify by checking the Jekyll server output and manually reviewing key pages.

## Verification Commands

```bash
# Check Jekyll build for errors
bundle exec jekyll build 2>&1 | grep -i error

# List generated pages
ls -la _site/workshop-*/ _site/presentations/*/ _site/course-*/ _site/proj*/
```

## Report Format

Each agent should report:
- Pages checked
- Issues found
- Fixes applied
- Remaining issues (if any)
