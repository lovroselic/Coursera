def lcs2(source, target):
    global Matrix
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


A = "123qwertzui"
B = "123yxcvbq"
sol = lcs2(A,B)