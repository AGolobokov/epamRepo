"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable
import os


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    list_of_files = os.listdir(dir_path)
    target_file_list = [
        file_name for file_name in list_of_files if file_extension in file_name
    ]
    for file in target_file_list:
        with open(file, "r") as file:
            for line in file:
                if tokenizer is None:
                    counter += 1
                else:
                    if type(tokenizer) is list:
                        counter += len(line.split(*tokenizer))
                    else:
                        counter += len(tokenizer(line))
    return counter