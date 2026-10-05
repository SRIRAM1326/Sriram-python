# Simple Address Book

## Description
A digital address book to manage contacts, with persistent storage using JSON.

## Features
- Add contact
- View contacts
- Search contact
- Update contact
- Delete contact
- Exit
- Store contacts in a JSON file so they remain after restarting

## Technologies
- Python 3
- Python Standard Library (`json`, `os` modules)

## How to Run
```bash
python main.py
```

## Example
```text
=== Address Book ===

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Name: Sriram
Phone: 9876543210
Email: sriram@example.com

Contact saved!
```

## What I Learned
- Implementing basic CRUD (Create, Read, Update, Delete) operations.
- Validating strings for basic formats (email `@`, `.`, phone `isdigit()`).
- Storing structured dictionaries in JSON files.
