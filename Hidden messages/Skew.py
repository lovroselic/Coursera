# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:46:42 2020

@author: SELICLO1
"""
def readTextFroFile(name, dropHeader = True, join = True):
    lines = []
    with open(name) as file:
        for line in file:
            lines.append(line)
    if dropHeader:
        del(lines[0])
    if join:
        lines = "".join(map(lambda x: x.rstrip("\r\n"), lines))
    return lines
    
def Skew(genome):
    skew = [0]
    for g in genome:
        last = skew[-1]
        if g == 'G': 
            last +=1
        elif g == 'C':
            last -= 1
        skew.append(last)
        
    return skew

def findMin(skew):
    m = min(skew)
    mins = []
    for i,v in enumerate(skew):
        if v == m:
            mins.append(i)
    return mins

def FindMinSkewIndex(genome):
    indices = findMin(Skew(genome))
    return " ".join(map(str, indices))
    
fileName = "Salmonella_enterica.txt"
genome = readTextFroFile(fileName)

#genome = 'GATACACTTCCCGAGTAGGTACTG'
sol = FindMinSkewIndex(genome)
print(sol)