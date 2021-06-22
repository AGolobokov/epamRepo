"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    result_of_check = 0
    local_list = []
    for x in data:
        local_list.append(x)
    list_len = len(local_list)

    if list_len > 2:
        if local_list[0] == 0 or local_list[0] == 1:
            for i in range(0, list_len - 2):
                if local_list[i + 2] == local_list[i] + local_list[i + 1]:
                    result_of_check = 1
                else:
                    result_of_check = 0
                    break
        else:
            result_of_check = 0

    return bool(result_of_check)
