import uuid
from datetime import datetime

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.serial_number = uuid.uuid4().hex
        self.date_of_entry = datetime.today().strftime('%Y-%m-%d')
        self.species = species
        self.medical_conditions = []
    
    def add_medical_condition(self, medical_condition):
        self.medical_conditions.append(medical_condition)
        return self.medical_conditions
    
    def remove_medical_condition(self, medical_condition):
        self.medical_conditions.remove(medical_condition)
        return self.medical_conditions
    
    def change_name(self, new_name):
        self.name = new_name
    
    # Static Function (used as a tool or utility)
    def get_list_of_species():
        species = ["tiger", "dog", "cat", "octopus", "giraffe"]
        return species


pet_1 = Pet("Alberto", "tiger")
pet_2 = Pet("Jimmy", "giraffe")
pets = [pet_1, pet_2]
    

