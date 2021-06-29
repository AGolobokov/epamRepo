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


def range_function(*args):
    args_counter = len(args)
    temp_list = list(args[0])
    start = 0
    step = 1
    if args_counter == 2:
        stop = temp_list.index(args[1])
    elif args_counter == 3:
        stop = temp_list.index(args[2])
        start = temp_list.index(args[1])
    elif args_counter == 4:
        stop = temp_list.index(args[2])
        start = temp_list.index(args[1])
        step = args[3]
    else:
        return -1

    answer_list = temp_list[start:stop:step]
    return answer_list
