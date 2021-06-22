"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_subarray = 0
    copy_k = k
    if k == 0:
        ...  # do nothing
    elif k > 0:
        while copy_k != 0:
            for i in range(0, len(nums) - copy_k + 1):
                summ = 0
                for j in range(0, copy_k):
                    summ += nums[j + i]
                    if max_subarray < summ:
                        max_subarray = summ
            copy_k = copy_k - 1
    return max_subarray
