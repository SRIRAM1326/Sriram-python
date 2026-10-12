import json
import os
from datetime import datetime

FILE_NAME = "attendance.json"

DEFAULT_DATA = {
    "students": [
        {"id": "S101", "name": "Aarav Sharma"},
        {"id": "S102", "name": "Diya Patel"},
        {"id": "S103", "name": "Rohan Verma"},
        {"id": "S104", "name": "Ananya Iyer"}
    ],
    "records": {}
}

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_DATA.copy()
    else:
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA.copy()

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_student(data):
    print("\n--- Register Student ---")
    s_id = input("Student ID (e.g. S105): ").strip().upper()
    if not s_id:
        print("Student ID cannot be empty.")
        return

    for s in data["students"]:
        if s["id"] == s_id:
            print(f"Error: A student with ID '{s_id}' already exists.")
            return

    name = input("Student Full Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    data["students"].append({"id": s_id, "name": name})
    save_data(data)
    print(f"✓ Student '{name}' ({s_id}) registered successfully.")

def list_students(data):
    students = data.get("students", [])
    if not students:
        print("\nNo registered students.")
        return

    print("\n" + "=" * 40)
    print(f"{'#':<4} | {'ID':<10} | {'Student Name'}")
    print("=" * 40)
    for i, s in enumerate(students, 1):
        print(f"{i:<4} | {s['id']:<10} | {s['name']}")
    print("=" * 40)

def mark_attendance(data):
    students = data.get("students", [])
    if not students:
        print("\nNo students registered. Add students first.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    date_str = input(f"\nEnter attendance date (YYYY-MM-DD, default: {today}): ").strip() or today

    if date_str in data["records"]:
        print(f"Notice: Attendance for {date_str} already exists.")
        overwrite = input("Do you want to re-take/overwrite it? (y/n): ").strip().lower()
        if overwrite != "y":
            return

    session_record = {}
    print(f"\n--- Mark Attendance for {date_str} ---")
    print("Enter 'p' for Present, 'a' for Absent (Default is Present):")

    for s in students:
        while True:
            val = input(f"• {s['name']} ({s['id']}) [P/a]: ").strip().lower()
            if val in ("", "p", "present"):
                session_record[s["id"]] = "P"
                break
            elif val in ("a", "absent"):
                session_record[s["id"]] = "A"
                break
            else:
                print("Invalid input. Type 'p' or 'a'.")

    data["records"][date_str] = session_record
    save_data(data)

    p_count = sum(1 for status in session_record.values() if status == "P")
    pct = (p_count / len(students)) * 100
    print(f"\n✓ Attendance saved for {date_str}!")
    print(f"Summary: {p_count}/{len(students)} Present ({pct:.1f}% Attendance)")

def view_date_report(data):
    records = data.get("records", {})
    if not records:
        print("\nNo attendance sessions recorded yet.")
        return

    dates = sorted(list(records.keys()), reverse=True)
    print("\nRecorded Sessions: " + ", ".join(dates[:5]) + ("..." if len(dates) > 5 else ""))
    target_date = input(f"Enter date to inspect (default: {dates[0]}): ").strip() or dates[0]

    if target_date not in records:
        print(f"No records found for {target_date}.")
        return

    session = records[target_date]
    student_map = {s["id"]: s["name"] for s in data["students"]}

    present_list = []
    absent_list = []

    for s_id, status in session.items():
        name = student_map.get(s_id, "Unknown")
        if status == "P":
            present_list.append((s_id, name))
        else:
            absent_list.append((s_id, name))

    total = len(session)
    pct = (len(present_list) / total) * 100 if total > 0 else 0

    print("\n" + "=" * 50)
    print(f"ATTENDANCE REPORT FOR {target_date}")
    print(f"Total: {total} | Present: {len(present_list)} | Absent: {len(absent_list)} ({pct:.1f}%)")
    print("=" * 50)

    print("\n[PRESENT]:")
    for s_id, name in present_list:
        print(f"  ✓ {s_id} - {name}")

    print("\n[ABSENT]:")
    for s_id, name in absent_list:
        print(f"  ✗ {s_id} - {name}")
    print("=" * 50)

def view_student_summary(data):
    students = data.get("students", [])
    records = data.get("records", {})

    if not students or not records:
        print("\nInsufficient data to compute statistics.")
        return

    total_sessions = len(records)
    print("\n" + "=" * 65)
    print(f"{'ID':<8} | {'Student Name':<20} | {'Present':<8} | {'Total':<6} | {'%':<6} | {'Status'}")
    print("=" * 65)

    for s in students:
        s_id = s["id"]
        present_count = 0
        for date_k, session in records.items():
            if session.get(s_id) == "P":
                present_count += 1

        pct = (present_count / total_sessions) * 100 if total_sessions > 0 else 0
        status_label = "Good ✓" if pct >= 75 else "Low ⚠️"

        print(f"{s_id:<8} | {s['name']:<20} | {present_count:<8} | {total_sessions:<6} | {pct:>5.1f}% | {status_label}")
    print("=" * 65)

def main():
    data = load_data()
    while True:
        print("\n=== Student Attendance Tracker ===")
        print("1. Mark Daily Attendance")
        print("2. View Attendance by Date")
        print("3. View Overall Attendance Ledger & Percentages")
        print("4. Register New Student")
        print("5. View Student Directory")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            mark_attendance(data)
        elif choice == "2":
            view_date_report(data)
        elif choice == "3":
            view_student_summary(data)
        elif choice == "4":
            add_student(data)
        elif choice == "5":
            list_students(data)
        elif choice == "6":
            print("Exiting Attendance Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
