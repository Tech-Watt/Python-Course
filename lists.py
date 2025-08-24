'''
Lists are used to store multiple items in a single variable.
List is a collection which is ordered and changeable. Allows duplicate members.

'''

names = ['Joy','Gold','Sam']
print(type(names))
print(names)

# The list constructor method of defining a list
# names = list(('Joy','Gold','Sam','Sam'))


# # Access item in a list 
# joy = names[0]
# print(joy)
# gold = names[1]
# print(gold)
# sam = names[-1]
# print(sam)

# # List slicing
# firt_two = names[0:] 
# print(firt_two)


# Adding items to a list
# Append
# names.append('Python')
# names.append('Java')


# # Insert
# names.insert(0,78)
# names.insert(2,'C-sharp')
# print(names)

# # Extend
# fruits = ['orange','mango','melon','banana']
# acid_levels = [5,2,1,1]
# fruits.extend(acid_levels)
# print(fruits)
# acid_levels.extend(fruits)
# print(acid_levels)




#Changing Items in a list 
# names = ['Joy','Gold','Sam','Felix']
# names[-1] = 'Cat'

# names[0:2] = ['Cat','Dog']
# print(names)


# Removing items in a list
# names = ['Joy','Gold','Sam','Felix']
# names.remove('Sam')
# names.pop(0)
# del names[1]
# names.clear()
# print(names)


# Sorting in python
# numbers = list((4,3,5,2,6,1))
# numbers.sort(reverse=True)
# s = sorted(numbers,reverse=True)
# s = ['Sam','Joy','Gold']
# s.sort()
# print(s)

# Copying a list
# numbers = list((4,3,5,2,6,1))
# num = numbers.copy()
# print(num)

# Looping through a list
marks = [65,44,67,76,86]
# marks[0] = marks[0] + 5
# marks[0] += 5
# marks[1] += 5
# marks[2] +=5
# marks[3] +=5
# marks[4] +=5
# print(marks)

for i in marks:
    i += 5
    i = i + 5
    print(i)

print(len(marks))