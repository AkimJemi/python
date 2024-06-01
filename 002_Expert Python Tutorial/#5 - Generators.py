import sys


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv


g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break


def gen(n):
    for i in range(n):
        yield i ** 2


def gen2(n):
    yield n * 1
    yield n * 10
    yield n * 100
    yield n * 1000
    yield n * 10000


g = gen(10000)
g2 = gen2(20)

for i in g:
    print(i)

print(next(g2))
print(next(g2))
print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))

x = [i ** 2 for i in range(7)]
g = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(g))
