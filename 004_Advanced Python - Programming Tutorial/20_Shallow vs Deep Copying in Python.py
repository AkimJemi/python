# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy
import copy

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
shallow_copy = copy.copy(org)  # -> shallow copy
deep_copy = copy.deepcopy(org)  # -> deep copy
# cpy = org[:]  # -> shallow copy
shallow_copy[0][1] = -10
deep_copy[0][1] = -9

print(org)
print(shallow_copy)
print(deep_copy)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.employees = employee
        self.boss = boss


p1 = Person("Alex", 27)
p2 = copy.copy(p1)

p2.age = 28
print(p2.age)
print(p1.age)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
