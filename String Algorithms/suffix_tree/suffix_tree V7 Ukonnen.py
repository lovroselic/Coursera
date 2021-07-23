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
    print("/// walking down/// : ", active_length, edgeLength)
    if active_length >= edgeLength:
        active_edge += edgeLength
        active_length -= edgeLength
        active_node = node
        print("node changed to", text[active_node.start:active_node.end + 1])
        return True
    else:
        print("node remains")
        return False

        
def extendST(pos):
    #print("-------------------------------------")
    global root
    global active_node
    global active_edge
    global active_length
    global remainder
    char = text[pos]
    #print(pos, "char:", char)
    #needSL = False
    #leafEnd = pos
    remainder += 1
    lastNewNode = None
    #active_edge vs char blunder
    while (remainder > 0):
        if active_length == 0: active_edge = pos
        #print("while start", "rem", remainder)
# =============================================================================
#         if active_node is not None:
#             print("root:", active_node.isRoot, "active node ->", text[active_node.start:active_node.end + 1], "children:", active_node.children.keys())
# =============================================================================
        if not (text[active_edge] in active_node.children):
            #print("ADD char", text[active_edge])
            #active_node.children[char] = Node(pos, leafEnd)
            leaf = Node(pos, len(text), root)
            active_node.children[text[active_edge]] = leaf
            #print("added leaf", text[leaf.start:leaf.end + 1])
            #add SL
            if lastNewNode is not None:
                #print("**************")
                #print("SL at adding char")
                lastNewNode.slink = active_node
                lastNewNode = None
        else:
            #print("EXISTS", text[active_edge])
            nxt = active_node.children[text[active_edge]]
            #print("walk", text[nxt.start:nxt.end + 1])
            if walkDown(nxt): continue

            #ext3    
            if text[nxt.start + active_length] == text[pos]:
                #print("processing existing", text[nxt.start + active_length])            
                #add SL
                if lastNewNode is not None and not active_node.isRoot:
                    #print("**************")
                    #print("SL added at rule 3")
                    lastNewNode.slink = active_node
                    lastNewNode = None
                active_length += 1
                break;
            ###########
            #print(" ... fell of the tree ...")
            #print(" ... Splitting ...")
            #internal node
            split = Node(nxt.start, nxt.start + active_length - 1, root)
            #print(split.end)
            #print("..into internal node-->", text[split.start: split.end])
            active_node.children[text[active_edge]] = split      
            ##leaf
            leaf = Node(pos, len(text), root)
            #print("... and into leaf-->", text[leaf.start: leaf.end])
            #set children
            split.children[char] = leaf
            nxt.start += active_length
            split.children[text[nxt.start]] = nxt
            #print("..setting children; leaf-->", char, "new-->", text[nxt.start])
            #add SL
            if lastNewNode is not None:
                #print("**************")
                #print("SL added after splitting")
                lastNewNode.slink = split
            lastNewNode = split
        ###
        remainder -= 1
        #print("##### after remainder --", remainder)
        #print("recheck active:")
# =============================================================================
#         if active_node is not None:
#             print("root:", active_node.isRoot, "active node ->", text[active_node.start:active_node.end + 1], "children:", active_node.children.keys())
#         
# =============================================================================
        if active_node.isRoot and active_length > 0:
            active_length -= 1
            active_edge = pos - remainder + 1
            #print("cont by active edge", active_edge, text[active_edge])
        elif not active_node.isRoot:
            #print("cont from active_node.slink")
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
    active_edge = -1 ##
    active_length = 0
    remainder = 0
    position = 0
    for p in range(len(text)):
        extendST(p)
    
    print("=======================")
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
    #build_suffix_tree(text)
    #print("\nukonnen:")
    
    ukonnen(text)