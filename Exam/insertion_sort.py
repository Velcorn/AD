def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        print(A)
        A[i+1] = key
    return A


A = [15, 33, 17, 8, 3, 2, 1]
print(insertion_sort(A))
