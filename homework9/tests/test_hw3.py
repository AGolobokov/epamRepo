import pytest

from homework9.tasks.hw3 import universal_file_counter
import os


@pytest.mark.parametrize(
    "extension, tokenizer, expected",
    [
        ("txt", None, 10),
        ("txt", str.split, 15),
    ],
)
def test_reading_magic_number_positive_case(extension, tokenizer, expected):
    """Testing that temp_file with"""
    assert universal_file_counter(os.getcwd(), extension, tokenizer) == expected
