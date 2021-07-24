import pytest

from homework6.tasks.counter import instances_counter


def test_decorator_instances_counter():
    @instances_counter
    class AnyClass:
        pass

    example_any_class = AnyClass()

    assert hasattr(example_any_class, 'counter')
    assert hasattr(example_any_class, 'get_created_instances') and callable(example_any_class.get_created_instances)
    assert hasattr(example_any_class, 'reset_instances_counter') and callable(example_any_class.reset_instances_counter)


