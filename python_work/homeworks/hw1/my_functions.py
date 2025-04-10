# Demetrius Schank
# Due 1/21/25
# HW1 My functions portion
def add_first_and_last(lst):
    '''
    this function adds the first and last elements of a list and returns the sum, assuming the
    list is filled with numerical elements. if the list has only 1 element, it will add the same
    element twice.
    '''
    return (lst[0] + lst[-1])

def introduction_generator(name="John", age="30", fav_color="red"):
    '''
    this function generates a sentence you can use to introduce your name, 
    age, and your favorite color for icebreakers. it returns a string.
    the function also has default values. 
    '''
    sentence = "Hi! My name is " + name + ", I am " + str(age) + " years old and my favorite color is " + fav_color + "."
    return sentence

#Test Statements.

print("First function test statements:")
nums = [1,2,5,1,5,8,9]
print(add_first_and_last(nums))
nums = [2,4]
print(add_first_and_last(nums))
nums = [100]
print(add_first_and_last(nums))
print()

print("Second function test statements:")
print(introduction_generator())
my_name = "Demetrius"
my_age = 21
my_color = "green"
print(introduction_generator(my_name, my_age, my_color))
print(introduction_generator("Stacy", 12, "rainbow unicorn sparkle"))
print()