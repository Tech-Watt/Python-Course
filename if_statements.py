'''
Conditional statements allow a program to execute different code 
blocks based on whether a given condition is true or false. They are fundamental 
in programming for creating dynamic and responsive applications. 

Core Concepts:
Condition:
A boolean expression that evaluates to either true or false. 
if-else statement:

The most basic structure. If the condition is true, the "if" block is executed; 
otherwise, the "else" block (if present) is executed. 

Nested conditionals:
Using conditional statements inside other conditional statements to create 
more complex logic. 
'''

number = 3
age = 5

if number > age:
    print('The number is greater than age')

elif number < age + 3:
     print('Number is less than age + 3')

else:
     print('The number is not greater than age')



