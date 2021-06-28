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
import string

def range_function(str, start='a', stop='z', step=1):
    set_of_vowels = list(str)
    start = set_of_vowels.index(start)
    stop = set_of_vowels.index(stop)
    list_of_range = set_of_vowels[start:stop:step]
    return list_of_range

print(range_function(string.ascii_lowercase, 'g'))


