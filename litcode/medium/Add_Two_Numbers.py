"""
You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two
numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    overload = False

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not (l1 or l2):
            return ListNode(1) if self.overload else None
        
        res = (l1.val + l2.val) if (l1 and l2) else (l1.val if l1 else l2.val)
        if self.overload:
            res += 1
            self.overload = False
        if res > 9:
            res -= 10
            self.overload = True
        return ListNode(
            res,
            self.addTwoNumbers(l1.next if l1 else None,
                               l2.next if l2 else None)
        )


def get_l(val: int, n: int) -> ListNode | None:
    return None if not n else ListNode(val, get_l(val, n-1))


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
case1 = (l1, l2)

l1 = ListNode(0, None)
l2 = ListNode(0, None)
case2 = (l1, l2)

l1 = get_l(9, 7)
l2 = get_l(9, 4)
case3 = (l1, l2)


l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
case4 = (l1, l2)

s = Solution()

res1 = s.addTwoNumbers(*case1)
pass

res2 = s.addTwoNumbers(*case2)
pass

res3 = s.addTwoNumbers(*case3)
pass

res4 = s.addTwoNumbers(*case4)
pass
