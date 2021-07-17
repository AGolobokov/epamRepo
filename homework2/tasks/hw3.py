"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import List, Any


def my_list_generator(temp_list: List[Any], value) -> Any:
    for elm in itertools.combinations(temp_list, value - 1):
        yield elm


def combinations(*args: List[Any]) -> List[List]:
    lists_counter, first_list_size = len(args), len(args[0])
    intermediate_list = list()
    for i in args[0]:
        new_list = [item for sublist in args[1:lists_counter] for item in sublist]
        for j in my_list_generator(new_list, first_list_size):
            temp_list = list()
            temp_list.append(i)
            temp_list.extend([*j])
            intermediate_list.append(temp_list)
    temp_set = {tuple(el) for el in intermediate_list}
    answer_list = [list(el) for el in temp_set]
    answer_list.sort()
    return answer_list
