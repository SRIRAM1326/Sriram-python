# URL Shortener

## Description
A CLI utility that converts lengthy URLs into compact short codes or custom aliases. Features persistent JSON storage, redirect analytics, and browser auto-launch.

## Features
- Shortens web addresses into randomized 6-character alphanumeric identifiers.
- Supports custom user-defined aliases.
- Persists all mapped routes locally in `urls.json`.
- Tracks real-time click/expansion counts.
- Seamlessly resolves and opens destinations in the default web browser.

## Technologies
- Python 3 (`json`, `webbrowser`, `random`)

## How to Run
```bash
python main.py
```

## Example
```text
=== URL Shortener ===
1. Shorten URL
2. Expand / Visit Short URL
3. List All Shortened URLs & Analytics
4. Delete Short URL
5. Exit

Choose an option (1-5): 1

Enter long URL: https://www.google.com/search?q=python+programming
Enter custom alias (press Enter for auto-generate): pysearch

✓ URL successfully shortened!
Short URL: http://short.ly/pysearch
Original:  https://www.google.com/search?q=python+programming
```

## What I Learned
- Generating random token identifiers and handling namespace collisions.
- Managing persistent JSON state with click tracking.
- Interfacing with system applications via Python's built-in `webbrowser` library.
