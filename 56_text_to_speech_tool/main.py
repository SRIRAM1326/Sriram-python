import os
import subprocess
import sys
from pathlib import Path

TTS_BACKEND = None

# Check backend priority 1: pyttsx3
try:
    import pyttsx3
    TTS_BACKEND = "pyttsx3"
except ImportError:
    pass

# Check backend priority 2: Windows native SAPI through pywin32
if not TTS_BACKEND:
    try:
        import win32com.client
        TTS_BACKEND = "win32com"
    except ImportError:
        pass

# Fallback: Windows PowerShell System.Speech
if not TTS_BACKEND and sys.platform == "win32":
    TTS_BACKEND = "powershell"

def speak(text, rate=0, volume=100):
    if not text.strip():
        return

    text = text.replace('"', '\\"').replace("'", "''")

    if TTS_BACKEND == "pyttsx3":
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 150 + rate * 10)
            engine.setProperty("volume", volume / 100.0)
            engine.say(text)
            engine.runAndWait()
            return
        except Exception as e:
            print(f"pyttsx3 error: {e}")

    if TTS_BACKEND == "win32com":
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Rate = rate  # -10 to 10
            speaker.Volume = volume  # 0 to 100
            speaker.Speak(text)
            return
        except Exception as e:
            print(f"SAPI error: {e}")

    if TTS_BACKEND == "powershell":
        try:
            ps_cmd = (
                f"Add-Type -AssemblyName System.Speech; "
                f"$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
                f"$s.Rate = {rate}; $s.Volume = {volume}; "
                f"$s.Speak('{text}')"
            )
            subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True)
            return
        except Exception as e:
            print(f"PowerShell TTS error: {e}")

    print(f"\n[Speech Simulation]: \"{text}\"")

def speak_direct():
    text = input("\nEnter text to read aloud: ").strip()
    if not text:
        print("Text cannot be empty.")
        return
    print("🔊 Speaking now...")
    speak(text)
    print("Done speaking.")

def speak_from_file():
    path_str = input("\nEnter path to .txt file: ").strip().strip('"')
    p = Path(path_str)
    if not p.exists() or not p.is_file():
        print("Error: File not found.")
        return

    try:
        with open(p, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if not content:
            print("File is empty.")
            return

        print(f"\nReading {p.name} ({len(content)} characters)...")
        print("🔊 Speaking now...")
        speak(content)
        print("Done speaking.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    rate = 0      # Normal rate
    volume = 100  # Max volume

    while True:
        print("\n=== Text-to-Speech Tool ===")
        print(f"Engine: {TTS_BACKEND or 'Console fallback'} | Rate: {rate} | Volume: {volume}%")
        print("1. Speak Custom Text")
        print("2. Read Text from File (.txt)")
        print("3. Adjust Speech Speed (Rate)")
        print("4. Adjust Volume")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            speak_direct()
        elif choice == "2":
            speak_from_file()
        elif choice == "3":
            try:
                r = int(input("Enter rate (-5 slow to 5 fast, default: 0): "))
                rate = max(-10, min(10, r))
                print(f"Rate set to {rate}.")
            except ValueError:
                print("Invalid rate.")
        elif choice == "4":
            try:
                v = int(input("Enter volume (0 to 100, default: 100): "))
                volume = max(0, min(100, v))
                print(f"Volume set to {volume}%.")
            except ValueError:
                print("Invalid volume.")
        elif choice == "5":
            print("Exiting Text-to-Speech. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
