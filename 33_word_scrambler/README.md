# Word Scrambler

## Description
A word scrambling game where players try to guess the original word from a scrambled set of letters.

## Features
- Store a collection of words
- Randomly select a word
- Scramble its letters
- Ask the player to guess the original word
- Tell the player whether the answer is correct
- Track score
- Allow multiple rounds
- Display final score
- Option to exit

## Technologies
- Python 3
- Python Standard Library (`random` module)

## How to Run
```bash
python main.py
```

## Example
```text
=== Word Scrambler ===

Scrambled word: YHTPON
Your guess: PYTHON

Correct!
Score: 1
```

## What I Learned
- Shuffling lists in place with `random.shuffle()`.
- Validating strings and utilizing `while` loops to enforce specific outcomes (like ensuring the scrambled word is actually different).
