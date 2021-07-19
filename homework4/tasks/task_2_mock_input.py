"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


# >>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import requests

TARGET = "i"


def service_func(url: str) -> str:
    try:
        response = requests.get(url)
        if response.ok:
            return response.text
    except requests.exceptions.RequestException:
        raise ValueError(f"Unreachable {url})")


def count_dots_on_i(url: str) -> int:
    data = service_func(url)
    temp_list = list()

    for line in data:
        temp_list.append([1 if char == TARGET else 0 for char in line])
    return sum([item for sublist in temp_list for item in sublist])
