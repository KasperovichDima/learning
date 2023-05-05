"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made
by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]
                      ) -> Optional[ListNode]:

        if list1 and list2:
            return ListNode(
                min(list1.val, list2.val), ListNode(
                    max(list1.val, list2.val), self.mergeTwoLists(
                            list1.next, list2.next
                        )
                    )
                )
        elif list1 or list2:
            lst = list1 if list1 else list2
            return ListNode(
                lst.val, self.mergeTwoLists(lst)
            )

        else:
            return None


s = Solution()

n1 = ListNode(1, ListNode(2, ListNode(4)))
n2 = ListNode(1, ListNode(3, ListNode(4)))

cases = (
    (n1, n2),
    (None, None),
    (ListNode(0), None),
)

for case in cases:
    res = s.mergeTwoLists(*case)
    print(res)
