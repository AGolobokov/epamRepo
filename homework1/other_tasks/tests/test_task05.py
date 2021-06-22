import pytest

from homework1.other_tasks.tasks.task05 import find_maximal_subarray_sum

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def test_positive_case_find_maximal_subarray_sum_v1():
    assert find_maximal_subarray_sum(nums, k) == 16


n = 1


def test_positive_case_find_maximal_subarray_sum_v2():
    assert find_maximal_subarray_sum(nums, n) == 7


j = 5


def test_positive_case_find_maximal_subarray_sum_v3():
    assert find_maximal_subarray_sum(nums, j) == 21
