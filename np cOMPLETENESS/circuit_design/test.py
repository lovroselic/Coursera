# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:33:46 2020

@author: SELICLO1
"""

def lit_to_vertex(lit):
    v = (abs(lit)-1) * 2
    if lit > 0: v += 1
    return v

def vertex_to_lit(v):
    lit = (v + 1)// 2
    if v % 2 != 1:
        lit *= -1
        lit -= 1
    return lit
    

# =============================================================================
# for i in range (1, 10):
#     print(i, lit_to_vertex(i), lit_to_vertex(-i))
#     
# print("\n")
# for i in range (20):
#     print(i, "lit", vertex_to_lit(i))
# =============================================================================
 
print("\nCHECK")
for i in range (-10, 10):
    print(i, vertex_to_lit(lit_to_vertex(i)))
    
print(lit_to_vert())
