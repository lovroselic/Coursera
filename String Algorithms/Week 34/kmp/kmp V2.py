# python3
import sys
#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample3", "r")


def PrefixFunction(P):
    LP = len(P)
    s = [None] * LP
    s[0] = 0
    border = 0
    for i in range(1, LP):
        while (border > 0) and (P[i] != P[border]):
            border = s[border -1]
        if P[i] == P[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def KMP(pattern, text):
    result = []
    S = pattern + '$' + text
    global s
    s = PrefixFunction(S)
    for i in range(len(pattern) + 1, len(S)):
        if s[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    return result

def overlap(pre, suf):
    for p in range(len(pre)):
        pat = pre[:p]
        print(pat, KMP(pat, suf))


text = 'TGCATATACTTGATATA'        
pattern = 'GATATATGCATTTTTTT'

test1 = "ABRAtrew"
test2 = "qwerABRA"

print(pattern, text)
print("======================")
    
result = KMP(pattern, text)
#print(" ".join(map(str, result)))
# =============================================================================
# for p in range(len(pattern)):
#     pat = pattern[:p]
#     print(pat, KMP(pat, text))
# =============================================================================
o = overlap(test1,test2)
print(o)

