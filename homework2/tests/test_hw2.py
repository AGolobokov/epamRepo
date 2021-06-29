import pytest


from homework2.tasks.hw2 import major_and_minor_elem


def test_positive_major_and_minor_elem_1():
    """Testing that temp_file with data [3,2,3] give (3, 2)"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_positive_major_and_minor_elem_2():
    """Testing that temp_file with data [2,2,1,1,1,2,2] give (2, 1)"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_positive_major_and_minor_elem_with_char():
    """Testing that temp_file with data [2,2,1,1,1,2,2] give (2, 1)"""
    assert major_and_minor_elem(["a", "a", "a", "b", "b", "c"]) == ("a", "c")
