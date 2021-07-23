#Uses python3
#https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
#https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

# =============================================================================
# function LCSLength(X[1..m], Y[1..n])
#     C = array(0..m, 0..n)
#     for i := 0..m
#        C[i,0] = 0
#     for j := 0..n
#        C[0,j] = 0
#     for i := 1..m
#         for j := 1..n
#             if X[i] = Y[j]
#                 C[i,j] := C[i-1,j-1] + 1
#             else
#                 C[i,j] := max(C[i,j-1], C[i-1,j])
#     return C[m,n]
# =============================================================================

import sys

def edit_distance(source, target):
    m = len(source) + 1
    n = len(target) + 1
    D = [[0 for n in range(n)] for m in range(m)]
    for i in range(1, m):
        D[i][0] = i
    for j in range(1, n):
        D[0][j] = j
        
    for j in range(1, n):
        for i in range(1, m):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + cost)
    return D[m - 1][n - 1]

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
#         3
#         2 7 5
#         2
#         2 5'''
#     input = '''
#     1
#     7
#     4
#     1 2 3 4
#     '''
#     input = '''
#     4
#     2 7 8 3
#     4
#     5 2 8 7
#     '''
# =============================================================================
    data = list(map(int, input.split()))

    n = data[0]
    carve = data[1:]
    A = carve[:n]

    carve = carve[n:]
    m = carve[0]
    carve = carve[1:]
    B = carve[:m]

    print(lcs2(A, B))
