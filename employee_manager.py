import csv
from employee import Employee


#            EmployeeManager class description:
# The class has 2 datafields which are file_name, employees "A list of employee"
# The class has 7 methods:
#   First method: load_employees(), this method loads the employees "read" from the csv file. 
#   Second method: store_employees(), this method store the employees "write" in the csv file. 
#   Third method: add_employees(), this method adds an employee in the csv file.
#   Fourth method: delete_employees(), this method deletes an employee from the csv file.
#   Fifth method: update_employees(), this method updates the data of an employee in the csv file.
#   Sixth method: search_employees(), this method searches for an employee in the csv file.
#   Seventh method: list_employees(), this method lists all the employees in the csv file.



class EmployeeManager:
    def __init__(self, file_name = "employees.csv"): # Constructor
        self.file_name = file_name
        self.employees = self.load_employees() # loading existing employee data from the csv file.
    

    def load_employees(self):
        employees = []   # an empty list to store employees
        try:
            with open(self.file_name, mode = 'r') as file:  # openning the csv file in read mode
                reader = csv.DictReader(file)   # reading the csv file as a dictionary
                for row in reader:
                    employee = Employee(row['id'], row['name'], row['position'], row['salary'], row['email'])
                    employees.append(employee)
        except:
            print(f"The file {self.file_name} was not found")
        return employees
    


    def store_employees(self):
        with open(self.file_name , mode = 'w', newline= '') as file: # openning the csv file in write mode
            writer = csv.DictWriter(file, fieldnames = ['id', 'name', 'position', 'salary', 'email'])
            writer.writeheader()    # writing the header row to the csv file.
            for emp in self.employees:
                writer.writerow(emp.__dict__)  # emp.__dict__ converts the Employee object into a dictionary
    


    def add_employees(self, id, name, position, salary, email):
        employee = Employee(id, name, position, salary, email)
        self.employees.append(employee)
        self.store_employees()
    


    def delete_employees(self, id):
        new_emp = []   # a new list to hold the remaining employees
        for emp in self.employees:
            if emp.id != id:
                new_emp.append(emp)
        self.employees = new_emp    # updating the employees list to the new list
        self.store_employees() 
    


    def update_employees(self, id, name = None, position = None, salary = None, email = None):
        for emp in self.employees:
            if emp.id == id:
                emp.update_data(name, position, salary, email)
                self.store_employees()
                return True
        return False
    


    def search_employees(self, id):
        for emp in self.employees:
            if emp.id == id:
                return emp
        return None
    


    def list_employees(self):
        return self.employees
