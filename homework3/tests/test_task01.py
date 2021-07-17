import pytest
from homework3.tasks.task01 import cache


ARGS1, ARGS2 = 200, 100


def test_positive_cache():
    """Testing that 6 times call cache func with the same args give one value but different id"""
    result_of_call = list()

    def func_example(a, b):
        return (a ** b) ** 2

    cache_func_example = cache(times=2)(func_example)

    for i in range(0, 6):
        result_of_call.append(cache_func_example(ARGS1, ARGS2))
    assert result_of_call[0] is result_of_call[1] is result_of_call[2]
    assert result_of_call[3] is result_of_call[4] is result_of_call[5]
    assert result_of_call[0] is not result_of_call[4]
