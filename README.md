# Python Mini Projects Collection 🚀

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Projects](https://img.shields.io/badge/projects-60%20Total-brightgreen.svg)](#-projects-directory)
[![Tests](https://img.shields.io/badge/tests-pytest%20passing-success.svg)](./tests)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-orange.svg)](./.github/workflows/ci.yml)

Welcome to the **Python Mini Projects** collection! A curated portfolio of **60 standalone, production-ready Python CLI applications**. Designed for developers mastering core Python fundamentals, algorithms, data structures, encryption, media processing, networking, and filesystem automation.

---

## ⚡ Quick Start: Master Interactive Launcher

Instead of manually navigating into folders, you can launch, search, and run any of the 60 applications directly from the root with the master CLI dashboard:

```bash
python run.py
```

### Dashboard Commands:
- **`1 - 60`** — Instantly runs any project by number.
- **`search`** — Substring search across all 60 projects by keyword (e.g. `qr`, `password`, `json`, `calc`).
- **`b1 - b5`** — Filters and lists projects in a specific batch.
- **`test`** — Runs the automated `pytest` test suite.
- **`all`** — Displays the full categorized directory.

```text
=================================================================
      🚀 PYTHON MINI PROJECTS COLLECTION (60 APPS) 🚀
=================================================================
Commands & Options:
  • 1 - 60    : Run any project directly by number
  • b1 - b5   : View projects in Batch 1 through Batch 5
  • all       : List all 60 projects with descriptions
  • search    : Search projects by name or keyword
  • test      : Run automated unit test suite (pytest)
  • exit / q  : Quit launcher

Select an option or project # > 42
▶ Launching: [42] Qr Code Generator...
```

---

## 🛠 Manual Execution

Each project is completely self-contained in its own numbered folder:

```bash
cd 41_email_validator
python main.py
```

Each project directory includes a localized `README.md` explaining the implementation logic, code architecture, and learning objectives.

---

## 🧪 Automated Testing

The repository includes a comprehensive unit test suite written with `pytest` covering core algorithms, validations, security routines, and mathematical helpers:

```bash
# Run all unit tests
pytest -v
```

---

## 📂 Projects Directory

### Batch 1: Basics & Fundamentals (01 – 10)
1. **[01 Calculator CLI](./01_calculator_cli)** - Basic arithmetic operations with zero-division guards.
2. **[02 Password Generator](./02_password_generator)** - Cryptographically secure password generation using `secrets`.
3. **[03 Number Guessing Game](./03_number_guessing_game)** - High-low numeric guessing game.
4. **[04 To-Do CLI](./04_todo_cli)** - Task manager with JSON persistence.
5. **[05 Countdown Timer](./05_countdown_timer)** - Terminal countdown timer.
6. **[06 Dice Simulator](./06_dice_simulator)** - Standard six-sided dice roller with statistical logs.
7. **[07 Grade Calculator](./07_grade_calculator)** - Computes percentage and academic grades.
8. **[08 Expense Tracker](./08_expense_tracker)** - Track expenses with SQLite persistence.
9. **[09 Temperature Converter](./09_temperature_converter)** - Converts between Celsius, Fahrenheit, and Kelvin.
10. **[10 File Organizer](./10_file_organizer)** - Automatically sorts directory contents into categorical folders by file extension.

### Batch 2: Strings & Logic (11 – 20)
11. **[11 Word Counter](./11_word_counter)** - Analyzes text for word, character, and sentence density.
12. **[12 Palindrome Checker](./12_palindrome_checker)** - Punctuation-agnostic palindrome validation.
13. **[13 Prime Number Checker](./13_prime_number_checker)** - Algorithmic primality testing.
14. **[14 Multiplication Table](./14_multiplication_table)** - Formatted arithmetic multiplication tables.
15. **[15 Text Case Converter](./15_text_case_converter)** - Shifts string casing conventions dynamically.
16. **[16 Character Frequency Counter](./16_character_frequency_counter)** - Tallies character frequencies using dictionaries.
17. **[17 Anagram Checker](./17_anagram_checker)** - Evaluates if two strings share exact character signatures.
18. **[18 Leap Year Checker](./18_leap_year_checker)** - Verifies leap years using astronomical standards.
19. **[19 Rock Paper Scissors](./19_rock_paper_scissors)** - Play against randomized computer heuristics.
20. **[20 Quiz Game](./20_quiz_game)** - Interactive multiple-choice trivia with score tracking.

### Batch 3: Tools & Utilities (21 – 30)
21. **[21 PIN Validator](./21_pin_validator)** - Validates numeric constraints on PIN codes.
22. **[22 Unit Converter](./22_unit_converter)** - Converts multiple imperial and metric measurements.
23. **[23 Digital Clock](./23_digital_clock)** - Real-time updating terminal digital clock.
24. **[24 Receipt Generator](./24_receipt_generator)** - Formats shopping cart inputs into aligned tabular receipts.
25. **[25 Shopping List Manager](./25_shopping_list_manager)** - Interactive CLI memory list for groceries.
26. **[26 Age Calculator](./26_age_calculator)** - Calculates age in years, months, and days with leap-year handling.
27. **[27 Calendar Generator](./27_calendar_generator)** - Terminal-based visual calendar renderer.
28. **[28 Fibonacci Generator](./28_fibonacci_generator)** - Dynamically generates Fibonacci number sequences iteratively.
29. **[29 Memory Game](./29_memory_game)** - Interactive hidden grid pair matching terminal game.
30. **[30 High Score Tracker](./30_high_score_tracker)** - Leaderboard tracking with local JSON persistence.

### Batch 4: Intermediate Systems (31 – 40)
31. **[31 Even/Odd Analyzer](./31_even_odd_analyzer)** - Categorizes and reports counts of filtered numeric lists.
32. **[32 Number Statistics](./32_number_statistics)** - Computes minimum, maximum, mean, and medians on datasets.
33. **[33 Word Scrambler](./33_word_scrambler)** - Reorganizes characters to guess randomized words.
34. **[34 Random Name Picker](./34_random_name_picker)** - Selects random candidates from user-submitted pools.
35. **[35 Text File Editor](./35_text_file_editor)** - Terminal-based file IO tool to create, read, and edit `.txt` files natively.
36. **[36 Simple Address Book](./36_simple_address_book)** - Full CRUD application storing contacts locally to JSON.
37. **[37 JSON Data Manager](./37_json_data_manager)** - Generic table manager tracking custom categories directly mapped to a file database.
38. **[38 Duplicate Finder](./38_duplicate_finder)** - Scans directories dynamically and reports hash-collided duplicates.
39. **[39 Text Cleaner](./39_text_cleaner)** - Strips duplicate spaces, artifacts, and trims padding aggressively.
40. **[40 Employee Manager](./40_employee_manager)** - Full object-oriented system utilizing custom tracking classes.

### Batch 5: Media, Security & Productivity (41 – 60)
41. **[41 Email Validator](./41_email_validator)** - Validates format compliance and detects domain typos (`gmai.com` → `gmail.com`).
42. **[42 QR Code Generator](./42_qr_code_generator)** - Encodes text/URLs to terminal ASCII blocks and exports `.png` files.
43. **[43 URL Shortener](./43_url_shortener)** - Shortens URLs with custom aliases, click analytics, and auto-browser launching.
44. **[44 Currency Converter](./44_currency_converter)** - Multi-currency exchange rate conversions with offline data and live API sync.
45. **[45 Typing Speed Tester](./45_typing_speed_tester)** - Benchmarks typing velocity (Gross/Net WPM) and character precision.
46. **[46 Strong Password Checker](./46_strong_password_checker)** - Evaluates entropy (bits), character variety, common patterns, and suggests fixes.
47. **[47 Image Resizer](./47_image_resizer)** - Resizes images to custom dimensions, percentages, or social presets with Lanczos antialiasing.
48. **[48 PDF Merger](./48_pdf_merger)** - Combines multiple PDF files sequentially or merges entire directories.
49. **[49 Contact Book CLI](./49_contact_book_cli)** - Full CRUD address directory with search, tabular display, and in-place editing.
50. **[50 Pomodoro Timer](./50_pomodoro_timer)** - Productivity sprints with in-place progress bars and audible completion alerts.
51. **[51 Bulk File Renamer](./51_bulk_file_renamer)** - Batch rename files via prefixes, suffixes, token replacement, or numbering with dry-run preview.
52. **[52 Website Status Checker](./52_website_status_checker)** - Diagnoses endpoint availability, HTTP response codes, and network latency.
53. **[53 YouTube Playlist Manager](./53_youtube_playlist_manager)** - Curates video playlists, normalizes links, and launches browser playback.
54. **[54 Daily Journal](./54_daily_journal)** - Private journal with mood logging, keyword search, word statistics, and Markdown export.
55. **[55 Random Quote Generator](./55_random_quote_generator)** - Displays inspirational quotes framed in styled Unicode card boxes.
56. **[56 Text-to-Speech Tool](./56_text_to_speech_tool)** - Reads text aloud from input or `.txt` files with adjustable rate and volume.
57. **[57 Speech-to-Text Tool](./57_speech_to_text_tool)** - Transcribes speech from live microphone or `.wav` audio files into text.
58. **[58 Password-Protected Notes](./58_password_protected_notes)** - Encrypted notes vault using PBKDF2-HMAC-SHA256 and Fernet symmetric encryption.
59. **[59 Duplicate Image Finder](./59_duplicate_image_finder)** - Detects identical images across directories using file sizes and SHA-256 chunk hashes.
60. **[60 Student Attendance Tracker](./60_student_attendance_tracker)** - Records roll-call attendance, computes cohort percentages, and flags students below 75%.

---

## 📜 License
This project is licensed under the [MIT License](./LICENSE) — free to use, modify, and distribute for educational and commercial purposes.
