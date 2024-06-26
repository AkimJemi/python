# 1 - values()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.values())
print([user for user in users])

# 2 - keys()
print(users.keys())

# 3 - pop()
user = users.pop(1)
print(user, users)

# 4 - popitem()
user = users.popitem()
print(user, users)
user = users.popitem()
print(user, users)
print(type(user))  # tuple

# 5 - copy()

sample_dict: dict = {0: ['a', 'b'], 1: 'c', 2: 'd'}
my_copy: dict = sample_dict.copy()

print(id(sample_dict))  # 1637274581888
print(id(my_copy))  # 1637274581888

my_copy[0][0] = '!!!'
print(sample_dict, my_copy)
# use deepcopy

# 6 - get()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.get(1))  # Luigi
print(users.get(999))  # None
print(users.get(999, 'Missing!'))  # Missing!

# 7 - setdefault()
print(users.setdefault(0, '???'))  # Mario
print(users.setdefault(999, '???'))  # ???
print(users)  # {0: 'Mario', 1: 'Luigi', 2: 'James', 999: '???'}

# 8 - clear()
# users.clear()

# 9 - fromkeys()
people: list[str] = ['Mario', 'Luigi', 'James']
users: dict = dict.fromkeys(people)
print(users)

users: dict = dict.fromkeys(people, 'Unknown')
print(users)

# 10 - items()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.items())
for k, v in users.items():
    print(k, v)

user_tuple = [{k: v} for k, v in users.items()]
print(user_tuple[2].get(2))
for k in user_tuple:
    print(k)

# 11 - update()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
users.update({2: 'Bob', 3: 'James\'s sister'})
print(users | {10: 'Spam', 11: 'Eggs'})
users |= {10: 'Spam', 11: 'Eggs'}
print(users)
