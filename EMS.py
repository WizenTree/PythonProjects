#Employee management system 
#step 1 - Making a dictionary to store data 
employees ={
    101: {"name": "John Doe", "age":20, "department": "HR", "salary": 50000},
    102: {"name": "Ravi", "age":23, "department": "Finance", "salary": 60000},
    103: {"name": "Vishal", "age":19, "department": "IT", "salary": 55000},
}

#step 2 - making a Function to display the main menu
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID:"))
        if emp_id in employees:
            print("Employee Id already exists. Please enter a unique ID.")
            return
        name = input("Enter Employee Name:")
        age = int(input("Enter Employee Age:"))
        department =input("Enter Employee Department:")
        salary = int(input("Enter Employee salary:"))

        employees[emp_id]={
            'name':name,
            'age':age,
            'department':department,
            'salary':salary,
        }
        print(f"Employee {name} added sucessfully.")
    except ValueError:
        print("Invalid input. PLease enter correct values.")

#step 4 Function to view all Employees in the dictionary
def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print("\nEmployee Details:")
        print(f"{'ID':<5}{'Name':<20}{'Age':<5}{'Department':<20}{'Salary':<10}")
        print("-"*50)
        for emp_id, details in employees.items():
            print(f"{emp_id:<5}{details['name']:<20}{details['age']:<5}{details['department']:<20}{details['salary']:<10}")

#step 5 Search for Employe by ID
def search_employee():
    try:
        emp_id = int(input("Enter Empolyee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print(f"Empolyee Found: {details}")
        else:
            print("Employee not Found.")
    except ValueError:
        print("Invalid input. Please enter a valid Employee ID.")

# step 6 RUN the Program 
main_menu()