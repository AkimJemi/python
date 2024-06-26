class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")


p = Person("Hike", 25)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("add method")
        print(self)
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X : {self.x}, Y : {self.y}"

    def __len__(self):
        print("len method")
        return 10

    def __call__(self, *args, **kwargs):
        print("hello I was called")


v1 = Vector(10, 20)
v2 = Vector(13, 25)
v3 = v1 + v2
print(v3)
print(len(v3))
v3()
