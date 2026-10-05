# JSON Data Manager

## Description
A generic JSON record management application that acts as a simple file-based database for structured data.

## Features
- Add record
- View all records
- Search records
- Update record
- Delete record
- Save records to `data.json`
- Automatically create the JSON file if it doesn't exist
- Handle invalid/corrupted JSON gracefully
- Exit option

## Technologies
- Python 3
- Python Standard Library (`json`, `os` modules)

## How to Run
```bash
python main.py
```

## Example
```text
=== JSON Data Manager ===

1. Add Record
2. View Records
3. Search
4. Update
5. Delete
6. Exit
```

## What I Learned
- Designing generic CRUD systems.
- Handling JSON read/write operations and catching JSONDecodeErrors for corrupted files.
