# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:28:22 2020

@author: SELICLO1
"""

def cToN(c):
    if c == 'A': return 0
    if c == 'C': return 1
    if c == 'G': return 2
    if c == 'T': return 3
    
MAP = ['A', 'C', 'G', 'T']
    
def NumberToPattern(x, K):
    pat = []
    while K > 0: 
        R = x % 4
        x = x // 4
        #print(x, R)
        pat.insert(0, MAP[R])
        K -= 1
    return "".join(pat)
    
def PatternToNumber(pat):
    K = len(pat) - 1
    number = 0
    for i, p in enumerate(pat):
        K = len(pat) - i - 1
        #print(K, p)
        number += cToN(p) * (4 ** K)
    return number

def ComputingFrequencies(text,k):
    FrequencyArray = [0 for i in range(4**k)]
    for i in range(len(text) - k + 1):
        Pattern = text[i:i+k]
        #print(Pattern)
        n = PatternToNumber(Pattern)
        FrequencyArray[n] += 1
    
    return FrequencyArray
    
    
text = 'ACGCGGCTCTGAAA'
n = 2

FA = ComputingFrequencies(text, n)
print(" ".join(map(str, FA)))