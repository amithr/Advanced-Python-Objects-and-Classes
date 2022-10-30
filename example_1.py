import uuid
from datetime import datetime

# Keep track of pets in an animal shelter

# Super Class
# Parent Class
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        # Automatically generate alphanumeric serial code
        self.serial_number = uuid.uuid4()
        self.date_of_entry = datetime.today().strftime('%Y-%m-%d')
        self.medical_conditions = []
    
    def add_medical_condition(self, medical_condition):
        self.medical_conditions.append(medical_condition)
        return self.medical_conditions
    
    def get_serial_number(self):
        return self.serial_number
    
    def get_diet(self):
        return ['rice']
    
    # Static Function
    def get_list_of_species():
        species = ["tiger", "dog", "cat", "octopus", "giraffe"]
        return species
# Sub Class
# Child Class   
class Tiger(Pet):
    def __init__(self, name, type_of_tiger, volume_of_meat):
        species = "tiger"
        super().__init__(name, species)
        self.type_of_tiger = type_of_tiger
        self.volume_of_meat = volume_of_meat
    
    # Function Overloading
    def get_diet(self, age):
        if age > 2:
            return ['rice', 'meat']
        else:
            return ['milk']
    
tiger_1 = Tiger("Eddie", "Siberia", "20")
print("Species:", tiger_1.species)
print("Type of Tiger", tiger_1.type_of_tiger)
print("Serial Number", tiger_1.serial_number)
tiger_1.add_medical_condition('covid')
print("Diet: ", tiger_1.get_diet(1))
    

