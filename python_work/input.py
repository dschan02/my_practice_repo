name = input("Enter your name: ")
print("Hello,", name)

# num = input("Enter a number: ")

# need try-catch block to if casting to int immediately, just incase a string is entered. 
try: 
    num = int(input("Enter a number: "))
    print("you entered", num)
    double = num*2
    print("doubled:", double)
except:
    print("You did not enter a valid number.")

'''
#inputs are read as strings, so you need to cast if you want to treat as any other data type
double = num * 2
print("doubled:", double)

num = int(num)
double = num * 2
print("doubled:", double)
'''

# opening up file
with open("movies.txt") as file:    # stores in variable "file"
    for line in file:   #iterate through each line
        print(line.strip())   #.strip removes the invis new line character in the .txt file, since it has them for each new line made
        
with open("heights.txt") as file:
    for line in file:
        info = line.strip().split()     #.split() splits based on all white space in a line
                                        #stores as list of strings with each white space. You can change the split delimator. 
        info[2] = int(info[2])          #converts string to int at index place 2
        print(info)

# Excersize
'''
prompt user for a file name to read in, then print each line with the line number before it
ex: 
movies.txt
1. The Wizard of Oz
2. Citizen Kane
.... continue
'''
file_name = input("Enter a file name with the ending extension: ")
line_num = 1
with open(file_name) as file:
    for line in file:
        print(f"{line_num}. {line.strip()}")
        line_num += 1
