# YouTube Playlist Manager

## Description
A command-line curator that organizes external video URLs into customized categorical playlists with persistent JSON indexing, browser auto-launching, and queue management.

## Features
- Create, manage, and delete custom playlists (e.g. Tutorials, Music, Workouts).
- Normalizes long and short (`youtu.be`) links into canonical watch URLs.
- Lists video entries with addition timestamps.
- Instantly opens single videos or launches entire playlists directly in your default web browser.
- Saves all state locally in `playlists.json`.

## Technologies
- Python 3 (`json`, `webbrowser`, `datetime`)

## How to Run
```bash
python main.py
```

## Example
```text
=== YouTube Playlist Manager ===
1. View Playlists & Open Videos
2. Create New Playlist
3. Add Video to Playlist
4. Remove Video from Playlist
5. Delete Playlist
6. Exit

Choose an option (1-6): 2

Enter new playlist name: Python Masterclass
✓ Playlist 'Python Masterclass' created successfully.
```

## What I Learned
- Structuring nested dictionaries for grouping records.
- Canonical URL normalization using string parsing.
- Interacting with client browser runtime environments using `webbrowser`.
