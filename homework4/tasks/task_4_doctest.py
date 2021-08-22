"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List
import doctest


def fizzbuzz(n: int) -> List[str]:
    """
    Get the int value and return sequence.
    Example:
    >>> fizzbuzz(5)
    [1, 2, 'fuzz', 4, 'buzz']
    >>> fizzbuzz(15)
    [1, 2, 'fuzz', 4, 'buzz', 'fuzz', 7, 8, 'fuzz', 'buzz', 11, 'fuzz', 13, 14, 'fuzz buzz']
    """
    result_list = [
        "fuzz buzz"
        if not i % 3 and not i % 5
        else "fuzz"
        if not i % 3
        else i
        if i % 5
        else "buzz"
        for i in range(1, n + 1)
    ]
    return result_list


if __name__ == "__main__":
    fizzbuzz(1)
    doctest.testmod(verbose=True)
