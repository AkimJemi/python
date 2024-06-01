# def hello():
#     class Hi:
#         pass
#
#     return Hi


# class Test:
#     t = 2
#
#     def __init__(self):
#         print("init")
#         print(self.t)
#
#     pass

# print(Test.t)
# print("-")
# print(Test().t)
# print(type(Test()))
# print(type(2))
# print(type(Test.__init__))
# print(type(Test))

class Foo:
    def show(self):
        print("hi")


def add_attribute(self):
    self.z = 9


# Test = type('Test', (Foo,), {"x": 5, "add_attribute": add_attribute})
# t = Test()
# t.wy = "hello"
# print(t.x)
# print(t.wy)
#
# t.show()
# t.add_attribute()
# print(t.z)


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val

        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")


d = Dog()

print(d.X)
d.HELLO()
