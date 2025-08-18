
# h = 'hello'
# h = "hello"

# multi-line strings

story = '''
Hi 👋, I'm Felix Sam
AI / Machine Learning Engineer and Robotics Enthusiast.
I Help Companies and 8k+ People Build ML Pipelines, Generative AI,
and Computer Vision Applications and many more
'''

new = 'joijgdfjgdfjdjdjsjf' \
'sfdfsfdfsfdsfsdfsfsfsfsff' \
'fsfdf'
  

name = 'Gold Diamonds'
name_length  = len(name)
print(name_length)

# checking if a character or word is in a given string
if 'Diamond' in name:
    print('yes is in name')


# slicing of strings
# accessing a character from a string
first_word = name[-2]
print(first_word)

# accessing a word from the string
word = name[0:4] 
print(word)


# String concatenation
a = 'Hello'
b = 'Gold'
d = ' '
c = a + d + b
print(c+story)


# F-strings in python
student_name = 'Joy'
course_name = 'Science'
score = 86

sentence  = F'{student_name} got {score} in {course_name}'
print(sentence)

name = 'Gold'
age = 17


#Format method
output_sentence = '{} is {} years old'.format(name,age)
print(output_sentence)


