from pypdf import PdfReader
import os

path = r"C:\Users\Gilles Colling\Documents\website\assets\downloads\liams_workshop.pdf"
r = PdfReader(path)
size_kb = os.path.getsize(path) / 1024
print(f"Total pages: {len(r.pages)}")
print(f"File size: {size_kb:.0f} KB")
text = r.pages[0].extract_text()[:400]
print(f"\nFirst page preview:\n{text}")
