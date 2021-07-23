# python3

# =============================================================================
# test = '''add world
# add HellO
# check 4
# find World
# find world
# del world
# check 4
# del HellO
# add luck
# add GooD
# check 2
# del good'''
# tests = test.split("\n");
# =============================================================================

test = '''check 11
del cwNqazSgq
find nvURhSyKS
find wAG
add CioXHYV
find eBxHRU
check 35
check 31
add t
find MZm
find s
find t
find fIeyns
add laJZNL
del arZZXPp
del cHJjD
add vMWlPvkPvuf
add O
check 29
find ZuzOjbCxhYKl
add CioXHYV
add CdpInczxYRyfBj
check 4
add gHUR
check 17
find tUvsiIUxzUbdb
check 11
find lKikJgNGhnPMgSE
find fKl
check 19
find BqHlql
del SNK
del moedzmytBtth
add O
check 37
check 24
del CRvmMOn
add sZrzjJIf
check 6
find snYyWMhYrKKtK
del F
add m
del nupqimflfTe
find FnIwVveUbm
del nISZ
add UjNkKtHxBwRj
del ydr
find fksIHIZtgwHQAJl
add fhzLy
check 42
add pUvhkEQzm
del i
check 8
add tWLfcAO
del t
check 14
check 15
find pFKwzJoYPRib
find JcKlh
del IjrYsmaQIECB
check 36
check 7
find K
find etIlCjME
check 18
check 38
add qvxNdIxpWrbbCS
add MSNFc
add Wrula
check 35
add TN
add UVgxfLpJYCM
add pNYThzpnzX
find xffmYLB
find ICSGW
find L
del m
check 24
del O
check 18
find LfUWtcVaebHab
add Vzep
add MSNFc
del UeqCvdjfCzousF
del OsMWahyK
check 5
find kxeahgVrGVQR
check 26
add TN
check 11
find QlEyEjLRWdUQTcO
find YQz
check 9
add MzJyihsDPoLNGi
del RPpY
find NcYerUntZzUX'''
tests = test.split("\n");

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [None] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        if chain is not None:
            print(' '.join(chain))
        else:
            print(' ')

    def read_query(self):
        #return Query(input().split())
        return Query(test.split())

    def process_query(self, query):
        #
        #print("+++++++++++++++")
        #print("query", vars(query))
# =============================================================================
#         if hasattr(query, "s"): 
#             print("query.s:", query.s, self._hash_func(query.s))
# =============================================================================
        #
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
# =============================================================================
#             # use reverse order, because we append strings to the end
#             self.write_chain(cur for cur in reversed(self.elems)
#                         if self._hash_func(cur) == query.ind)
# =============================================================================
        else:
            hashKey = self._hash_func(query.s)
            #print("hashKey", hashKey)
            if query.type == 'add':
                if self.elems[hashKey] == None:
                    self.elems[hashKey] = [query.s]
                else:
                    if query.s not in self.elems[hashKey]:
                        self.elems[hashKey].insert(0, query.s)
            elif query.type == 'find':
                if self.elems[hashKey] is not None and query.s in self.elems[hashKey]:
                    self.write_search_result(True)
                else:
                    self.write_search_result(False)
            elif query.type == 'del':
                if self.elems[hashKey] is not None and query.s in self.elems[hashKey]:
                    self.elems[hashKey].remove(query.s)
                    if len(self.elems[hashKey]) == 0:
                        self.elems[hashKey] = None
            else:
                print("query.type ERROR", query.type)
# =============================================================================
#             try:
#                 ind = self.elems.index(query.s)
#             except ValueError:
#                 ind = -1
#             if query.type == 'find':
#                 self.write_search_result(ind != -1)
#             elif query.type == 'add':
#                 if ind == -1:
#                     self.elems.append(query.s)
#             else:
#                 if ind != -1:
#                     self.elems.pop(ind)
# =============================================================================

    def process_queries(self):
        #n = int(input())
        n = 96
        for i in range(n):
            #self.process_query(self.read_query())
            self.process_query(Query(tests[i].split()))

if __name__ == '__main__':
    #bucket_count = int(input())
    bucket_count = 43
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
