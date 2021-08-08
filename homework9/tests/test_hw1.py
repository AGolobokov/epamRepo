import pytest
import tempfile
from homework9.tasks.hw1 import merge_sorted_files


@pytest.fixture()
def test_file(param, file_list) -> list:
    list_of_file = list()
    temp_dir = tempfile.gettempdir()
    for elm in file_list:
        temp_file = f"{temp_dir}/test{elm}.txt"
        with open(temp_file, "w") as f:
            f.write(param[int(elm)])
        list_of_file.append(temp_file)
    return list_of_file


@pytest.mark.parametrize(
    "param, file_list, expected",
    [
        (['1\n10\n100\n', '2\n20\n200\n'], ['0','1'], [1, 2, 10, 20, 100, 200]),
    ],
)
def test_reading_magic_number_positive_case(test_file, file_list, param, expected):
    """Testing that temp_file with"""
    assert list(merge_sorted_files(test_file)) == expected
