names = [
    'Daniel',
    'Milk',
    'William'
]

# List Comprehension
length = [len(name) for name in names]

# Dictionary Comprehension
length2 = {name: len(name) for name in names}

print(length)
print(length2)
