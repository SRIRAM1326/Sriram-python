# Receipt Generator

## Description
A script to generate a formatted shopping receipt with multiple items, quantities, and calculated tax.

## Features
- Add product name, quantity, and price
- Calculate item total
- Add multiple products
- Calculate subtotal, tax, and grand total
- Display a formatted receipt

## Technologies
- Python 3

## How to Run
```bash
python main.py
```

## Example
```text
========== RECEIPT ==========

Product       Qty     Price
--------------------------------
Apple          2      ₹100.00
Milk           1      ₹60.00
Bread          2      ₹80.00

------------------------------
Subtotal:       ₹240.00
Tax (5%):       ₹12.00
------------------------------
Total:          ₹252.00
==============================
```

## What I Learned
- Collecting structured data via user input in a loop.
- Formatting strings with specific alignment `<15`, `<5`.
