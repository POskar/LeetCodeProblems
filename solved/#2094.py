#2094. Finding 3-Digit Even Numbers

import itertools
from typing import List

def findEvenNumbers(self, digits: List[int]) -> List[int]:
    if sum(x for x in digits if x % 2 == 0) <= 0 and 0 not in digits:
        return []

    numbers = list(itertools.permutations(digits, 3))
    to_delete = []

    for x in numbers:
        if x[0] == 0 or x[2] % 2 != 0:
            to_delete.append(x)
        else:
            numbers[numbers.index(x)] = int(''.join([str(value) for value in x]))

    numbers = [x for x in numbers if x not in to_delete]
    numbers = list(dict.fromkeys(numbers))
    return sorted(numbers)

digits = [2,2,8,8,2]
print(findEvenNumbers(0, digits))