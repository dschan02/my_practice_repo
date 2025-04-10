# list (known as array literally everywhere else)
cart=["apples", "bananas", "cherries"]
print(cart)

cart.append("donut")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
if "cherry" in cart:
    cart.remove("cherry")
print(cart)

cart.pop(2)     # removes element number 2 ("donut") from list
print(cart)
cart.pop()      # list acts like a stack in python, so you can pop LILO (last in last out)
print(cart)

#reverse sorted order
cart.reverse()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

# creating new list from existing list
fruit_basket = cart[3:]
print(fruit_basket)
print(cart)

squares=[]
for i in range(1,11):
    squares.append(i*i)
print(squares)

#list comprehension (USE THIS ITS FASTER)
# list_name = [(expression) for ? in range(?,?)]
squares = [i*i for i in range (1,11)]
print(squares)
#can add optional if clause if boolean clause
# list_name = [(expression) for ? in range(?,?) if (condition) == (condition)]

print(cart)
b_items = [item for item in cart if item.startswith("b")]
print(b_items)

# when reading in from file, it reads in from string
# here is list comprehension to easily convert it to ints
lst=['1', '10', '190']
num_lst=[int(x) for x in lst]
print(num_lst)

inventory=[]
# inventory[0] = 1      # this is invalid, as the list is currently empty. Must use .append()
inventory = [0]*len(cart)   # fills list with default value in bracket (0 in this case)
print(inventory)
inventory[0] = 1
print(inventory)

# TOPIC CHANGE:
# sets
'''
sets do not print duplicates. recall discrete structures lol

when you add an element in set, the order it is not stored is NOT
guarenteed. can store in memeory in whatever order
'''
#empty=set{} ????????
nums_set={1,1,3,4}
nums_set.add(5)
nums_set.add(10)
print(nums_set)
lst=[1,2,2,3,3,4]
unique=set(lst)
print(unique)
unique=list(unique)
print(unique)

st={4,10,3,7,8}
print(st)
sorted(st)
print(st)

# TOPIC CHANGE:
# dictionary
'''
you have a key that acts as an index place to find value in dictonary
ex: key PA value "Pennsylvania"

also used for frequency counts
'''
fav_snacks={}
fav_snacks= {
    "kathleen":"tortilla chips",
    "ava":"chex mix",
    "emily":"buffalo chicken dip",
    "wade":"popcorn"
}
print(fav_snacks)
fav_snacks["lucas"] = "chocolate"
print(fav_snacks)

for key in fav_snacks:
    print(f"{key}'s favorite snack is {fav_snacks[key]}")
    print(key+"'s" + " favorite snack is " + fav_snacks[key])

for key, value in fav_snacks.items():
    print(key, value)

if "Bob" in fav_snacks:
    print("Bob's fav snack is" + fav_snacks["Bob"])
else:
    fav_snacks["Bob"]="chips"

keys= fav_snacks.keys()     #keys are stored as a set, no duplicates. 
values=fav_snacks.values()
print(sorted(keys))
print(sorted(values))

fav_snacks['Alice'] = ["chips","nuts"]
print(fav_snacks)