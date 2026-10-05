# Text Cleaner

## Description
A text-cleaning utility that provides various options to normalize and clean up messy text strings.

## Features
- Accept text from the user
- Remove extra spaces (leading, trailing, and multiple internal spaces)
- Optionally remove punctuation
- Convert text to lowercase
- Convert text to uppercase
- Display original text
- Display cleaned text
- Allow repeated cleaning

## Technologies
- Python 3
- Python Standard Library (`string` module)

## How to Run
```bash
python main.py
```

## Example
```text
=== Text Cleaner ===

Original:
   Hello    Python!!!   This   is   a test.   

Cleaned:
hello python this is a test
```

## What I Learned
- Using `str.maketrans()` and `str.translate()` for efficient multi-character replacement/deletion.
- Normalizing whitespace with `" ".join(string.split())`.
