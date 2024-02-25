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


def filter_numbers(numbers, filter):
    return [num for num in numbers if num % 2] if filter == ODD else [num for num in numbers if not num % 2]\
    if filter == EVEN else [num for num in numbers if is_prime(num)]