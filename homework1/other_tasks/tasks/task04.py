"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0
    list_sum_1 = list()
    for i in a:
        for j in b:
            list_sum_1.append(i+j)

    list_sum_2 = list()
    for k in c:
        for l in d:
            list_sum_2.append(k+l)

    for i in list_sum_1:
        for j in list_sum_2:
            if i + j == 0:
                result += 1
    return result

