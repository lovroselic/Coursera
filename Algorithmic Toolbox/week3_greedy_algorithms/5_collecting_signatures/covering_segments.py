# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def isIn(i, segment):
    #print(i, segment)
    if i >= segment.start and i <= segment.end:
        return True
    else:
        return False

def optimal_points(segments):
    segments.sort(key = lambda x: x.end)
    #print(segments, "segments")
    points = []
    #write your code here
# =============================================================================
#     for s in segments:
#         points.append(s.start)
#         points.append(s.end)
# =============================================================================
    #n = len(segments)
    #index = 0
    while len(segments) > 0:
        include = segments[0].end
        #print("inc", include)
        points.append(include)
        segments.pop(0) #remove
        while len(segments) > 0:
            if isIn(include, segments[0]):
                segments.pop(0) #remove
            else: 
                break            
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "3 1 3 2 5 3 6"
    #input = "4 4 7 1 3 2 5 5 6"
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
