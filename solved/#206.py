#206. Reverse Linked List

from typing import List, Optional


def reverseList(self, head: Optional[List]) -> Optional[List]:
    x = head[::-1]
    return x

list = [1,2,3,4,5]
print(reverseList(0, list))