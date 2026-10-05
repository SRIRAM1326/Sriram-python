import time
from datetime import datetime
import sys

def main():
    print("=== Digital Clock ===")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            sys.stdout.write(f"\rCurrent Time: {current_time}")
            sys.stdout.flush()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nClock stopped.")

if __name__ == "__main__":
    main()
