# Password-Protected Notes

## Description
A secure encrypted terminal notebook that protects sensitive data at rest using PBKDF2-HMAC-SHA256 key derivation with 100,000 iterations and Fernet symmetric encryption.

## Features
- Cryptographic security: Vault files (`vault.dat`) are fully encrypted at rest.
- PBKDF2-HMAC-SHA256 password derivation with randomized 16-byte salt.
- Authenticated AES/Fernet encryption preventing tampering.
- Password change functionality re-encrypts the vault with fresh cryptographic seeds.
- Rate-limited authentication lockout after repeated failed unlock attempts.

## Technologies
- Python 3
- `cryptography` / `hashlib`

## How to Run
```bash
python main.py
```

## Example
```text
=== Password-Protected Notes ===
🔒 Encrypted Vault Detected.
Enter Master Password (3 attempt(s) remaining): ********
✓ Access granted! Vault decrypted successfully.

--- Vault Menu ---
1. List & Read Notes
2. Add New Note
3. Delete Note
4. Change Master Password
5. Lock Vault & Exit

Choose an option (1-5): 1
=======================================================
#    | Title                          | Date
=======================================================
1    | Server Root Keys               | 2026-10-12 20:30
=======================================================
```

## What I Learned
- Implementing key derivation functions (KDF) using cryptographic salts.
- Symmetric block and stream cipher encryption standards (Fernet / AES).
- Serializing encrypted payloads and handling authentication failures.
