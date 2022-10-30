class User:
    def __init__(self, name, employee_id, date_hired, salary):
        self.name = name
        self.employee_id = employee_id
        self.data_hired = date_hired
        self.salary = salary

class Manager(User):
    def __init__(self, name, employee_id, date_hired, salary):
        super.__init__(name, employee_id, date_hired, salary)
        self.position = "manager"
        self.employees = []
    
    # Function overloading
    def update_salary(self, years):
        return
        
    
class Driver(User):
    def __init__(self, name, employee_id, date_hired, salary, num_of_routes):
        super.__init__(name, employee_id, date_hired, salary, num_of_routes)
        self.position = "driver"
        self.trainees = []
        self.num_of_routes = num_of_routes
        self.num_of_miles = 0
    
    # Function overloading
    def update_salary(self, years, miles):
        return

class Trainee(Driver):
    def __init__(self, grad_date):
        self.position = "trainee"
        self.num_of_routes = 0
        grad_date = ""
    
    # Function overloading
    def update_salary(self, routes, grad_date):
        return
    