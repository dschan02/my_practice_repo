from student import Student

student1 = Student("Demetrius", "Schank", 1111111)

print(student1)

Student.greeting(student1)

Student.take_exam(student1)
Student.take_exam(student1)

curr_energy = Student.get_energy_level(student1)
print(curr_energy)
