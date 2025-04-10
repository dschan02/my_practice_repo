print("Hello World!")

# this is a single line with a comment

'''
this type can use lots
of lines for a comment
'''

# line 1
# line 2
# line 3
# Do ctrl + '/' to comment multiple lines that are highlighted.

# Variables
x = 10
x = "hello"
x = [1,2,3]
print(x)


x = 100
y = 10
result = x/y
result = int(result)    # convert to integer
print(result)
# can also do just result = int(x/y)

x = 105
result = x // y # this divides and takes the floor (prints int and removes any remainder in decimal)
print(result)

#EXPONENTS, MIN/MAX
min_val = min(1,10,50)
print(min_val)
raised = pow(2,3) # 2^3 = 8
print(raised)
raised = 2**3     # Also 2^3 = 8 
print(raised)

# if statements
x = -1
if x < 0: 
    print("x is negative")
elif x > 0:
    print("x is positive")
else: 
    print("x is 0")

#Compound conditional statement
start = 10
end = 100 

if x >= start and x <= end:
    print("x is within range")
    
if x<start and x>end:
    print("x is not within range")

# 1/16/2025

counter = 0
while counter<5:
    print(counter)
    counter+=1

for i in range (1,5):  # for loop, if you want to count by dif number then 1 add a third parameter
    print(i, end = " ")
print() # new line

# simple lists
lst = [2,4,6,8]
for i in range(len(lst)):   #len(lst) is the length of our list named lst
    print(i, lst[i], end = " ")
print()

for val in lst: # alternative way of going through entire list
    print(val)

# if you like list values stored in variables do this loop
for index, value in enumerate(lst):
    print(index, value, end= " ")
print()

#FUNCTIONS
def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("hello " +name)   #concat operator is +name for strings
    print("Hello", name)    #prints same thing
hello("demetrius")

def hello2(name="Bob"): #parameter has default value
    print("Hello " +name)
hello2("jane")

#slicing strings
course = "Platform Computing"
#plat = course[start:end] goes up to but not including end index space
plat = course[:8]
print(plat)
comp = course[9:]
print(comp)

'''
string method string.count("substring") counts the amount of times a substring appears 
in a string. 
string.lower()
string.upper()
string.strip() strips new line character from the end of each line
string.split('delimater') splits string based on delimeter defined. do .split() to split for whitespace. 
                            this stores in a list each split substring. 
'''