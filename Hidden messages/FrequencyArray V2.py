# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:28:22 2020

@author: SELICLO1
"""
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