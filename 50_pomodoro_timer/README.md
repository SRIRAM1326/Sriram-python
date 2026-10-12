# Pomodoro Timer

## Description
A command-line productivity timer based on the Pomodoro Technique. Alternates between high-intensity focused working sprints and structured break intervals, featuring real-time in-place progress bars and audible completion chimes.

## Features
- Standard 25m Focus / 5m Short Break / 15m Long Break intervals over 4 cycles.
- Dynamic single-line terminal progress bar updating live without screen spamming (`\r`).
- Sound alerts via Windows `winsound.Beep` with ASCII bell fallback (`\a`).
- Custom duration configuration for power users.
- Fast 10-second testing mode.

## Technologies
- Python 3 (`time`, `sys`, `winsound`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Pomodoro Timer ===
1. Start Standard Pomodoro (25m Work / 5m Break / 4 Cycles)
2. Custom Durations
3. Quick Test Demo (10 seconds)
4. Exit

Choose an option (1-4): 1

🍅 Starting Pomodoro Timer: 4 cycles
Work: 25m | Short Break: 5m | Long Break: 15m
Press Enter to begin...

==================== CYCLE 1/4 ====================
🎯 FOCUS TIME: Put away all distractions!
FOCUS #1 [24:48] |████░░░░░░░░░░░░░░░░░░░░░| 1% 
```

## What I Learned
- Managing single-line terminal animations using carriage return `\r` and `sys.stdout.flush()`.
- Audio dispatching using platform-native audio hardware interfaces (`winsound`).
- Designing state machine workflows cycling through work and rest sessions.
