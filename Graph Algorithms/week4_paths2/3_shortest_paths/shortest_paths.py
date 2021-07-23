#Uses python3

import sys
import queue
import math

#test = open("tests\\3", "r")
DEBUG = False

class Node():
    def __init__(self):
        self.dist = float("inf")
        #self.dist = 10**19
        self.prev = None
        self.visited = False
        
def BF(adj, cost, G, changed):
    changed.clear()
    ln = len(adj)
    for v in range(ln):
        #if DEBUG: print("vertice", v)
        for e in range(len(adj[v])):
            node = adj[v][e]
            C = cost[v][e]
            #if DEBUG: print("... edge to", node)
            #if DEBUG: print("... cost", C)
            if G[node].dist > G[v].dist + C:
                G[node].dist = G[v].dist + C
                G[node].prev = v
                changed.append(node)

def BFS(G, adj, Q):

    while (Q.qsize() > 0):
        node = Q.get()
        for v in adj[node]:
            if (not G[v].visited):
                Q.put(v)
                G[v].dist = float("-inf")
                G[v].visited = True
                #G[v].prev = node


def shortet_paths(adj, cost, s, distance, reachable, shortest, G):
    #write your code here
    changed = []
    V = len(adj)
    G[s].dist = 0
    G[0].prev = "Start"
    #G[0].changed = True
    for v in range(V):
        #if DEBUG: print("######### iteration:", v + 1)
        BF(adj, cost, G, changed)
    if DEBUG: print("\n changed", changed)
    #BFS on all in changed
    Q = queue.Queue()
    for A in changed:
        Q.put(A)
        BFS(G, adj, Q)     
    return


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    G = [Node() for i in range(len(adj))]
    shortet_paths(adj, cost, s, distance, reachable, shortest, G)
    for g in range(n):
        if G[g].dist == float("inf"):
            print('*')
        elif G[g].dist == float("-inf"):
            print('-')
        else:
            print(G[g].dist)
# =============================================================================
#     for x in range(n):
#         if reachable[x] == 0:
#             print('*')
#         elif shortest[x] == 0:
#             print('-')
#         else:
#             print(distance[x])
# =============================================================================

