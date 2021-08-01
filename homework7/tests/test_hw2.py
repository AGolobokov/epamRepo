import pytest
from homework7.tasks.hw2 import backspace_compare


@pytest.mark.parametrize(
    "arg1, arg2, expected",
    [
        ("my_string", "my_string", True),
        ("1aab##c", "1a2e##c", True),
        ("#######", "#######", True),
        ("a#c", "b", False),
        ("123#567", "234#567", False)
    ],
)
def test_backspace_compare(arg1, arg2, expected):
    """Testing with different strings"""
    assert backspace_compare(arg1, arg2) == expected
