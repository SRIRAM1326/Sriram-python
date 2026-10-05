# Text File Editor

## Description
A simple terminal-based text file editor to create, read, append, and overwrite local files.

## Features
- Create a text file
- Write content to the file
- Read/display file contents
- Append content
- Clear/overwrite file contents
- Show file information
- Handle missing files
- Exit option

## Technologies
- Python 3
- Python Standard Library (`os` module)

## How to Run
```bash
python main.py
```

## Example
```text
=== Text File Editor ===

1. Create File
2. Read File
3. Append Text
4. Overwrite File
5. File Information
6. Exit

Choose: 2
Enter filename to read: demo.txt

--- File Content ---
Hello World!
--------------------
```

## What I Learned
- Working with file handling modes (`r`, `w`, `a`).
- Managing contexts with `with open() as`.
- Using `os.path.exists()` and `os.path.getsize()`.
