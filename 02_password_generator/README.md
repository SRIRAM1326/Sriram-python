# Password Generator

## Description
A secure command-line password generator that creates random passwords with a mix of characters.

## Features
- Ask the user for password length
- Generate random passwords using the `secrets` module
- Include uppercase letters, lowercase letters, numbers, and special characters
- Validate password length
- Allow generating multiple passwords
- Option to exit

## Technologies
- Python 3
- `secrets` module
- `string` module

## How to Run
```bash
python main.py
```

## Example Usage
```text
=== Password Generator ===

Password length: 16

Generated Password:
X7@kP2!mQ9#zL4$r
```

## What I Learned
- Using the `secrets` module instead of `random` for cryptographic security.
- Manipulating strings using the built-in `string` module constants.
- Validating integer inputs.
