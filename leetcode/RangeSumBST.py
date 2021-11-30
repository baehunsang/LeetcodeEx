import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union

 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#class Solution:
#    ret: int = 0
#    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#        if root:
#            if root.val < low:
#                self.rangeSumBST(root.right, low, high)
#            if root.val > high:
#                self.rangeSumBST(root.left, low, high)
#            if root.val >= low and root.val <= high:
#                self.ret += root.val
#                self.rangeSumBST(root.left, low, high)
#                self.rangeSumBST(root.right, low, high)
#            return self.ret

#Not using class variable
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0
            if root.val < low:
                return dfs(root.right)
            elif root.val > high:
                return dfs(root.left)
            return dfs(root.left) + root.val + dfs(root.right)
        
    




if __name__ == '__main__':
    
    s = Solution()
    print(s.fun())