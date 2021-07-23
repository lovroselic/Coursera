#uses python3

import sys
import threading

#DEBUG = False
DEBUG = True
#LOG = True
LOG = False
if DEBUG: test = open("tests\\03", "r")
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
    if LOG: 
        print("\n* vertex", vertex, "children", tree[vertex].children)
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.
    #if LOG: print("** child", child)
    #for leaf in tree[child].children:
        #if LOG: print("*** leaf", leaf +1)
        
    #vertex
    if LOG: 
        print("*** vertex", vertex, "Parent:", parent)
        print("\n**** NODE", vertex + 1, "W:",tree[vertex].weight, "fun:", tree[vertex].fun)
    
    if tree[vertex].hasChildren(parent) != True:
        if LOG: print("~~~~~~~~ no children")
        tree[vertex].fun = tree[vertex].weight
    else:
        M1 = tree[vertex].weight
        for u in tree[vertex].children:
            if u != parent:
                if LOG:
                    print("GC, child", u+1, tree[u].children)
                for w in tree[u].children:
                    if w != vertex:
                        print("GC, gc", w+1, "fun", tree[w].fun)
                        M1 += tree[w].fun
        if LOG: print("M1", M1)
        M0 = 0
        for u in tree[vertex].children:
            if u != parent:
                if LOG:
                    print("C, child", u+1, "fun", tree[u].fun)
                M0 += tree[u].fun
        if LOG: print("M0", M0)     
        tree[vertex].fun = max(M1, M0)
        if LOG: print("FUN", tree[vertex].fun)
        


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)
    # You must decide what to return.
    if LOG:
        print("\nlast fun", tree[0].fun)
        print("\TREE ...........")
        displayTree(tree, 0, -1)
    return tree[0].fun


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()


