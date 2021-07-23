#Uses python3

import sys
import queue
import math

#test = open("tests\\3", "r")
DEBUG = False

class Node():
    def __init__(self):
        self.dist = float("inf")
        self.prev = None
        

def DIJSKTRA(G, S, adj):
    Q = queue.PriorityQueue()
    G[S].dist = 0
    G[S].prev = "Start"
    Q.put((G[S].dist, S))
    while (not Q.empty()):
        node = Q.get()
        u = node[1]
        if DEBUG: print(node,"-> node:", u)
        for x in range(len(adj[u])):
            v = adj[u][x]
            c = cost[u][x]
            if DEBUG: print("...vertice", v)
            if DEBUG: print("...cost", c)
            if G[v].dist > G[u].dist + c:
                G[v].dist = G[u].dist + c
                G[v].prev = u
                Q.put((G[v].dist, v))

def distance(adj, cost, s, t, G):
    #write your code here
    DIJSKTRA(G, s, adj)
    dist = G[t].dist
    if math.isinf(dist): return -1
    return dist


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    global edges
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    G = [Node() for i in range(len(adj))]
    print(distance(adj, cost, s, t, G))
