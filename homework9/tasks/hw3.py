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
import pathlib
from typing import Optional, Callable


def universal_file_counter(
    dir_path: pathlib.Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for current_file in dir_path.iterdir():
        if current_file.suffixes and current_file.suffixes[0] == ("." + file_extension):
            with open(str(current_file), "r") as file:
                for line in file:
                    if tokenizer is None:
                        counter += 1
                    else:
                        if type(tokenizer) is list:
                            counter += len(line.split(*tokenizer))
                        else:
                            counter += len(tokenizer(line))
    return counter
