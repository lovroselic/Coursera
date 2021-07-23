#Uses python3

import sys
#test = open("tests\\3", "r")

class Node():
    def __init__(self):
        self.visited = False
        self.area = None
        self.pre = None
        self.post = None

def DFS(x, area):
    #write your code here
    def previsit(x):
        global clock
        G[x].pre = clock
        clock += 1
    
    def postvisit(x):
        global clock, order
        G[x].post = clock
        #quicksort
        order[clock] = x
        #
        clock += 1
        
        
    global clock, adj, G, order
    G[x].visited = True
    G[x].area = area
    previsit(x)
    for w in adj[x]:
        if (not G[w].visited):
            DFS(w, area)
    postvisit(x)
    return None


def toposort(adj):
    #used = [0] * len(adj)
    global order
    order = [None] * (2 * len(adj) + 1)
    #write your code here
    area = 0
    for v in range(len(adj)):
        if (not G[v].visited):
            DFS(v, area)
            area += 1
    #sort
    order = [x for x in order if x is not None]
    return order

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
    order = toposort(adj)
    for x in reversed(order):
        print(x + 1, end=' ')

