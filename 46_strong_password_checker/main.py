import math
import re
import string
import secrets

COMMON_WEAK_PATTERNS = [
    "password", "123456", "12345678", "qwerty", "admin", "welcome",
    "abc123", "letmein", "monkey", "dragon", "baseball", "football"
]

def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"\d", password):
        pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>\-_=+[\]\\\/]", password):
        pool += 33

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 1)

def evaluate_password(password):
    issues = []
    score = 0

    length = len(password)
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>\-_=+[\]\\\/]", password))

    # Length scoring
    if length < 8:
        issues.append("Length is under 8 characters (Critical risk).")
    elif length >= 14:
        score += 3
    elif length >= 10:
        score += 2
    else:
        score += 1

    # Character varieties
    if has_lower:
        score += 1
    else:
        issues.append("Add lowercase letters (a-z).")

    if has_upper:
        score += 1
    else:
        issues.append("Add uppercase letters (A-Z).")

    if has_digit:
        score += 1
    else:
        issues.append("Add numeric digits (0-9).")

    if has_symbol:
        score += 1
    else:
        issues.append("Add special symbols (!@#$%^&*...).")

    # Pattern checks
    lower_pw = password.lower()
    for bad in COMMON_WEAK_PATTERNS:
        if bad in lower_pw:
            issues.append(f"Contains common insecure pattern: '{bad}'.")
            score = max(0, score - 2)

    # Repetition check (3 or more same characters in a row)
    if re.search(r"(.)\1\1", password):
        issues.append("Avoid repeated consecutive characters (e.g. 'aaa' or '111').")
        score = max(0, score - 1)

    entropy = calculate_entropy(password)

    # Determine Rating
    if score >= 6 and entropy >= 60:
        strength = "VERY STRONG 🛡️"
        color_code = "[EXCELLENT]"
    elif score >= 5 and entropy >= 45:
        strength = "STRONG 💪"
        color_code = "[GOOD]"
    elif score >= 3:
        strength = "MODERATE ⚠️"
        color_code = "[MEDIUM]"
    else:
        strength = "WEAK ❌"
        color_code = "[POOR]"

    return {
        "length": length,
        "has_lower": has_lower,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "entropy": entropy,
        "score": score,
        "strength": strength,
        "color_code": color_code,
        "issues": issues
    }

def generate_strong_alternative(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(chars) for _ in range(length))

def run_checker():
    pw = input("\nEnter password to inspect: ")
    if not pw:
        print("Password cannot be empty.")
        return

    res = evaluate_password(pw)

    print("\n" + "=" * 50)
    print(f"STRENGTH ASSESSMENT: {res['strength']} {res['color_code']}")
    print("=" * 50)
    print(f"Length:          {res['length']} characters")
    print(f"Entropy:         {res['entropy']} bits")
    print(f"Lowercase (a-z): {'✓' if res['has_lower'] else '✗'}")
    print(f"Uppercase (A-Z): {'✓' if res['has_upper'] else '✗'}")
    print(f"Digits (0-9):    {'✓' if res['has_digit'] else '✗'}")
    print(f"Special Symbols: {'✓' if res['has_symbol'] else '✗'}")

    if res["issues"]:
        print("\nRecommendations to Improve:")
        for issue in res["issues"]:
            print(f" - {issue}")
    else:
        print("\nAll standard security criteria met!")

    if "WEAK" in res["strength"] or "MODERATE" in res["strength"]:
        suggest = generate_strong_alternative()
        print(f"\n💡 Suggested Secure Alternative: {suggest}")

    print("=" * 50)

def main():
    while True:
        print("\n=== Strong Password Checker ===")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            run_checker()
        elif choice == "2":
            suggested = generate_strong_alternative()
            print(f"\nGenerated Secure Password: {suggested}")
        elif choice == "3":
            print("Stay safe and secure! Exiting...")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
