import pytest

from homework1.other_tasks.tasks.task03 import find_maximum_and_minimum

my_file = open("my_file.txt", "w+")
my_file.write("12\n-2\n789\n1\n0\n78")
my_file.close()


def test_positive_case_find_max_and_min():
    """"""
    assert find_maximum_and_minimum("my_file.txt") == (789, -2)
