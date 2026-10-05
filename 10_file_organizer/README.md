# File Organizer

## Description
A file organization utility that automatically sorts files in a selected directory into subfolders based on their extensions.

## Features
- Ask the user for a directory path
- Detect file extensions
- Create folders automatically (Images, Documents, Videos, Audio, Python, Others, etc.)
- Move files into appropriate folders
- Handle unknown extensions by placing them in an "Others" folder
- Do not move directories
- Avoid overwriting existing files
- Display a summary after completion
- Handle invalid paths gracefully

## Technologies
- Python 3
- `pathlib` module
- `shutil` module
- `os` module

## How to Run
```bash
python main.py
```

## Example Usage
```text
=== File Organizer ===
Enter the directory path to organize: ./Downloads/

Organizing files in: /path/to/Downloads

Moved photo.jpg -> Images/
Moved resume.pdf -> Documents/
Moved script.py -> Python/

Summary: Successfully moved 3 file(s).
```

## What I Learned
- Using the `pathlib` module for modern path manipulations.
- Using `shutil.move` to move files across directories.
- Grouping files by extension using a dictionary mapping.
