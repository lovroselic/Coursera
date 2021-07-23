# python3
import sys
DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample5", "r")
global CA


def PreprocessBWT(bwt):
    global CA
    global sorted_bwt
    CA = {}
    for P in range(len(bwt)):
        C = bwt[P]
        if not (C in CA):
            CA[C] = [0] * (P + 1)
        for key in CA:
            last = CA[key][-1]
            if C == key:
                CA[key].append(last + 1)
            else:
                CA[key].append(last)
    SA = sorted(CA)
    sorted_bwt = sorted(bwt)
    starts = {}
    for S in SA:
        starts[S] = sorted_bwt.index(S)
        
    return [starts, CA]

def CountOccurrences(pattern, bwt, starts, occ):
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            if not (symbol in starts): return 0
            pattern = pattern[:-1]
            top = starts[symbol] + occ[symbol][top]
            bottom = starts[symbol] + occ[symbol][bottom + 1] - 1
        else:
            return bottom - top + 1
    return 0
     


if __name__ == '__main__':
    if DEBUG:
        bwt = test.readline().strip()
        pattern_count = int(test.readline().strip())
        patterns = test.readline().strip().split()
        print("start: ", bwt, pattern_count, patterns)
    else: 
        bwt = sys.stdin.readline().strip()
        pattern_count = int(sys.stdin.readline().strip())
        patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).  
    global starts, occ_counts_before
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
      occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
