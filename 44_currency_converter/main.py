import json
import urllib.request
import urllib.error

# Baseline exchange rates relative to USD (1 USD = X Currency)
DEFAULT_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "INR": 86.50,
    "JPY": 152.40,
    "CAD": 1.38,
    "AUD": 1.54,
    "CHF": 0.88,
    "CNY": 7.24,
    "SGD": 1.34,
    "AED": 3.67,
    "NZD": 1.68
}

CURRENCY_NAMES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "INR": "Indian Rupee",
    "JPY": "Japanese Yen",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SGD": "Singapore Dollar",
    "AED": "UAE Dirham",
    "NZD": "New Zealand Dollar"
}

RATES = DEFAULT_RATES.copy()

def update_live_rates():
    global RATES
    url = "https://open.er-api.com/v6/latest/USD"
    print("\nFetching latest exchange rates from live API...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data.get("result") == "success":
                live_rates = data.get("rates", {})
                for curr in CURRENCY_NAMES:
                    if curr in live_rates:
                        RATES[curr] = round(live_rates[curr], 4)
                print("✓ Live exchange rates updated successfully!")
            else:
                print("Notice: API responded with non-success status. Using cached rates.")
    except Exception as e:
        print(f"Notice: Could not connect to live API ({e}). Using offline rates.")

def convert_currency():
    print("\nSupported Currencies: " + ", ".join(RATES.keys()))
    from_curr = input("From Currency (e.g. USD): ").strip().upper()
    to_curr = input("To Currency   (e.g. INR): ").strip().upper()

    if from_curr not in RATES or to_curr not in RATES:
        print("Error: Unsupported currency code. Please choose from supported list.")
        return

    try:
        amount = float(input(f"Enter amount in {from_curr}: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid number entered.")
        return

    # Convert to USD first, then to target currency
    usd_amount = amount / RATES[from_curr]
    result = usd_amount * RATES[to_curr]

    unit_rate = RATES[to_curr] / RATES[from_curr]

    print("\n" + "=" * 45)
    print(f"Result: {amount:,.2f} {from_curr} = {result:,.2f} {to_curr}")
    print(f"Rate:   1 {from_curr} = {unit_rate:.4f} {to_curr}")
    print("=" * 45)

def display_rate_table():
    print("\n" + "=" * 55)
    print(f"{'Code':<6} | {'Currency Name':<24} | {'1 USD Equivalent':<16}")
    print("=" * 55)
    for code, rate in sorted(RATES.items()):
        name = CURRENCY_NAMES.get(code, code)
        print(f"{code:<6} | {name:<24} | {rate:>12.4f}")
    print("=" * 55)

def multi_comparison():
    print("\nSupported Currencies: " + ", ".join(RATES.keys()))
    base_curr = input("Enter base currency (default: USD): ").strip().upper() or "USD"
    if base_curr not in RATES:
        print("Invalid currency.")
        return

    try:
        amount = float(input(f"Enter amount in {base_curr} (default 100): ") or "100")
    except ValueError:
        print("Invalid number.")
        return

    usd_amount = amount / RATES[base_curr]
    print(f"\n--- {amount:,.2f} {base_curr} in all currencies ---")
    for code, rate in sorted(RATES.items()):
        converted = usd_amount * rate
        print(f"{code:<5}: {converted:>12,.2f} ({CURRENCY_NAMES.get(code, '')})")

def main():
    while True:
        print("\n=== Currency Converter ===")
        print("1. Convert Between Two Currencies")
        print("2. Multi-Currency Quick Table")
        print("3. View Current Exchange Rate Sheet")
        print("4. Fetch Live Rates (Online)")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            convert_currency()
        elif choice == "2":
            multi_comparison()
        elif choice == "3":
            display_rate_table()
        elif choice == "4":
            update_live_rates()
        elif choice == "5":
            print("Exiting Currency Converter. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
