import math


def merge_max_heaps(A1, A2):
    A = A1 + A2
    i = len(A)-1
    while i > 0:
        pi = math.floor(i/2)
        if A[i] > A[pi]:
            A[i], A[pi] = A[pi], A[i]
        i -= 1
    return A


A1 = [10, 7, 6, 4, 3]
A2 = [12, 8, 5, 2, 1]
print(A1+A2)
print(merge_max_heaps(A1, A2))
