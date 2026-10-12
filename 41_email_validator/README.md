# Email Validator

## Description
A command-line tool that checks whether an email address adheres to standard RFC format specifications using regular expressions, local/domain length rules, and domain typo detection.

## Features
- Validates single or batch email addresses.
- Checks local part (max 64 characters) and domain format.
- Disallows illegal characters, consecutive dots, and improper top-level domains.
- Detects common domain typos (e.g. `gmai.com`, `outlok.com`) and suggests corrections.
- Zero external dependencies using standard Python `re`.

## Technologies
- Python 3

## How to Run
```bash
python main.py
```

## Example
```text
=== Email Validator ===
1. Validate Single Email
2. Validate Batch Emails
3. Exit

Choose an option (1-3): 1

Enter an email address to validate: user@example.com

[✓] Status: VALID
Details: Valid email format!
```

## What I Learned
- Constructing robust regular expressions with lookahead assertions.
- Parsing and validating RFC-compliant email string partitions.
- Implementing domain typo heuristics for improved user experience.
