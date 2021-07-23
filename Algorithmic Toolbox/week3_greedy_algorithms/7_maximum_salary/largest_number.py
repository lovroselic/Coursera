#Uses python3

import sys

def isGreater(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largest_number(a):
    answer = []
    while len(a) > 0:
        maxDigit = 0
        for digit in a:
            if isGreater(digit, maxDigit):
                maxDigit = digit  
        answer.append(maxDigit)
        a.remove(maxDigit) 
        
    res = ""
    for x in answer:
        res += str(x)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
