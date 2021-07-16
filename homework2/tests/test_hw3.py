import pytest

from homework2.tasks.hw3 import combinations



@pytest.mark.parametrize(
    "arg1, arg2, expected",
    [
        ([1, 2], [2, 3], [[1, 2], [1, 3], [2, 2], [2, 3]]),
        (['a', 'b', 'c'], ['a', 'a', 'd'], [['a', 'a', 'a'], ['a', 'a', 'd'], ['b', 'a', 'a'], ['b', 'a', 'd'], ['c', 'a', 'a'], ['c', 'a', 'd']]),
    ],
)
def test_positive_combinations(arg1, arg2, expected):
    """Testing with int and char different size """
    assert combinations(arg1, arg2) == expected





