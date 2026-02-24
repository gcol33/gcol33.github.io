"""Create a professional PDF of Liam's workshop for teaching material."""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

output_path = Path(r"C:\Users\Gilles Colling\Documents\website\assets\downloads\liams_workshop.pdf")

# Colors matching the website
DARK = HexColor("#212121")
MEDIUM = HexColor("#5e5e5e")
ACCENT = HexColor("#8B7355")
LIGHT_LINE = HexColor("#CCCCCC")

# Styles
style_title = ParagraphStyle(
    "Title",
    fontName="Helvetica-Bold",
    fontSize=22,
    leading=28,
    textColor=DARK,
    alignment=TA_LEFT,
    spaceAfter=4 * mm,
)

style_subtitle = ParagraphStyle(
    "Subtitle",
    fontName="Helvetica",
    fontSize=13,
    leading=17,
    textColor=ACCENT,
    alignment=TA_LEFT,
    spaceAfter=2 * mm,
)

style_meta = ParagraphStyle(
    "Meta",
    fontName="Helvetica",
    fontSize=10,
    leading=14,
    textColor=MEDIUM,
    alignment=TA_LEFT,
    spaceAfter=6 * mm,
)

style_description = ParagraphStyle(
    "Description",
    fontName="Helvetica-Oblique",
    fontSize=10.5,
    leading=16,
    textColor=MEDIUM,
    alignment=TA_LEFT,
    spaceAfter=8 * mm,
    leftIndent=0,
    rightIndent=0,
)

style_heading = ParagraphStyle(
    "Heading",
    fontName="Helvetica-Bold",
    fontSize=14,
    leading=20,
    textColor=DARK,
    spaceBefore=8 * mm,
    spaceAfter=4 * mm,
)

style_body = ParagraphStyle(
    "Body",
    fontName="Helvetica",
    fontSize=10.5,
    leading=16,
    textColor=DARK,
    alignment=TA_LEFT,
    spaceAfter=5 * mm,
)

style_link = ParagraphStyle(
    "Link",
    fontName="Helvetica",
    fontSize=10.5,
    leading=16,
    textColor=DARK,
    alignment=TA_LEFT,
    spaceAfter=5 * mm,
)

style_footer = ParagraphStyle(
    "Footer",
    fontName="Helvetica",
    fontSize=8,
    leading=11,
    textColor=MEDIUM,
    alignment=TA_CENTER,
)

# Build the document
doc = SimpleDocTemplate(
    str(output_path),
    pagesize=A4,
    topMargin=2.5 * cm,
    bottomMargin=2.5 * cm,
    leftMargin=2.5 * cm,
    rightMargin=2.5 * cm,
    title="Species Accumulation Curves",
    author="Gilles Colling",
    subject="Teaching Material",
)

story = []

# Title block
story.append(Paragraph("Species Accumulation Curves", style_title))
story.append(Paragraph("January 26–27, 2026 · Division of BioInvasions, Global Change &amp; Macroecology · University of Vienna", style_meta))

# Divider
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_LINE, spaceAfter=4 * mm))

# Description
story.append(Paragraph(
    "A two-day ecology workshop designed for a visiting school student, introducing "
    "biodiversity sampling, species accumulation curves, and spatial algorithms through "
    "hands-on R programming exercises.",
    style_description,
))

# Day 1
story.append(Paragraph("Day 1: Concepts and First Steps in R", style_heading))
story.append(Paragraph(
    "The first day focused on foundational concepts. We started with what biodiversity means "
    "and why it is difficult to measure directly. From there, we moved into sampling theory: "
    "how ecologists collect data in the field, why complete censuses are rarely possible, and "
    "how accumulation curves allow us to estimate total species richness from incomplete "
    "samples. The concept of asymptotes was introduced as the theoretical limit a curve "
    "approaches, representing the total number of species in an area.",
    style_body,
))
story.append(Paragraph(
    "In the practical session, Liam worked through eight exercises that progressed from "
    "basic R syntax to his first real data analysis. Starting with simple operations and data "
    "structures, the exercises gradually built up to loading ecological datasets, computing "
    "species counts, and plotting his first accumulation curve. By the end of the day, he had "
    "written working R code that visualized how species richness increases with sampling effort.",
    style_body,
))

# Day 2
story.append(Paragraph("Day 2: Algorithms and a Research Project", style_heading))
story.append(Paragraph(
    "The second day shifted to more advanced topics. The theory session covered spatial "
    "ordering of samples, nearest-neighbor algorithms, and the concept of multiple seeds for "
    "generating different accumulation curve trajectories from the same dataset. These ideas "
    "are directly relevant to my own R package work and gave Liam a glimpse into how "
    "algorithmic choices affect ecological conclusions.",
    style_body,
))
story.append(Paragraph(
    "The practical session consisted of seven exercises structured as a mini research project. "
    "Liam explored uncertainty in accumulation curves by running multiple randomizations, "
    "learned how to produce publication-quality figures, and drew his own conclusions from the "
    "data. The exercises culminated in a final analysis where he had to interpret results and "
    "communicate findings, mirroring the workflow of an actual research project.",
    style_body,
))

# Workshop Materials
story.append(Paragraph("Workshop Materials", style_heading))
story.append(Paragraph(
    'The full workshop materials, including theory slides and interactive exercises for both '
    'days, are available as a standalone bilingual web application at '
    '<link href="https://gillescolling.com/liams_stay/" color="#8B7355">'
    'gillescolling.com/liams_stay</link>.',
    style_link,
))

# Footer spacer + line
story.append(Spacer(1, 15 * mm))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_LINE, spaceAfter=3 * mm))
story.append(Paragraph(
    "Gilles Colling · gillescolling.com · University of Vienna",
    style_footer,
))

doc.build(story)
print(f"PDF created: {output_path}")
