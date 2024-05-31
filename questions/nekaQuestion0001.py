def answer(param1, param2):
    product = param1 * param2
    if product <= 1000:
        return product
    else:
        return param1 + param2


print(answer(20, 30))
print(answer(40, 30))
