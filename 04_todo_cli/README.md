# To-Do CLI

## Description
A command-line task manager to help you keep track of your tasks. It stores tasks locally in a JSON file to persist data between sessions.

## Features
- Add task
- List tasks with status indication
- Mark task as completed
- Delete task
- Exit
- Store tasks locally in a JSON file
- Preserve tasks when the application is restarted

## Technologies
- Python 3
- `json` module
- `os` module

## How to Run
```bash
python main.py
```

## Example Usage
```text
=== To-Do Manager ===

1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit

Choose an option: 2

=== Tasks ===
1. [ ] Learn Python
2. [✓] Build mini project
3. [ ] Practice APIs
```

## What I Learned
- Reading from and writing to files in Python.
- Using the `json` module to serialize and deserialize data.
- Managing lists of dictionaries to store structured data.
