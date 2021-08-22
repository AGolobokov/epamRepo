import pytest

from homework1.other_tasks.tasks.task02 import check_fibonacci


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([0, 1, 1, 2, 3], True),
        ([1, 1, 2, 3, 5, 8, 13, 21], True),
        ([3, 5, 8, 13, 21, 34], True),
    ],
)
def test_positive_check_fibonacci(arg, expected):
    assert check_fibonacci(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([], False),
        ([0, 1, 1, 2, 3, 4], False),
        ([1, 1, 2, 3, 5, 8, 12, 20, 21], False),
        ([0, 1, 1, 2, 3, 5, 9, 14, 23], False),
        ([0, 1], False),
        ([1, 1], False),
    ],
)
def test_negative_check_fibonacci(arg, expected):
    """Testing that [] give False"""
    assert check_fibonacci(arg) == expected
