# python3
import sys
DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample1", "r")

def BWT(text):
    global bwtArray
    bwtArray = []
    #bwtArray.append(text)
    for t in range(0, len(text)):
        cycle = text[t:]+text[:t]
        bwtArray.append(cycle)
        bwtArray.sort()
    bwt =""
    for t in bwtArray:
        bwt += t[-1]
    return bwt

if __name__ == '__main__':
    if DEBUG:
        text = test.readline().strip()
    else:
        text = sys.stdin.readline().strip()
    if DEBUG: 
        print("TEXT:", text)
        print("===============")
    print(BWT(text))