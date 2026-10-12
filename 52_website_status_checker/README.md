# Website Status Checker

## Description
An automated HTTP connectivity monitor that tests website availability, extracts HTTP response codes, benchmarks millisecond network latency, and diagnoses network/DNS errors.

## Features
- Inspects single domains or URLs with custom headers.
- Measures end-to-end network round-trip latency in milliseconds.
- Batch inspection table for monitoring collections of endpoints.
- Continuous heartbeat polling loop with customizable intervals.
- Handles HTTP errors (403, 404, 500) vs transport/DNS timeouts cleanly.

## Technologies
- Python 3 (`urllib.request`, `time`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Website Status Checker ===
1. Check Single Website
2. Batch Check Multiple Websites
3. Continuous Live Monitor
4. Exit

Choose an option (1-4): 1

Enter website URL to check: github.com
Pinging github.com...

=============================================
[✓] Status:   ONLINE
URL:        https://github.com
HTTP Code:  200
Latency:    142.18 ms
Server:     GitHub.com
=============================================
```

## What I Learned
- Performing HTTP requests and capturing headers with `urllib.request.urlopen`.
- Handling `HTTPError` and `URLError` exception differentiation.
- Benchmarking request latency with microsecond resolution.
