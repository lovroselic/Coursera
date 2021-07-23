# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:27:16 2020

@author: SELICLO1
"""

from collections import defaultdict

D = defaultdict(set)
T = "T"
D[T].add(1)
D[T].add(2)
D[T].add(3)
D[T].remove(4)