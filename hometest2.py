# def add_numbers(a, b):
#     return a + b

# print(add_numbers(a = 5,b = 3))   
# print(add_numbers(b=10,a= -2)) 

# def even(number):
#     if number % 2 == 0:
#         return True
#     else: return False

# def is_even(n):
#     return n % 2 == 0

# print(even(4))   
# print(even(7)) 





# def factorial(n):
#     if n < 0:
#         return None
    
#     if n == 0:
#         return 1
    
#     result = 1

#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))  
# print(factorial(0))  



# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)




# numbers = [10, 15, 20, 25, 30, 35]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)




# numbers = [10, 15, 20, 25, 30, 35]
# even = lambda x: x % 2 == 0
# even_numbers = list(filter(even,numbers))
# print(even_numbers)

# square = lambda x: x**2
# squared_numbers = list(map(square,even_numbers))
# print(squared_numbers)


# squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
# print(squared_evens)





# with open("students.txt", "w") as file:
#     file.write("Alice\n")
#     file.write("Brandon\n")
#     file.write("Chloe\n")
#     file.write("Daniel\n")
#     file.write("Ella\n")

# print("students.txt has been created with 5 student names.")






# with open("students.txt", "r") as file:
#     for line in file:
#         print(line)  


# with open("students.txt", "a") as file:
#     file.write('Emma \n')
#     file.write('Gold \n')

# Write a function to do this same thing
# count = 0
# with open('students.txt','r') as file:
#     for line in file:
#         print(line)
#         word = line.split()
#         print(word)
#         count += len(word)

# print(count)


#Create scores.txt with sample data
with open("scores.txt", "w") as file:
    file.write("John 85\n")
    file.write("Alice 45\n")
    file.write("Mark 60\n")
    file.write("Sophie 30\n")
    file.write("Liam 70\n")


#Function to read and display students with their scores
def read_scores(filename):
    with open(filename, "r") as file:
        scores = []
        for line in file:
            name, score = line.strip().split()
            scores.append((name, int(score)))
    return scores


# #Read and display all students
scores = read_scores("scores.txt")
print("All Students and Scores:")
for name, score in scores:
    print(f"{name}: {score}")


#Use filter() to extract students who scored above 50
passed_students = list(filter(lambda x: x[1] > 50, scores))
print("\nStudents Who Scored Above 50:")
for name, score in passed_students:
    print(f"{name}: {score}")


#Use map() to add 5 bonus marks to every student's score
updated_scores = list(map(lambda x: (x[0], x[1] + 5), scores))


#Save updated scores into updated_scores.txt
with open("updated_scores.txt", "w") as file:
    for name, score in updated_scores:
        file.write(f"{name} {score}\n")


# print("\nUpdated scores saved to updated_scores.txt successfully!")



