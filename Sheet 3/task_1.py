import math


def stooge_sort(A, i, j):
    if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
    if i+1 >= j:
        return
    k = math.floor((j-i+1)/3)
    stooge_sort(A, i, j-k)
    print(A)
    stooge_sort(A, i+k, j)
    print(A)
    stooge_sort(A, i, j-k)
    print(A)
    return A


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(A)
print(stooge_sort(A, 0, len(A)-1))
