"""Render shortened workshop PDFs (no R code / exercise pages)."""

import io
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl_canvas

docs_dir = Path(r"C:\Users\Gilles Colling\Documents\liams stay\docs")
output_dir = Path(r"C:\Users\Gilles Colling\Documents\website\assets\downloads")


def make_page_number_overlay(page_num):
    """Create a single-page PDF with a centered page number."""
    packet = io.BytesIO()
    w, h = A4
    c = rl_canvas.Canvas(packet, pagesize=A4)
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0.53, 0.53, 0.53)
    c.drawCentredString(w / 2, 8, str(page_num))
    c.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]


# Sections: theory + results + summary only (no exercises)
sections = {
    "en": [
        {"day": "Day 1", "part": "Theory", "subtitle": "Biodiversity & Species Accumulation Curves", "file": "day1_theory.html"},
        {"day": "Day 2", "part": "Theory", "subtitle": "Algorithms & Spatial Ordering", "file": "day2_theory.html"},
        {"day": "After the Workshop", "part": "Results", "subtitle": "Analysis Outputs", "file": "day3_results.html"},
        {"day": "After the Workshop", "part": "Summary", "subtitle": "Workshop Review", "file": "day3_summary.html"},
    ],
    "de": [
        {"day": "Tag 1", "part": "Theorie", "subtitle": "Biodiversität & Artenakkumulationskurven", "file": "day1_theory.html"},
        {"day": "Tag 2", "part": "Theorie", "subtitle": "Algorithmen & räumliche Ordnung", "file": "day2_theory.html"},
        {"day": "Nach dem Workshop", "part": "Ergebnisse", "subtitle": "Analyse-Ergebnisse", "file": "day3_results.html"},
        {"day": "Nach dem Workshop", "part": "Zusammenfassung", "subtitle": "Workshop-Rückblick", "file": "day3_summary.html"},
    ],
}

cover_info = {
    "en": {
        "title": "Species Accumulation Curves",
        "tagline": "",
        "type": "Ecology Workshop",
        "date": "January 26\u201327, 2026",
        "institution": "Division of BioInvasions, Global Change &amp; Macroecology",
        "university": "University of Vienna",
        "author": "Gilles Colling",
        "toc_label": "Contents",
    },
    "de": {
        "title": "Artenakkumulationskurven",
        "tagline": "",
        "type": "\u00d6kologie-Workshop",
        "date": "26.\u201327. J\u00e4nner 2026",
        "institution": "Division of BioInvasions, Global Change &amp; Macroecology",
        "university": "Universit\u00e4t Wien",
        "author": "Gilles Colling",
        "toc_label": "Inhalt",
    },
}


def make_cover_html(lang):
    ci = cover_info[lang]
    return f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<style>
