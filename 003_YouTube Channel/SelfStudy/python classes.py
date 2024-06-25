class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello {}!".format(self.name))


person = Person("JM")
person.say_hello()
