def quicksort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        print(A)
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


# A = [20, 13, 8, 5, 2, 12, 9]
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# A = [1, 2, 4, 3, 8, 6, 7, 9, 5]
print(quicksort(A[::-1], 0, len(A)-1))
