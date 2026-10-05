# PIN Validator

## Description
A utility that validates whether a user's input qualifies as a valid 4-digit or 6-digit numerical PIN.

## Features
- Ask the user to enter a PIN
- PIN must contain only numbers
- Support 4-digit and 6-digit PINs
- Reject letters and special characters
- Reject incorrect lengths
- Display appropriate error messages
- Allow repeated validation

## Technologies
- Python 3

## How to Run
```bash
python main.py
```

## Example
```text
=== PIN Validator ===

Enter PIN: 1234

Valid PIN.
```

## What I Learned
- Using string methods like `isdigit()` to validate numerical input without parsing integers.
- Managing multiple return values from functions.
