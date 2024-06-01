# def func(f):
#     def wrapper():
#         print("Started")
#         f()
#         print("Ended")
#
#     return wrapper
#
#
# def func2():
#     print("i am func2")
#
#
# def func3():
#     print("i am func3")
#
#
# x = func(func2)
# y = func(func3)
# print(x)
# x()
# y()
import time


def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv

    return wrapper


@func
def func2(x, y):
    print(f"{x}, {y}")
    return x + y


@func
def func3():
    print("i am func3")


# x = func2(x=5, y=5)
# print(x)
# func3()


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time :", total)
        return rv

    return wrapper


@timer
def test():
    for _ in range(1000000):
        pass


@timer
def test2():
    time.sleep(2)


test()
test2()
