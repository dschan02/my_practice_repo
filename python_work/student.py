# 1/23/2025 in class activity, student.py. Intructions on blackboard.

class Student:
    def __init__(self, fname, lname, id, energy_level = 10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level
    
    def __str__(self):
        return f"{self.lname}:{self.id}"
    
    def greeting(self):
        print(f"Hello! My name is {self.fname} {self.lname}!")
    
    def take_exam(self):
        self.energy_level -= 1

    def get_energy_level(self):
        return self.energy_level
    