import pytest
from homework7.tasks.hw3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']], "unfinished!"),
        ([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']], "x wins!"),
        ([['o', '-', 'x'], ['-', 'o', 'x'], ['x', 'x', 'o']], "o wins!"),
        ([['o', 'o', 'x'], ['x', 'x', 'o'], ['o', 'x', 'o']], "draw!")

    ],
)
def test_tic_tac_toe_checker(arg, expected):
    """Testing with different strings"""
    assert tic_tac_toe_checker(arg) == expected
