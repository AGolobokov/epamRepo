"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    unique_set = set()
    with open(file_path) as file:
        for line in file:
            for el in line.split():
                if el not in unique_set:
                    unique_set.add((len(set(el)) + len(el), el))
    return [i[1] for i in sorted(unique_set)[:-11:-1]]


def get_rarest_char(file_path: str) -> str:
    collection_char = dict()
    with open(file_path) as file:
        for line in file:
            for char in line:
                if char not in collection_char:
                    counter_value = 1
                    collection_char.update({char: counter_value})
                else:
                    for key, value in collection_char.items():
                        if key == char:
                            value += 1
                            collection_char.update({char: value})
    for key, value in collection_char.items():
        if value == 1:
            return key


def count_punctuation_chars(file_path: str) -> int:
    result_counter = 0
    with open(file_path) as file:
        for line in file:
            for char in line:
                if 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
                    result_counter = result_counter + 1
    return result_counter


def count_non_ascii_chars(file_path: str) -> int:
    result_counter = 0
    with open(file_path) as file:
        for line in file:
            for char in line:
                if ord(char) > 127 or ord(char) < 0:
                    result_counter += 1
    return result_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    collection_non_ascii_char = dict()
    with open(file_path) as file:
        for line in file:
            for char in line:
                if ord(char) > 127 or ord(char) < 0:
                    if char not in collection_non_ascii_char:
                        counter_value = 0
                        collection_non_ascii_char.update({char: counter_value})
                    else:
                        for key, value in collection_non_ascii_char.items():
                            if key == char:
                                value = value + 1
                                collection_non_ascii_char.update({char: value})
    if bool(collection_non_ascii_char):
        max_v = max([value for value in collection_non_ascii_char.values()])

        for key, value in collection_non_ascii_char.items():
            if value == max_v:
                return key
