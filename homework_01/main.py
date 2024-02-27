"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import Callable


def power_numbers(*args) -> list:
    return [arg ** 2 for arg in args]


def prime(num: int) -> bool:
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def even(num: int) -> bool:
    return not num % 2


def odd(num: int) -> int:
    return num % 2


ODD = odd
EVEN = even
PRIME = prime


def filter_numbers(numbers: list, num_filter: Callable):
    return list(filter(lambda x: num_filter(x), numbers))