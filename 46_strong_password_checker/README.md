# Strong Password Checker

## Description
A cybersecurity evaluation utility that inspects passwords across length, character diversity, dictionary patterns, repetition heuristics, and information entropy (bits). Provides remediation guidance and generates cryptographic alternatives.

## Features
- Calculates information-theoretic entropy in bits ($L \times \log_2(N)$).
- Inspects length, lowercase, uppercase, numeric digits, and special symbols.
- Flags insecure sequences and repeated characters (`123456`, `qwerty`, `aaa`).
- Ranks passwords across 4 tiers: Weak, Moderate, Strong, Very Strong.
- Built-in cryptographically secure generator for alternative passwords using `secrets`.

## Technologies
- Python 3 (`re`, `math`, `secrets`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Strong Password Checker ===
1. Check Password Strength
2. Generate Strong Password
3. Exit

Choose an option (1-3): 1

Enter password to inspect: MySecretP@ssw0rd!

==================================================
STRENGTH ASSESSMENT: VERY STRONG 🛡️ [EXCELLENT]
==================================================
Length:          18 characters
Entropy:         118.0 bits
Lowercase (a-z): ✓
Uppercase (A-Z): ✓
Digits (0-9):    ✓
Special Symbols: ✓

All standard security criteria met!
==================================================
```

## What I Learned
- Formulating mathematical Shannon entropy scores for password security.
- Regular expression pattern matching for character classifications.
- Implementing actionable security heuristics for user credential validation.
