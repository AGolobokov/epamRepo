import pytest

from homework1.other_tasks.tasks.task02 import check_fibonacci


def test_positive_case_when_start_with_0():
    """Testing that [0, 1, 1, 2, 3] give True"""
    assert check_fibonacci([0, 1, 1, 2, 3])


def test_positive_case_when_start_with_1():
    """Testing that [1, 1, 2, 3, 5, 8, 13, 21] give True"""
    assert check_fibonacci([1, 1, 2, 3, 5, 8, 13, 21])


def test_positive_case_when_start_from_non_beginning():
    """Testing that [3, 5, 8, 13, 21, 34] give True"""
    assert check_fibonacci([3, 5, 8, 13, 21, 34])


def test_negative_case_no_numbers():
    """Testing that [] give False"""
    assert not check_fibonacci([])


def test_negative_case_when_start_with_0_var_0():
    """Testing that [0, 1, 1, 2, 3, 4] give False"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 4])


def test_negative_case_when_start_with_1_var_0():
    """Testing that [1, 1, 2, 3, 5, 8, 12, 20, 21] give False"""
    assert not check_fibonacci([1, 1, 2, 3, 5, 8, 12, 20, 21])


def test_negative_case_when_start_with_0_var_1():
    """Testing that [0, 1] give False"""
    assert not check_fibonacci([0, 1])


def test_negative_case_when_start_with_1_var_1():
    """Testing that [1, 1] give False"""
    assert not check_fibonacci([1, 1])
