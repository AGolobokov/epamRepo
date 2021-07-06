import pytest
from homework3.tasks.task02 import slow_calculate
import timeit


t = timeit.timeit(slow_calculate(0))

# пока не понял как написать тест, ясен квасен что надо смпользовать либу time или что то такое
# по тупому как мне кажется можно
# 1) считаем время с либой time"
# 2) переводим в int получаенное значение
# 3) сверяем что оно меньше требуемого

# подскажите пожалуйста :3
