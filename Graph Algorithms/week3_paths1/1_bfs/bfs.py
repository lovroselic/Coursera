#Uses python3

import sys
import queue

#test = open("tests\\1", "r")

class Node():
    def __init__(self):
        self.visited = False
        self.dist = None
        self.prev = None
       

def BFS(G,S, adj):
    Q = queue.Queue()
    G[S].dist = 0
    G[S].visited = True
    G[S].prev = "Start"
    Q.put(S)
    while (Q.qsize() > 0):
        node = Q.get()
        for v in adj[node]:
            if (not G[v].visited):
                Q.put(v)
                G[v].dist = G[node].dist + 1
                G[v].visited = True
                G[v].prev = node

def distance(adj, s, t, G):
    #BFS
    BFS(G,s, adj)
    #
    dist = G[t].dist
    if (dist is None): dist = -1
    return dist

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    #global G
    G = [Node() for i in range(len(adj))]
    print(distance(adj, s, t, G))
