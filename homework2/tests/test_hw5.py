import pytest
import string

from homework2.tasks.hw5 import range_function


def test_positive_range_function():
    """Testing that [0, 1, 1, 2, 3] give True"""
    assert range_function(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']