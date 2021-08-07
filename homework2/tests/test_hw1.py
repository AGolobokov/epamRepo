import pytest
import tempfile

from homework2.tasks.hw1 import get_longest_diverse_words
from homework2.tasks.hw1 import get_rarest_char
from homework2.tasks.hw1 import count_punctuation_chars
from homework2.tasks.hw1 import count_non_ascii_chars
from homework2.tasks.hw1 import get_most_common_non_ascii_char


@pytest.fixture
def test_file() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/new_file.txt"
    with open(f"{temp_dir}/new_file.txt", "w") as f:
        f.write(
            "After 1912, the Republican Party began to undergo an ideological shift to the right.\n "
            "Following the Civil Rights Act of 1964 and the Voting Rights Act of 1965,\n "
            "the party's core base shifted, with southern states becoming \n"
            "more reliably Republican in \\u00dc presidential politics."
        )
    return temp_file


def test_positive_get_longest_diverse_words(test_file):
    """Testing that temp_file give ['presidential', 'Republican', 'ideological',
    'politics.', 'southern', 'shifted,', 'becoming', 'Following', 'reliably', 'undergo']"""
    assert get_longest_diverse_words(test_file) == [
        "presidential",
        "Republican",
        "ideological",
        "politics.",
        "southern",
        "shifted,",
        "becoming",
        "Following",
        "reliably",
        "undergo",
    ]


def test_positive_get_rarest_char(test_file):
    """Testing that temp_file give 2"""
    assert get_rarest_char(test_file) == "2"


def test_positive_count_punctuation_chars(test_file):
    """Testing that temp_file give 6"""
    assert count_punctuation_chars(test_file) == 6


@pytest.fixture
def test_file_with_non_ascii() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/new_file.txt"
    with open(f"{temp_dir}/new_file.txt", "w") as f:
        f.write(
            "The Republican Party, also referr\\u00dced to as the GOP (Grand Old Party)\n"
            "is one of the two maj\\u00bbor contemporary political parties in the United States,\n"
            "along with i\\u00dcts main histo\\u00dcric rival, the Democratic Party.\n"
        )
    return temp_file


def test_positive_count_non_ascii_chars(test_file_with_non_ascii):
    """Testing that test_file_with_non_ascii give 37"""
    assert count_non_ascii_chars(test_file_with_non_ascii) == 4


def test_positive_get_most_common_non_ascii_char(test_file_with_non_ascii):
    """Testing that temp_file give 6"""
    assert get_most_common_non_ascii_char(test_file_with_non_ascii) == "Ü"
