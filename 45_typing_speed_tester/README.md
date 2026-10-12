# Typing Speed Tester

## Description
A terminal benchmarking tool that measures keyboard typing velocity and precision. It computes Gross Words Per Minute (WPM), Net WPM, and accuracy percentages with real-time countdowns.

## Features
- Standard typing calculation standard: 5 keystrokes per word.
- Accurate fractional second benchmarking via `time.perf_counter()`.
- Precision matching calculating percentage accuracy and character mismatches.
- Performance rating tiers (Master, Fast, Fluent, Average, Beginner).
- Interactive 3-second countdown buffer.

## Technologies
- Python 3 (`time`, `random`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Typing Speed Tester ===
1. Start Typing Test
2. Exit

Choose an option (1-2): 1

Starting in 1...
GO! Type the text below exactly as shown:

-----------------------------------------------------------------
The quick brown fox jumps over the lazy dog.
-----------------------------------------------------------------

> The quick brown fox jumps over the lazy dog.

=============================================
              TEST RESULTS
=============================================
Time Taken:      5.82 seconds
Characters:      44 typed (44/44 correct)
Accuracy:        100.0%
Gross Speed:     90.7 WPM
Net Speed:       90.7 WPM
Rating:          Professional / Master typist 🚀
=============================================
```

## What I Learned
- Utilizing high-resolution timers (`perf_counter`) for performance benchmarking.
- Character-by-character alignment and accuracy calculations.
- Computing standard gross and net Words Per Minute (WPM) formulas.
