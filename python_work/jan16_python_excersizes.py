# Loop excersises
# Write a for loop to print all numbers from 1 to 20 that are divisible by 3.
for i in range (1,21):
    if i%3 == 0:
        print(i, end=" ")
print()        

#Write a while loop that calculates the sum of all even numbers between 1 and 50 (inclusive). Print the result.
counter = 2
sum = 0
while counter <= 50:
    sum += counter
    counter+=2
print(sum)

# You are given a list of numbers:
# numbers = [5, 8, 2, 15, 10, 3, 7]
# 1. Use a for loop to print the numbers greater than 5.
numbers = [5, 8, 2, 15, 10, 3, 7]
for num in numbers:
    if num>5:
        print(num, end= " ")
print()


#Function excersize  1
'''
Write a function called swap that takes a list of elements and swaps the first and last elements. For
example, if the input to the function is [0,3,8,4,5] the swapped list would be [5,3,8,4,0]. You do not need
to return the list. Test the function like this:
lst=[0,3,8,4,5]
swap(lst)
print(lst)
Test your function with another list to confirm it works on all input.
'''
#def swap(lst):
#     tmp = lst[0]
#     for i in range (len(lst)-1):
#         lst[i] = lst2[len(lst2)-1-i]
# lst=[0,3,8,4,5]
# swap(lst)
# print(lst)


