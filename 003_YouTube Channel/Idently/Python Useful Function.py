numbers = [1, 2, 3, 4]
names = ['Mario', 'Jeff', 'Carlos', 'Top']

print(max(names))
print(min(names))
print(max(names, key=len))
print(min(names, key=len))
print(max(numbers))
print(min(numbers))

dir_list = [1, 0, 2, 0, 4, 6]

for item in dir_list:
    if item == 0:
        dir_list.remove(item)
        dir_list.append(item)

print(dir_list)

dir_list = [1, 0, 2, 0, 4, 6]
zero_list = []
for item in dir_list:
    if item == 0:
        dir_list.remove(item)
        zero_list.append(item)

dir_list = zero_list + dir_list
print(dir_list)
