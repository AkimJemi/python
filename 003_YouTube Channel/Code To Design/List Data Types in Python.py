# https://www.youtube.com/watch?v=JwQTE1ndOig

# What is List Data Type?
# Mutable ordered collection of items.

# Purpose
# To store values of same type, different types, or mix type with unique and duplicate values.

# [elements]
# Syntax: [element1, element2, element3]

# list
# Maintains the insertion order
# Can perform both indexing and slicing operation.
# Indexing: Process of accessing individual elements.
# Process of accessing multiple elements.
# Mutable
#  Modify Elements
#  Add Elements
#  Remove Elements
# Pre-defined Function
#  Built-in function available in language.
#   1.append()  2.insert()  3.copy()  4.remove()  5.pop()
#   6.clear()  7.index()  8.count()  9.reverse()  10.sort()  11.extend()
mylist = ["Hi", 1, True]
print(mylist, type(mylist))

fruits = ["Apple", "Orange", "Banana"]
# print(fruits[2])
# print(fruits[0:3])
fruits_copy1 = fruits.copy()
fruits_copy2 = fruits
fruits[2] = "test"
print(fruits)
print(fruits_copy1)
print(fruits_copy2)
# print(fruits.index("Apple"))

# 6:46