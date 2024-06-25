# Inheritance
# Create another class
# Class attributes
# Static methods


class Pet:
    def __init__(self):
        print("init")
        print(self.__class__.__name__)
        class_name = self.__class__.__name__.lower()
        if class_name == "dog":
            self.language = "waa"
        elif class_name == "cat":
            self.language = "yaa"
        else:
            self.language = "no"

    def speak(self):
        print(f"I speak {self.language}")


class Dog(Pet):

    def speak(self):
        super().speak()


# pet = Pet()
# dog = Dog()
# pet.speak()
# dog.speak()


# Class attribute

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


# p1 = Person("Kim")
# p2 = Person("Neka")
# print(Person.get_number_of_people())

# Static methods
class Math:
    @staticmethod
    def add5(x):
        return x * 5


print(Math.add5(5))
