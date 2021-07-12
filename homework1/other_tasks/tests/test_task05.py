import pytest

from homework1.other_tasks.tasks.task05 import find_maximal_subarray_sum

DATASET = [1, 3, -1, -3, 5, 3, 6, 7]


@pytest.mark.parametrize(
    "arg1, arg2,  expected",
    [(DATASET, 3, 16), (DATASET, 5, 21), (DATASET, 1, 7), (DATASET, 0, -1)],
)
def test_positive_case_find_maximal_subarray_sum(arg1, arg2, expected):
    assert find_maximal_subarray_sum(arg1, arg2) == expected
