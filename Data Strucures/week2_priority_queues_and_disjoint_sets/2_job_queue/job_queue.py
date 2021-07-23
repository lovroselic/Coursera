# python3


#https://docs.python.org/3.0/library/heapq.html
#https://stackoverflow.com/questions/47564075/most-efficient-1-loop-way-to-use-priority-queue-in-parallel-jobs-task
#https://codereview.stackexchange.com/questions/208772/parallel-processing-simulation
from collections import namedtuple

class Worker:
    def __init__(self, index, workstart):
        self.index = index
        self.workStart = workstart

class BinHeap:
    def __init__(self):
        self.HEAP = []
        self.last = len(self.HEAP) - 1
    
    def swap(self, x, y):
        self.HEAP[x], self.HEAP[y] = self.HEAP[y],self.HEAP[x] 
    
    def resize(self):
        self.last = len(self.HEAP) - 1
    
    def parent(self, i):
        return (i - 1) // 2
    
    def leftChild(self, i):
        return i * 2 + 1
    
    def rightChild(self, i):
        return i * 2 + 2
    
    def siftUp(self, i):
        if i <= 0: return
        if self.HEAP[self.parent(i)].workStart > self.HEAP[i].workStart:
            self.swap(i, self.parent(i))
            self.siftUp(self.parent(i))
        elif self.HEAP[self.parent(i)].workStart == self.HEAP[i].workStart:
            if self.HEAP[self.parent(i)].index > self.HEAP[i].index:
                self.swap(i, self.parent(i))
                self.siftUp(self.parent(i))
                        
    def siftDown(self, i):
        maxIndex = i
        
        L = self.leftChild(i)
        if L <= self.last:
            if self.HEAP[L].workStart < self.HEAP[maxIndex].workStart:
                maxIndex = L
            elif self.HEAP[L].workStart == self.HEAP[maxIndex].workStart:
                if self.last and self.HEAP[L].index < self.HEAP[maxIndex].index:
                    maxIndex = L
                
        R = self.rightChild(i)
        if R <= self.last:
            if self.HEAP[R].workStart < self.HEAP[maxIndex].workStart:
                maxIndex = R
            elif self.HEAP[R].workStart == self.HEAP[maxIndex].workStart:
                if self.HEAP[R].index < self.HEAP[maxIndex].index:
                    maxIndex = R
            
        if i != maxIndex:
            self.swap(i, maxIndex)
            self.siftDown(maxIndex)
            
    def insert(self, node):
        self.HEAP.append(node)
        self.resize()
        self.siftUp(self.last)
        
    def extractMax(self):
        out = self.HEAP[0]
        self.HEAP[0]= self.HEAP[self.last]
        self.HEAP.pop()
        self.resize()
        self.siftDown(0)
        return out
    
    def display(self):
        while self.last >= 0:
            out = self.extractMax()
            print("index:", out.index, "ws:", out.workStart)

def makeWorkerList(n):
    BH = BinHeap()
    for w in range(n):
        BH.insert(Worker(w,0))
    return BH

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    result = []
    workers = makeWorkerList(n_workers)
    for job in jobs:
        next_worker = workers.extractMax()
        result.append(AssignedJob(next_worker.index, next_worker.workStart))
        workers.insert(Worker(next_worker.index, next_worker.workStart + job))

    return result

n_workers, n_jobs = map(int, input().split())
jobs = list(map(int, input().split()))
    
# =============================================================================
# n_workers, n_jobs = map(int, "2 5".split())
# jobs = list(map(int, "1 2 3 4 5".split()))
# =============================================================================
# =============================================================================
# n_workers, n_jobs = map(int, "4 20".split())
# jobs = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split()))
# =============================================================================
assert len(jobs) == n_jobs

assigned_jobs = assign_jobs(n_workers, jobs)

for job in assigned_jobs:
    print(job.worker, job.started_at)