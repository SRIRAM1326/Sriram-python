# Digital Clock

## Description
A live terminal digital clock that updates every second without scrolling the screen.

## Features
- Display current time
- Update every second
- Format as HH:MM:SS
- Keep running until the user stops it
- Display a clean terminal interface
- Handle interruption gracefully

## Technologies
- Python 3
- `datetime` module
- `time` module
- `sys` module

## How to Run
```bash
python main.py
```

## Example
```text
=== Digital Clock ===

Current Time: 11:45:32
```

## What I Learned
- Formatting time with `strftime`.
- Overwriting terminal lines using `sys.stdout.write` and carriage returns (`\r`).
- Handling `KeyboardInterrupt` gracefully.
