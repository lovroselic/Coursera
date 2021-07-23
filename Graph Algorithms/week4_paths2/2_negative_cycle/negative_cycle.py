#Uses python3

import sys

#test = open("tests\\1", "r")
DEBUG = False

class Node():
    def __init__(self):
        #self.dist = float("inf")
        self.dist = 10**6
        self.prev = None

def BF(adj, cost, G, changed):
    changed.clear()
    ln = len(adj)
    for v in range(ln):
        if DEBUG: print("vertice", v)
        for e in range(len(adj[v])):
            node = adj[v][e]
            C = cost[v][e]
            if DEBUG: print("... edge to", node)
            if DEBUG: print("... cost", C)
            if G[node].dist > G[v].dist + C:
                G[node].dist = G[v].dist + C
                G[node].prev = v
                changed.append(node)


def negative_cycle(adj, cost, G):
    #write your code here
    changed = []
    V = len(adj)
    G[0].dist = 0
    G[0].prev = "Start"
    G[0].changed = True
    for v in range(V):
        if DEBUG: print("######### iteration:", v + 1)
        BF(adj, cost, G, changed)
    if DEBUG: print("\n changed", changed)
    if len(changed) > 0: return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    G = [Node() for i in range(len(adj))]
    print(negative_cycle(adj, cost, G))
