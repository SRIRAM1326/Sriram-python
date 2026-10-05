# Duplicate Finder

## Description
A utility that scans a specified directory to find duplicate files based on their cryptographic hashes.

## Features
- Ask the user for a folder path
- Scan files inside the folder recursively
- Compare files using MD5 file hashes
- Identify duplicate files
- Display duplicate groups with file paths
- Do NOT delete files automatically
- Handle invalid folder paths
- Ignore directories
- Exit safely

## Technologies
- Python 3
- Python Standard Library (`hashlib`, `pathlib`, `os` modules)

## How to Run
```bash
python main.py
```

## Example
```text
=== Duplicate Finder ===

Folder: C:/Users/User/Downloads

Duplicate Files Found:

Group 1:
C:\Users\User\Downloads\photo1.jpg
C:\Users\User\Downloads\photo_copy.jpg

Total duplicate groups: 1
```

## What I Learned
- Reading files in binary chunks (`rb`) to avoid memory overflow on large files.
- Utilizing `hashlib.md5()` to create unique file fingerprints.
- Using `pathlib.Path.rglob()` for recursive directory traversal.
