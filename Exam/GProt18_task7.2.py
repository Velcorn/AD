def longest_ascending_subsequence(A):
    n = len(A)
    table = [1 for x in range(n)]
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                table[i] = max(table[i], table[j] + 1)
    return table, max(table)


A = [1, 3, 1, 7, 1, 1, 9, 3, 4]
print(A)
print(longest_ascending_subsequence(A))
print(A[::-1])
print(longest_ascending_subsequence(A[::-1]))
