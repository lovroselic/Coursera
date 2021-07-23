#Uses python3
#Run DFS(Gr)
#

import sys
test = open("tests\\3", "r")

sys.setrecursionlimit(200000)

class Node():
    def __init__(self):
        self.visited = False
        self.area = None
        self.pre = None
        self.post = None
        #self.SCC_visited = False
        #self.SCC = None

def DFS(x, area, g, ad, sort):
    def previsit(x):
        global clock
        g[x].pre = clock
        clock += 1
    
    def postvisit(x):
        global clock
        g[x].post = clock
        #quicksort
        sort[clock] = x
        #
        clock += 1       
        
    global clock
    g[x].visited = True
    g[x].area = area
    previsit(x)
    for w in ad[x]:
        if (not g[w].visited):
            DFS(w, area, g, ad, sort)
    postvisit(x)
    return None


def number_of_strongly_connected_components(adj, R_adj, G, GR):
    area = 0
    global order
    order = [None] * (2 * len(R_adj) + 1)
    global clock
    clock = 1
    for v in range(len(R_adj)):
        if (not GR[v].visited):
            DFS(v, area, GR, R_adj, order)
            area += 1
    #ordered in postorder:
    order = [x for x in order if x is not None]
    SCC = 0
    #reverse
    dummy = [None] * (2 * len(R_adj) + 1)
    clock = 1
    for x in reversed(order):
        if (not G[x].visited):
            DFS(x, SCC, G, adj, dummy)
            SCC += 1
    return SCC

if __name__ == '__main__':
    #input = sys.stdin.read()
    input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #reverse edges
    reversedEdges = list(zip(data[1:(2 * m):2], data[0:(2 * m):2]))
    global adj, R_adj
    adj = [[] for _ in range(n)]
    R_adj = [[] for _ in range(n)]
    
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        
    for (a, b) in reversedEdges:
        R_adj[a - 1].append(b - 1)
        
    global clock
    clock = 1

    G = [Node() for i in range(len(adj))]
    R = [Node() for i in range(len(R_adj))]

    print(number_of_strongly_connected_components(adj, R_adj, G, R))
