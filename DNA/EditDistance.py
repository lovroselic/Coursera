# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:46:10 2020

@author: SELICLO1
"""

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

ed = edit_distance("Shakespear", "shake spea")
print(ed)