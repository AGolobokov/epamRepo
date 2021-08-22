"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    result_of_check = False

    list_len = len(data)
    for i in range(0, list_len - 2):
        if data[i + 2] == data[i] + data[i + 1]:
            result_of_check = True
        else:
            result_of_check = False
            break

    return result_of_check
