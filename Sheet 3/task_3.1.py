import math


def merge_max_heaps(A1, A2):
    A = A1 + A2
    print(A)
    i = len(A)-1
    while i > 0:
        pi = math.floor((i-1)/2)
        if A[i] > A[pi]:
            A[i], A[pi] = A[pi], A[i]
        i -= 1
    return A


A1 = [10, 7, 6]
A2 = [12, 8, 5]
print(merge_max_heaps(A1, A2))