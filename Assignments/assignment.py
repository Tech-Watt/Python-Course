# """
# QUIZ ONE
# Project: Why Python?
# Research 5 companies or platforms that use Python.
# Write a paragraph explaining why Python is a good language to start with.

# Bonus: Write your first print("Hello, Tech Watt!") line in Python.
# This is assignment one
# """





# """
# QUIZ TWO
# Variables and Data Types
# Project: Student Gradebook

# Ask for student name, course name, and score.

# Use appropriate variable types for each input.

# Print a formatted sentence: "[Student] got [Score] in [Course]".

# """
# student_name = 'Joy'
# course_name = 'Science'
# score = 86

# sentence = student_name + ' ' + 'got ' + str(score) + ' in ' + course_name  
# print(sentence)


# '''
# QUIZ THREE
# 🔢 Module 3: Type Casting
# Project: GHS to USD Converter

# Ask the user to input an amount in GHS (as string).

# Convert the string to float.

# Multiply by an exchange rate and print the USD value.

# '''
# amount = '5555'
# amount_float = float(amount)
# usd_exchange_rate = 74784
# amount_usd = amount_float * usd_exchange_rate

# '''
# QUIZ FOUR
# Project: Username Generator

# Ask for user's full name.

# Slice and manipulate the name to create a username.

# Example: John Doe → jdoe23

# Use len(), lower(), and slicing.

# '''

# username = 'John Doe'
# username = username.lower()
# j = username[0]
# doe = username[5:]
# print(username)
# print(doe)
# final = f'{j}{doe}23'
# print(final)


# '''
# QUIZ FIVE
# Project: Simple Calculator

# Ask user for two numbers.

# Ask for an operation (+, -, *, /).

# Perform the operation and return the result.

# '''
# num1 = 6
# num2 = 45
# operator = 'additon'

# result = num1 + num2


# '''
# QUIZ SIX
# Project: Grading System

# Ask for test score.
# check if the score is greater than 90
# check if the score is less than 60
# check of the score is less than or equal to 87
# check of the score is greater than or equal to 54

# check if the score is less than 40 and greater than 70
# check if the score is less than or equal to 30  and greater than 68
# check if the score is greater than or equal to 40  and less than or equal to 63
# check if score is not equal to 50 greater than score 
# check if not score equals 60 < score
# '''

# test_score = 85
# great = (test_score > 90)
# print (great)

# less = (test_score < 60)
# print (less)

# less_than = (test_score <= 87)
# print (less_than)

# great_than = (test_score >= 54)
# print (great_than)

# less_great = (test_score < 40 and test_score > 70)
# print (less_great)

# lessthaneqal_great = (test_score <= 30 and test_score > 68)
# print (lessthaneqal_great)

# greathanequal = (test_score >= 40 and test_score <= 63)
# print (greathanequal)

# not(test_score == 50 ) > test_score
# not(test_score == 60) < test_score


"""
PROJECT ONE
You are a student and you are tasked to create a program that 
helps you and your friends to average your examination results.
Your program should:
- Ask students for the number of courses they have taken for the semester
- Take the name of the courses and store them in a list
- Take the corresponding grades and store them in a list
- Print courses and their corresponding grades
- Return the average grade for the semester
- Return the highest grade obtained
- Return the lowest grade obtained

"""

# num_courses = int(input('Enter the number of courses taken: '))

# course_names = []
# grades = []

# for i in range(num_courses):
#     course_name = input('Enter the name of the course taken: ')
#     course_names.append(course_name)

# for i in range(num_courses):
#     grade = float(input(f'Enter the grade you have gotten for {course_names[i]}: '))
#     grades.append(grade)


# total_grade = 0
# for grade in grades:
#     total_grade += grade

# average = total_grade / len(grades)
# print(f'Average grade is: {average}')

# highest_grade = 0
# lowest_grade = 100
# for grade in grades:
#     if grade > highest_grade:
#         highest_grade = grade

#     if grade < lowest_grade:
#         lowest_grade = grade

# print(F'Lowest grade: {lowest_grade}')
# print(F'Highest grade: {highest_grade}')


'''
# Q1: Create a list of 5 fruits and print it.
# Q2: How can you access the third item in a list?
# Q3: What happens if you try to access an index that doesn't exist?

# Q4: Given the list: colors = ['red', 'green', 'blue', 'yellow', 'pink']
#     Write code to print:
#     a) The first element
#     b) The last element
#     c) Elements from index 1 to 3

# Q5: What does this code output?
#     nums = [10, 20, 30, 40, 50]
#     print(nums[1:4])


# Q6: Add "grape" to the list: fruits = ['apple', 'banana']
# Q7: Change the second item in a list to "kiwi"
# Q8: Remove "banana" from the list

# Q9: What will be the output of the following?
#     a = [3, 1, 4, 1, 5]
#     a.sort()
#     print(a)

# Q10: What does list.append() do? How is it different from list.extend()?

# Q11: Remove duplicates from this list:
#     numbers = [1, 2, 2, 3, 4, 4, 4, 5]

# Q12: Print each element of the list using a for loop.
# Q13: Create a new list that contains only the even numbers from:
#      nums = [1, 2, 3, 4, 5, 6]

# Q14: Use a loop to find the largest number in this list:
#      a = [4, 8, 2, 9, 5]

'''

fruits = ['apple','melon','orange','mango','strawberry']
print(f'The list of fruits are: {fruits}')

third_item = fruits[2]
print(f'The third item in the list is: {third_item}')


# item_not_exist = fruits[5]
# print(item_not_exist)
'''
Since the item is not in the range of our list the error will be:
IndexError: list index out of range
'''

colors = ['red', 'green', 'blue', 'yellow', 'pink']
first_element = colors[0]
third_element = colors[2]
element_one_to_three = colors[1:4]

print(f'''The first element in the list is: {first_element} . 
          The third element is: {third_element} .
          Elements from one to three is: {element_one_to_three}
       ''')

# fruits = ['apple', 'banana']
# fruits.append('grape')
# fruits[1] = 'kiwi'

for i in fruits:
    print(i)

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
removed_dups = list(set(numbers))
print(removed_dups)


even_numbers = []
for i in removed_dups:
    if i % 2 == 0:
        even_numbers.append(i)

print(f'Even numbers are: {even_numbers}')


a = [4, 8, 2, 9, 5]
largest_number = 0
for l in a:
    if l > largest_number:
        largest_number = l 

print(f'The largest number is: {largest_number}')
