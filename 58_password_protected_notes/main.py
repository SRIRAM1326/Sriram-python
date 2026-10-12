import os
import json
import base64
import hashlib
from datetime import datetime

VAULT_FILE = "vault.dat"

# Check if cryptography library is available
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

def derive_key(password: str, salt: bytes) -> bytes:
    """Derives a base64-encoded 32-byte key from password using PBKDF2-HMAC-SHA256."""
    if CRYPTO_AVAILABLE:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    else:
        # Standard library PBKDF2
        derived = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
        return base64.urlsafe_b64encode(derived[:32])

def encrypt_payload(data_dict: dict, password: str) -> bytes:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    plaintext = json.dumps(data_dict).encode("utf-8")

    if CRYPTO_AVAILABLE:
        fernet = Fernet(key)
        ciphertext = fernet.encrypt(plaintext)
    else:
        # Stream cipher fallback using derived key bytes
        key_raw = base64.urlsafe_b64decode(key)
        ciphertext = bytes([b ^ key_raw[i % len(key_raw)] for i, b in enumerate(plaintext)])

    # Format: 16-byte salt + ciphertext
    return salt + ciphertext

def decrypt_payload(raw_bytes: bytes, password: str) -> dict:
    if len(raw_bytes) < 17:
        raise ValueError("Corrupted vault file.")

    salt = raw_bytes[:16]
    ciphertext = raw_bytes[16:]
    key = derive_key(password, salt)

    if CRYPTO_AVAILABLE:
        fernet = Fernet(key)
        plaintext = fernet.decrypt(ciphertext)
    else:
        key_raw = base64.urlsafe_b64decode(key)
        plaintext = bytes([b ^ key_raw[i % len(key_raw)] for i, b in enumerate(ciphertext)])

    return json.loads(plaintext.decode("utf-8"))

def init_or_unlock():
    if not os.path.exists(VAULT_FILE):
        print("\n--- Initial Setup: Create Your Secure Vault ---")
        while True:
            pw1 = input("Set Master Password: ")
            pw2 = input("Confirm Master Password: ")
            if not pw1:
                print("Password cannot be empty.")
                continue
            if pw1 != pw2:
                print("Passwords do not match. Try again.")
                continue
            break

        initial_data = {"notes": []}
        blob = encrypt_payload(initial_data, pw1)
        with open(VAULT_FILE, "wb") as f:
            f.write(blob)
        print("✓ Vault created and initialized successfully!")
        return pw1, initial_data

    # Existing vault
    print("\n🔒 Encrypted Vault Detected.")
    attempts = 3
    while attempts > 0:
        pw = input(f"Enter Master Password ({attempts} attempt(s) remaining): ")
        try:
            with open(VAULT_FILE, "rb") as f:
                blob = f.read()
            data = decrypt_payload(blob, pw)
            print("✓ Access granted! Vault decrypted successfully.")
            return pw, data
        except Exception:
            attempts -= 1
            print("✗ Access denied: Invalid master password.")

    print("\nMaximum attempts exceeded. Exiting for security.")
    return None, None

def save_vault(data, password):
    blob = encrypt_payload(data, password)
    with open(VAULT_FILE, "wb") as f:
        f.write(blob)

def add_note(data, password):
    title = input("\nNote Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    print("Enter note content (Type 'END' on a separate line when finished):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    content = "\n".join(lines).strip()
    new_note = {
        "id": len(data["notes"]) + 1,
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    data["notes"].append(new_note)
    save_vault(data, password)
    print(f"✓ Note '{title}' encrypted and stored in vault.")

def list_and_read_notes(data):
    notes = data.get("notes", [])
    if not notes:
        print("\nNo notes in vault.")
        return

    print("\n" + "=" * 55)
    print(f"{'#':<4} | {'Title':<30} | {'Date'}")
    print("=" * 55)
    for i, n in enumerate(notes, 1):
        print(f"{i:<4} | {n['title']:<30} | {n['date']}")
    print("=" * 55)

    ch = input("\nEnter note # to read (or press Enter to return): ").strip()
    if ch.isdigit():
        idx = int(ch) - 1
        if 0 <= idx < len(notes):
            target = notes[idx]
            print("\n" + "-" * 55)
            print(f"TITLE: {target['title']} ({target['date']})")
            print("-" * 55)
            print(target["content"])
            print("-" * 55)

def delete_note(data, password):
    notes = data.get("notes", [])
    if not notes:
        return

    try:
        idx = int(input("\nEnter note number to delete: ")) - 1
        if 0 <= idx < len(notes):
            removed = notes.pop(idx)
            save_vault(data, password)
            print(f"✓ Deleted note: '{removed['title']}'")
    except ValueError:
        pass

def change_password(data, current_pw):
    old_check = input("\nEnter current password to confirm: ")
    if old_check != current_pw:
        print("Current password incorrect.")
        return current_pw

    new_pw = input("Enter new master password: ")
    confirm_pw = input("Confirm new master password: ")
    if new_pw != confirm_pw or not new_pw:
        print("Password mismatch or empty.")
        return current_pw

    save_vault(data, new_pw)
    print("✓ Master password updated. Vault re-encrypted with new key.")
    return new_pw

def main():
    print("=== Password-Protected Notes ===")
    password, data = init_or_unlock()
    if not password:
        return

    while True:
        print("\n--- Vault Menu ---")
        print("1. List & Read Notes")
        print("2. Add New Note")
        print("3. Delete Note")
        print("4. Change Master Password")
        print("5. Lock Vault & Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            list_and_read_notes(data)
        elif choice == "2":
            add_note(data, password)
        elif choice == "3":
            delete_note(data, password)
        elif choice == "4":
            password = change_password(data, password)
        elif choice == "5":
            print("Vault securely locked. Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
