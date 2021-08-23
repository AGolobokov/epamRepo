import pytest

from homework9.tasks.hw3 import universal_file_counter
import pathlib


@pytest.mark.parametrize(
    "extension, tokenizer, expected",
    [
        ("txt", None, 10),
        ("txt", str.split("."), 15),
        ("txt", str.split, 10),
    ],
)
def test_reading_magic_number_positive_case(extension, tokenizer, expected):
    """Testing that temp_file with"""
    path = pathlib.Path().resolve()
    assert universal_file_counter(path, extension, tokenizer) == expected
