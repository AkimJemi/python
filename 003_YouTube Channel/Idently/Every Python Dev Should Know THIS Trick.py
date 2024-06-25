elements = ['a', 'b', 'c', 'd']

for i, elem in enumerate(elements):
    print(f'{i + 1}: {elem}')

for i, elem in enumerate(elements, 1):
    print(f'{i}: {elem}')

for i, elem in enumerate(elements, 0):
    print(f'{i}: {elem} = {elements[i]}')

# 10 Noody Mistakes Devs Often Make In Python
# People Still Make THIS Mistake In Python

# Wrong exampleZ
items = ['A', 'B', 'B', 'B', 'B', 'C', 'D']
for item in items:
    print(item)
    if item == 'B':
        items.remove('B')
    else:
        print(item)

# Correct example
new_items = []
for item in items:
    if item == 'B':
        continue
    else:
        new_items.append(item)

print(items)
print(new_items)
