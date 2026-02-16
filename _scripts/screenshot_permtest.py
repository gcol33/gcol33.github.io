"""Screenshot the fixed permutation test histogram."""
from pathlib import Path
from playwright.sync_api import sync_playwright

docs_dir = Path(r"C:\Users\Gilles Colling\Documents\liams stay\docs")
out = Path(r"C:\Users\Gilles Colling\Documents\website\_scripts\permtest_fixed.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1200, "height": 900})
    page.goto((docs_dir / "day3_results.html").as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate("""() => {
        document.querySelectorAll('.de').forEach(el => el.style.display = 'none');
        document.querySelectorAll('.en').forEach(el => el.style.display = 'inline');
        document.querySelectorAll('.lang-toggle').forEach(el => el.style.display = 'none');
    }""")
    page.wait_for_timeout(500)
    imgs = page.query_selector_all("img")
    imgs[8].screenshot(path=str(out))
    print("Done")
    browser.close()
