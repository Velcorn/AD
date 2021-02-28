def longest_ascending_subsequence(A):
    l = [1 for x in range(len(A))]
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            l[i] = l[i-1] + 1
    return l, max(l)


A = [1, 3, 5, 7, 9, 1, 2, 3, 4]
print(A)
print(longest_ascending_subsequence(A))
print(A[::-1])
print(longest_ascending_subsequence(A[::-1]))
