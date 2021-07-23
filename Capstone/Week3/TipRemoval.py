#python3
#split to 15-mers

import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

class Node():
    def __init__(self):
        self.visited = False
        self.area = None
        self.pre = None
        self.post = None


def loadReads():
  reads = []
  for _ in range(numReads):
    reads.append(input())

  return reads

def split(reads, k):
    splitted = []
    for r in reads:
        #print(r)
        for s in range(len(r) - k + 1):
            #print(r[s:s+k])
            splitted.append(r[s:s+k])
    return splitted

def deBruijn(reads):
    nodes = set()
    edges = []
    revEdges = []
    for r in reads:
        node1 = r[:-1]
        node2 = r[1:]
        nodes.add(node1)
        nodes.add(node2)
        edges.append((node1,node2))
        revEdges.append((node2, node1))
        
    return list(nodes), edges, revEdges

def MakeAdj(Edges, Map):
    #ADJ = [[] for _ in range(len(Nodes))]
    ADJ = [set() for _ in range(len(Nodes))]
    
    for edge in Edges:
        frm = Map[edge[0]]
        to = Map[edge[1]]
        #ADJ[frm].append(to)
        ADJ[frm].add(to)
       
    ADJ = [list(s) for s in ADJ]
    return ADJ

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

# =============================================================================
# # Main
# =============================================================================

#def main():
DEBUG = True

if DEBUG:
    #test = open("tests\\t01", "r")
    test = open("dataset1.txt", "r", encoding="utf8")
    reads = [line.strip() for line in test.readlines()]
    reads = reads[1:]
    #K = 3
    K = 15
else:
    numReads = 1618
    reads = loadReads()
    K = 15
    
    
splitted = split(reads, K)
Nodes, Edges, ReverseEdges = deBruijn(splitted)
Map = {node:i for i, node in enumerate(Nodes)}
ADJ = MakeAdj(Edges, Map)
R_ADJ = MakeAdj(ReverseEdges, Map)
G = [Node() for i in range(len(Nodes))]
R = [Node() for i in range(len(Nodes))]

#global SCC_Matrix
SCC_Matrix = []

REMOVED = 0
scc = getSCC(ADJ, R_ADJ, G, R)

while scc > 1:
    #repeat, while scc > 1
    SCC_Matrix = [0 for _ in range(scc)]
    
    for i in range(len(Nodes)):
        SCC_Matrix[G[i].area] +=1
        
    Conected = SCC_Matrix.index(max(SCC_Matrix))
    
    #remove all not SCC
    toRemove = []
    for i in range(len(Nodes)):
        if G[i].area != Conected:
            toRemove.append(i)
    REMOVED += len(toRemove)
            
    for r in reversed(toRemove):
        node = Nodes[r]
        #print(r,"remove", Nodes[r])
        for i in range(len(Edges)-1, -1, -1):
            e1,e2 = Edges[i]
            #print(i,"edge", e1,e2) 
            if node == e1 or node == e2: 
                Edges.pop(i)
                ReverseEdges.pop(i)    
        Nodes.pop(r)
        
    #recreate
    Map = {node:i for i, node in enumerate(Nodes)}
    ADJ = MakeAdj(Edges, Map)
    R_ADJ = MakeAdj(ReverseEdges, Map)
    G = [Node() for i in range(len(Nodes))]
    R = [Node() for i in range(len(Nodes))]
    
    SCC_Matrix = []
    scc = getSCC(ADJ, R_ADJ, G, R)
    #end repeat

print(REMOVED)  

#main()
# This is to avoid stack overflow issues
#threading.Thread(target=main).start()