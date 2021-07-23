# python3
import sys
DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample3", "r")


def build_suffix_array(text):
    global temp
    temp = {}
    for i in range(len(text)):
        temp[text[i:]] = i
    result = [temp[sf] for sf in sorted(temp)]
    return result


if __name__ == '__main__':

    if DEBUG:
        text = test.readline().strip()
        print(text)
        print("======================")
    else:
        text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
    #print(" ".join(map(str, build_suffix_array(text))))
    #print(sorted(build_suffix_array(text)))
