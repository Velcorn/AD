def quicksort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        print(A, p)
        quicksort(A, l, p-1)
        quicksort(A, p+1, r)


def partition(A, l, r):
    x = A[r]
    i = l-1
    for n in range(l, r):
        if A[n] <= x:
            i += 1
            A[i], A[n] = A[n], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


A = [12, 10, 6, 3, 1, 14, 9]
# A = [15, 33, 17, 8, 3, 2, 1]
print(quicksort(A, 0, len(A)-1))
