import re

COMMON_DOMAINS = {
    "gmai.com": "gmail.com",
    "gamil.com": "gmail.com",
    "gmial.com": "gmail.com",
    "yaho.com": "yahoo.com",
    "yaho.co": "yahoo.com",
    "hotmial.com": "hotmail.com",
    "outlok.com": "outlook.com",
    "icld.com": "icloud.com"
}

EMAIL_REGEX = re.compile(
    r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validate_email(email):
    email = email.strip()
    if not email:
        return False, "Email address cannot be empty."

    if " " in email:
        return False, "Email address cannot contain spaces."

    if "@" not in email:
        return False, "Missing '@' symbol."

    parts = email.split("@")
    if len(parts) != 2:
        return False, "Email must have exactly one '@' symbol."

    local_part, domain_part = parts

    if len(local_part) == 0:
        return False, "Username/local part cannot be empty."
    if len(local_part) > 64:
        return False, "Username exceeds standard limit of 64 characters."

    if "." not in domain_part:
        return False, "Domain must contain at least one '.' (e.g. example.com)."

    if not EMAIL_REGEX.match(email):
        return False, "Invalid characters or invalid dot placement."

    tld = domain_part.split(".")[-1]
    if len(tld) < 2 or not tld.isalpha():
        return False, "Top-level domain (extension) must be at least 2 alphabetic characters."

    typo_suggestion = COMMON_DOMAINS.get(domain_part.lower())
    if typo_suggestion:
        return True, f"Valid format! (Did you mean @{typo_suggestion}?)"

    return True, "Valid email format!"

def test_single():
    email = input("\nEnter an email address to validate: ")
    is_valid, message = validate_email(email)
    symbol = "✓" if is_valid else "✗"
    status = "VALID" if is_valid else "INVALID"
    print(f"\n[{symbol}] Status: {status}")
    print(f"Details: {message}")

def test_batch():
    print("\nEnter emails separated by commas or spaces:")
    raw = input("> ")
    emails = [e.strip() for e in re.split(r"[,;\s]+", raw) if e.strip()]
    if not emails:
        print("No emails provided.")
        return

    print("\n--- Batch Validation Results ---")
    for email in emails:
        is_valid, msg = validate_email(email)
        status = "✓ VALID  " if is_valid else "✗ INVALID"
        print(f"{status} | {email:<30} | {msg}")

def main():
    while True:
        print("\n=== Email Validator ===")
        print("1. Validate Single Email")
        print("2. Validate Batch Emails")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            test_single()
        elif choice == "2":
            test_batch()
        elif choice == "3":
            print("Exiting Email Validator. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
