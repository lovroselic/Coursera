
from itertools import permutations
from collections import defaultdict

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
    
def overlap(a, b, min_length=3):

    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match
        
def naive_overlap_map(reads,k):
    olaps = {}
    for a,b in permutations(reads,2):
        olen = overlap(a,b, min_length = k)
        if olen > 0:
            olaps[(a,b)] = olen
    return olaps

def createKMerDict(reads, k):
    D = defaultdict(set)
    for r in reads:
        for i in range(0, len(r)-k +1):
            kmer = r[i:i+k]
            D[kmer].add(r)
    return D
    
def Overlap_all_pairs(reads, min_length = 30):
    D = createKMerDict(reads, k)
    overlap_graph = defaultdict(set)
    for read in reads:
        read_suffix = read[-min_length:]
        #print(read, read_suffix)
        readSet = D[read_suffix]
        readSet.discard(read)
        #print("..", readSet)
        for B in readSet:
            #print("....compar to", B)
            olap = overlap(read, B, min_length)
            #print(".....olap", olap)
            if olap > 0:
                overlap_graph[(read,B)] = olap
    return overlap_graph


def countActiveNodes(GR):
    nodes = defaultdict(int)
    for edge in GR:
        node = edge[0]
        nodes[node] += 1
    return nodes

def scs(ss):
    shortest = None
    for sspers in permutations(ss):
        sup = sspers[0]
        for i in range(len(ss)-1):
            olen = overlap(sspers[i], sspers[i+1], 1)
            sup += sspers[i+1][olen:]
        if shortest is None or len(sup) < len(shortest):
            shortest = sup
    return shortest

def scs2(ss):
    shortest = defaultdict(list)
    for sspers in permutations(ss):
        sup = sspers[0]
        for i in range(len(ss)-1):
            olen = overlap(sspers[i], sspers[i+1], 1)
            sup += sspers[i+1][olen:]
        shortest[len(sup)].append(sup) 
    return shortest
            
def pick_max_overlap(reads, k):
    readA, readB = None, None
    best_olen = 0
    for a,b in permutations(reads,2):
        olen = overlap(a, b, k)
        if olen > best_olen:
            readA, readB = a,b
            best_olen = olen
    return readA, readB, best_olen

def pick_max_overlap_fast(GR):
    if len(GR) == 0: return 0, 0, 0
    max_key = max(GR, key=lambda k: GR[k])
    #print(max_key)
    A = max_key[0]
    B = max_key[1]
    olap = GR[max_key]
    GR.pop(max_key)
    #print(A, B, olap)
    return A, B, olap

# =============================================================================
# def greedy_scs(reads,k):
#     readA, readB, olen = pick_max_overlap(reads, k)
#     while olen > 0:
#         reads.remove(readA)
#         reads.remove(readB)
#         reads.append(readA + readB[olen:])
#         readA, readB, olen = pick_max_overlap(reads, k)
#     return ''.join(reads)
# =============================================================================

def greedy_scs(reads,k):
    #readA, readB, olen = pick_max_overlap(reads, k)
    GR = Overlap_all_pairs(reads, k)
    readA, readB, olen = pick_max_overlap_fast(GR)
    print("start", reads)
    print(readA, readB, olen)
    while olen > 0:
        print("while", reads)
        reads.remove(readA)
        reads.remove(readB)
        reads.append(readA + readB[olen:])
        print("..removed",readA, readB)
        print("..appended", readA + readB[olen:])
        GR = Overlap_all_pairs(reads, k)
        readA, readB, olen = pick_max_overlap_fast(GR)
        print(readA, readB, olen, reads)
    return ''.join(reads)

# =============================================================================
# # MAin
# =============================================================================

reads = ["ABC", "BCD", "CDE", "DEFG", "FGH"]
#t1 = greedy_scs(test,2)
#print(t1)
k = 2
D = createKMerDict(reads, k)
#GR = Overlap_all_pairs(reads, D, k)
test = greedy_scs(reads,k)