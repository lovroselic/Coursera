# python3
import sys
#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample4", "r")
global CA


# =============================================================================
# def PreprocessBWT(bwt):
#     """
#     Preprocess the Burrows-Wheeler Transform bwt of some text
#     and compute as a result:
#       * starts - for each character C in bwt, starts[C] is the first position 
#           of this character in the sorted array of 
#           all characters of the text.
#       * occ_count_before - for each character C in bwt and each position P in bwt,
#           occ_count_before[C][P] is the number of occurrences of character C in bwt
#           from position 0 to position P inclusive.
#     """
#     # Implement this function yourself
#     global CA
#     CA = {}
# # =============================================================================
# #     for C in bwt:
# #         if DEBUG: print(C)
# #         if not (C in CA):
# #             CA[C] = [0]
# #     #CA = sorted(CA)
# #     print("CA", CA)
# # =============================================================================
#     for P in range(len(bwt)):
#         C = bwt[P]
#         if DEBUG: print(P, C)
#         if not (C in CA):
#             
#         for key in CA:
#             if DEBUG: print("....", key, C)
#             last = CA[key]
#             print(last)
#             if C == key:
#                 CA[key].append(CA[key][-1])
#             else:
#                 CA[key].append(CA[key][-1] + 1)
#     CA = sorted(CA)
#     print("CA", CA)
#     pass
# =============================================================================

def PreprocessBWT(bwt):
    global CA
    CA = {}
    for P in range(len(bwt)):
        C = bwt[P]
        if DEBUG: print("P, C", P, C)
        if not (C in CA):
            CA[C] = [0] * (P + 1)
        for key in CA:
            last = CA[key][-1]
            if DEBUG: 
                print("....", key, C)
                print("...... last", last)
            if C == key:
                CA[key].append(last + 1)
            else:
                CA[key].append(last)
    print("CA", CA)
    return

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
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
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
      occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
