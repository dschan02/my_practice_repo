# Demetrius Schank
# tester for car.py
# reads in file cars.txt

from car import Car     #imports Car function from car.py

'''
Needed for below
(string_name).strip() removes new line character
(string_name).split() splits the string based on white 
    space character, and stores in a user-named list.
    you can define a new delimiter in the (), like (",")
    to split based on comma.
(string_name).strip().split() does both in one line
'''

car_lst = []    #store objects created in for loop in list
with open("cars.txt") as file:  # file is variable name
    for line in file:
        txt_info = line.strip().split() #txt_info is list
        txt_info[2] = int(txt_info[2])  # gas_tank to int
        txt_info[3] = int(txt_info[3])  # odometer to int
        car_object = Car(txt_info[0], txt_info[1], txt_info[2], txt_info[3])
        car_lst.append(car_object)

#first car testings
print(car_lst[0])
Car.drive(car_lst[0])
print(Car.get_gas_tank(car_lst[0]))
print(Car.get_odometer(car_lst[0]))

#second car testings
print(car_lst[1])
Car.drive(car_lst[1])
print(Car.get_gas_tank(car_lst[1]))
print(Car.get_odometer(car_lst[1]))