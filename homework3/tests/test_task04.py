import pytest

from homework3.tasks.task04 import is_armstrong


@pytest.mark.parametrize("arg, expected", [
    (153, True),
    (407, True),
    (9, True),
    ])
def test_positive_is_armstrong(arg, expected):
    assert is_armstrong(arg) == expected, 'Is Armstrong number'


@pytest.mark.parametrize("arg, expected", [
    (10, False),
    (408, False),
    (154, False),
    ])
def test_negative_is_armstrong(arg, expected):
    assert is_armstrong(arg) == expected, 'Is not Armstrong number'
