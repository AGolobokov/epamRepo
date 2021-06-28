import pytest

from homework2.tasks.hw3 import combinations


def test_positive_combinations():
    """Testing that [1, 2], [3, 4] give
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4]
]"""
    assert combinations([1, 2], [2, 3]) == [[1, 2], [1, 3], [2, 2], [2, 3]]


def test_positive_combinations_2():
    """Testing that [1, 2], [3, 4], [5, 6] give
    [1, 3],
    [1, 4],
    [1, 5],
    [1, 6],
    [2, 3],
    [2, 4],
    [2, 5],
    [2, 6]
]"""
    assert combinations([1, 2], [3, 4], [5, 6]) == [[1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6]]
