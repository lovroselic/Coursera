# python3
from sys import stdin
import itertools

EPS = 1e-9
TOL = 1e-3

#DEBUG = False
DEBUG = True
#LOG = True
LOG = False
if DEBUG: test = open("tests\\189", "r")

def find_subsets(s, n):
    return list(itertools.combinations(s, n))

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while abs(a[pivot_element.row][pivot_element.column]) < EPS:
        pivot_element.row += 1
        if (pivot_element.row >= len(a)):
            return None
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    #optimize
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    scale = a[pivot_element.row][pivot_element.column]
    for x in range(pivot_element.column, len(a[pivot_element.row])):
        a[pivot_element.row][x] /= scale
    b[pivot_element.row] /= scale

    for y in range(pivot_element.column + 1, len(a)):
        factor = a[y][pivot_element.column] / a[pivot_element.row][pivot_element.column]
        for x in range(pivot_element.column, len(a[pivot_element.row])):
            a[y][x] -= factor * a[pivot_element.row][x]
        b[y] -= factor * b[pivot_element.row]
    return

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if pivot_element is None:
            return None
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
        
    for row in range(size-1, 0, -1):
        for c in range(row-1, -1, -1):
            factor = a[c][row]/a[row][row]
            a[c][row] -= factor * a[row][row]
            b[c] -= factor *b[row]

    return b

def EquationFromSubset(s):
    a = []
    b = []
    for t in s:
        a.append(A[t].copy())
        b.append(B[t])
    return Equation(a,b)

def calcEQ(e, sol):
    sum = 0;
    for i in range (len(e)):
        sum += e[i]*sol[i]
    return sum

def setZero(solution):
    for s in range(len(solution)):
        if solution[s] < 0: solution[s] = 0
    return solution

def checkSolution(solution):
    satisfy = True
    for e in range(len(A)):
        check = calcEQ(A[e], solution)
        solves = check <= B[e] + TOL
        if solves == False:
            satisfy = False
            break
            
    if satisfy == True:
        return solution
    else:
        return None
 
def solve_diet_problem(n, m, A, b, c):  
      subsets = find_subsets([i for i in range(len(A))], m)
      Solutions = []
      
      for s in subsets:
        eq = EquationFromSubset(s)
        solution = SolveEquation(eq)
        if solution is not None:
            solution = checkSolution(solution)
            if solution is not None:
                Solutions.append(solution)
 
      if len(Solutions) == 0:
          return [-1, [0] * m]
      else:
          sol, pl = maximize(Solutions)
          if sum(sol) >= 1e9-TOL:
              return [1, [0] * m]
          else:
              return [0, sol]
  
def maximize(Solutions):
    i = -1
    pl = -float("Inf")
    for sol in range(len(Solutions)):
        val = calcEQ(C, Solutions[sol])
        if LOG: print(Solutions[sol], "val", val)
        if val > pl: 
            i = sol
            pl = val
    return [Solutions[i], pl]

if DEBUG:
    n, m = list(map(int, test.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, test.readline().split()))]
    B = list(map(int, test.readline().split()))
    C = list(map(int, test.readline().split()))
else:
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    B = list(map(int, stdin.readline().split()))
    C = list(map(int, stdin.readline().split()))
    
#add >0
for i in range(m):
    temp = [0] * m
    temp[i] = -1
    A += [temp]
    B.append(0)

#add <1e9 infinity boundary    
temp = [1] * m
A += [temp]
B.append(1e9)

anst, ansx = solve_diet_problem(n, m, A, B, C)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
