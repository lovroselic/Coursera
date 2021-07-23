#python3

filename = "ads1_week4_reads.fq"

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

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
            
    result = [cycle[i] for i in range(len(cycle)-1, -1, -1)]
    #result = [cycle[i] for i in range(len(cycle)-1, 0, -1)]
    return result

def Assemble(path, Nodes, Map):
    text = ""
    while len(path) > 0:
        v = path.pop(0)
        text += Nodes[v][1]
        #text += Nodes[v][-1]
    return text

def kmerize(reads, k):
    kmers = []
    for r in reads:
        for i in range(0, len(r)-k +1):
            kmer = r[i:i+k]
            kmers.append(kmer)
    return kmers
# =============================================================================
# # main
# =============================================================================

#15894
#inp,_ = readFastq(filename)
reads,_ = readFastq(filename)
reads = list(set(reads))
K = len(reads[0])
#K = 10
#reads = kmerize(inp, K)
Nodes, Edges = deBruijn(reads)
Map = {node:i for i, node in enumerate(Nodes)}
ADJ = MakeAdj(Nodes, Edges, Map)
path = Euler(ADJ)
result = Assemble(path, Nodes, Map)
print(result, len(result))



