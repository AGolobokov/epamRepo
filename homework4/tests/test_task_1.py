import pytest

from homework4.tasks.task_1_read_file import extract_line_form_file, read_magic_number


import tempfile


@pytest.fixture()
def test_file(param) -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/test.txt"
    with open(temp_file, "w") as f:
        f.write(param)
    return temp_file


@pytest.mark.parametrize(
    "param, expected",
    [
        ("1", True),
        ("3", True),
        ("2.9", True),
    ],
)
def test_reading_magic_number_positive_case(test_file, param, expected):
    """Testing that read_magic_number return True"""
    assert read_magic_number(test_file) is expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("0", False),
        ("3.1", False),
        ("3", False),
    ],
)
def test_reading_magic_number_negative_case(test_file, param, expected):
    """Testing that read_magic_number return False"""
    assert read_magic_number(test_file) is expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("message", True),
    ],
)
def test_reading_magic_number_throws_exception(test_file, param, expected):
    """Testing that read_magic_number return exception ValueError"""
    result = False
    try:
        read_magic_number(test_file)
    except ValueError:
        result = True

    assert result is True
