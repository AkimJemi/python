# Seq 1 to 9,000,000
import sys


def mygenerator(n):
    for x in range(n):
        yield x ** 3


values = mygenerator(100)
print(sys.getsizeof(values))


# print(next(values))
# print(next(values))

# for x in values:
#     print(x)


def infinite_sequence():
    result = 1
    while True:
        yield result
        result += 1


values = infinite_sequence()
print(sys.getsizeof(values))
# for x in values:
#     print(x)
