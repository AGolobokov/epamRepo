import pytest

from homework1.other_tasks.tasks.task05 import find_maximal_subarray_sum

nums = [1, 3, -1, -3, 5, 3, 6, 7]


def test_positive_case_find_maximal_subarray_sum_v1():
    """Testing that [1, 3, -1, -3, 5, 3, 6, 7] and k=3 give 16"""
    assert find_maximal_subarray_sum(nums, 3) == 16


def test_positive_case_find_maximal_subarray_sum_v2():
    """Testing that [1, 3, -1, -3, 5, 3, 6, 7] and k=1 give 7"""
    assert find_maximal_subarray_sum(nums, 1) == 7


def test_positive_case_find_maximal_subarray_sum_v3():
    """Testing that [1, 3, -1, -3, 5, 3, 6, 7] and k=5 give 21"""
    assert find_maximal_subarray_sum(nums, 5) == 21
