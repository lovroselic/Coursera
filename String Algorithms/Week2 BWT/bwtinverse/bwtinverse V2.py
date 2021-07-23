# python3
import sys
DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample4", "r")

def naiveInverseBWT(bwt):
    #global Tarr
    BL = len(bwt)
    Tarr = [""] * BL
    for q in range(BL):
        for t in range(BL):
            Tarr[t] = bwt[t] + Tarr[t]
        Tarr.sort()
    return Tarr[0][1:] + Tarr[0][:1]

def compShift():
    pass

def inverseBWT(bwt):
    string = ""
    BL = len(bwt)
    global bwtSorted
    global nodeList
    global L_Shift
    bwtSorted = sorted(bwt)
    nodeList = {}
    L_Shift = [] * BL
    for i in range(BL):
        c = bwt[i]
        if not (c in nodeList):
            nodeList[c] = []
        nodeList[c].append(i)
    for c in bwtSorted:
        L_Shift.append(nodeList[c].pop(0))
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

    if DEBUG:
        bText = naiveInverseBWT(text)
        print("=============== Naive:")
        print(bText)
        print("=============== Fast:")
    bText = inverseBWT(text)
    print(bText)