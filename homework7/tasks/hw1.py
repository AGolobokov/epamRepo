"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Find element in tree.
    :param tree: a dictionary (tree), that can contains multiple nested structures.
    :param element: finds the number of occurrences of this element in the tree
    :return: int, the number of found elements in three
    """
    counter = 0

    def recursive_traversal(obj, target):
        """
        Recursive traversal tree.
        :param obj: composite part of tree
        :param target: the object we are looking for in composite part of tree
        :return: None
        """
        nonlocal counter
        # if obj is composite
        if isinstance(obj, dict):
            for key, value in obj.items():
                if type(key) == type(target) and key == target:
                    counter += 1
                if type(value) == type(target) and value == target:
                    counter += 1
                else:
                    recursive_traversal(value, target)
        elif isinstance(obj, (list, tuple, set)):
            for item in obj:
                recursive_traversal(item, target)
        else:
            # if obj is simple
            if type(obj) == type(target) and obj == target:
                counter += 1
    # walk on the tree
    for elm in tree:
        # checking keys in three
        if type(elm) == type(element) and elm == element:
            counter += 1
        if type(tree[elm]) == type(element) and tree[elm] == element:
            counter += 1
        elif isinstance(tree[elm], (list, tuple, dict, set)):
            recursive_traversal(tree[elm], element)
        else:
            # if tree[elm] is simple
            if type(tree[elm]) == type(element) and tree[elm] == element:
                counter += 1
    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6

