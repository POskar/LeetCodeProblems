#21. Merge Two Sorted Lists

from typing import List, Optional


def mergeTwoLists(self, l1: Optional[List], l2: Optional[List]) -> Optional[List]:
    if not l1 or not l2:
        return l1 or l2
    
    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(0, list1, list2))