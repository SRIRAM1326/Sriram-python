# Speech-to-Text Tool

## Description
An automated transcription utility that converts spoken audio from a live microphone or pre-recorded `.wav` sound files into digital text transcripts, saving timestamped logs locally.

## Features
- Real-time acoustic capture from system microphones with automatic ambient noise calibration.
- Direct transcription of pre-recorded `.wav` audio files.
- Integration with standard Google Speech Recognition API engines.
- Persistent logging of transcribed notes into `transcriptions.txt`.
- Graceful error messaging handling unrecognized utterances and network interruptions.

## Technologies
- Python 3
- `SpeechRecognition` (optional microphone integration via `pyaudio`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Speech-to-Text Tool ===
SpeechRecognition Module: Installed ✓
1. Transcribe Live Microphone Input
2. Transcribe Audio File (.wav)
3. View Saved Transcriptions History
4. Exit

Choose an option (1-4): 2

Enter path to .wav audio file: speech_sample.wav
Loading audio file: speech_sample.wav...
Transcribing audio...

=============================================
TRANSCRIPTION FOR speech_sample.wav:
=============================================
hello world this is a python speech to text demo
=============================================
✓ Saved to 'transcriptions.txt'
```

## What I Learned
- Capturing analog acoustic streams and normalizing decibel ambient baselines.
- Streaming discrete audio chunk segments to speech recognition APIs.
- Logging structured transcription records with ISO timestamps.
