#python3

# https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm

DEBUG = False
LOG = False
if DEBUG: test = open("tests/01", "r", encoding="utf8")



class Vertex:
   def  __init__(self, id):
       self.id = id
       self.inD = 0
       self.outD = 0
       self.prev = []
       self.next = []
       
   def balanced(self):
       return self.inD == self.outD
             
class Edge:
    def __init__(self, fro, to):
        self.visited = False
        self.fro = fro
        self.to = to
       

def ReadData():
    if DEBUG:
        nV, nE = map(int, test.readline().split())
    else:
        nV, nE = map(int, input().split())
        
    Vertices = [Vertex(i+1) for i in range(nV)]
    ADJ = [[] for _ in range(nV)]
    for e in range(nE):
        if DEBUG:
            f,t = map(int, test.readline().split())
        else:
            f,t = map(int, input().split())
        edge = Edge(f,t)
        
        Vertices[f-1].next.append(edge)
        Vertices[f-1].inD += 1
        Vertices[t-1].prev.append(edge)
        Vertices[t-1].outD += 1
        ADJ[f-1].append(t-1)
        
    return nV, nE, Vertices, ADJ

def checkBalance(vertices):
    for ver in vertices:
        if ver.balanced() == False: return False
    return True

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
            
    result = [cycle[i]+1 for i in range(len(cycle)-1, 0, -1)]
    return result

# =============================================================================
# # Main
# =============================================================================

nV, nE, Vertices, ADJ = ReadData()
hasCycle = checkBalance(Vertices)
#path = Euler(ADJ)
if hasCycle == False:
    print("0")
else:
    print("1")
    path = Euler(ADJ)
    print(" ".join(map(str, path)))