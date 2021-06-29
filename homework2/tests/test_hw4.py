import pytest

from homework2.tasks.hw4 import cache

DATA_1 = 100, 200
DATA_2 = 10, 20


def test_positive_cache():
    """Testing that objects is equal"""

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    val_1 = cache_func(*DATA_1)
    val_2 = cache_func(*DATA_1)
    val_3 = cache_func(*DATA_2)
    val_4 = cache_func(*DATA_2)
    assert val_1 is val_2 and val_3 is val_4
