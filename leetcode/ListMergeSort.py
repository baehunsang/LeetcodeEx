import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Pest your function

    def merge_list(self, l1: Optional[ListNode], l2:Optional[ListNode]):
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.merge_list(l1.next, l2)
        return l1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head and head.next):
            return head
        fast, slow, half = head, head, None
        while fast and  fast.next:
            fast, slow, half = fast.next.next, slow.next, slow
        half.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge_list(left, right)







if __name__ == '__main__':
    
    s = Solution()
    M_list = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    S_list = s.sortList(M_list)
    while S_list:
        print(S_list.val, end=' ')
        S_list = S_list.next

