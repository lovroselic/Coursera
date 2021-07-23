# python3

# =============================================================================
# # n vertice
# # m edge
# # CNF : p cnf V(vars) C(clauses)
# #
# # output C V
# # C lines: clause; k terms; 0 terminated
# =============================================================================

def var(i, j):
    return 1 + (i)*n +(j)

def OneNodeAppearOnce(i):
    clauses.append([var(i,j) for j in range(n)])
    
def EachPositionOnlyOne(j):
    clauses.append([var(i,j) for i in range(n)])
    
def NotTwiceOnDifferent(i):
    for j in range(n):
        for k in range(n):
            if j != k and j < k:
                clauses.append([-var(i,j), -var(i,k)])
                
def NoTwoOnSamePosition(j):
    for i in range(n):
        for k in range(n):
            if i != j and j < i:
                clauses.append([-var (i,k), -var (j,k)])

#DEBUG = False
DEBUG = True
#LOG = True
LOG = False
if DEBUG: test = open("tests\\01", "r")

if DEBUG:
    n, m = map(int, test.readline().split())
    edges = [ list(map(int, test.readline().split())) for i in range(m) ]
else:
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    
clauses = []
ADJ = [[0 for i in range (n)] for i in range (n)]
for edge in edges:
    ADJ[edge[0]-1][edge[1]-1] = 1
    ADJ[edge[1]-1][edge[0]-1] = 1

for i in range(n):
    OneNodeAppearOnce(i)
    EachPositionOnlyOne(i)
    NotTwiceOnDifferent(i)
    NoTwoOnSamePosition(i)
    
#Nonadjacent cannot be adjacent in the path
for x in range(n):
    for y in range(n):
        if ADJ[x][y] == 0 and x != y:
            for k in range(n-1):
                clauses.append([-var(x, k), -var(y, k+1)])
    
    

def printEquisatisfiableSatFormula():
    if LOG: print("\n-----------RESULT------------\n")
    print(len(clauses), n*n)
    for C in clauses:
        c = ' '.join(str(i) for i in C)
        print(c,"0")

printEquisatisfiableSatFormula()
