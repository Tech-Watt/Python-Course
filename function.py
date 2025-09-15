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