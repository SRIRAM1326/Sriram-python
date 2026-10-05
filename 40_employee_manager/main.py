class Employee:
    def __init__(self, emp_id, name, department, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = float(salary)
        
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary:.2f}")

def add_employee(employees):
    emp_id = input("\nEmployee ID: ").strip()
    if any(e.emp_id == emp_id for e in employees):
        print("Employee ID already exists.")
        return
        
    name = input("Name: ").strip()
    department = input("Department: ").strip()
    position = input("Position: ").strip()
    
    try:
        salary = float(input("Salary: "))
        new_emp = Employee(emp_id, name, department, position, salary)
        employees.append(new_emp)
        print("\nEmployee added successfully.")
    except ValueError:
        print("Invalid salary input.")

def view_employees(employees):
    if not employees:
        print("\nNo employees found.")
        return
    print("\n=== Employee List ===")
    for e in employees:
        print(f"{e.emp_id} | {e.name} | {e.department} | {e.position}")

def search_employee(employees):
    query = input("\nSearch term (ID or Name): ").strip().lower()
    found = False
    for e in employees:
        if query in e.emp_id.lower() or query in e.name.lower():
            print("\n--- Match Found ---")
            e.display()
            found = True
    if not found:
        print("No matches found.")

def update_employee(employees):
    emp_id = input("\nEnter Employee ID to update: ").strip()
    for e in employees:
        if e.emp_id == emp_id:
            print("Leave blank to keep current value.")
            name = input(f"Name ({e.name}): ").strip()
            department = input(f"Department ({e.department}): ").strip()
            position = input(f"Position ({e.position}): ").strip()
            salary_input = input(f"Salary ({e.salary}): ").strip()
            
            if name: e.name = name
            if department: e.department = department
            if position: e.position = position
            if salary_input:
                try:
                    e.salary = float(salary_input)
                except ValueError:
                    print("Invalid salary ignored.")
                    
            print("\nEmployee updated successfully.")
            return
    print("Employee not found.")

def delete_employee(employees):
    emp_id = input("\nEnter Employee ID to delete: ").strip()
    for i, e in enumerate(employees):
        if e.emp_id == emp_id:
            employees.pop(i)
            print("\nEmployee deleted successfully.")
            return
    print("Employee not found.")

def calculate_average_salary(employees):
    if not employees:
        print("\nNo employees to calculate average.")
        return
    total_salary = sum(e.salary for e in employees)
    avg_salary = total_salary / len(employees)
    print(f"\nAverage Salary: {avg_salary:.2f}")

def main():
    employees = []
    
    while True:
        print("\n=== Employee Manager ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Average Salary")
        print("7. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            update_employee(employees)
        elif choice == '5':
            delete_employee(employees)
        elif choice == '6':
            calculate_average_salary(employees)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
