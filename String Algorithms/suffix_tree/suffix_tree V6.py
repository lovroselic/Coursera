# python3

#https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english
#http://brenden.github.io/ukkonen-animation/
#https://gist.github.com/makagonov/f7ed8ce729da72621b321f0ab547debb
#https://github.com/mutux/Ukkonen-s-Suffix-Tree-Algorithm/blob/master/suffixtree.py

import sys
sys.setrecursionlimit(15000)
#import time

#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample9", "r")

class Node:
    def __init__(self, pos = -1):
        self.children = {}
        self.position = pos
        self.length = 1
        self.printed = False
        
    def isLeaf(self):
        return len(self.children) == 0
    def isSingle(self):
        return len(self.children) == 1
    def printSubstring(self, text):
        if self.position == -1: return
        print(text[self.position: self.position + self.length])
        self.printed = True

def suffix_trie(text):
    root = Node()
    for t in range(len(text)):
        pat = text[t:]
        node = root
        for ci in range(len(pat)):
            c = pat[ci]
            pos = t + ci
            if c in node.children:
                node = node.children[c]
            else:
                actNode = Node(pos)
                node.children[c] = actNode
                node = actNode
    return root
      
def walkDFS(node):
    if node.isSingle():
        child = next(iter(node.children.values()))
        node.length +=1 
        if child.isLeaf():
            node.children = {}
            node.printSubstring(text)
            return
        else:
            node.children = child.children   
        if child.isSingle():
            walkDFS(node)

    if not node.printed: node.printSubstring(text)    
    for c in node.children:
        walkDFS(node.children[c])
    return

def build_suffix_tree(text):
      global trie
      trie = suffix_trie(text)
      walkDFS(trie)
      return
  
def ukonnen(text):
    pass


if __name__ == '__main__':
    global text
    if DEBUG: 
        text = test.readline ().strip ()
    else:
        text = sys.stdin.readline ().strip ()
    build_suffix_tree(text)
    print("\nukonnen:")
    ukonnen(text)