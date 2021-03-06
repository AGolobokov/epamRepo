"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import unicodedata2 as unicodedata


def extract_lines_form_file(file_path: str) -> any:
    with open(file_path, "r", encoding="utf8") as file:
        for line in file:
            prepared_line = line.encode().decode("unicode-escape")
            yield prepared_line


def get_longest_diverse_words(file_path: str) -> List[str]:
    unique_words = set()

    for line in extract_lines_form_file(file_path):
        for element in line.split():
            if element not in unique_words:
                unique_words.add((len(set(element)) + len(element), element))
    return [i[1] for i in sorted(unique_words)[:-11:-1]]


def get_rarest_char(file_path: str) -> str:
    collection_char_dict = dict()

    for line in extract_lines_form_file(file_path):
        for elm in list(line):
            if elm in collection_char_dict:
                collection_char_dict[elm] += 1
            else:
                collection_char_dict[elm] = 1
    if collection_char_dict:
        return min(collection_char_dict, key=collection_char_dict.get)


def count_punctuation_chars(file_path: str) -> int:
    result_counter = 0
    for line in extract_lines_form_file(file_path):
        for char in line:
            if unicodedata.category(char).startswith("P"):
                result_counter += 1
    return result_counter


def count_non_ascii_chars(file_path: str) -> int:
    result_counter = 0

    for line in extract_lines_form_file(file_path):
        for elm in list(line):
            if not elm.isascii():
                result_counter += 1
    return result_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    collection_non_ascii_char = dict()

    for line in extract_lines_form_file(file_path):
        for elm in [elm for elm in list(line) if not elm.isascii()]:
            if elm in collection_non_ascii_char:
                collection_non_ascii_char[elm] += 1
            else:
                collection_non_ascii_char[elm] = 1
    if collection_non_ascii_char:
        return max(collection_non_ascii_char, key=collection_non_ascii_char.get)
