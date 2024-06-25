from uuid import uuid4, UUID
from typing import Self

# 1 Last used value
# Python Console
# >> 10
# 10
# >> _ + 30
# 40

# 2 Snake-case
long_list: list[str] = ['a', 'b']

# 3 Number formatting
big_number: int = 1_000_000_000_000
print(big_number)

# 4 Unimportant values
stats: tuple[str, str, int] = ('Bob', 'Programmer', 27)
name, _, age = stats
print(f'{name}')
print(f'{age}')
print(f'{_}')

# 5 Star underscore
values: list[int] = [1, 2, 3, 4, 5]
first, *_, last = values
print(first, last, sep=', ')
print(_)

# 6 For loops
for _ in range(3):
    print('For loop!')

[print('yo') for _ in range(3)]


# 7 Semiprivate variables


class Lamp:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self._id: UUID = uuid4()

    def get_id(self) -> UUID:
        return self._id


class SubLamp(Lamp):
    def __init__(self, brand: str) -> None:
        super().__init__(brand)

    def sublamp_method(self) -> None:
        print(self._id)


test = Lamp('Bob')
sub_class = SubLamp('Bob')
print(test.get_id())
sub_class.sublamp_method()


class Lamp:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.__hidden_id = uuid4()


# 8 Name mangling
pam: Lamp = Lamp(brand='Pam')
print(pam.brand)
# print(pam__hidden_id)
print(pam._Lamp__hidden_id)


# 9 Dunder methods
class CustomNumber:
    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: Self) -> int:
        return (self.value + other.value) * 10000

    def __repr__(self) -> str:
        return f'CustomNumber(value={self.value})'

    def __or__(self, other) -> str:
        return f'{self.value} | {other.value}'

    def __and__(self, other) -> str:
        return f'{self.value} & {other.value}'


n1: CustomNumber = CustomNumber(10)
n2: CustomNumber = CustomNumber(300)
print(n1)
print(n1 + n2)
print(n1 | n2)
print(n1 & n2)

# 10 Reserved names
class_ = 'bob'
for_ = 'bob'


# 11 Default case
def match_method(weather: str) -> None:
    match weather:
        case 'rain':
            print('rain')
        case 'sunny':
            print('sunny')
        case _:
            print('default')


match_method('rain')
match_method('sunny')
match_method('None')
