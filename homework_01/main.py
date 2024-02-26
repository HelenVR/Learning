"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [arg ** 2 for arg in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def filter_numbers(numbers, num_filter):
    return list(filter(lambda x: x % 2, numbers)) if num_filter == ODD else list(filter(lambda x: not x % 2, numbers))\
    if num_filter == EVEN else list(filter(lambda x: is_prime(x), numbers))