@page {{ margin: 0; size: A4; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width: 210mm; height: 297mm;
    background: #fff; color: #212121;
    display: flex; flex-direction: column;
}}
.cover {{
    flex: 1;
    display: flex; flex-direction: column; justify-content: center;
    padding: 50mm 30mm 30mm 30mm;
}}
.accent-bar {{ width: 60px; height: 4px; background: #2E7D32; margin-bottom: 20mm; }}
.workshop-type {{
    font-size: 13pt; color: #2E7D32; text-transform: uppercase;
    letter-spacing: 3px; font-weight: 600; margin-bottom: 8mm;
}}
h1 {{ font-size: 32pt; font-weight: 700; line-height: 1.15; color: #212121; margin-bottom: 6mm; }}
.tagline {{ font-size: 14pt; color: #5e5e5e; font-style: italic; margin-bottom: 15mm; line-height: 1.4; }}
.meta {{ font-size: 10.5pt; color: #5e5e5e; line-height: 1.8; }}
.meta strong {{ color: #212121; }}
.footer-bar {{ height: 8mm; background: linear-gradient(135deg, #2E7D32, #4CAF50); }}
</style></head>
<body>
    <div class="cover">
        <div class="accent-bar"></div>
        <div class="workshop-type">{ci["type"]}</div>
        <h1>{ci["title"]}</h1>
        <div class="tagline">{ci["tagline"]}</div>
        <div class="meta">
            <strong>{ci["author"]}</strong><br>
            {ci["institution"]}<br>
            {ci["university"]}<br><br>
            {ci["date"]}
        </div>
    </div>
    <div class="footer-bar"></div>
</body></html>'''


def make_toc_html(lang, secs, page_numbers):
    ci = cover_info[lang]
    toc_items = ""
    for i, sec in enumerate(secs):
        pg = page_numbers[i]
        title = f'{sec["day"]}  {sec["part"]}'
        toc_items += f'''
        <a href="#section-{i}" class="toc-item">
            <span class="toc-number">{i + 1}</span>
            <div class="toc-text">
                <span class="toc-title">{title}</span>
                <span class="toc-sub">{sec["subtitle"]}</span>
            </div>
            <span class="toc-dots"></span>
            <span class="toc-page">{pg}</span>
        </a>'''

    return f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<style>
@page {{ margin: 0; size: A4; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width: 210mm; height: 297mm;
    background: #fff; color: #212121;
    display: flex; flex-direction: column;
}}
.toc-page-container {{
    flex: 1;
    padding: 30mm 30mm 25mm 30mm;
    display: flex; flex-direction: column;
}}
.toc-header {{
    font-size: 11pt; color: #2E7D32; text-transform: uppercase;
    letter-spacing: 2px; font-weight: 600;
    margin-bottom: 10mm; padding-bottom: 3mm;
    border-bottom: 2px solid #2E7D32;
}}
.toc-item {{
    display: flex; align-items: baseline; gap: 4mm;
    padding: 4.5mm 0;
    border-bottom: 1px solid #f0f0f0;
    text-decoration: none; color: inherit;
    transition: background 0.15s;
}}
.toc-item:hover {{ background: #f8f9fa; }}
.toc-number {{
    font-size: 20pt; font-weight: 300; color: #2E7D32;
    min-width: 14mm; text-align: right;
}}
.toc-text {{ flex-shrink: 0; }}
.toc-title {{
    font-size: 11.5pt; font-weight: 600; color: #212121; display: block;
}}
.toc-sub {{
    font-size: 9.5pt; color: #888; display: block; margin-top: 1mm;
}}
.toc-dots {{
    flex: 1; min-width: 10mm;
    border-bottom: 1.5px dotted #ccc;
    margin: 0 2mm;
    align-self: end;
    margin-bottom: 3px;
}}
.toc-page {{
    font-size: 11pt; font-weight: 600; color: #2E7D32;
    min-width: 10mm; text-align: right;
}}
.footer-bar {{ height: 8mm; background: linear-gradient(135deg, #2E7D32, #4CAF50); }}
</style></head>
<body>
    <div class="toc-page-container">
        <div class="toc-header">{ci["toc_label"]}</div>
        {toc_items}
    </div>
    <div class="footer-bar"></div>
</body></html>'''


def make_divider_html(section):
    return f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<style>
@page {{ margin: 0; size: A4; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width: 210mm; height: 297mm; background: #f8f9fa;
    display: flex; align-items: center; justify-content: center;
}}
.divider {{ text-align: center; padding: 30mm; }}
.bar {{ width: 40px; height: 3px; background: #2E7D32; margin: 0 auto 12mm auto; }}
h1 {{ font-size: 28pt; font-weight: 700; color: #212121; margin-bottom: 3mm; }}
.part {{ font-size: 18pt; font-weight: 600; color: #2E7D32; margin-bottom: 5mm; }}
.sub {{ font-size: 13pt; color: #5e5e5e; }}
</style></head>
<body>
    <div class="divider">
        <div class="bar"></div>
        <h1>{section["day"]}</h1>
        <p class="part">{section["part"]}</p>
        <p class="sub">{section["subtitle"]}</p>
    </div>
</body></html>'''


def render_html_to_pdf(browser, html_content, out_path, margins="0mm"):
    page = browser.new_page()
    page.set_content(html_content)
    page.wait_for_timeout(300)
    m = {"top": margins, "bottom": margins, "left": margins, "right": margins}
    page.pdf(path=str(out_path), format="A4", margin=m, print_background=True)
    page.close()


def render_file_to_pdf(browser, html_path, out_path, hide_cls, show_cls, lang_suffix):
    page = browser.new_page()
    page.goto(html_path.as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate(f"""() => {{
        document.querySelectorAll('.{hide_cls}').forEach(el => el.style.display = 'none');
        document.querySelectorAll('.{show_cls}').forEach(el => el.style.display = 'inline');
        document.querySelectorAll('.lang-toggle').forEach(el => el.style.display = 'none');
        if ('{lang_suffix}' === 'de') {{
            document.body.classList.add('lang-de');
        }} else {{
            document.body.classList.remove('lang-de');
        }}
        // Hide R code blocks and fix styling
        const style = document.createElement('style');
        style.textContent = `
            pre.r {{ display: none !important; }}
            p code, li code, h1 code, h2 code, h3 code {{ font-size: inherit; }}
            img {{ max-width: 100%; height: auto; }}
            .figure, .float-figure {{ max-width: 100%; overflow: hidden; }}
            #session-infosession-info, #session-info {{ display: none !important; }}
        `;
        document.head.appendChild(style);
    }}""")
    page.wait_for_timeout(500)
    page.pdf(
        path=str(out_path), format="A4",
        margin={"top": "15mm", "bottom": "18mm", "left": "15mm", "right": "15mm"},
        print_background=True,
    )
    page.close()


languages = [
    ("en", "de", "en", "English"),
    ("de", "en", "de", "German"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for lang_suffix, hide_cls, show_cls, lang_label in languages:
        print(f"\n=== {lang_label} (short) ===")
        secs = sections[lang_suffix]
        temp_files = []

        print("  Rendering cover...")
        cover_tmp = docs_dir / f"_temp_{lang_suffix}_s_cover.pdf"
        render_html_to_pdf(browser, make_cover_html(lang_suffix), cover_tmp)
        temp_files.append(cover_tmp)

        section_pdfs = []
        current_page = 3
        section_start_pages = []

        for sec in secs:
            html_path = docs_dir / sec["file"]
            if not html_path.exists():
                print(f"  Skipping {sec['file']} (not found)")
                continue

            print(f"  Rendering divider: {sec['day']} {sec['part']}...")
            div_tmp = docs_dir / f"_temp_{lang_suffix}_s_div_{sec['file'].replace('.html', '.pdf')}"
            render_html_to_pdf(browser, make_divider_html(sec), div_tmp)

            print(f"  Rendering {sec['file']}...")
            content_tmp = docs_dir / f"_temp_{lang_suffix}_s_{sec['file'].replace('.html', '.pdf')}"
            render_file_to_pdf(browser, html_path, content_tmp, hide_cls, show_cls, lang_suffix)

            section_start_pages.append(current_page)

            div_pages = len(PdfReader(str(div_tmp)).pages)
            content_pages = len(PdfReader(str(content_tmp)).pages)
            current_page += div_pages + content_pages

            section_pdfs.append((div_tmp, content_tmp))
            temp_files.extend([div_tmp, content_tmp])

        print(f"  Rendering TOC (pages: {section_start_pages})...")
        toc_tmp = docs_dir / f"_temp_{lang_suffix}_s_toc.pdf"
        render_html_to_pdf(browser, make_toc_html(lang_suffix, secs, section_start_pages), toc_tmp)
        temp_files.append(toc_tmp)

        print(f"  Merging...")
        writer = PdfWriter()
        writer.append(str(cover_tmp))
        writer.append(str(toc_tmp))
        for div_path, content_path in section_pdfs:
            writer.append(str(div_path))
            writer.append(str(content_path))

        print("  Adding page numbers...")
        for i in range(2, len(writer.pages)):
            writer.pages[i].merge_page(make_page_number_overlay(i + 1))

        # Bookmarks
        day_groups = {}
        page_idx = 2
        for sec, (div_path, content_path) in zip(secs, section_pdfs):
            day_label = sec["day"]
            if day_label not in day_groups:
                day_groups[day_label] = []
            day_groups[day_label].append((sec["part"], page_idx))
            page_idx += len(PdfReader(str(div_path)).pages) + len(PdfReader(str(content_path)).pages)

        for day_label, children in day_groups.items():
            parent = writer.add_outline_item(day_label, children[0][1])
            for sub_label, pg_idx in children:
                writer.add_outline_item(sub_label, pg_idx, parent=parent)

        output_path = output_dir / f"liams_workshop_{lang_suffix}_short.pdf"
        with open(output_path, "wb") as f:
            writer.write(f)

        for tmp in temp_files:
            tmp.unlink()

        print(f"  Done! -> {output_path}")

    browser.close()
