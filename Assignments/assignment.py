"""
QUIZ ONE
Project: Why Python?
Research 5 companies or platforms that use Python.
Write a paragraph explaining why Python is a good language to start with.

Bonus: Write your first print("Hello, Tech Watt!") line in Python.
This is assignment one
"""





"""
QUIZ TWO
Variables and Data Types
Project: Student Gradebook

Ask for student name, course name, and score.

Use appropriate variable types for each input.

Print a formatted sentence: "[Student] got [Score] in [Course]".

"""
student_name = 'Joy'
course_name = 'Science'
score = 86

sentence = student_name + ' ' + 'got ' + str(score) + ' in ' + course_name  
print(sentence)


'''
QUIZ THREE
🔢 Module 3: Type Casting
Project: GHS to USD Converter

Ask the user to input an amount in GHS (as string).

Convert the string to float.

Multiply by an exchange rate and print the USD value.

'''
amount = '5555'
amount_float = float(amount)
usd_exchange_rate = 74784
amount_usd = amount_float * usd_exchange_rate

'''
QUIZ FOUR
Project: Username Generator

Ask for user's full name.

Slice and manipulate the name to create a username.

Example: John Doe → jdoe23

Use len(), lower(), and slicing.

'''

username = 'John Doe'
username = username.lower()
j = username[0]
doe = username[5:]
print(username)
print(doe)
final = f'{j}{doe}23'
print(final)


'''
QUIZ FIVE
Project: Simple Calculator

Ask user for two numbers.

Ask for an operation (+, -, *, /).

Perform the operation and return the result.

'''
num1 = 6
num2 = 45
operator = 'additon'

result = num1 + num2


'''
QUIZ SIX
Project: Grading System

Ask for test score.
check if the score is greater than 90
check if the score is less than 60
check of the score is less than or equal to 87
check of the score is greater than or equal to 54

check if the score is less than 40 and greater than 70
check if the score is less than or equal to 30  and greater than 68
check if the score is greater than or equal to 40  and less than or equal to 63
check if score is not equal to 50 greater than score 
check if not score equals 60 < score
'''

test_score = 85
great = (test_score > 90)
print (great)

less = (test_score < 60)
print (less)

less_than = (test_score <= 87)
print (less_than)

great_than = (test_score >= 54)
print (great_than)

less_great = (test_score < 40 and test_score > 70)
print (less_great)

lessthaneqal_great = (test_score <= 30 and test_score > 68)
print (lessthaneqal_great)

greathanequal = (test_score >= 40 and test_score <= 63)
print (greathanequal)

not(test_score == 50 ) > test_score
not(test_score == 60) < test_score