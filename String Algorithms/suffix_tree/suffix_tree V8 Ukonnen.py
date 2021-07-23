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
if DEBUG: test = open("sample_tests\\sample6", "r")

global root

class Node:
    _count = -1
    def __init__(self, start, end, slink = None, isRoot = False):
        self.children = {}
        self.start = start
        self.end = end
        #self.index = -1
        self.slink = slink
        self.isRoot = isRoot
        Node._count += 1
        self.id = Node._count 
        
    def edgeLength(self):
        if self.isRoot: return 0
        return self.end - self.start + 1;
    
    
def walkDown(node):
    global active_node
    global active_edge
    global active_length
    
    edgeLength = node.edgeLength()
    if active_length >= edgeLength:
        active_edge += edgeLength
        active_length -= edgeLength
        active_node = node
        return True
    else:
        return False

        
def extendST(pos):
    global root
    global active_node
    global active_edge
    global active_length
    global remainder
    char = text[pos]
    remainder += 1
    lastNewNode = None
    while (remainder > 0):
        if active_length == 0: active_edge = pos
        
        if not (text[active_edge] in active_node.children):
            leaf = Node(pos, len(text), root)
            active_node.children[text[active_edge]] = leaf
            
            if lastNewNode is not None:
                lastNewNode.slink = active_node
                lastNewNode = None
        else:
            nxt = active_node.children[text[active_edge]]
            if walkDown(nxt): continue   
            if text[nxt.start + active_length] == text[pos]:
                if lastNewNode is not None and not active_node.isRoot:
                    lastNewNode.slink = active_node
                    lastNewNode = None
                active_length += 1
                break;

            split = Node(nxt.start, nxt.start + active_length - 1, root)
            active_node.children[text[active_edge]] = split      
            leaf = Node(pos, len(text), root)
            split.children[char] = leaf
            nxt.start += active_length
            split.children[text[nxt.start]] = nxt
            
            if lastNewNode is not None:
                lastNewNode.slink = split
                
            lastNewNode = split

        remainder -= 1
        if active_node.isRoot and active_length > 0:
            active_length -= 1
            active_edge = pos - remainder + 1
        elif not active_node.isRoot:
            active_node = active_node.slink
    
    return
  
def ukonnen(text):
    global root
    global active_node
    global active_edge
    global active_length
    global remainder
    root = Node(-1, -1, None, True)
    active_node = root
    active_edge = -1 
    active_length = 0
    remainder = 0
    for p in range(len(text)):
        extendST(p)
    
    printST(root)
    return
    
def printST(node):
    for c in node.children:
        print(text[node.children[c].start: node.children[c].end + 1])
        printST(node.children[c])   
    return    


if __name__ == '__main__':
    global text
    if DEBUG: 
        text = test.readline ().strip ()
    else:
        text = sys.stdin.readline ().strip ()
    ukonnen(text)