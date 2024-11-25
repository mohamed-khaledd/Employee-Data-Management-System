'''
            Employee class description:
The class has 5 datafields which are Id, Name, Position, Salary and Email
The class has 2 methods:
    First method:  display_data(), this method displays the employee data
    Second method: update_data(), this method updates the employee data 

'''
class Employee:
    def __init__(self, id, name, position, salary, email): # Constructor
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email
    

    def display_data(self):
        return f"Id: {self.id}, Name:{self.name}, Position:{self.position}, Salary:{self.salary}, Email:{self.email},"
    

    def update_data(self, name = None, position = None, salary = None, email = None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary
        if email:
            self.email = email