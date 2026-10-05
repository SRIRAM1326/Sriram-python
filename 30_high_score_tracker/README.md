# High Score Tracker

## Description
A leaderboard system that records player names and scores locally in a JSON file.

## Features
- Ask for player name and score
- Store scores in a JSON file
- Display all scores sorted from highest to lowest
- Display top 5 players
- Preserve scores after restarting
- Handle missing or empty score files

## Technologies
- Python 3
- `json` module
- `os` module

## How to Run
```bash
python main.py
```

## Example
```text
=== High Score Tracker ===

1. Add Score
2. View Scores
3. View Top 5
4. Exit

Player Name: Sriram
Score: 950

Score saved!

========== LEADERBOARD ==========

1. Sriram     950
2. Arun       875
3. Kumar      810
```

## What I Learned
- Saving and loading persistent data with the `json` module.
- Sorting dictionaries using lambda functions as a sort key.
