import pytest

from homework4.tasks.task_2_mock_input import service_func, count_dots_on_i

import mock


@mock.patch("homework4.tasks.task_2_mock_input.service_func")
def test_count_dots_on_i(mock_service_func):
    """Testing that service_func return"""
    mock_service_func.return_value = "This is my point"
    assert count_dots_on_i("any path") == 3
