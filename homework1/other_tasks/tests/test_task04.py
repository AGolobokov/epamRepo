import pytest

from homework1.other_tasks.tasks.task04 import check_sum_of_four

DATA_EXAMPLE_1 = [0, 1, 3]
DATA_EXAMPLE_2 = [0, -1, 2]
DATA_EXAMPLE_3 = [0, 1, 4]
DATA_EXAMPLE_4 = [0, -1, 5]


def test_positive_case_check_sum_of_four():
    """Testing that DATA_EXAMPLE_1..4 give 6"""
    assert (
        check_sum_of_four(
            DATA_EXAMPLE_1, DATA_EXAMPLE_2, DATA_EXAMPLE_3, DATA_EXAMPLE_4
        )
        == 6
    )
