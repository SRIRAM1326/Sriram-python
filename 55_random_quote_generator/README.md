# Random Quote Generator

## Description
A curated inspirational quotation engine. Displays thoughtful perspectives across programming, philosophy, and motivation formatted in framed ASCII quote cards, with filtering and user submission capabilities.

## Features
- Generates random quotes framed in box-drawn ASCII display cards.
- Filter quotes by themes (Programming, Motivation, Wisdom, Perseverance).
- Add new custom quotations persisted automatically in `quotes.json`.
- Keyword and author search functionality.
- Pre-seeded with famous quotes from Steve Jobs, Linus Torvalds, Dijkstra, Einstein, etc.

## Technologies
- Python 3 (`json`, `random`, `os`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Random Quote Generator ===
1. Get Random Quote
2. Get Random Quote by Category
3. Search Quotes by Author or Keyword
4. Add New Quote to Collection
5. Exit

Choose an option (1-5): 1

┌────────────────────────────────────────────────────────┐
│  🏷️  Category: Programming                            │
├────────────────────────────────────────────────────────┤
│  “Talk is cheap. Show me the code.”                    │
│                                                        │
│  — Linus Torvalds                                      │
└────────────────────────────────────────────────────────┘
```

## What I Learned
- Formatting box-drawing Unicode characters for stylized CLI output cards.
- Text line-wrapping algorithms fitting dynamic terminal bounding boxes.
- Seed data initialization and JSON persistent storage.
