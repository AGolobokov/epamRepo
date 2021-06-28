"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    temp_dict = dict()
    for i in inp:
        if i not in temp_dict:
            counter_value = 0
            temp_dict.update({i: counter_value})
        else:
            for key, value in temp_dict.items():
                if key == i:
                    value = value + 1
                    temp_dict.update({i: value})
    max_value = max([value for value in temp_dict.values()])
    min_value = min([value for value in temp_dict.values()])

    most_common = least_common = 0
    for key, value in temp_dict.items():
        if value == max_value:
            most_common = key
        if value == min_value:
            least_common = key
    answer = (most_common, least_common)
    return answer
