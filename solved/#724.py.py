#724. Find Pivot Index

from typing import List


def pivotIndex(self, nums: List[int]) -> List[int]:
    lsum = 0
    rsum = sum(nums)
    for i in range(0, len(nums)):
        rsum -= nums[i]
        if lsum == rsum:
            return i
        lsum += nums[i]

    return 0

nums = [1,7,3,6,5,6]
print(pivotIndex(0, nums))
