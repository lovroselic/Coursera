#Uses python3
#https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

import sys
#test = open("tests\\1", "r")

class Node():
    def __init__(self):
        self.visited = False
        self.area = None
        self.pre = None
        self.post = None

def Explore(x):   
    #print("explore:", x)      
    global adj, G, cycle,stack
    if (G[x].visited): return

    G[x].visited = True
    stack[x] = True
    for w in adj[x]:
        #print("..TRY", w)
        if (not G[w].visited):
            #print(".....next", w)
            Explore(w)
        else:
            if (stack[w]):
                #print("CYCLE!")
                cycle = True
                return
        stack[w] = False
    return

def acyclic(adj):
    global cycle, stack
    cycle = False
    for v in range(len(adj)):
        #print("v ROUND", v)
        stack = [False for i in range(len(adj))]
        #if (cycle): break
        if (not G[v].visited):
            Explore(v)
        if (cycle): break
    if (cycle): return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    global adj
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    global clock
    clock = 1
    global G
    G = [Node() for i in range(len(adj))]
    print(acyclic(adj))
