"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:

    list_sum_a_b = [(i + j) for i in a for j in b]
    list_sum_c_d = [(i + j) for i in c for j in d]
    list_sum = [1 if i + j == 0 else 0 for i in list_sum_a_b for j in list_sum_c_d]
    result = sum(list_sum)
    return result
