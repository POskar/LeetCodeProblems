#1. Two Sum

from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for index, value in enumerate(nums):
        t = target - value
        if nums.__contains__(t) and index != nums.index(t):
            return index, nums.index(t)
    return list()

nums = [2,5,5,11]
target = 10
print(twoSum(0, nums, target))
