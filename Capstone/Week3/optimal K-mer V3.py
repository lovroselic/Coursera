#python3
#from collections import OrderedDict


DEBUG = False
LOG = False

def loadReads():
  reads = []
  for _ in range(numReads):
    reads.append(input())

  return reads

# =============================================================================
# #
# =============================================================================

def deBruijn(reads):
    nodes = set()
    edges = []
    for r in reads:
        node1 = r[:-1]
        node2 = r[1:]
        nodes.add(node1)
        nodes.add(node2)
        edges.append((node1,node2))
        #print(r, ":", node1, node2)
        
    return list(nodes), edges

def split(reads, k):
    splitted = []
    for r in reads:
        #print(r)
        for s in range(len(r) - k + 1):
            #print(r[s:s+k])
            splitted.append(r[s:s+k])
    return splitted

def MakeAdj(Nodes, Edges, Map):
    ADJ = [[] for _ in range(len(Nodes))]
    
    for edge in Edges:
        #print("edge", edge)
        frm = Map[edge[0]]
        to = Map[edge[1]]
        #print("...", frm, to)
        ADJ[frm].append(to)
        
    return ADJ

def Euler(ADJ):
    currentpath = [0]
    cycle = []
    
    while len(currentpath) > 0:
        vertex = currentpath[-1]
        if ADJ[vertex]:
            nextVertex = ADJ[vertex].pop()
            currentpath.append(nextVertex)
        else:
            cycle.append(currentpath.pop())
            
    result = [cycle[i] for i in range(len(cycle)-1, 0, -1)]
    return result

# =============================================================================
# # main
# =============================================================================


if DEBUG: test = open("tests/01", "r", encoding="utf8")
numReads = 400

if DEBUG:
    reads = [line.strip() for line in test.readlines()]
else:
    reads = loadReads()
    
K = len(reads[0])

for k in range(K-1, 1, -1):
    #print("k", k)
    splittedReads = split(reads, k)
    Nodes, Edges = deBruijn(splittedReads)
    Map = {node:i for i, node in enumerate(Nodes)}
    ADJ = MakeAdj(Nodes, Edges, Map)
    path = Euler(ADJ)
    if len(path) == len(Edges):
        break
    
print(k)
    