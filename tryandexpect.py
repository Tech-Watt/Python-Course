text = '''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the 
result of the try- and except blocks.
'''

# Example 1: Using try and except
# x = 4
# try:
   
#     print(x)

# except NameError:
#     print("Variable x is not defined")  

# except:
#     print("Something else went wrong")

# # Example 2: Using try, except, and else
# try:
#     f = open('demo.txt','w')
#     f.write(text)
#     f.close()
    
    
# except:
#     print("Error: could not write to file")


# else:
#     print("File written successfully")

# finally:
#     print("Executing finally block")



# def add_numbers(a, b):
#     return a + b

# try:
    
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     result = add_numbers(num1, num2)

#     print("The sum is:", result)

# except ValueError:
#     print("Please enter valid numbers only.")




x = input("Enter a number: ") 
if type(x) is not int:
    raise Exception("Only integers are allowed")




# Raise an exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise Exception("Age must be at least 18")
    else:
        return "Age is valid"
    
try:
    user_age = int(input("Enter your age: "))
    print(check_age(user_age))
except ValueError as ve:
    print("ValueError:", ve)