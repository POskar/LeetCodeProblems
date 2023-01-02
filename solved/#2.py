#2. Add Two Numbers

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry_over = 0
    l1 += [0]
    for x in range(0, len(l1)):
        if x >= len(l2):
            l1[x] += carry_over
        else:
            l1[x] += l2[x] + carry_over
            
        carry_over = 0 if carry_over > 0 else 0

        if l1[x] >= 10:
            l1[x] -= 10
            carry_over += 1
        
    if l1[len(l1)-1] == 0:
        del(l1[len(l1)-1])

    return l1

l1, l2 = [9,9,9,9,9,9,9], [9,9,9,9]
print(addTwoNumbers(0, l1, l2))