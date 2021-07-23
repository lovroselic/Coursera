# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:32:49 2020

@author: SELICLO1
"""

def RC_char(c):
    if c == 'A': return 'T'
    if c == 'C': return 'G'
    if c == 'G': return 'C'
    if c == 'T': return 'A'
    
def ReverseComplement(string):
    rc = ""
    for c in reversed(string):
        rc += RC_char(c)
    return rc
    
test = 'GCTAGCT'
sol = ReverseComplement(test)
print(sol)