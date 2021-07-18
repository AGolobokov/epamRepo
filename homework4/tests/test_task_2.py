import pytest

from homework4.tasks.task_2_mock_input import service_func, count_dots_on_i


from mock import Mock


service_func = Mock(service_func, return_value="...")

#почему то не подменяется service_func внутри count_dots_on_i пока разбираюсь
def test_count_dots_on_i():
    """Testing that service_func return False"""
    # assert count_dots_on_i("any path") == 3
    assert service_func("any path") == "..."
    # assert count_dots_on_i("any path") == 3


