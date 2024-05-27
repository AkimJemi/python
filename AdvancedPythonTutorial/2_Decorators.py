def mydecorator(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function!")
        return return_value

    return wrapper


@mydecorator
def hello_world():
    called = 1
    called += 1
    print(f"Hello World! I called {called} times")


@mydecorator
def hello(person):
    print(f"Hello {person}!")


@mydecorator
def hello2(person):
    print(f"Hello {person} before return")
    return f"Hello {person}!"


# hello_world()
# print(hello2("jm"))

# Practical Example #1 - Logging
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            file_name = function.__name__
            message = f"{file_name} function : return value {value}"
            print(message)
            f.write(message + "\n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


# print(add(10, 60))

# Practical Example #2 - Timing
import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result += i
    return result



print(myfunction(100000000))
