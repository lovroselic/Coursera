# python3

#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
if DEBUG: test = open("tests\\01x", "r")

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    if DEBUG: 
        size = int(test.readline())
    else:
        size = int(input())
    a = []
    b = []
    for row in range(size):
        if DEBUG:
            line = list(map(float, test.readline().split()))
        else:
            line = list(map(float, input().split()))
        if LOG: print(row,"/", size, ":", line)
            
        a.append(line[:size])
        b.append(line[size])
    if LOG: print("-----------------------------------------\n")
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
        
    #correct for float
    #while abs(a[pivot_element.row][pivot_element.column]) == 0:
    while abs(a[pivot_element.row][pivot_element.column]) < EPS:
        pivot_element.row += 1
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    #optimize
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    if LOG: print("before:...a:", a, "b", b, "r:",pivot_element.row, "c:", pivot_element.column)
    
    #scale
    scale = a[pivot_element.row][pivot_element.column]
    if LOG: print(".... scale", scale)
    for x in range(pivot_element.column, len(a[pivot_element.row])):
        a[pivot_element.row][x] /= scale
    b[pivot_element.row] /= scale
    #substract
    for y in range(pivot_element.column + 1, len(a)):
        factor = a[y][pivot_element.column] / a[pivot_element.row][pivot_element.column]
        if LOG: print("factor", factor)
        for x in range(pivot_element.column, len(a[pivot_element.row])):
            a[y][x] -= factor * a[pivot_element.row][x]
        b[y] -= factor * b[pivot_element.row]
        
    if LOG: print("after...a:", a, "b", b, "r:",pivot_element.row, "c:", pivot_element.column)
    if LOG: print("-----------------------------------------\n")
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
        if LOG: print("pivot_element", "r:",pivot_element.row, "c:", pivot_element.column)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
        
    if LOG: print("########### process triangular form ###########")
    for row in range(size-1, 0, -1):
        for c in range(row-1, -1, -1):
            factor = a[c][row]/a[row][row]
            a[c][row] -= factor * a[row][row]
            b[c] -= factor *b[row]

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    if not DEBUG: exit(0)
