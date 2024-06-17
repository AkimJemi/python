# How to ruin a function in Python
# https://www.youtube.com/shorts/s9LFrLQI6tg
# Wrong example
def func(key, value, dic={}):
    dic[key] = value
    return dic


print(func(1, "b"))
print(func(2, "b"))


# Solution
def func(key, value, dic=None):
    dic = dic or {}
    # d = d if d is not None else {}
    # if d is None:
    #     d = {}
    dic[key] = value
    return dic


d = func(1, "b")
print(func(2, "b", d))
