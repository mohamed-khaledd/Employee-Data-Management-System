import re
from employee_manager import EmployeeManager

def validate_name(name):
    if type(name) is str and all(char.isalpha() or char.isspace() for char in name):  # checking if the name contains only alphabets and spaces
        return name
    else:
        raise ValueError("Invalid name.")

def validate_salary(salary):
    if type(salary) in [int, float] and salary > 0:  # checking if the salary is numeric and > 0 or not
        return salary
    else:
        raise ValueError("Invalid salary.")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return email
    else:
        raise ValueError("Invalid email format.")

def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Data Management System")
        print(" For adding an Employee enter 1.")
        print(" For deleting an Employee enter 2.")
        print(" For searching for an Employee enter 3.")
        print(" For updating an Employee enter 4.")
        print(" For Viewing all Employees enter 5.")
        print(" For exiting the system enter 6.")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter id: ")
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = input("Enter salary: ")
            email = input("Enter email: ")
            try:
                name = validate_name(name)
                try: 
                    salary = float(salary) # Attempt to convert to float 
                except ValueError:
                     raise ValueError("Invalid salary.") 
                salary = validate_salary(salary)  
                email = validate_email(email)
                manager.add_employee(id, name, position, salary, email)
            except ValueError as e:
                print(e)
            
        elif choice == '2':
            id = input("Enter the id of the employee you want to delete: ")
            manager.delete_employee(id)

        elif choice == '3':
            id = input("Enter the id of the employee you want to search for: ")
            emp = manager.search_employee(id)
            if emp:
                print(emp.display_data())
            else:
                print("Employee not found.")

        elif choice == '4':
            id = input("Enter the id of the employee you want to update: ")
            name = input("Enter the new Name (or leave blank to keep the current name): ")
            position = input("Enter the new Position (or leave blank to keep the current position): ")
            salary = input("Enter the new Salary (or leave blank to keep the current salary): ")
            email = input("Enter the new Email (or leave blank to keep the current email): ")
            try:
                if name:
                    name = validate_name(name)

                if salary:
                    try: 
                        salary = float(salary) # Attempt to convert to float 
                    except ValueError:
                        raise ValueError("Invalid salary.") 
                    salary = validate_salary(salary) 

                if email:
                    email = validate_email(email)
                    
                manager.update_employee(id, name, position, salary, email)
            except ValueError as e:
                print(e)

        elif choice == '5':
            for emp in manager.list_employees():
                print(emp.display_data())

        elif choice == '6':
            break

        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()
