'''
Functions in python is a block of code which only 
runs when it is called. You can pass data, known as parameters, 
into a function. A function can return data as a result.
'''

# Creating a function
# def Addition():
#     a = 10
#     b = 20
#     c = a + b
#     print("Addition is:", c)

def Addition(a,b):
    c = a + b
    print("Addition is:", c)


# Calling a function
Addition(10, 20)#positional arguments
Addition(b=30, a=40)#keyword arguments


# Function with return keyword
def Subtraction(a, b):
    c = a - b
    return c
    

result = Subtraction(a=50, b=20)
print("Subtraction is:", result)


def Addition (a,b):
    return a + b
    

add_result = Addition (b=10 , a=40)
print("Addition is:", add_result)

def Subtraction (d,b):
    return d - b
print("Subtraction is:", Subtraction(50, 20))


# Lambda Function
# A lambda function is a small anonymous function.
# It can take any number of arguments, but can only 
# have one expression.

# Syntax: lambda arguments: expression

# Example
add = lambda a,b: a + b
print("Addition is:", add(a=10, b=20))


sub = lambda a,b,c: a - b - c
print("Subtraction is:", sub(a=50, b=20, c=10))


multi = lambda d,e,f,g: d*e*f*g
print("Multiplication is:" , multi(70,40,21,43))




# Map Function
# The map() function applies a given function to all 
# the items in an iterable (list, tuple etc.) and 
# returns a map object (an iterator).

# Syntax: map(function, iterable)

scores = (55,65,76)
mark = 10

# def add_marks(score):
#     return score + mark

# add_m = lambda score: score + mark

result = map(lambda x: x + mark, scores)
print(result) #map object
# print(list(result)) #converting map object to list
# print(tuple(result)) #converting map object to tuple
print(set(result)) #converting map object to set


# Example 2 solved by Gold
# numbers = {5,10,15,20,25}
# subtract_two = lambda x: x - 2
# results = map(subtract_two, numbers)
# results_list = list(results)
# print(results_list) 


# Filter Function
# The filter() function constructs an iterator from 
# elements of an iterable for which a function returns true.
# Syntax: filter(function, iterable)
ages = [5,12,17,18,24,32]

check_age = lambda age: age >= 18

adults = filter(check_age, ages)
print(adults) #filter object
print(list(adults)) #converting filter object to list


# Reduce Function
# The reduce() function is used to apply a particular
# function passed in its argument to all of the list
# elements mentioned in the sequence passed along.
# This function is defined in "functools" module.
# Syntax: reduce(function, iterable)


