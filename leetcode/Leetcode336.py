import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union

def isPal(word: str)->bool:
	if word:
		return word == word[::-1]
	return False


class TriNode:
	def __init__(self):
		self.word = -1
		self.is_next_pal = []
		#	no more need to detect presence of charactor
		self.children = collections.defaultdict(TriNode)
		
class Trie:
	def __init__(self):
		self.root = TriNode()
		
	def insert(self, idx: int, word: str)-> None:
		node = self.root
		for i ,char in enumerate(word[::-1]):
			if isPal(word[0: len(word) - i]):
				node.is_next_pal.append(idx)
			node = node.children[char]
		node.word = idx
	
	
	def search(self, idx:int, word:str)->List:
		ret = []
		node = self.root
		# ex) 'a', ''
		#if node.word >= 0 and node.word != idx:
		#		if isPal(word[:]):
		#			ret.append([idx, node.word])
		#for i, char in enumerate(word):
		#	if char not in node.children:
		#		return ret
		#	node = node.children[char]
			# word = ssll, ss
		#	if node.word >= 0 and node.word != idx:
		#		if isPal(word[i + 1:]):
		#			ret.append([idx, node.word])
		while word:
			# word = ssll, ss
			if node.word >= 0:
				if isPal(word) and node.word != idx:
					ret.append([idx, node.word])
					
			#No exist matching pair
			if word[0] not in node.children:
				return ret
			node = node.children[word[0]]
			word = word[1:]
			
		# word = ssll, llss
		if node.word >= 0 and node.word != idx:
			ret.append([idx, node.word])
		
		#ex) word = ss, llss 
		for idx2 in node.is_next_pal:
			ret.append([idx, idx2])
			
		return ret
		
		
		
class Solution:
		def palindromPairs(self, words: List[str]) -> List[List[int]]:
			my_trie = Trie()
			ret = []
			for idx, word in enumerate(words):
				my_trie.insert(idx, word)
				
			for idx, word in enumerate(words):
				ret.extend(my_trie.search(idx, word))
				
			return ret
if __name__ == '__main__':
	s = Solution()
	
	words = ['d', ""]
	words2 = ['abcd', 'dcba', 'lls', 's', 'sssll']
	print(s.palindromPairs(words))

