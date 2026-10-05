# Countdown Timer

## Description
A terminal countdown timer that counts down from a user-specified duration in real-time.

## Features
- Ask for hours, minutes, and seconds
- Display countdown in real time
- Update the timer every second using Python's `time` module
- Stop when it reaches zero and display a completion message
- Handle invalid input

## Technologies
- Python 3
- `time` module

## How to Run
```bash
python main.py
```

## Example Usage
```text
=== Countdown Timer ===

Hours: 0
Minutes: 1
Seconds: 30

Time Remaining: 00:01:30

Time's up!
```

## What I Learned
- Using `time.sleep()` to create delays.
- Formatting strings to display time in HH:MM:SS format.
- Using carriage return (`\r`) to overwrite the console output dynamically.
