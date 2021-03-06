"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

from typing import List, Iterable, Any


def range_function(
    iterable_seq: Iterable,
    start: Any = None,
    stop: Any = None,
    step: int = 1,
) -> List[Any]:
    start, stop, step = start, stop, step
    temp_list = list(iterable_seq)

    if start is not None and stop is None:
        stop, start = temp_list.index(start), 0
    elif start is not None and stop is not None and step == 1:
        stop, start = temp_list.index(stop), temp_list.index(start)
    elif start is not None and stop is not None and step != 1:
        stop, start = temp_list.index(stop), temp_list.index(start)
    return temp_list[start:stop:step]
