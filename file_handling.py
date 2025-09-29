# file handling in python
'''
File handling in Python is a way to store and manipulate data on your computer.
Python provides built-in functions to create, read, update, and delete files.
There are different types of files, such as text files, binary files, and CSV files.
You can open a file using the open() function, which takes two arguments: the 
file name and the mode (read, write, append, etc.).
You can read the contents of a file using the read() or readline() methods, 
and write to a file using the write() or writelines() methods.
After you are done with a file, it is important to close it using the close() method
''' 

# Creating a file and writing to it
story = """
once upon a time, in a land far, far away, there lived a young princess named
Aurora. She was kind and beautiful, with hair as golden as the sun and eyes as blue as the sky.
She lived in a grand castle with her parents, the king and queen, who loved her dearly.
One day, a wicked fairy named Maleficent cast a spell on Aurora, causing her to
fall into a deep sleep. The only way to break the spell was for Aurora to be awakened by true love's kiss.
Many princes from far and wide came to the castle to try and wake Aurora, but none were
successful. Finally, a brave and handsome prince named Phillip arrived at the castle.
He had heard of Aurora's plight and was determined to save her. With the help of the good fairies,
Phillip fought his way through Maleficent's dark magic and reached Aurora's bedside.
He leaned down and gently kissed her on the lips, and to everyone's amazement, Aurora's eyes fluttered open.
She had been awakened from her deep sleep by true love's kiss.
The king and queen were overjoyed to see their daughter awake and well, and they
thanked Phillip for his bravery and kindness. Aurora and Phillip soon fell in love and were married.
They lived happily ever after, ruling the kingdom with wisdom and compassion.
The end.
"""

# # writing to a file
# f = open('story.txt', 'w')
# f.write(story)
# f.close()

# with open('story1.txt', 'w') as f:
#     f.write(story)


# # reading from a file
# f = open('story.txt', 'r')
# print(f.read())
# f.close()

# with open('story.txt', 'r') as f:
#     print(f.read())


# appending to a file
with open('story.txt', 'a') as f:
    f.write("And they lived happily ever after.")



