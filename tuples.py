'''
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
'''

names = ("Alice", "Bob", "Charlie",'Felix')
# names = tuple(('Alice', 'Bob', 'Charlie', 'Charlie'))
print(type(names))

numberofitems = len(names)
print(numberofitems)



# Accessing Tuple Items
first_item = names[0]
print(first_item)
second_item = names[1]
print(second_item)
last_item = names[-1]
print(last_item)

# Slicing Tuples
first_two = names[0:2]
print(first_two)

# Concatenating Tuples
new_names = names + ("David", "Eva")
tuple_one = (4,5)
tuple_two = (6,7)
joint_tuple = tuple_one + tuple_two
print(f'Joint Tuple: {joint_tuple}')
print(new_names)

# Repeating Tuples
repeated_names = names * 2
print(repeated_names)

# Checking Membership
is_bob_present = "Bob" in names
print(is_bob_present)

if 'Bobs' in names:
    print("Bob is present in the tuple.")

else:
    print("Bob is not present in the tuple.")


# changing tuple values
# Tuples are immutable, so you cannot change their values directly.
ages = (25, 30, 35)
# ages[0] = 26  # This will raise a TypeError
ages_list = list(ages)  # Convert to list
ages_list[0] = 26  # Now this works
ages = tuple(ages_list)  # Convert back to tuple
print(ages)

# Updating Tuple Values
'''
But, in Python, we are also allowed to extract the values back 
into variables. This is called "unpacking":
'''
x, y, z = ages
print(x)
print(y)
print(z)



fruits = ('Apple', 'Banana', 'Cherry','Mango','Grapes')
a,b, *rest = fruits
print(a)
print(b)
print(rest) #['Cherry', 'Mango', 'Grapes'] the rest of the fruits is a list 


# Looping through a tuple
for fruit in fruits:
    print(fruit)


# Tuple Methods
# count()
print(f"Count of 'Apple': {fruits.count('Apple')}")

# index()
print(f"Index of 'Mango': {fruits.index('Mango')}")