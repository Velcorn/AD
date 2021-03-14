def lis(A):
    n = len(A)
    table = [1 for x in range(n)]
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                table[i] = max(table[i], table[j] + 1)
    return max(table)


A = [1, 3, 1, 7, 1, 1, 9, 3, 4]
print(A)
print(lis(A))
print(A[::-1])
print(lis(A[::-1]))
