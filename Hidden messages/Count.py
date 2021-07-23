# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:04:53 2020

@author: SELICLO1
"""

def Count(text, pattern):
    count = 0
    start = 0
    while True:
        start = text.find(pattern, start) + 1
        if start > 0:
            count +=1
        else:
            return count
        
def PatternMatching(pattern, text):
    count = 0
    start = 0
    position = []
    while True:
        start = text.find(pattern, start)
        if start > -1:
            count +=1
            position.append(start)
            start += 1
        else:
            return position

# =============================================================================
# text = 'ACAACTATGCATACTATCGGGAACTATCCT'
# pattern = 'ACTAT'
# =============================================================================

text = 'GATATATGCATATACTT'
pattern = 'ATAT'
#print(Count(text, pattern))
#print(StartingPosition(text, pattern))
#count = Count(text, pattern)
#print(count)
#print(" ".join(map(str, pos)))
result = PatternMatching(pattern, text)
print(result)