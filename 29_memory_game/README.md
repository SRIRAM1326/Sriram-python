# Memory Game

## Description
A terminal-based memory matching game where players flip pairs of hidden cards to find matches.

## Features
- Generate pairs of characters
- Hide the values initially
- Allow the player to select two positions
- Reveal the selected values
- Determine whether they match
- Track number of attempts
- Continue until all pairs are matched
- Display final score

## Technologies
- Python 3
- `random` module
- `time` module

## How to Run
```bash
python main.py
```

## Example
```text
=== Memory Game ===

  0 1 2 3
0 * * * *
1 * * * *
2 * * * *
3 * * * *

Choose first position (0-15): 2
Choose second position (0-15): 6

Position 2: A
Position 6: B

No match!
```

## What I Learned
- Managing a 1D list to represent a 2D grid.
- Managing game state (revealed vs hidden).
- Using `time.sleep()` to pause the game briefly.
