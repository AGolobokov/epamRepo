"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 0


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_subarray = -1
    list_of_summ_subarray = list()

    if k > 0:
        while k != 0:
            for i in range(0, len(nums) - k + 1):
                summ = 0
                list_of_summ_subarray.append(
                    sum([summ + nums[j + i] for j in range(0, k)])
                )
            k = k - 1
        max_subarray = max(list_of_summ_subarray)
    return max_subarray


print(find_maximal_subarray_sum(nums, k))
