# Duplicate Image Finder

## Description
A high-performance filesystem analyzer that detects bit-for-bit identical duplicate images using a two-stage pipeline: fast file-size grouping followed by streaming SHA-256 cryptographic checksums.

## Features
- Two-stage comparison pipeline minimizing disk I/O on large image libraries.
- Chunked 64KB cryptographic hashing via `hashlib.sha256` preventing memory spikes.
- Supports JPEG, PNG, WEBP, GIF, BMP, SVG, and TIFF image formats.
- Visual cluster report showing original file, redundant copies, and reclaimable disk storage.
- Optional automated cleanup deleting duplicate copies while preserving 1 original copy.

## Technologies
- Python 3 (`hashlib`, `pathlib`, `collections`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Duplicate Image Finder ===
1. Scan Directory for Duplicate Images
2. Exit

Choose an option (1-2): 1

Enter directory path to scan: C:\Users\User\Pictures
Include subdirectories recursively? (y/n, default: y): y

Scanning 142 image file(s) for duplicates...

======================================================================
                     DUPLICATE IMAGES DETECTED
======================================================================

[Group 1] SHA-256: 4a2b8e91... (2.45 MB each)
  Keep (Original): C:\Users\User\Pictures\banner.png
  Duplicate:       C:\Users\User\Pictures\backup\banner_copy.png

======================================================================
Summary: 1 duplicate file(s) found across 1 group(s).
Potential Space Reclaimable: 2.45 MB
======================================================================
```

## What I Learned
- Optimizing directory search performance by grouping by byte size before computing hashes.
- Chunked cryptographic hashing of binary file streams.
- Implementing safe batch deletion routines with path validations.
