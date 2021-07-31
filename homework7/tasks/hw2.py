"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""

TARGET = '#'


def processing_string(data: str) -> list:
    create_list = list()
    step = -1
    skip_element_flag = 0

    for i in data[::step]:
        if i != TARGET:
            if not skip_element_flag:
                create_list.append(i)
            else:
                skip_element_flag = 0
        else:
            skip_element_flag = 1
    return create_list


def backspace_compare(first: str, second: str):
    result = True

    if len(processing_string(first)) != len(processing_string(second)):
        result = False

    if result:
        for i, j in zip(processing_string(first), processing_string(second)):
            if i != j:
                result = False
                return result
    return result
