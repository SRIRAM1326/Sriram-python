import time

def start_timer(total_seconds):
    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Display dynamically in-place
        time_format = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(f"\rTime Remaining: {time_format}", end="")
        
        time.sleep(1)
        total_seconds -= 1
        
    print("\n\nTime's up!")

def main():
    print("=== Countdown Timer ===")
    
    try:
        hours = int(input("\nHours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))
        
        if hours < 0 or minutes < 0 or seconds < 0:
            print("\nPlease enter positive values.")
            return
            
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        if total_seconds <= 0:
            print("\nPlease enter a duration greater than 0.")
            return
            
        print() # New line before timer
        start_timer(total_seconds)
        
    except ValueError:
        print("\nInvalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
