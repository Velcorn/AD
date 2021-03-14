def lis(A):
    n = len(A)
    l = [1 for x in range(n)]
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                l[i] = max(l[i], l[j] + 1)
    return max(l)


A = [1, 3, 1, 7, 1, 1, 9, 3, 4]
print(A)
print(lis(A))
print(A[::-1])
print(lis(A[::-1]))
