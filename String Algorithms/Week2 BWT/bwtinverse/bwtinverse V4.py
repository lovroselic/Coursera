# python3
import sys
import time
DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample4", "r")

def BWT(text):
    global bwtArray
    bwtArray = []
    for t in range(0, len(text)):
        cycle = text[t:]+text[:t]
        bwtArray.append(cycle)
        bwtArray.sort()
    bwt =""
    for t in bwtArray:
        bwt += t[-1]
    return bwt

def inverseBWT(bwt):
    string = ""
    BL = len(bwt)
    global bwtSorted
    global nodeList
    global L_Shift
    bwtSorted = {}
    nodeList = {}
    L_Shift = [] * BL
    
    for i in range(BL):
        c = bwt[i]
        if not (c in nodeList):
            nodeList[c] = []
            bwtSorted[c] = 0
        nodeList[c].append(i)
        bwtSorted[c] += 1   
    
    for c in sorted(bwtSorted):
        L_Shift.extend(nodeList[c])
    
    x = L_Shift[0]
    
    for i in range(BL):
        x = L_Shift[x]
        string += bwt[x]
        
    return string


if __name__ == '__main__':
    if DEBUG:
        text = test.readline().strip()
    else:
        text = sys.stdin.readline().strip()
    if DEBUG: 
        print("TEXT:", text)
        print("===============")
        
    #text = BWT(text)
    #start_time = time.perf_counter()
    bText = inverseBWT(text) 
    #end_time = time.perf_counter()
    #print("iBWT: --- %.4f ---" %(end_time - start_time))
    #print("===============")
    
    print(bText)