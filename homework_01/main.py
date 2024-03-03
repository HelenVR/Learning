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
            if not num % i:
                return False
        return True
    return False


ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'


def filter_numbers(numbers: list, num_filter: Callable):
    return list(filter(lambda x: x % 2, numbers)) if num_filter == ODD \
        else list(filter(lambda x: not x % 2, numbers)) if num_filter == EVEN \
        else list(filter(lambda x: prime(x), numbers))
