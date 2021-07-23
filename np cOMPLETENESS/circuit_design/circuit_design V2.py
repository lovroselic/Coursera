# python3

#https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/
#https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
#https://stackoverflow.com/questions/4664050/iterative-depth-first-tree-traversal-with-pre-and-post-visit-at-each-node/60803684#60803684

import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

DEBUG = False
#DEBUG = True
#LOG = True
LOG = False
if DEBUG: test = open("tests\\06", "r")

def lit_to_vertex(lit):
    v = (abs(lit)-1) * 2
    if lit > 0: v += 1
    return v

def vertex_to_lit(v):
    lit = (v + 1)// 2
    if v % 2 != 1:
        lit *= -1
        lit -= 1
    return lit

class Node():
    def __init__(self):
        self.visited = False
        self.area = None
        self.pre = None
        self.post = None

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



def getSCC(adj, R_adj, G, GR):
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


def isSatisfiable(G):
    for L in range(1, n+1):
        if G[lit_to_vertex(L)].area == G[lit_to_vertex(-L)].area: return False
    return True

def createEdges():
    edges = []
    reversed_edges = []
    for c in clauses:
        #print("clause", c)
        edges.append((lit_to_vertex(-c[0]), lit_to_vertex(c[1])))
        edges.append((lit_to_vertex(-c[1]), lit_to_vertex(c[0])))
        reversed_edges.append((lit_to_vertex(c[1]), lit_to_vertex(-c[0])))
        reversed_edges.append((lit_to_vertex(c[0]), lit_to_vertex(-c[1])))
        
    return edges, reversed_edges

def solve():
    #global solution
    solution = [None] * n
    area = -1

    for x in reversed(order):
        #print("vertex", x,"c of scc", G[x].area)
        #area = G[x].area
        L = vertex_to_lit(x)          
        index = (abs(L)) - 1
        if solution[index] is None:
            if L > 0:
                solution[index] = 1
            else:
                solution[index] = 0
    return solution

def main():
    global n, m, clauses
    if DEBUG:
        n, m = map(int, test.readline().split())
        clauses = [ list(map(int, test.readline().split())) for i in range(m) ]
    else:
        n, m = map(int, input().split())
        clauses = [ list(map(int, input().split())) for i in range(m) ]
         
    #implication graph
        
    edges, reversed_edges = createEdges()
    adj = [[] for _ in range(2*n)]
    R_adj = [[] for _ in range(2*n)]
    
    for (a, b) in edges:
        #adj[a - 1].append(b - 1)
        adj[a].append(b)
        
    for (a, b) in reversed_edges:
        R_adj[a].append(b)
        
    global clock
    clock = 1
    
    G = [Node() for i in range(len(adj))]
    R = [Node() for i in range(len(R_adj))]
    
    SCC = getSCC(adj, R_adj, G, R)
    
    
    if isSatisfiable(G):
        print("SATISFIABLE");
        solution = solve()
        print(" ".join(str(i+1 if solution[i] else -(i+1)) for i in range(n)))
    else:
        print("UNSATISFIABLE")

#main()
# This is to avoid stack overflow issues
threading.Thread(target=main).start()

