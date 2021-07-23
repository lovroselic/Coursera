# python3

#test1
test = '''add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213'''
test2 = '''find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0'''

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

# =============================================================================
# def read_queries(test):
#     q = test.split("\n")
#     n = len(q)
#     return [Query(q[i].split()) for i in range(n)]
# =============================================================================

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    #contacts = [None for i in range(10**7 + 1)]
    contacts = [None] * (10**7)
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        else:
            response = 'not found'
            if contacts[cur_query.number] is not None:
                response = contacts[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
    #write_responses(process_queries(read_queries(test2)))

