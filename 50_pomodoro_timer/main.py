import time
import sys

try:
    import winsound
    WINSOUND_AVAILABLE = True
except ImportError:
    WINSOUND_AVAILABLE = False

def alert_sound():
    """Triggers an audio chime when a phase concludes."""
    if WINSOUND_AVAILABLE:
        try:
            for freq in [600, 800, 1000]:
                winsound.Beep(freq, 150)
            return
        except Exception:
            pass
    print("\a", end="", flush=True)

def render_progress(label, remaining, total):
    elapsed = total - remaining
    pct = (elapsed / total) if total > 0 else 1.0
    bar_len = 25
    filled = int(bar_len * pct)
    bar = "█" * filled + "░" * (bar_len - filled)
    mins = remaining // 60
    secs = remaining % 60
    sys.stdout.write(f"\r{label} [{mins:02d}:{secs:02d}] |{bar}| {int(pct * 100)}% ")
    sys.stdout.flush()

def countdown(seconds, label):
    total = seconds
    while seconds >= 0:
        render_progress(label, seconds, total)
        if seconds == 0:
            break
        time.sleep(1)
        seconds -= 1
    sys.stdout.write("\n")
    alert_sound()

def run_session(work_min=25, break_min=5, long_break_min=15, target_cycles=4):
    print(f"\n🍅 Starting Pomodoro Timer: {target_cycles} cycles")
    print(f"Work: {work_min}m | Short Break: {break_min}m | Long Break: {long_break_min}m")
    input("Press Enter to begin...")

    for cycle in range(1, target_cycles + 1):
        print(f"\n{'='*20} CYCLE {cycle}/{target_cycles} {'='*20}")
        print("🎯 FOCUS TIME: Put away all distractions!")
        countdown(work_min * 60, f"FOCUS #{cycle}")

        if cycle < target_cycles:
            print(f"\n☕ SHORT BREAK: Take a stretch or sip water ({break_min} min)")
            input("Press Enter to start break...")
            countdown(break_min * 60, f"BREAK #{cycle}")
        else:
            print(f"\n🎉 ALL {target_cycles} CYCLES COMPLETE! Time for a LONG BREAK ({long_break_min} min)")
            input("Press Enter to start long break...")
            countdown(long_break_min * 60, "LONG BREAK")

    print("\n✓ Pomodoro session completed! Great job on your productivity today.\n")

def run_quick_demo():
    print("\nRunning Quick 10-Second Demo (Work: 10s, Break: 5s)...")
    countdown(10, "DEMO WORK")
    print("Demo break starting:")
    countdown(5, "DEMO BREAK")
    print("Demo completed successfully!")

def main():
    while True:
        print("\n=== Pomodoro Timer ===")
        print("1. Start Standard Pomodoro (25m Work / 5m Break / 4 Cycles)")
        print("2. Custom Durations")
        print("3. Quick Test Demo (10 seconds)")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            run_session(work_min=25, break_min=5, long_break_min=15, target_cycles=4)
        elif choice == "2":
            try:
                w = int(input("Enter work duration in minutes (e.g. 25): "))
                b = int(input("Enter short break in minutes (e.g. 5): "))
                lb = int(input("Enter long break in minutes (e.g. 15): "))
                c = int(input("Enter number of cycles before long break (e.g. 4): "))
                run_session(work_min=w, break_min=b, long_break_min=lb, target_cycles=c)
            except ValueError:
                print("Invalid input. Enter positive integers.")
        elif choice == "3":
            run_quick_demo()
        elif choice == "4":
            print("Stay focused and productive! Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
