"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [arg ** 2 for arg in args]


def prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def even(num):
    return not num % 2


def odd(num):
    return num % 2


ODD = odd
EVEN = even
PRIME = prime


def filter_numbers(numbers, num_filter):
    return list(filter(lambda x: num_filter(x), numbers))