import pytest
import pytest
import string

from homework2.tasks.hw5 import range_function


@pytest.mark.parametrize(
    "arg1, arg2, arg3, arg4,  expected",
    [
        (string.ascii_lowercase, "g", None, None, ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            "g",
            "p",
            None,
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
    ],
)
def test__range_function(arg1, arg2, arg3, arg4, expected):
    """Testing with different arguments"""
    assert range_function(arg1, arg2, arg3, arg4) == expected
