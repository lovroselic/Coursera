# python3

#https://towardsdatascience.com/course-2-data-structure-part-2-priority-queues-and-disjoint-set-ed11a0383011

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        if (self.ranks[dst] > self.ranks[src]):
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] = self.row_counts[src_parent] + self.row_counts[dst_parent]
            self.row_counts[src_parent] = 0
        else:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] = self.row_counts[src_parent] + self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1
        
        # update max_row_count with the new maximum table size
        self.max_row_count = max(self.row_counts)
        return True

    def get_parent(self, table):
        # find parent and compress path
        if (table != self.parents[table]):
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


# =============================================================================
# def main():
#     n_tables, n_queries = map(int, input().split())
#     counts = list(map(int, input().split()))
#     assert len(counts) == n_tables
#     db = Database(counts)
#     for i in range(n_queries):
#         dst, src = map(int, input().split())
#         db.merge(dst - 1, src - 1)
#         print(db.max_row_count)
# 
# 
# if __name__ == "__main__":
#     main()
# =============================================================================

#n_tables, n_queries = map(int, input().split())
n_tables, n_queries = map(int, "6 4".split())
n_tables, n_queries = map(int, "5 5".split())
#counts = list(map(int, input().split()))
counts = list(map(int, "10 0 5 0 3 3".split()))
counts = list(map(int, "1 1 1 1 1".split()))
assert len(counts) == n_tables
inp = ['6 6', '6 5', '5 6', '4 3']
inp = ['3 5', '2 4', '1 4', '5 4', '5 3']
db = Database(counts)
for i in range(n_queries):
    #dst, src = map(int, input().split())
    dst, src = map(int, inp[i].split())
    db.merge(dst - 1, src - 1)
    print(db.max_row_count)