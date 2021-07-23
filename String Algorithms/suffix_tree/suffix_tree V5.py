# python3

#https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english
#http://brenden.github.io/ukkonen-animation/
import sys
sys.setrecursionlimit(11000)
import time

DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample3", "r")

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

def printST(node):
    for c in node.children:
        print(text[node.children[c].position: node.children[c].position + node.children[c].length])
        printST(node.children[c])   
    return
      
def walkDFS(node):
    if node.isSingle():
        child = next(iter(node.children.values()))
        node.length +=1 
        if child.isLeaf():
            node.children = {}
            #print(text[node.position: node.position + node.length])
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
      #first_time = time.perf_counter()
      #start_time = time.perf_counter()
      trie = suffix_trie(text)
      #end_time = time.perf_counter()
      #print("build: --- %.4f ---" %(end_time - start_time))
      #start_time = time.perf_counter()
      walkDFS(trie)
      #end_time = time.perf_counter()
      #print("walk: --- %.4f ---" %(end_time - start_time))
      #start_time = time.perf_counter()
      #printST(trie)
      #end_time = time.perf_counter()
      #print("print: --- %.4f ---" %(end_time - start_time))
      #print("all: --- %.4f ---" %(end_time - first_time))
      return


if __name__ == '__main__':
    global text
    if DEBUG: 
        text = test.readline ().strip ()
    else:
        text = sys.stdin.readline ().strip ()
    #if DEBUG: print(text)
    build_suffix_tree(text)