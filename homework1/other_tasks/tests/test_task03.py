import pytest
import tempfile

from homework1.other_tasks.tasks.task03 import find_maximum_and_minimum


@pytest.fixture
def test_file() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/new_file.txt"
    with open(f"{temp_dir}/new_file.txt", "w") as f:
        f.write("12\n-2\n789\n1\n0\n78")
    return temp_file


def test_positive_case_find_max_and_min(test_file):
    """Testing that temp_file with data 12 -2 789 1 0 78 give (789, -2)"""
    assert find_maximum_and_minimum(test_file) == (789, -2)
