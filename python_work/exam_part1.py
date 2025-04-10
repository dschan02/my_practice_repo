# Demetrius Schank
# Exam 1
# Date: 1/30/2025

def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    if len(s) < 2:
        return s*3
    else:
        return (s[0] + s[1])*3 
    


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The first element should become the last.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    tmp_lst = []
    for i in range(len(lst)):
        if i == len(lst) -1:        # for last element in new list
            tmp_lst.append(lst[0])
        else:
            tmp_lst.append(lst[i+1])    #for everything else
    return tmp_lst
    
    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    return len([char for char in s if char.isdigit()])  #returns the length of a list that is made up of all the digits in a string
    

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    min_index = 0
    min = lst[min_index]
    for index, value in enumerate(lst):
        if value < min:
            min_index = index
            min = value
    lst[min_index] = lst[0]
    lst[0] = min
    return lst
    

def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    class_grades = {}
    with open("grades.txt") as file:
        for line in file:
            line_info = line.strip().split()    #splits line into lst
            first_and_last = f"{line_info[0]} {line_info[1]}"   #first_and_last now one string
            grade_num = int(line_info[2])
            class_grades[first_and_last] = grade_num
    return class_grades
    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))
print('repeat_start("e") expected: eee')
print('repeat_start("e") actual:', repeat_start("e"))

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))
print('shift_left([5, 10, 15, 20, 25, 30]) expected: [10, 15, 20, 25, 30, 5]')
print('shift_left([5, 10, 15, 20, 25, 30]) actual:', shift_left([5, 10, 15, 20, 25, 30]))

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))
print('count_digits("Call 1-800-999-9999!") expected: 11')
print('count_digits("Call 1-800-999-9999!") actual:', count_digits("Call 1-800-999-9999!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print(build_grades_dict())
