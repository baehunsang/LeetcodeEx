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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s_list = h = ListNode(None)
        while head:
            while s_list.next and s_list.next.val < head.val:
                s_list = s_list.next
            s_list.next, head.next, head = head, s_list.next, head.next
            if head and (s_list.next.val > head.val):
                s_list = h
        return h.next

if __name__ == '__main__':
    
    s = Solution()
    M_list = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    S_list = s.insertionSortList(M_list)
    while S_list:
        print(S_list.val, end=' ')
        S_list = S_list.next

