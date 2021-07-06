from unittest.mock import MagicMock  # пока не доконца раскурил


from homework3.tasks.task01 import cache


def func(a, b):
    return (a ** b) ** 2


# мне кажется я сделал какую то херню :/
cache_func = cache(times=2)(func)

VAL_1 = cache_func(2, 1)
VAL_2 = cache_func(2, 2)
VAL_3 = cache_func(2, 3)
VAL_4 = cache_func(2, 4)
VAL_5 = cache_func(2, 5)
VAL_6 = cache_func(2, 6)


def test_positive_cache_1():
    assert VAL_1 is VAL_1


def test_positive_cache_2():
    assert VAL_1 is VAL_3


def test_positive_cache_3():
    assert VAL_3 is not VAL_4 and VAL_4 is VAL_5
