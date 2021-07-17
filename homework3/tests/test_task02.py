import pytest

from homework3.tasks.task02 import slow_calculate
import time
from multiprocessing import Pool



def test_slow_calculate():
    """Testing that time of execution less than 1 min"""
    start_time = time.time()
    with Pool(32) as p:
        answer = sum(p.map(slow_calculate, range(0, 500)))
    result_time = (time.time() - start_time)
    assert result_time < 60
