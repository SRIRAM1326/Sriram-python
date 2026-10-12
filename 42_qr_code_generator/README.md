# QR Code Generator

## Description
A CLI application that encodes any text string or website URL into a scannable QR Code. It outputs both a live ASCII terminal representation for immediate phone camera scanning and exports a high-resolution `.png` file.

## Features
- Generates QR codes from arbitrary text strings or website URLs.
- Displays full terminal ASCII QR blocks directly in the console for instant scanning.
- Saves clean `.png` raster files to local disk.
- Custom output filename configuration.

## Technologies
- Python 3
- `qrcode` library

## How to Run
```bash
python main.py
```

## Example
```text
=== QR Code Generator ===
1. Generate QR Code (Terminal + PNG)
2. Exit

Choose an option (1-2): 1

Enter the text or URL to encode: https://github.com
Enter output PNG filename (default: qrcode.png): my_qr.png

✓ QR Code saved successfully as: my_qr.png
```

## What I Learned
- Utilizing the `qrcode` library to generate standard matrices.
- Rendering 2D boolean matrices into console Unicode character blocks (`██` and `  `).
- Exporting PIL-compatible raster images to disk.
