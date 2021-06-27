"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    temp_data = list()
    result_val_1 = result_val_2 = 0
    with open(file_name) as file:
        for line in file:
            temp_data.append([int(x) for x in line.split()])
            result_val_1 = max(temp_data)
            result_val_2 = min(temp_data)

    return (*result_val_1, *result_val_2)

