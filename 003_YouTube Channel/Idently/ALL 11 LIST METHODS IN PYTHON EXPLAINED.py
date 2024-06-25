import copy


def list_methods():
    i: int = 0

    for method in dir(list):
        # if '_' not in method:
        i += 1
        print(i, method, sep=': ')


# list_methods()
# 1: append
people: list[str] = ['Mario', 'Elon', 'Trump']
people.append('Luigi')
# 2: clear
people.clear()
print(people)
# 3: copy
people: list[str] = ['Mario', 'Elon', 'Trump']
copy_people: list[str] = people.copy()
copy_people.remove('Trump')
people: list[str] = ['Mario', ['Elon', 'Bob'], 'Trump']
copy_people: list[str] = people.copy()
copy_people[1][1] = 'Cat'
people: list[str] = ['Mario', ['Elon', 'Bob'], 'Trump']
copy_people: list[str] = copy.deepcopy(people)
copy_people[1][1] = 'Cat'
# 4: count
people: list[str] = ['Mario', 'Elon', 'Trump']
elons = people.count('Elon')
# print(elons)

# 5: extend
people: list[str] = ['Mario', 'Elon', 'Trump']
people2: list[str] = ['Apple', 'Banana']
people.extend(people2)
print(people)
# 6:
people: list[str] = ['Mario', 'Elon', 'Trump']
print(people.index('Trump'))
indexOf = lambda item, list_: list_.index(item) if item in list_ else -1
print(indexOf('Trump', people))
# 7:
people.insert(1, 'Luigi')
print(people)
# 8: pop
# print(people.pop(2))
# pop = lambda item, list_: list_.pop(item) if item < list_ else -1
pop = lambda item, list_: list_.pop(item) if item < len(list_) else -1
# print(pop(3, people))
# 9: remove
remove = lambda item, list_: list_.remove(item) if item in list_ else -1
print(remove('Trump', people))
print(remove('Trump', people))
# 10: reverse
people.reverse()
# 11: sort
people.sort(key=lambda name:len(name), reverse=True)
print(people)
people.sort(key=lambda name: name.startswith(('L', 'E')), reverse=True)
print(people)
