# python3

#from pprint import pprint
import queue
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
# =============================================================================
#                 self.n = N
#                 self.parent = list(map(int, nodes.split()))
# =============================================================================

        def compute_height(self):
                # Replace this code with a faster implementation
                global nodeList
                nodeList = [Node(i) for i in range(self.n)]
                for i in range(self.n):
                    if (self.parent[i] == -1):
                        self.root = nodeList[i]
                    else:
                        nodeList[self.parent[i]].addChild(nodeList[i])
                Q = queue.Queue()
                Q.put(self.root)
                height = 0
                while not Q.empty():
                    height += 1
                    for j in range(Q.qsize()):
                        item = Q.get()
                        for child in item.children:
                            Q.put(child)
                return height

def main():
  global N, nodes
  #N = 5
  #nodes = "-1 0 4 0 3"     
  tree = TreeHeight()
  tree.read()
  #print(vars(tree))
  print(tree.compute_height())

threading.Thread(target=main).start()


