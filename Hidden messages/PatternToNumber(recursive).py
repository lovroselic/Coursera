# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:06:00 2020

@author: SELICLO1
"""



def NumberToPattern(x, K):
    MAP = ['A', 'C', 'G', 'T']
    pat = []
    while K > 0: 
        R = x % 4
        x = x // 4
        pat.insert(0, MAP[R])
        K -= 1
    return "".join(pat)

def SymbolToNumber(c):
    if c == 'A': return 0
    if c == 'C': return 1
    if c == 'G': return 2
    if c == 'T': return 3

def LastChar(Pattern):
    return Pattern[-1]

def Prefix(Pattern):
    return Pattern[:len(Pattern)-1]

def PatternToNumber(Pattern):
    if len(Pattern) == 0: return 0
    char = LastChar(Pattern)
    prefix = Prefix(Pattern)
    return 4 * PatternToNumber(prefix) + SymbolToNumber(char)
    
X = 7342
K = 10
Pattern = 'AGT'
solution = PatternToNumber(Pattern)
print(solution)
#solution = NumberToPattern(X, K)
#print(solution)
