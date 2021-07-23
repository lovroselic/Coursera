# python3

#https://www.geeksforgeeks.org/generalized-suffix-tree-1/
#https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english
#http://brenden.github.io/ukkonen-animation/
import sys

NA = -1

#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample6", "r")

class Node:
    def __init__(self, pos = -1):
        self.children = {}
        self.position = pos
        self.length = 1
        
    def isLeaf(self):
        return len(self.children) == 0
    def isSingle(self):
        return len(self.children) == 1

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
        
        #concat, node is single but not child 
        if not (child.isSingle() or child.isLeaf()):
            node.length +=1
            node.children = child.children
        else:   
            #concat, node is single so it's child
            while child.isSingle() or child.isLeaf():
                node.length +=1
                if child.isLeaf():
                    node.children = {}
                    return
                else:
                    node.children = child.children
                    child = next(iter(child.children.values()))
            #node not finished!
            walkDFS(node)
            
    for c in node.children:
        walkDFS(node.children[c])
    return

def build_suffix_tree(text):
      global trie
      trie = suffix_trie(text)
      walkDFS(trie)
      if DEBUG: print("===============================")
      printST(trie)
      return


if __name__ == '__main__':
    global text
    if DEBUG: 
        text = test.readline ().strip ()
    else:
        text = sys.stdin.readline ().strip ()
    if DEBUG: print(text)
    build_suffix_tree(text)