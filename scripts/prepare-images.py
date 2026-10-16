"""Generate responsive WebP thumbnails and their Jekyll lookup table."""
import json
from pathlib import Path

import yaml
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/images/responsive"
OUTPUT.mkdir(parents=True, exist_ok=True)
sources = set()
for folder in ROOT.glob("_*"):
    if folder.is_dir() and folder.name != "_site":
        for page in folder.glob("*.md"):
            parts = page.read_text(encoding="utf-8").split("---", 2)
            if len(parts) == 3 and not parts[0].strip():
                metadata = yaml.safe_load(parts[1]) or {}
                source = metadata.get("thumbnail_webp") or metadata.get("thumbnail")
                if source and source.startswith("/assets/"):
                    sources.add(source)

manifest = {}
for source in sorted(sources):
    path = ROOT / source.lstrip("/")
    with Image.open(path) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        variants = []
        for width in (400, 800, 1200):
            if width > image.width:
                continue
            target = OUTPUT / f"{path.stem}-{width}.webp"
            image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS).save(target, quality=80, method=6)
            variants.append({"url": "/" + target.relative_to(ROOT).as_posix(), "width": width})
        if variants:
            manifest[source] = variants

for theme in ("background-hero", "background-hero-dark"):
    with Image.open(ROOT / f"assets/images/content/{theme}.webp") as image:
        for width in (800, 1600):
            image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS).save(OUTPUT / f"{theme}-{width}.webp", quality=78, method=6)

(ROOT / "_data/responsive_images.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(f"Prepared responsive thumbnails for {len(manifest)} images.")
