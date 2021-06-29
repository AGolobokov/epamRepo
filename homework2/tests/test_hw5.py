import pytest
import pytest
import string

from homework2.tasks.hw5 import range_function


def test_positive_range_function_with_2_args():
    """Testing that [0, 1, 1, 2, 3] give True"""
    assert range_function(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']


def test_positive_range_function_with_3_args():
    """Testing that [0, 1, 1, 2, 3] give True"""
    assert range_function(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_positive_range_function_with_4_args():
    """Testing that [0, 1, 1, 2, 3] give True"""
    assert range_function(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
