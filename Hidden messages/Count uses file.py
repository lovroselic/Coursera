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
        
def StartingPosition(text, pattern):
    count = 0
    start = 0
    position = []
    while True:
        start = text.find(pattern, start)
        if start > -1:
            count +=1
            position.append(start)
            start += 1
            #
            #return position, count
        else:
            return position, count

# =============================================================================
# text = 'ACAACTATGCATACTATCGGGAACTATCCT'
# pattern = 'ACTAT'
# =============================================================================

file = open("Vibrio_cholerae.txt", "r", encoding="utf8")
text = file.readline()
#print(len(text))
pattern = 'CTTGATCAT'
#print(Count(text, pattern))
#print(StartingPosition(text, pattern))
pos, count = StartingPosition(text, pattern)
print(" ".join(map(str, pos)))