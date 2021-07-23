# python3

#https://www.geeksforgeeks.org/generalized-suffix-tree-1/
import sys

NA = -1

#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample3", "r")

class Node:
    __num__ = -1
    def __init__(self, parentkey, pos = -1, substr = "", suffixlink = None):
        self.parent = parentkey
        self.children = {}
        self.suffixlink = suffixlink
        self.position = pos
        Node.__num__ += 1
        self.id = Node.__num__
        self.length = 1
        self.substring = substr
        
    def isLeaf(self):
        return len(self.children) == 0
    def isSingle(self):
        return len(self.children) == 1

def suffix_trie(text):
    root = Node(None)
    for t in range(len(text)):
        pat = text[t:]
        #if DEBUG: print(pat, t)
        node = root
        for ci in range(len(pat)):
            c = pat[ci]
            pos = t + ci
            #if DEBUG: print(c, "pos:", pos)
            if c in node.children:
                node = node.children[c]
            else:
                actNode = Node(node.id, pos, c)
                node.children[c] = actNode
                node = actNode
    return root

def printST(node):
    for c in node.children:
        print(node.children[c].substring)
        printST(node.children[c])
    
    return
        
def walkDFS(node):
    print(".......")
    print("node:", node.id, "single", node.isSingle(), "leaf", node.isLeaf()) 
    if node.isSingle():
        child = next(iter(node.children.values()))
        print("..parent", node.parent, "child", child.id)
        #concat
        while child.isSingle() or child.isLeaf():
            print("** CONCAT ** ", node.id, "with", child.id)
            #add child to node
            node.length +=1
            node.substring += child.substring
            print("==", node.substring)
            #point to next child
            if child.isLeaf():
                node.children = {}
                return
            else:
                child = next(iter(child.children.values()))
                
        node.children = {}
        return #really?
            
    print ("******")   
    for c in node.children:
        print(c, " -> ", node.children[c].id)
        walkDFS(node.children[c])
    return

def build_suffix_tree(text):
      """
      Build a suffix tree of the string text and return a list
      with all of the labels of its edges (the corresponding 
      substrings of the text) in any order.
      """
      global trie
      trie = suffix_trie(text)
      walkDFS(trie)
      print("===============================")
      printST(trie)
      #result = []
      # Implement this function yourself
      #return result
      return


if __name__ == '__main__':
    global text
    if DEBUG: 
        text = test.readline ().strip ()
    else:
        text = sys.stdin.readline ().strip ()
        #text = sys.stdin.readline().strip()
    build_suffix_tree(text)
    #if DEBUG: print(text)
    #print("\n".join(result))