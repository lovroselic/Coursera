# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:12:21 2020

@author: SELICLO1
"""

def HammingDistance(a,b):
    mm = 0
    for i,s in enumerate(a):
        if s != b[i]: mm+= 1
    return mm

def ApproximatePatternMatching(pat, text, tol):
    SL = len(text)
    PL = len(pat)
    starts = []
    for i in range(SL - PL + 1):
        window = text[i:i + PL]
        hd = HammingDistance(pat, window)
        if hd <= tol:
            starts.append(i)
    return starts

def ApproximatePatternCount(Text, Pattern, d):
    return len(ApproximatePatternMatching(Pattern, Text, d))

Pattern = 'ATTCTGGA'
Text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
d = 3

result = ApproximatePatternMatching(Pattern, Text, d)
print(result)

# =============================================================================
# starts = ApproxymatMatching(pat, string, tol)
# print(len(starts))
# print(" ".join(map(str, starts)))
# =============================================================================
    