import pytest

from homework1.other_tasks.tasks.task04 import check_sum_of_four

data_example_1 = [0, 1, 3]
data_example_2 = [0, -1, 2]
data_example_3 = [0, 1, 4]
data_example_4 = [0, -1, 5]


def test_positive_case_check_sum_of_four():
    """"""
    assert (
        check_sum_of_four(
            data_example_1, data_example_2, data_example_3, data_example_4
        )
        == 6
    )
