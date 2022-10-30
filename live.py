class User:
    def __init__(self, name, employee_id, date_hired, salary):
        self.name = name
        self.employee_id = employee_id
        self.date_hired = date_hired
        self.salary = salary
    
    def change_name(self, new_name):
        self.name = new_name
        return self.name

class Driver(User):
    def __init__(self, name, employee_id, date_hired, salary):
        super.__init__()
        self.position = "Driver"
        self.trainees = []
    
    def add_route(self):
        self.num_of_routes += 1

driver_1 = Driver('89XJ', 2)
print(driver_1.position)
