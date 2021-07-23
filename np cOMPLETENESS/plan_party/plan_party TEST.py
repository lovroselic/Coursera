#uses python3

import sys
import threading

#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
if DEBUG: test = open("tests\\66", "r")
global T

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.fun = -1
        
    def hasChildren(self, parent):
        count = 0
        for child in self.children:
            if child != parent:
                count += 1
        if count > 0:
            return True
        else:
            return False


def ReadTree():
    if DEBUG:
        size = int(test.readline())
    else:  
        size = int(input())
        
    if DEBUG:
        tree = [Vertex(w) for w in map(int, test.readline().split())]
    else:
        tree = [Vertex(w) for w in map(int, input().split())]
        
    for i in range(1, size):
        if DEBUG:
            a, b = list(map(int, test.readline().split()))
        else:
            a, b = list(map(int, input().split()))
            
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def displayTree(tree, vertex, parent):
    print("NODE", vertex + 1, "FUN", tree[vertex].fun)
    for child in tree[vertex].children:
        if child != parent:
            displayTree(tree, child, vertex)

def dfs(tree, vertex, parent):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)
    
    if tree[vertex].hasChildren(parent) != True:
        tree[vertex].fun = tree[vertex].weight
    else:
        M1 = tree[vertex].weight
        for u in tree[vertex].children:
            if u != parent:
                for w in tree[u].children:
                    if w != vertex:
                        M1 += tree[w].fun
        M0 = 0
        for u in tree[vertex].children:
            if u != parent:
                M0 += tree[u].fun     
        tree[vertex].fun = max(M1, M0) 
        return


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)
    if LOG:
        print("\TREE ...........")
        displayTree(tree, 0, -1)
    return tree[0].fun



tree = ReadTree();
# =============================================================================
# if LOG:
#     print("\TREE ...........")
#     displayTree(tree, 0, -1)
# =============================================================================

weight = MaxWeightIndependentTreeSubset(tree);
print(weight)


# This is to avoid stack overflow issues
#threading.Thread(target=main).start()


