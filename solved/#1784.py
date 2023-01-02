#1748. Sum of Unique Elements

from typing import List


def sumOfUnique(self, nums: List[int]) -> int:
    sum = 0
    for number in nums:
        if nums.count(number) == 1:
            sum += number
        else:
            nums = list(filter(number.__ne__, nums))
    return sum

nums = [1,2,3,4,5]
print(sumOfUnique(0, nums))