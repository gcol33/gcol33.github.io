"""Check HTML structure of workshop pages for code block classes."""
from pathlib import Path
from bs4 import BeautifulSoup

docs_dir = Path(r"C:\Users\Gilles Colling\Documents\liams stay\docs")

for fname in ["day1_exercises.html", "day2_exercises.html", "day3_results.html"]:
    print(f"\n=== {fname} ===")
    with open(docs_dir / fname, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    for tag in ["pre", "code"]:
        elements = soup.find_all(tag)
        classes = set()
        for el in elements:
            if el.get("class"):
                classes.update(el["class"])
        print(f"  {tag}: {len(elements)} elements, classes: {classes}")
    for pre in soup.find_all("pre")[:3]:
        parent = pre.parent
        print(f"  pre parent: <{parent.name}> class={parent.get('class')}")
        print(f"    pre class={pre.get('class')}")
        code = pre.find("code")
        if code:
            print(f"    code class={code.get('class')}")
            print(f"    first 80 chars: {code.text[:80]}")
