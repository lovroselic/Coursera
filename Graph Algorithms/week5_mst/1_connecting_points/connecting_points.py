#Uses python3
import sys
import math
import queue

class Node():
    def __init__(self):
        self.cost = float("inf")
        self.parent = None

#test = open("tests\\2", "r")
DEBUG = False

def minCost(G, PQ):
    m = float("inf")
    i = -1
    for pq in PQ:
        if G[pq].cost < m:
            m = G[pq].cost
            i = pq
    return i

def dist(s,t):
    global x, y
    return math.sqrt((x[s] - x[t])**2 + (y[s] - y[t])**2)

def Prim(G):
    start = 0
    G[start].cost = 0
    G[start].parent = -1
    PQ = []
    for g in range(len(G)):
        PQ.append(g)
          
    while (len(PQ) > 0):
        if DEBUG: print("PQ", PQ)
        node = minCost(G, PQ)
        cost = G[node].cost
        if DEBUG: print("node", node, "cost", cost)
        PQ.remove(node)
        
        for z in range(n):
            if z in PQ:
                w = dist(node,z)
                if G[z].cost > w:
                    G[z].cost = w
                    G[z].parent = node
                    if DEBUG: print("z", z, w)
    
def minimum_distance(x, y):
    result = 0.
    #write your code here
    for node in G:
        result += node.cost
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    global n
    n = data[0]
    global x, y
    x = data[1::2]
    y = data[2::2]
    G = [Node() for i in range(n)]
    Prim(G)
    print("{0:.9f}".format(minimum_distance(x, y)))
