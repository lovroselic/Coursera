# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    STACK = []
    #global unmatched
    unmatched = []
    for i, next in enumerate(text):
        #print (i, next)
        if next in "([{":
            # Process opening bracket, write your code here
            #print("pushing", next)
            STACK.append(next)
            unmatched.append(i+1)

        if next in ")]}":
            # Process closing bracket, write your code here
            if (len(STACK) == 0): return i + 1
            left = STACK.pop()
            #print("pulling", left)
            if are_matching(left, next):
                #print("matched", left, next)
                _ = unmatched.pop()
                continue
            else:
                #print("not matching")
                return i + 1
    if len(STACK) == 0: 
        return "Success"
    else:
        #print("DEBUG", i + 1, len(STACK), unmatched.pop())
        return unmatched.pop()


def main():
    text = input()
    #text = "foo(bar[i);"
    global mismatch
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
