# python3

import random

def read_input():
    #return ("aaaaa".rstrip(), "baaaaaaa".rstrip())
    #return ("Test".rstrip(), "testTesttesT".rstrip())
    #return ("aba".rstrip(), "abacaba".rstrip())
    return (input().rstrip(), input().rstrip())
    
def hash_func(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = ((ans * x + ord(c)) % p + p) % p
    return ans

def precompute_hashes(pattern, text, p, x):
    hashes = [None] * (len(text) - len(pattern) + 1)
    S = text[(len(text)-len(pattern)):len(text)]
    #print(S)
    hashes[len(text)-len(pattern)] = hash_func(S, p, x)
    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
        #print("y", y)
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        hashes[i] = (x * hashes[i+1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % p
    
    return hashes

# =============================================================================
# def _hash_func(self, s):
#         ans = 0
#         for c in reversed(s):
#             ans = (ans * self._multiplier + ord(c)) % self._prime
#         return ans % self.bucket_count
# =============================================================================

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    _prime = 1000000007
    x = random.randint(0, _prime)
    #print(x)
    hashes = precompute_hashes(pattern, text, _prime, x)
    #print(hashes)
    result = []
    pHash = hash_func(pattern, _prime, x)
    #print(pHash)
    for i in range(0, len(text) - len(pattern) + 1):
        if pHash != hashes[i]:
            continue
        else:
            if text[i:i + len(pattern)] == pattern:
                result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

