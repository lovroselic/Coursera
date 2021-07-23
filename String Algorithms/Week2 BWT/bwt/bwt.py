# python3
import sys
#DEBUG = False
DEBUG = True
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
        #text = test.readline().strip()
        text = """The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character string into runs of similar characters. 
        This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by 
        techniques such as move-to-front transform and run-length encoding. More importantly, the transformation is reversible, 
        without needing to store any additional data except the position of the first original character. The BWT is thus a "free" 
        method of improving the efficiency of text compression algorithms, costing only some extra computation.$"""
    else:
        text = sys.stdin.readline().strip()
    if DEBUG: 
        print("TEXT:", text)
        print("===============")
    print(BWT(text))