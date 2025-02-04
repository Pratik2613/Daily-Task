employees = []  # List to store employee data

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    position = input("Enter Position: ")
    salary = float(input("Enter Salary: "))
    employees.append({"ID": emp_id, "Name": name, "Department": department, "Position": position, "Salary": salary})
    print("Employee added successfully!\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    for emp in employees:
        if emp["ID"] == emp_id:
            print("Current Data: ", emp)
            emp["Name"] = input("Enter new Name (or press Enter to keep current): ") or emp["Name"]
            emp["Department"] = input("Enter new Department (or press Enter to keep current): ") or emp["Department"]
            emp["Position"] = input("Enter new Position (or press Enter to keep current): ") or emp["Position"]
            new_salary = input("Enter new Salary (or press Enter to keep current): ")
            emp["Salary"] = float(new_salary) if new_salary else emp["Salary"]
            print("Employee details updated successfully!\n")
            return
    print("Employee not found!\n")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print("Employee removed successfully!\n")
            return
    print("Employee not found!\n")

def view_employees():
    if not employees:
        print("No employees to display.\n")
    else:
        print("\nEmployee List:")
        for emp in employees:
            print(emp)
        print()

def main():
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. View Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            update_employee()
        elif choice == '3':
            remove_employee()
        elif choice == '4':
            view_employees()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
