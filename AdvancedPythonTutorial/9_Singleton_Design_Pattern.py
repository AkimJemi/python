from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_date():
        """ implement in child class """


class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_date():
        print(f"Name : {PersonSingleton.__instance.name} , Age : {PersonSingleton.__instance.age}")


# p0 = PersonSingleton.get_instance()
# print(p0)
# p0.print_date()

p1 = PersonSingleton("Mike", 30)
print(p1)
p1.print_date()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_date()
