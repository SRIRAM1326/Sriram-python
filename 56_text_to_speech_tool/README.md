# Text-to-Speech Tool

## Description
A voice narration terminal application that converts textual strings or entire files into spoken audible voice. Features dynamic speech-rate and volume modulation with fallback to Windows SAPI and PowerShell speech synthesizers.

## Features
- Speaks typed console input aloud through the system speakers.
- Loads and recites arbitrary `.txt` text files.
- Adjustable speech velocity (-10 to 10 rate scale).
- Adjustable speaker volume (0 to 100%).
- Multi-tier speech backend supporting `win32com.client` (SAPI), `pyttsx3`, and PowerShell `System.Speech.Synthesis`.

## Technologies
- Python 3 (`win32com`, `subprocess`, `sys`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Text-to-Speech Tool ===
Engine: win32com | Rate: 0 | Volume: 100%
1. Speak Custom Text
2. Read Text from File (.txt)
3. Adjust Speech Speed (Rate)
4. Adjust Volume
5. Exit

Choose an option (1-5): 1

Enter text to read aloud: Welcome to Python Mini Projects collection!
🔊 Speaking now...
Done speaking.
```

## What I Learned
- Interfacing with OS speech synthesis subsystems using COM Dispatchers.
- Configuring speech properties (pitch rate and volume).
- Graceful degradation through fallback execution engines.
