import inspect
from queue import Queue as q

# print(inspect.getsource(list))
x = [1, 2, 3]
y = [4, 5]

print(type(list))
print(x + y)
print(x * 3)
print(len(x))
print(type(x))


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        print("ttt")
        if type(x) is not int:
            raise Exception("Invaild argument, must be int")

        self.name = self.name * x

    def __call__(self, y):
        print(y)

    def __len__(self):
        return len(self.name)


p = Person("tim222")
print("t")
p * 4
print("s")
p("call test")
print(p.name)
print(len(p))


# https://docs.python.org/ja/3/reference/datamodel.html


# q = Queue()
# print(q)
# print(inspect.getsource(Queue))


class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, other):
        self.put(other)

    def __sub__(self, other):
        self.get()


qu = Queue()
qu + 9
qu + 10
qu - None
print(qu)
