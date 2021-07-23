#python3

'''
this problem is quite similar to problem 2. use 3 mers as example. 
000=0, 001=1 ..., 111=7. to build graph, simply connect number to number*2%8 and number*2%8+1.
 for example vertex 6 (110) is conect to 6*2%8=4 (100) and 6*2%8+1=5 (101). 
 after this the problem is exactly this sample as problem two. when print out, just print number%2.
'''
#https://www.geeksforgeeks.org/de-bruijn-sequence-set-1/

DEBUG = True

def Euler(ADJ):
    currentpath = [0]
    cycle = []
    
    while len(currentpath) > 0:
        vertex = currentpath[-1]
        if ADJ[vertex]:
            nextVertex = ADJ[vertex].pop()
            currentpath.append(nextVertex)
        else:
            cycle.append(currentpath.pop())
            
    result = [cycle[i] for i in range(len(cycle)-1, 0, -1)]
    return result


# =============================================================================
# # Main
# =============================================================================

N = int(input())
#N = 4
nodes = 2 ** (N-1)
ADJ = [[] for _ in range(nodes)]
for n in range(nodes):
    i = (n * 2) % nodes
    ADJ[n].append(i)
    ADJ[n].append(i+1)
    
result = Euler(ADJ)
#string =[i % 2 for i in result]
print("".join(map(str, [i % 2 for i in result])))