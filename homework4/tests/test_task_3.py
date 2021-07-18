import pytest
from homework4.tasks.task_3_get_print_output import my_precious_logger


def test_positive_my_precious_logger_with_error(capsys):
    """Testing that func write to stderr"""
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_positive_my_precious_logger_with_or(capsys):
    """Testing that func write to stdout"""
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"


