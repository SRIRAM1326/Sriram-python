# Currency Converter

## Description
A versatile currency conversion terminal application that converts monetary amounts across global foreign exchange currencies using pre-configured offline baselines or real-time rates fetched from open exchange APIs.

## Features
- Convert between major fiat currencies (USD, EUR, GBP, INR, JPY, CAD, AUD, etc.).
- Real-time exchange rate updates via public internet APIs using standard `urllib.request`.
- Graceful offline fallback with preloaded benchmark exchange rates.
- Multi-currency comparison mode to view value across all currencies simultaneously.
- Exchange rate overview table.

## Technologies
- Python 3 (`urllib.request`, `json`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Currency Converter ===
1. Convert Between Two Currencies
2. Multi-Currency Quick Table
3. View Current Exchange Rate Sheet
4. Fetch Live Rates (Online)
5. Exit

Choose an option (1-5): 1

From Currency (e.g. USD): USD
To Currency   (e.g. INR): INR
Enter amount in USD: 50

=============================================
Result: 50.00 USD = 4,325.00 INR
Rate:   1 USD = 86.5000 INR
=============================================
```

## What I Learned
- Mathematical normalization of foreign exchange rates against a pivot currency (USD).
- Handling network requests and JSON API responses using Python's built-in `urllib.request`.
- Structuring fallback mechanisms when network access is unavailable.
