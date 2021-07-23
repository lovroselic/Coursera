#python3

DEBUG = False
LOG = False

def loadReads():
  reads = []
  for _ in range(numReads):
    reads.append(input())

  return reads

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

def Assemble(path, Nodes, Map):
    text = ""
    while len(path) > 0:
        v = path.pop(0)
        text += Nodes[v][1]
    return text

# =============================================================================
# # main
# =============================================================================


if DEBUG: test = open("tests/gen03.txt", "r", encoding="utf8")
#02: TACTCCTCCA
#03: TGCCATGGGA
numReads = 5396
#numReads = 5

if DEBUG:
    reads = [line.strip() for line in test.readlines()]
else:
    reads = loadReads()

#nodeList = dict()
K = len(reads[0])

Nodes, Edges = deBruijn(reads)
Map = {node:i for i, node in enumerate(Nodes)}
ADJ = MakeAdj(Nodes, Edges, Map)
path = Euler(ADJ)

result = Assemble(path, Nodes, Map)
print(result)

