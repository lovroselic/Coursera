#Uses python3

import sys

#test = open("tests\\2", "r")

class Node():
    def __init__(self):
        self.visited = False
        self.pre = None
        self.post = None
        
def FindPath(x, y):
    
    def previsit(x):
        global clock
        G[x].pre = clock
        clock += 1
    
    def postvisit(x):
        global clock
        G[x].post = clock
        clock += 1
        
    global clock, adj, G
    G[x].visited = True
    previsit(x)
    for w in adj[x]:
        if (not G[w].visited):
            FindPath(w, y)
    postvisit(x)
    return None

def reach(x, y):
    global adj
    #write your code here
    #print("xy", x,y)
    global G
    G = [Node() for i in range(len(adj))]
    FindPath(x, y)
    if (not G[y].visited): return 0
    if (G[x].pre < G[y].pre and G[x].post > G[y].post): return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = test.read()
    #print(input)
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    global adj
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    global clock
    clock = 1
    print(reach(x, y))
