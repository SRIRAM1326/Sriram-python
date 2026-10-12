# PDF Merger

## Description
A command-line document utility that aggregates and fuses multiple independent PDF documents into a unified output PDF. Supports custom sequenced file lists and directory batch modes.

## Features
- Merges arbitrary sequences of PDF files.
- Directory batch mode to automatically sort and combine all PDFs in a folder.
- Reports per-file page counts and total aggregated output length.
- Resilient error handling skipping damaged or unreadable files.
- Compatible with modern `pypdf` and legacy `PyPDF2`.

## Technologies
- Python 3
- `pypdf`

## How to Run
```bash
python main.py
```

## Example
```text
=== PDF Merger ===
1. Merge Selected PDF Files
2. Merge All PDFs from a Directory
3. Exit

Choose an option (1-3): 1

Enter paths of PDF files to merge (one per line). Enter a blank line when done:
File 1: invoice_jan.pdf
File 2: invoice_feb.pdf
File 3: 

Enter output PDF filename (default: merged_document.pdf): invoices_q1.pdf

Processing PDF files...
  + Added 'invoice_jan.pdf' (2 page(s))
  + Added 'invoice_feb.pdf' (3 page(s))

✓ Successfully merged 2 files (5 total pages) into:
  C:\path\to\invoices_q1.pdf
```

## What I Learned
- Manipulating binary PDF document streams using Python.
- Extracting document metadata and page tree counts via `PdfReader`.
- Concatenating and writing finalized document payloads using `PdfMerger`.
