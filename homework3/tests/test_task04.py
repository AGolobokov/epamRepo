import pytest

from homework3.tasks.task04 import is_armstrong


def test_is_armstrong_with_153():
    assert is_armstrong(153) is True, 'Is Armstrong number'


def test_is_armstrong_with_10():
    assert is_armstrong(10) is False, 'Is not Armstrong number'
