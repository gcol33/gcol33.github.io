# Responsive images

Run `python scripts/prepare-images.py` after adding or changing collection thumbnails. The script requires Pillow and PyYAML. It reads thumbnail paths from page front matter, generates 400-, 800-, and 1200-pixel WebP variants without upscaling, and writes `_data/responsive_images.json` for the shared image include.

Commit the generated images and manifest together. Original images remain available for full-size views. The shared include accepts `sizes`, `loading`, and `priority` for each placement.
