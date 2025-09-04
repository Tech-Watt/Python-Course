'''
Python Sets
A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unordered, unchangeable, and do not allow duplicate values.
'''

# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
print(len(thisset))

# Set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Access Items
# first_value =  thisset[0] # this will raise an error because sets are unordered
for x in thisset:
  print(x)

# Check if "banana" is present in the set
if "banana" in thisset:
    print("Yes, 'banana' is in the set")
else:
    print("No, 'banana' is not in the set")


print("banana" in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.


# Add Items
thisset.add("orange")
print(thisset)

# adding two sets together
newset = {"kiwi", "mango", "papaya"}
my_list = ["kiwi", "mango", "papaya"]
thisset.update(my_list)
print(thisset)


# Remove Items
thisset.remove("orange") # raises an error if the item to remove does not exist
print(thisset)


thisset.discard("banana") # does not raise an error if the item to remove does not exist
print(thisset)

# pop() method removes a random item
x = thisset.pop()
print(x)
print(thisset)

# clear() method empties the set
# thisset.clear()
# print(thisset)

# del thisset # deletes the set completely
# print(thisset) # this will raise an error because the set no longer exists
# del thisset
# print(thisset) # this will raise an error because the set no longer exists


# Loop through a set
# for x in thisset:
#     print(x)


# Joint Sets
set1 = {"a", "b" , "c",1}
set2 = {1, 2, 3}

universal_set = set1.union(set2)
print(universal_set)

intersection_set = set1.intersection(set2)
print(intersection_set) # this will print an empty set because there are no common items

# Difference
diff_set = set1.difference(set2)
print(diff_set)

diff_set2 = set2.difference(set1)
print(diff_set2)

# Symmetric Difference
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)