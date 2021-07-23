# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, M, m, op):
    min_val = math.inf
    max_val = -math.inf
    for k in range(i,j):
        A = evalt(M[i][k], M[k+1][j],op[k])
        B = evalt(M[i][k], m[k+1][j],op[k])
        C = evalt(m[i][k], m[k+1][j],op[k])
        D = evalt(m[i][k], M[k+1][j],op[k])
        #print(A,B,C,D)
        min_val = min(min_val, A, B, C, D)
        max_val = max(max_val, A, B, C, D)
    return min_val, max_val

def get_maximum_value(dataset):
    #write your code here
    #print(dataset)
    global operators, operands
    operators = []
    operands = []
    for i in dataset:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))
    n = len(operands)
    global M,m
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]
    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, M, m, operators)
    return M[0][n-1]


if __name__ == "__main__":
    #test = "5-8+7*4-8+9"
    print(get_maximum_value(input()))
    #print(get_maximum_value(test))
