import pytest
from homework4.tasks.task_4_doctest import fizzbuzz


@pytest.mark.parametrize(
    "arg, expected",
    [
        (7, [1, 2, "fuzz", 4, "buzz", "fuzz", 7]),
        (
            16,
            [
                1,
                2,
                "fuzz",
                4,
                "buzz",
                "fuzz",
                7,
                8,
                "fuzz",
                "buzz",
                11,
                "fuzz",
                13,
                14,
                "fuzz buzz",
                16,
            ],
        ),
        (0, []),
    ],
)
def test_fizzbuzz(arg, expected):
    """Testing func with different args"""
    assert fizzbuzz(arg) == expected
