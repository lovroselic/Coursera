# python3

# =============================================================================
# # https://pypi.org/project/pycosat/
# # n vertice
# # m edge
# # CNF : p cnf V(vars) C(clauses)
# #
# # output C V
# # C lines: clause; k terms; 0 terminated
# # Ensure that 1 ≤ 𝐶 ≤ 5000 and 1 ≤ 𝑉 ≤ 3000.
# =============================================================================



#import pycosat
import itertools

DEBUG = False
#DEBUG = True
#LOG = True
LOG = False
if DEBUG: test = open("tests\\02", "r")

def var(i, j):
    return 1 + (i)*3 +(j)

def exactlyOne(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
        
def notTheSame(vertex):
    for j in range(3):
        edge = []
        for v in vertex:
            edge.append(-1 * var (v-1,j))
        if LOG: print(vertex, ":", edge)
        clauses.append(edge)

if DEBUG:
    n, m = map(int, test.readline().split())
    edges = [ list(map(int, test.readline().split())) for i in range(m) ]
else:
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    
clauses = []

    
for i in range(n):
    literals = [var(i, j) for j in range(3)]
    if LOG: print(literals)
    exactlyOne(literals)
    
for i, vertex in enumerate(edges):
    if LOG: print(i+1, vertex)
    notTheSame(vertex)

def printEquisatisfiableSatFormula():
    if LOG: print("-----------------------")
    print(len(clauses), 3*n)
    for C in clauses:
        c = ' '.join(str(i) for i in C)
        print(c,"0")


printEquisatisfiableSatFormula()
