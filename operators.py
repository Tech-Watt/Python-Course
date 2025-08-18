"""
Python divides the operators in the following groups:
Arithmetic operators
Assignment operators
Comparison operators
Logical operators

Identity operators
Membership operators
Bitwise operators
"""

# Arithmetic operators
# Arithmetic operators are used with numeric values to perform common mathematical operations
x = 78
y = 2

# addition
addi_result = x + y 

# subtraction
sub_result = x - y

# Division
div_result = x / y

# Multiplication
mul_result = x * y

# Modulus
mod_result = x % y 

# Exponentiation
expo_result = x ** y 

# 	Floor division
floor_div = x//y

# -------------------------------------------------------------------------------------------------------------------

# Assignment Operators
# Assignment operators are used to assign values to variables:
a = 5 
a += 2
print(a)

b = 5 
b += 2
print(b)

c = 5 
c *= 2
print(c)

d = 5 
d **= 2
print(d)


e = 5 
e /= 2
print(e)

f = 5 
f //= 2
print(f)


# Comparison Operators
# Comparison operators are used to compare two values:

t = 7
v = 7
# Equal
equal_check = t == v
print(equal_check)

# Not Equal
not_equal_check = t != v
print(not_equal_check)

# Greater than
great_result = v > t
print(great_result)

# Less Than
less_result = v < t
print(less_result)

# Greater than or equal to 
great_equal = t >= v
print(great_equal)

# Less than or equal to 
less_equal = t <= v
print(less_equal)


# Logical Operators
# Logical operators are used to combine conditional statements:
check_and = t < 5 and v > 6
print(check_and)

check_or = t < 5 or v > 6
print(check_or)


not_result = not(t < 5 and t < 10)
print(not_result)