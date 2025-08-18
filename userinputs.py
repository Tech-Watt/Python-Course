# name = input('Enter your name: ')
# print(type(name))
# print(name)


age,height = input('Enter your age and height separate them by comma: ').split(',')
age,height = float(age), float(height)
print(age,height,sep='\n')
