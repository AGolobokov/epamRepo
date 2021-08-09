"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def get_from_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            prepare_line = line.strip()
            yield prepare_line


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    data_list = list()

    for fname in file_list:
        for data in get_from_file(fname):
            data_list.append(int(data))

    for num in sorted(data_list):
        yield num
