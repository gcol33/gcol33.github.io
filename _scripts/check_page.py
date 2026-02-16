from playwright.sync_api import sync_playwright
from pathlib import Path

output = Path(r"C:\Users\Gilles Colling\Documents\website\_scripts\check_divtalk.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=1)
    page.goto("http://127.0.0.1:4000/presentations/division-talk-2026/")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=str(output))
    print("Done")
    browser.close()
