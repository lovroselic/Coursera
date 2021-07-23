# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:12:21 2020

@author: SELICLO1
"""

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Text, Pattern, d):
    count = 0 # initialize count variable
    # your code here
    SL = len(Text)
    PL = len(Pattern)
    for i in range(SL - PL + 1):
        if HammingDistance(Pattern, Text[i:i + PL]) <= d: count+=1
    return count


# Insert your HammingDistance function on the following line.
def HammingDistance(a,b):
    mm = 0
    for i,s in enumerate(a):
        if s != b[i]: mm+= 1
    return mm


Pattern = 'TGT'
Text = 'CGTGACAGTGTATGGGCATCTTT'
d = 1

result = ApproximatePatternCount(Text, Pattern, d)
print(result)

# =============================================================================
# starts = ApproxymatMatching(pat, string, tol)
# print(len(starts))
# print(" ".join(map(str, starts)))
# =============================================================================
    