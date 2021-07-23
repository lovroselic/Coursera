# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:53:04 2020

@author: SELICLO1
"""

def LSP(S):
    n = len(S)
    lps = [0] * n
    L = 0
    i = 1
    while (i < n):
        if S[i] == S[L]:
            L +=1
            lps[i] = L
            i += 1
        else:
            if L != 0:
                L = lps[L-1]
            else:
                lps[i] = 0
                i += 1
    
    global result
    result = lps[n-1]
    
    if result > n/2:
        return n//2
    else:
        return result
    
S = "CLOVROSELICLO"
print(LSP(S))