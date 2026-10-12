import os
import sys
from pathlib import Path
from datetime import datetime

SR_AVAILABLE = False
try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    pass

TRANSCRIPTS_LOG = "transcriptions.txt"

def save_transcript(text, source="Audio"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TRANSCRIPTS_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ({source})\n{text}\n\n")
    print(f"✓ Saved to '{TRANSCRIPTS_LOG}'")

def transcribe_microphone():
    if not SR_AVAILABLE:
        print("\nError: The 'SpeechRecognition' library is needed for live mic input.")
        print("Install via: pip install SpeechRecognition pyaudio")
        return

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\nAdjusting for ambient background noise... please wait 1 second.")
            r.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Microphone is active! Please speak clearly into your mic:")

            audio = r.listen(source, timeout=8, phrase_time_limit=15)
            print("Processing audio with Google Speech Recognition...")

            text = r.recognize_google(audio)
            print("\n" + "=" * 45)
            print("TRANSCRIPTION RESULT:")
            print("=" * 45)
            print(text)
            print("=" * 45)
            save_transcript(text, source="Microphone")

    except sr.WaitTimeoutError:
        print("No speech detected within the timeout window.")
    except sr.UnknownValueError:
        print("Could not understand audio. Try speaking closer to the microphone.")
    except sr.RequestError as e:
        print(f"Could not request results from recognition service: {e}")
    except Exception as e:
        print(f"Microphone error: {e}")

def transcribe_audio_file():
    if not SR_AVAILABLE:
        print("\nError: 'SpeechRecognition' is required. Install via: pip install SpeechRecognition")
        return

    path_str = input("\nEnter path to .wav audio file: ").strip().strip('"')
    p = Path(path_str)
    if not p.exists() or not p.is_file():
        print("File does not exist.")
        return

    r = sr.Recognizer()
    try:
        print(f"\nLoading audio file: {p.name}...")
        with sr.AudioFile(str(p)) as source:
            audio = r.record(source)

        print("Transcribing audio...")
        text = r.recognize_google(audio)
        print("\n" + "=" * 45)
        print(f"TRANSCRIPTION FOR {p.name}:")
        print("=" * 45)
        print(text)
        print("=" * 45)
        save_transcript(text, source=p.name)

    except sr.UnknownValueError:
        print("Audio was unintelligible or contained no recognizable speech.")
    except sr.RequestError as e:
        print(f"API request error: {e}")
    except Exception as e:
        print(f"Audio processing error: {e}")

def view_transcriptions():
    if not os.path.exists(TRANSCRIPTS_LOG):
        print("\nNo saved transcriptions found.")
        return

    print("\n" + "=" * 55)
    print("SAVED TRANSCRIPTION HISTORY")
    print("=" * 55)
    with open(TRANSCRIPTS_LOG, "r", encoding="utf-8") as f:
        print(f.read())
    print("=" * 55)

def main():
    while True:
        print("\n=== Speech-to-Text Tool ===")
        print(f"SpeechRecognition Module: {'Installed ✓' if SR_AVAILABLE else 'Not Installed (pip install SpeechRecognition)'}")
        print("1. Transcribe Live Microphone Input")
        print("2. Transcribe Audio File (.wav)")
        print("3. View Saved Transcriptions History")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            transcribe_microphone()
        elif choice == "2":
            transcribe_audio_file()
        elif choice == "3":
            view_transcriptions()
        elif choice == "4":
            print("Exiting Speech-to-Text Tool. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
