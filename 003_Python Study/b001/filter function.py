nums = range(1, 1000)


def is_prime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
        return True


primes = filter(is_prime, nums)
print(list(primes))

number = range(1, 100)


def check_even(num):
    if num % 2:
        return True
    else:
        return False


even_nums = filter(check_even, number)
print(list(even_nums))
