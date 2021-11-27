import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = ["#"]
        if not root:
            return '# #'
        Q = collections.deque([root])
        while Q:
            node = Q.popleft()
            if node:
                ret.append(str(node.val))
                Q.append(node.left)
                Q.append(node.right)
            else:
                ret.append("#")
        return ' '.join(ret)

    def deserialize(self, data):
        """Decodes your encoded num to tree.
        
        :type num: str
        :rtype: TreeNode
        """
        num = data.split()
        runner = 1
        if num[runner] != '#':
            root = TreeNode(int(num[runner]))
        else:
            return None
        Q = collections.deque([root])
        while Q:
            node = Q.popleft()
            if runner < len(num) - 1:
                if num[runner + 1] != '#':
                    node.left = TreeNode(int(num[runner + 1]))
                    Q.append(node.left)
                runner += 1
                if num[runner + 1] != '#':
                    node.right = TreeNode(int(num[runner + 1]))
                    Q.append(node.right)
                runner += 1
        return root
    



# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = ser.serialize(deser.deserialize("# 1 2 3 # # 4 5 # # # #"))
print(ans)
