from PIL import Image, ImageEnhance
import os

# Source images
base_path = r'c:\Users\Gilles Colling\Documents\website\assets\images\content'
images = [
    'presentation_vdsee_2024_personal.jpg',
    'presentation_vdsee_2024_personal.webp'
]

for img_name in images:
    img_path = os.path.join(base_path, img_name)
    if os.path.exists(img_path):
        img = Image.open(img_path)
        # Darken by 45% (brightness factor of 0.55)
        enhancer = ImageEnhance.Brightness(img)
        darkened = enhancer.enhance(0.55)

        # Create dark version filename
        name, ext = os.path.splitext(img_name)
        dark_name = f'{name}-dark{ext}'
        dark_path = os.path.join(base_path, dark_name)

        # Convert RGBA to RGB for JPEG
        if darkened.mode == 'RGBA' and ext.lower() in ['.jpg', '.jpeg']:
            darkened = darkened.convert('RGB')

        darkened.save(dark_path, quality=90)
        print(f'Created: {dark_name}')
    else:
        print(f'Not found: {img_name}')
