# Student Attendance Tracker

## Description
A classroom record management utility that registers students, records daily roll-call attendance (Present / Absent), calculates individual and cohort attendance percentages, and flags students below 75% thresholds.

## Features
- Interactive roll-call attendance logging with fast default selection.
- Detailed date-specific attendance reports showing present and absent rosters.
- Semester ledger compiling individual attendance metrics against total class sessions.
- Automatic eligibility threshold calculation (75% cutoff indicator).
- Persistent JSON data schema preserving rosters and session histories.

## Technologies
- Python 3 (`json`, `datetime`, `os`)

## How to Run
```bash
python main.py
```

## Example
```text
=== Student Attendance Tracker ===
1. Mark Daily Attendance
2. View Attendance by Date
3. View Overall Attendance Ledger & Percentages
4. Register New Student
5. View Student Directory
6. Exit

Choose an option (1-6): 3

=================================================================
ID       | Student Name         | Present  | Total  | %      | Status
=================================================================
S101     | Aarav Sharma         | 18       | 20     |  90.0% | Good ✓
S102     | Diya Patel           | 19       | 20     |  95.0% | Good ✓
S103     | Rohan Verma          | 14       | 20     |  70.0% | Low ⚠️
=================================================================
```

## What I Learned
- Relational mapping across normalized roster keys and date-keyed sessions.
- Computing percentage ratios and condition alerts across dynamic collections.
- Designing high-speed CLI roll call interfaces.
