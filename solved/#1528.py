#1528. Shuffle String

from typing import List


def restoreString(self, s: str, indices: List[int]) -> str:
    string = ""
    dt = dict(zip(indices, s))
    dt = sorted(dt.items())
    for k, v in dt:
        string += v
    return string
    
s, indices = "codeleet", [4,5,6,7,0,2,1,3]
print(restoreString(0, s, indices))