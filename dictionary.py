"""
Dictionary items are presented in key:value pairs, and can
be referred to by using the key name.
"""
car_company = {
'name': 'Tesla',
'model': 'Model S',
'year': 2020,
'color': 'red',
'price': 79999.99
}


# Using dictionary constructor
# car_company = dict(name='Tesla', 
#                    model='Model S', 
#                    year=2020, color='red', 
#                    price=79999.99)

# Accessing items in a dictionary
name = car_company['name']
model = car_company.get('model')
year = car_company.get('year')
color = car_company.get('color')
price = car_company.get('price')

print(name)
print(model)
print(year)
print(color)
print(price)

# Knowing the keys and values in a dictionary
keys = car_company.keys()
values = car_company.values()

print(keys)
print(values)

# Checking the length of a dictionary
length = len(car_company)
print(length)

# Getting all items in a dictionary
items = car_company.items()
print(items)

# Checking if a key exists in a dictionary
if 'named' in car_company:
    print("Key 'name' exists in the dictionary")


# Changing values in a dictionary
car_company['color'] = 'blue'
car_company['price'] = 89999.99
print(car_company)

car_company.update({'color': 'black', 'price': 99999.99, 'year': 2021})
print(car_company)


# Adding items to a dictionary
car_company['mileage'] = 15000
car_company['owner'] = 'Gold'
print(car_company)

car_company.update({'warranty': '5 years', 'insurance': 'full'})
print(car_company)


# # Removing items from a dictionary
# car_company.pop('owner')
# print(car_company)
# car_company.popitem()  # removes the last item
# print(car_company)
# del car_company['mileage']
# print(car_company)

# car_company.clear()  # removes all items
# print(car_company)



# Loops in a dictionary
for key, value in car_company.items():
    print(value)

for key in car_company.keys():
    print(key)

for value in car_company.values():
    print(value)


# Copying a dictionary
car_company_copy = car_company.copy()
print(car_company_copy)


car_company_copy2 = dict(car_company)



# Nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# accessing items in a nested dictionary

print(len(myfamily))
child1_name = myfamily['child1']['name']
print(child1_name)

child2_name = myfamily['child2']['name']
print(child2_name)

child3_name = myfamily['child3']['name']
print(child3_name)


# Loops in a nested dictionary
for child, info in myfamily.items():
    
    print(child)

    for key, value in info.items():
        print(key, value)


