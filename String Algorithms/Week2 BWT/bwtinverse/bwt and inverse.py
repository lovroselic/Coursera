# python3
import sys
#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample4", "r")

def naiveInverseBWT(bwt):
    global Tarr
    BL = len(bwt)
    Tarr = [""] * BL
    for q in range(BL):
        for t in range(BL):
            Tarr[t] = bwt[t] + Tarr[t]
        Tarr.sort()
    return Tarr[0][1:] + Tarr[0][:1]


def BWT(text):
    global bwtArray
    bwtArray = []
    for t in range(0, len(text)):
        cycle = text[t:]+text[:t]
        #print(cycle)
        bwtArray.append(cycle)
    bwtArray.sort()
    bwt =""
    for t in bwtArray:
        bwt += t[-1]
    return bwt

if __name__ == '__main__':
    if DEBUG:
        text = test.readline().strip()
        #text = "SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES.$"
        #text = "banana$"
    else:
        text = sys.stdin.readline().strip()
    if DEBUG: 
        print("TEXT:", text)
        print("===============")

    bText = naiveInverseBWT(text)
    print(bText)