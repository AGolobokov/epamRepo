"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import List, Generator, Any


def generate_fuzz_buzz(n: int):
    value = ""
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            value = "fuzz buzz"
        elif i % 3 == 0:
            value = "fuzz"
        elif i % 5 == 0:
            value = "buzz"
        else:
            value = i
        yield str(value)


def fizzbuzz(n: int) -> Generator[None, None, str]:
    generate_fuzz_buzz(n)
    return generate_fuzz_buzz(n)


