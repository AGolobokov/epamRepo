import pytest

from homework3.tasks.task04 import is_armstrong


@pytest.mark.parametrize(
    "arg, expected",
    [
        (153, True),
        (407, True),
        (9, True),
    ],
)
def test_positive_is_armstrong(arg, expected):
    """Testing that 153, 407, 9 give True"""
    assert is_armstrong(arg) == expected, "Is Armstrong number"


@pytest.mark.parametrize(
    "arg, expected",
    [
        (10, False),
        (408, False),
        (154, False),
    ],
)
def test_negative_is_armstrong(arg, expected):
    """Testing that 10, 408, 154  give False"""
    assert is_armstrong(arg) == expected, "Is not Armstrong number"
