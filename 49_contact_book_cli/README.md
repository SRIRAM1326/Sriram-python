# Contact Book CLI

## Description
A full CRUD (Create, Read, Update, Delete) command-line address directory. Features persistent JSON storage, formatted tabular listings, partial search, and interactive field editing.

## Features
- Add contacts with name, phone number, email address, and category notes.
- Neatly aligned tabular display for all entries.
- Substring search matching names, numbers, or emails.
- In-place selective editing preserving unchanged fields on empty submit.
- Safe deletion confirmation prompts.
- Persistent state saved to `contacts.json`.

## Technologies
- Python 3 (`json`, `os`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Contact Book CLI ===
1. View All Contacts
2. Add Contact
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit

Choose an option (1-6): 2

--- Add New Contact ---
Full Name: Alex Johnson
Phone Number: +1 555-0199
Email Address: alex@example.com
Category / Notes (e.g. Work, Family): Colleague

✓ Contact 'Alex Johnson' added successfully.
```

## What I Learned
- Managing CRUD data lifecycles over serialized JSON files.
- Implementing safe fallback inputs during interactive record updates.
- Formatting structured tabular outputs in the terminal using Python string formatters.
