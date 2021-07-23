# python3

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
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
        else:
            hashKey = self._hash_func(query.s)
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

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
