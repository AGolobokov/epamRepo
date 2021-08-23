import pytest
from homework9.tasks.hw2 import SupressorClass, supressor_generator


def testSupressorClass():

    with SupressorClass(AssertionError):
        raise AssertionError

    flag = False
    try:
        with SupressorClass(AssertionError):
            raise NameError
    except NameError:
        flag = True
    assert flag is True


def test_supressor_generator():
    with supressor_generator(IndexError):
        raise IndexError

    flag = False
    try:
        with supressor_generator(AssertionError):
            raise NameError
    except NameError:
        flag = True
    assert flag is True
