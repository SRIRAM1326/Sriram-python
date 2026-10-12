# Image Resizer

## Description
A CLI graphics processing tool that transforms images to specified pixel dimensions, percentage scales, or standard device/social media presets while maintaining aspect ratio and image clarity.

## Features
- Custom width and height scaling with optional aspect ratio preservation.
- Proportional percentage scaling (e.g. 50% reduction, 200% enlargement).
- Standard dimensional presets (Thumbnail, Avatar, Instagram, HD 720p, Full HD 1080p).
- High-fidelity Lanczos antialiasing interpolation.
- Supports JPEG, PNG, WEBP, BMP, and GIF formats.

## Technologies
- Python 3
- Pillow (`PIL`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Image Resizer ===
1. Resize an Image
2. Exit

Choose an option (1-2): 1

Enter path to image file: sample.png
Image loaded: sample.png
Current dimensions: 1920px wide × 1080px high (Format: PNG)

Select Resizing Mode:
1. Custom Width/Height
2. Scale by Percentage
3. Predefined Standard Presets
Choose mode (1-3): 2
Enter scaling percentage: 50
Enter output file name (default: sample_resized.png): 

✓ Image successfully resized and saved!
New Dimensions: 960px × 540px
Saved Path: C:\path\to\sample_resized.png
```

## What I Learned
- Reading raster formats and metadata utilizing Pillow (`PIL.Image`).
- Implementing coordinate aspect-ratio preservation algorithms ($H = W \times \text{ratio}$).
- Configuring anti-aliased interpolation algorithms (`LANCZOS`).
