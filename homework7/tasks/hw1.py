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
        }
     },
    "fourth": "RED",
}


# кажется не очень похоже на pydentic хе-хе постараюсь упростить к следующему разу
# и я не понял надо ли считать 1 и "1" разными элементами, или "True" и True, но я считаю их разными
# и не понял надо ли уметь находить сложные обькты типа ["RED", "BLUE"], у себя это реализовал
def find_occurrences(tree: dict, element: Any) -> int:
    """
    Find element in tree.
    :param tree:
    :param element:
    :return: int, the number of found elements in three
    """
    counter = 0

    def recursive_traversal(obj, target):
        """
        Recursive traversal tree.
        :param obj:
        :param target:
        :return: None
        """
        nonlocal counter
        # if obj is composite
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(key, bool) and isinstance(target, bool):
                    if str(target) == str(key):
                        counter += 1
                elif isinstance(target, bool):
                    if str(target) == key:
                        counter += 1
                elif isinstance(key, bool):
                    if target == str(key):
                        counter += 1
                else:
                    if target == key:
                        counter += 1
                if value == target:
                    counter += 1
                else:
                    recursive_traversal(value, target)
        elif isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
            for item in obj:
                recursive_traversal(item, target)
        else:
            # if obj is simple
            if isinstance(obj, bool):
                if isinstance(target, bool):
                    if str(target) == str(obj):
                        counter += 1
                else:
                    if not isinstance(target, str) and target == str(obj):
                        counter += 1
            elif isinstance(obj, str):
                if target == obj:
                    counter += 1
            elif isinstance(obj, int):
                if isinstance(target, bool):
                    if str(target) == obj:
                        counter += 1
                else:
                    if target == obj:
                        counter += 1
    # walk on the tree
    for elm in tree:
        # checking keys in three
        if isinstance(element, bool) and isinstance(elm, bool):
            if str(elm) == str(element):
                counter += 1
        elif isinstance(element, bool):
            if not isinstance(elm, str) and elm == str(element):
                counter += 1
        elif isinstance(elm, bool):
            if str(elm) == element:
                counter += 1
        else:
            if elm == element:
                counter += 1
        # checking branch in three
        if tree[elm] == element:
            counter += 1
        elif isinstance(tree[elm], list) or isinstance(tree[elm], tuple) or isinstance(tree[elm], dict) or isinstance(tree[elm], set):
            recursive_traversal(tree[elm], element)
        else:
            if isinstance(tree[elm], str):
                if element == tree[elm]:
                    counter += 1
            elif isinstance(tree[elm], bool):
                if element == tree[elm]:
                    counter += 1
            elif isinstance(tree[elm], int):
                if element == tree[elm]:
                    counter += 1
    return counter


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
