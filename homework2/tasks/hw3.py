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
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    length = len(args)
    answer_list = list()
    for i in args[0]:
        for k in args[1:length]:
            for j in k:
                newlist = list()
                newlist.append(i)
                newlist.append(j)
                answer_list.append(newlist)
    return answer_list
