#Uses python3

import sys

def lcs3(source, target, another):
    m = len(source) + 1
    n = len(target) + 1
    o = len(another) + 1
    global Matrix
    Matrix = [[[0 for o in range(o)] for n in range(n)] for m in range(m)]
    for k in range (1, o):
        for j in range(1, n):
            for i in range(1, m):
                #print("debug", i, j, k, source[i - 1], target[j - 1], another[k -1])
                if source[i - 1] == target[j - 1] and target[j - 1] == another[k -1]:
                    Matrix[i][j][k] = Matrix[i - 1][j - 1][k -1] + 1
                else:
                    Matrix[i][j][k] = max(Matrix[i][j - 1][k], Matrix[i - 1][j][k], Matrix[i][j][k - 1])
    
    return Matrix[m - 1][n - 1][o - 1]

def lcs2(source, target):
    m = len(source) + 1
    n = len(target) + 1
    Matrix = [[0 for n in range(n)] for m in range(m)]
    for j in range(1, n):
        for i in range(1, m):
            if source[i - 1] == target[j - 1]:
                Matrix[i][j] = Matrix[i - 1][j - 1] + 1
            else:
                Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])
    
    return Matrix[m - 1][n - 1]


if __name__ == '__main__':
    input = sys.stdin.read()
# =============================================================================
#     input = '''
#     3
#     1 2 3
#     3
#     2 1 3
#     3
#     1 3 5
#     '''
#     input = '''
#     5
#     8 3 2 1 7
#     7
#     8 2 1 3 8 10 7
#     6
#     6 8 3 1 4 7
#     '''
# =============================================================================
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
