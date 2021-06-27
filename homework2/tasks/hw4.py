"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = list()

    def check_cache(*args):
        if func(*args) in cache_list:
            for i in cache_list:
                if i == func(*args):
                    return i
        elif func(*args) not in cache_list:
            cache_list.append(func(*args))
            for i in cache_list:
                if i == func(*args):
                    return i
    return check_cache
