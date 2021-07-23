#Uses python3

import sys
#test = open("tests\\1", "r")

class Node():
    def __init__(self):
        self.visited = False
        self.area = None
        self.pre = None
        self.post = None

def Explore(x, area):   
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
    G[x].area = area
    previsit(x)
    for w in adj[x]:
        if (not G[w].visited):
            Explore(w, area)
    postvisit(x)
    return None

def number_of_components(adj):
    result = 0
    #write your code here
    for v in range(len(adj)):
        if (not G[v].visited):
            Explore(v, result)
            result += 1
    return result

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
        adj[b - 1].append(a - 1)
    global clock
    clock = 1
    global G
    G = [Node() for i in range(len(adj))]
    print(number_of_components(adj))
