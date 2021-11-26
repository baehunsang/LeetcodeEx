import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Pest your function
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    	if n <= 2:
    		return [i for i in range(n)]
    	G = collections.defaultdict(list)
    	for f, t in edges:
    		G[f].append(t)
    		G[t].append(f)
    	# adjationcy list
    	
    	#leves = []
    	leves = collections.deque()
    	
    	for node in G:
    		if len(G[node]) <= 1:
    			leves.append(node)
    	#enqeue leaf node
    	#O(n)
    	 
    	while n > 2:
    		new_leves = collections.deque()
    		n -= len(leves)
    	#	for leaf in leves:
    	#		node = G[leaf].pop()
    	#		G[node].remove(leaf)
    	#		G.pop(leaf)
    		while leves:
    			leaf = leves.popleft()
    			node = G[leaf].pop()
    			G[node].remove(leaf)
    			if len(G[node]) == 1:
    				new_leves.append(node)
    		leves = new_leves
    	#O(n-(1 or 2))	-> O(n)	
    		
    		#new_leves = []
    		#for node in G:
    		#	if len(G[node]) <= 1:
    		#		new_leves.append(node)
    		#leves = new_leves 
    		#O(nh) h -> the height of the tree
    		#useless search
    	return list(leves)
    	
    		



if __name__ == '__main__':
    
    s = Solution()
    e =  [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print(s.findMinHeightTrees(6, e))
    