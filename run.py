#!/usr/bin/env python3
"""
Python Mini Projects - Master Launcher
Central interactive CLI dashboard to search, inspect, and execute any of the 60 projects.
"""

import os
import sys
import subprocess
from pathlib import Path

# ANSI Color codes for styled terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"

# Project metadata catalog
BATCHES = {
    1: ("Batch 1: Basics & Fundamentals", 1, 10),
    2: ("Batch 2: Strings & Logic", 11, 20),
    3: ("Batch 3: Tools & Utilities", 21, 30),
    4: ("Batch 4: Intermediate Systems", 31, 40),
    5: ("Batch 5: Media, Security & Productivity", 41, 60),
}

def get_project_list():
    root = Path(__file__).parent
    dirs = [d for d in root.iterdir() if d.is_dir() and d.name[:2].isdigit() and "_" in d.name]
    dirs.sort(key=lambda d: int(d.name.split("_")[0]))
    return dirs

def format_title(dir_name):
    parts = dir_name.split("_")
    num = parts[0]
    name = " ".join(parts[1:]).title()
    return num, name

def get_project_description(project_dir):
    readme = project_dir / "README.md"
    if readme.exists():
        try:
            with open(readme, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.strip().lower() == "## description" and i + 1 < len(lines):
                        for j in range(i + 1, min(i + 5, len(lines))):
                            desc = lines[j].strip()
                            if desc and not desc.startswith("#"):
                                return desc
        except Exception:
            pass
    return "Standalone Python application."

def run_project(project_dir):
    main_file = project_dir / "main.py"
    if not main_file.exists():
        print(f"{YELLOW}Warning: {main_file} not found.{RESET}")
        return

    num, title = format_title(project_dir.name)
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{GREEN}{BOLD}▶ Launching: [{num}] {title}{RESET}")
    print(f"{DIM}Directory: {project_dir.name}/{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")

    try:
        # Run subprocess with cwd set to the project directory
        subprocess.run([sys.executable, str(main_file.name)], cwd=str(project_dir))
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Project interrupted. Returning to menu...{RESET}")
    except Exception as e:
        print(f"\n{YELLOW}Execution error: {e}{RESET}")

    print(f"\n{DIM}Finished running [{num}] {title}.{RESET}")
    input(f"{DIM}Press Enter to return to main menu...{RESET}")

def print_header():
    print(f"\n{CYAN}{'='*65}{RESET}")
    print(f"{BOLD}{GREEN}      🚀 PYTHON MINI PROJECTS COLLECTION (60 APPS) 🚀{RESET}")
    print(f"{CYAN}{'='*65}{RESET}")

def display_batch(batch_num, projects):
    if batch_num not in BATCHES:
        return
    name, start, end = BATCHES[batch_num]
    print(f"\n{BOLD}{YELLOW}--- {name} ---{RESET}")
    for p in projects:
        num_int = int(p.name.split("_")[0])
        if start <= num_int <= end:
            num, title = format_title(p.name)
            desc = get_project_description(p)
            if len(desc) > 50:
                desc = desc[:47] + "..."
            print(f"  {GREEN}{num:>2}.{RESET} {BOLD}{title:<26}{RESET} {DIM}│ {desc}{RESET}")

def display_all(projects):
    for b in range(1, 6):
        display_batch(b, projects)

def search_projects(projects):
    term = input(f"\n{CYAN}Enter search term (e.g. 'qr', 'password', 'calc', 'file'): {RESET}").strip().lower()
    if not term:
        return

    matches = []
    for p in projects:
        num, title = format_title(p.name)
        desc = get_project_description(p)
        if term in title.lower() or term in desc.lower() or term in p.name.lower():
            matches.append((num, title, desc, p))

    if not matches:
        print(f"{YELLOW}No projects matching '{term}'.{RESET}")
        return

    print(f"\n{BOLD}{GREEN}Found {len(matches)} matching project(s):{RESET}")
    for num, title, desc, p in matches:
        print(f"  {GREEN}[{num}]{RESET} {BOLD}{title:<26}{RESET} {DIM}│ {desc}{RESET}")

    choice = input(f"\n{CYAN}Enter project number to run (or press Enter to return): {RESET}").strip()
    if choice.isdigit():
        target_num = int(choice)
        for num, title, desc, p in matches:
            if int(num) == target_num:
                run_project(p)
                return

def run_tests():
    print(f"\n{CYAN}--- Running Automated Unit Test Suite (pytest) ---{RESET}\n")
    try:
        subprocess.run([sys.executable, "-m", "pytest", "tests/"])
    except Exception as e:
        print(f"{YELLOW}Error executing tests: {e}{RESET}")
    input(f"\n{DIM}Press Enter to return to main menu...{RESET}")

def main():
    projects = get_project_list()
    project_map = {int(p.name.split("_")[0]): p for p in projects}

    while True:
        print_header()
        print(f"{BOLD}Commands & Options:{RESET}")
        print(f"  • {GREEN}1 - 60{RESET}    : Run any project directly by number")
        print(f"  • {CYAN}b1 - b5{RESET}   : View projects in Batch 1 through Batch 5")
        print(f"  • {CYAN}all{RESET}       : List all 60 projects with descriptions")
        print(f"  • {CYAN}search{RESET}    : Search projects by name or keyword")
        print(f"  • {MAGENTA}test{RESET}      : Run automated unit test suite (pytest)")
        print(f"  • {YELLOW}exit / q{RESET}  : Quit launcher")

        cmd = input(f"\n{BOLD}{CYAN}Select an option or project # > {RESET}").strip().lower()

        if cmd in ("q", "exit", "quit"):
            print(f"\n{GREEN}Happy Coding! Keep building great Python apps. 💻{RESET}\n")
            break
        elif cmd.isdigit():
            num = int(cmd)
            if num in project_map:
                run_project(project_map[num])
            else:
                print(f"{YELLOW}Project #{num} not found. Choose between 1 and 60.{RESET}")
        elif cmd == "all":
            display_all(projects)
            input(f"\n{DIM}Press Enter to return to menu...{RESET}")
        elif cmd.startswith("b") and cmd[1:].isdigit():
            b_num = int(cmd[1:])
            if 1 <= b_num <= 5:
                display_batch(b_num, projects)
                input(f"\n{DIM}Press Enter to return to menu...{RESET}")
            else:
                print(f"{YELLOW}Invalid batch. Choose b1 to b5.{RESET}")
        elif cmd in ("s", "search"):
            search_projects(projects)
        elif cmd in ("t", "test", "tests"):
            run_tests()
        else:
            print(f"{YELLOW}Unknown command '{cmd}'. Enter a number (1-60), 'search', or 'exit'.{RESET}")

if __name__ == "__main__":
    main()
