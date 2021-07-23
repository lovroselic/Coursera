# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:50:22 2020

@author: lovro
"""
import random
#text = open("alice2.txt", "r", encoding="utf8").readline().upper().replace('“','').replace('”','').replace(",","").replace(" ", "_")

text = "CAGATTAGCAGATCA"

LN = len(text)
K = 4
reads = int(round(LN/K, 0)) ** 2

readList = list()
for i in range(reads):
    r = random.randrange(LN - K)
    readList.append(text[r:r+K])
    
with open("tests/101", "w") as outfile:
    outfile.write("\n".join(readList))
