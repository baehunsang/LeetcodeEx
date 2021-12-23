import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
	if not prerequisites:
		return [crs  for crs in range(numCourses)]
	graph = collections.defaultdict(list)
	#	Kahn's algorithm
	#This algorithm is BFS, which starts from a node which has no income edge.
	
	#count income edge
	income_list = [0]*numCourses
	#genarate graph
	for dst, src in prerequisites:
		graph[src].append(dst)
		income_list[dst] += 1
	
	#Empty list that will contain the sorted elements
	L = []
	#Queue of all nodes with no incoming edge
	Q = collections.deque(node for node, income in enumerate(income_list) if income == 0)
	#BFS
	#O(V + E)
	while Q:
		node = Q.popleft()
		L.append(node)
		while graph[node]:
			#remove adj edge
			adj_node = graph[node].pop()
			income_list[adj_node] -= 1
			if income_list[adj_node] == 0:
				Q.append(adj_node)
	if any(graph[key] for key in list(graph)):
		return []
	return L			
			
	
print(findOrder(4, [[1, 0], [2, 0], [3, 1],[3, 2]]))
	
	