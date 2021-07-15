import pytest


from homework2.tasks.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        (["a", "a", "a", "b", "b", "c"], ("a", "c")),
    ],
)
def test_negative_check_fibonacci(arg, expected):
    """Testing that [] give False"""
    assert major_and_minor_elem(arg) == expected
