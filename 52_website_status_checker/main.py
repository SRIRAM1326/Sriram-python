import urllib.request
import urllib.error
import time

COMMON_CHECK_SITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.cloudflare.com"
]

def check_url(url, timeout=5):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) StatusChecker/1.0"}
    req = urllib.request.Request(url, headers=headers)

    start = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            latency_ms = (time.perf_counter() - start) * 1000
            code = response.getcode()
            server = response.headers.get("Server", "Undisclosed")
            return {
                "url": url,
                "status": "ONLINE",
                "code": code,
                "latency_ms": round(latency_ms, 2),
                "server": server,
                "error": None
            }
    except urllib.error.HTTPError as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return {
            "url": url,
            "status": "HTTP_ERROR",
            "code": e.code,
            "latency_ms": round(latency_ms, 2),
            "server": "N/A",
            "error": str(e)
        }
    except urllib.error.URLError as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return {
            "url": url,
            "status": "OFFLINE",
            "code": "N/A",
            "latency_ms": round(latency_ms, 2),
            "server": "N/A",
            "error": str(e.reason)
        }
    except Exception as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return {
            "url": url,
            "status": "ERROR",
            "code": "N/A",
            "latency_ms": round(latency_ms, 2),
            "server": "N/A",
            "error": str(e)
        }

def single_check():
    raw_url = input("\nEnter website URL to check: ").strip()
    if not raw_url:
        print("URL cannot be empty.")
        return

    print(f"Pinging {raw_url}...")
    res = check_url(raw_url)

    symbol = "✓" if res["status"] == "ONLINE" else "✗"
    print("\n" + "=" * 45)
    print(f"[{symbol}] Status:   {res['status']}")
    print(f"URL:        {res['url']}")
    print(f"HTTP Code:  {res['code']}")
    print(f"Latency:    {res['latency_ms']} ms")
    if res["server"] != "N/A":
        print(f"Server:     {res['server']}")
    if res["error"]:
        print(f"Reason:     {res['error']}")
    print("=" * 45)

def batch_check():
    print("\nBatch Options:")
    print("1. Check Common Popular Websites")
    print("2. Enter Custom URLs")
    sub = input("Choose (1-2): ").strip()

    if sub == "1":
        urls = COMMON_CHECK_SITES
    elif sub == "2":
        raw = input("Enter URLs separated by commas or spaces: ")
        urls = [u.strip() for u in raw.replace(",", " ").split() if u.strip()]
    else:
        print("Invalid option.")
        return

    print("\n" + "=" * 70)
    print(f"{'Status':<10} | {'Code':<6} | {'Latency':<10} | {'URL'}")
    print("=" * 70)

    for u in urls:
        res = check_url(u)
        tag = "✓ ONLINE " if res["status"] == "ONLINE" else "✗ " + res["status"]
        print(f"{tag:<10} | {str(res['code']):<6} | {str(res['latency_ms']) + 'ms':<10} | {res['url']}")
    print("=" * 70)

def continuous_monitor():
    raw_url = input("\nEnter URL to monitor: ").strip()
    if not raw_url:
        return
    try:
        interval = int(input("Check interval in seconds (default: 5): ") or "5")
    except ValueError:
        interval = 5

    print(f"\nMonitoring {raw_url} every {interval}s. Press Ctrl+C to stop.")
    try:
        while True:
            res = check_url(raw_url)
            t_str = time.strftime("%H:%M:%S")
            status = "UP  ✓" if res["status"] == "ONLINE" else "DOWN ✗"
            print(f"[{t_str}] {status} | Code: {res['code']} | Latency: {res['latency_ms']}ms")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def main():
    while True:
        print("\n=== Website Status Checker ===")
        print("1. Check Single Website")
        print("2. Batch Check Multiple Websites")
        print("3. Continuous Live Monitor")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            single_check()
        elif choice == "2":
            batch_check()
        elif choice == "3":
            continuous_monitor()
        elif choice == "4":
            print("Exiting Website Status Checker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
