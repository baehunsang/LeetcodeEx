import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union

def isPal(s):
	return s == s[::-1]


def palindromePairs(words: List[str]) -> List[List[int]]:
	ret = []
	
	#B
	rev_dict = {w[::-1]: i for (i, w) in enumerate(words)}
	
	#for A in words
	for idx, word in enumerate(words):	
		#len(A) == len(B)
		if word in rev_dict and idx != rev_dict[word]:
			ret.append([idx, rev_dict[word]])
		#	The window for prefix moves to left and window for postfix to right
		for j in range(1, len(word)+1):
			#if prefix in dict
			if word[:-j] in rev_dict and isPal(word[-j:]):
				ret.append([idx, rev_dict[word[:-j]]])
			#if postfix in dict
			if word[j:] in rev_dict and isPal(word[:j]):
				ret.append([rev_dict[word[j:]], idx])
	return ret