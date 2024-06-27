import time
from typing import Callable
import random


# Bad benchmarks
def pass_stmt() -> None:
    for i in range(10000000):
        ...


def ellipse() -> None:
    for i in range(10000000):
        ...


def get_time(func: Callable) -> None:
    start_time: float = time.perf_counter()
    func()
    end_time: float = time.perf_counter()
    print(f'{func.__name__}() took: {end_time - start_time:.5f} seconds')


# def main() -> None:
#     get_time(pass_stmt)  # warmup
#     get_time(ellipse)
#     get_time(pass_stmt)


# if __name__ == '__main__':
#     main()


# Premature optimisations
def is_valid_age(age: int) -> bool:
    if age >= 21:
        return True
    else:
        return False


def is_valid_age_optimized(age: int) -> bool:
    return age >= 21


def calculate_sum(n):
    result = 0
    for i in range(n):
        result += i

    return result


def calculate_sum_optimized(n):
    return (n * (n - 1)) // 2


def get_time2(func: Callable, *args: int) -> None:
    start_time: float = time.perf_counter()
    result = func(*args)
    end_time: float = time.perf_counter()
    print(f'result: {result}, {func.__name__}() took: {end_time - start_time:.5f} seconds')


def main() -> None:
    get_time2(calculate_sum, 10000)
    get_time2(calculate_sum_optimized, 1000000000)


if __name__ == '__main__':
    main()


# Type annotations
# name: str = 'Bob'
# age = '100'  # Wrong
# age: int = 100


def fire_employee(name: str) -> None:
    print(f'{name.capitalize()}... You Are Fired!')


# def main() -> None:
#     name: str = 'Bob'
#     age: int = 10
#
#     fire_employee(name)


# Wrong scripts
def get_description() -> str:
    return 'I am Bob'


# when import this scripts on another python file
def main() -> None:
    print(get_description())


#
if __name__ == '__main__':
    main()


# Planning
class SmartLamp:
    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

    def check_for_updates(self):
        raise NotImplementedError
