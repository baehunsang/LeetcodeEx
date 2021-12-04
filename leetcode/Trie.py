import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union


class TriNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TriNode()

    def insert(self, word:str)-> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TriNode()
            node = node.children[char]
        node.word = True

    def search(self, word:str)->bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.word

    def startWith(self, word:str)->bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


class Solution:
    pass


if __name__ == '__main__':
        Trie = Trie()
        print(Trie.insert("apple"))
        print(Trie.insert("appeal"))
        print(Trie.insert("appear"))
        print(Trie.startWith("app"))
        print(Trie.search("app"))
        print(Trie.search("apple"))
        print(Trie.search("appelllll"))


