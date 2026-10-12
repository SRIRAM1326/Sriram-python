# Daily Journal

## Description
A private personal diary and journaling CLI system. Saves date-keyed thoughts locally with mood tracking, categorical tagging, keyword search, word statistics, and Markdown document exports.

## Features
- Multi-line text capture with seamless append or overwrite modes.
- Date-stamped metadata records tracking mood, tags, and word count.
- Historical date browser sorted chronologically.
- Substring keyword and tag search engine across journal archives.
- Single-command export of entries into formatted Markdown files (`.md`).
- Persistent storage in UTF-8 serialized `journal.json`.

## Technologies
- Python 3 (`json`, `datetime`, `os`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Daily Journal ===
1. Write Today's Entry
2. Read Today's Entry
3. Browse Past Entries by Date
4. Search Journal Entries
5. Export Entry to Markdown (.md)
6. Exit

Choose an option (1-6): 1

--- Daily Journal: Entry for 2026-10-12 ---
Today's Mood: Energized
Tags: python, coding, learning

Write your entry below. Type 'EOF' or 'SAVE' on a new line when finished:
Completed a collection of 20 python projects today!
Feeling great about the progress.
SAVE

✓ Entry saved successfully (11 words).
```

## What I Learned
- Collecting multiline terminal input until termination sentinel tokens (`SAVE` / `EOF`).
- Serializing datetime keyed objects with UTF-8 encoding support.
- Generating automated markdown documents with structured frontmatter.
