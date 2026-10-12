# Bulk File Renamer

## Description
A resilient command-line file batching tool designed to systematically rename groups of files across directories using prefixes, suffixes, token replacement, case conversion, or zero-padded numeric sequences. Features safe dry-run visual diffs.

## Features
- Add uniform prefixes or suffixes to filenames.
- Substring find-and-replace across filenames.
- Zero-padded sequential numbering format (e.g. `Doc_001.pdf`, `Doc_002.pdf`).
- Case normalization (lowercase or uppercase).
- File extension filtering (`.jpg`, `.png`, `.txt`).
- **Dry-Run Preview**: Visual table displaying `Original -> Proposed` mapping before applying changes.

## Technologies
- Python 3 (`pathlib`, `os`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Bulk File Renamer ===

Enter directory path to organize: ./my_photos
Filter by extension: .jpg

Found 3 file(s). Select renaming strategy:
1. Add Prefix
2. Add Suffix
3. Find and Replace Text
4. Sequential Numbering Sequence
5. Lowercase / Uppercase Normalization
6. Cancel

Choose an option (1-6): 4
Enter base name: Vacation_
Enter number of digits for padding: 2

=================================================================
#    | Current Name                 -> New Name
=================================================================
1    | dsc001.jpg                   -> Vacation_01.jpg
2    | dsc002.jpg                   -> Vacation_02.jpg
3    | dsc003.jpg                   -> Vacation_03.jpg
=================================================================

Proceed with renaming? (y/n): y
✓ Completed! Successfully renamed 3 file(s).
```

## What I Learned
- Utilizing `pathlib.Path` for cross-platform filesystem path mutations.
- Implementing safe multi-phase execution (Preview Plan -> User Confirmation -> Atomicity).
- Formatting zero-padded numeric sequences using `.zfill()`.
