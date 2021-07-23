# Uses python3
import sys

def get_number_of_inversions(a):
    [count_inversions, sorted_result] = mergesort_inversions_count(a)
    return count_inversions

def mergesort_inversions_count(a):
    if len(a) == 1:
        return [0, a]
    mid = int(len(a) / 2)
    left = mergesort_inversions_count(a[0:mid])
    right = mergesort_inversions_count(a[mid:])
    return merge(left, right)

def merge(left, right):
    count_inversions = left[0] + right[0]
    left_array = left[1]
    right_array = right[1]

    result = []
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] > right_array[0]:
            result.append(left_array[0])
            count_inversions += len(right_array)
            del(left_array[0])
        else:
            result.append(right_array[0])
            del(right_array[0])
    result = result + left_array
    result = result + right_array
    return [count_inversions, result]


if __name__ == '__main__':
    input = sys.stdin.read()
    input = "5 2 3 9 2 9"
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
