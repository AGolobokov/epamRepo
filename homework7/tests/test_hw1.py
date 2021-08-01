import pytest
from homework7.tasks.hw1 import find_occurrences


EXAMPLE_TREE = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", True, "of", "RED", "valued", "1", 1],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
    "1": ["simple", "list", "of", "RED", "valued", "1", 1, True, "True"],
    True: (1, 2, 3, 4, "10"),
}


@pytest.mark.parametrize(
    "arg1, arg2, expected",
    [
        (EXAMPLE_TREE, "RED", 7),
        (EXAMPLE_TREE, "key1", 1),
        (EXAMPLE_TREE, "1", 3),
        (EXAMPLE_TREE, True, 3),
        (EXAMPLE_TREE, 1, 3),
        (EXAMPLE_TREE, ["RED", "BLUE"], 1),
        (EXAMPLE_TREE, ["a", "lot", "of", "values", {"nested_key": "RED"}], 1),
    ],
)
def test_find_occurrences(arg1, arg2, expected):
    """Testing with different strings"""
    assert find_occurrences(arg1, arg2) == expected
