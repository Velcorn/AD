import random

numbers = [random.randint(1, 1000) for x in range(10)]


def find_sse(A):
    if A[0] <= A[1]:
        j = 0
        i = 1
    else:
        j = 1
        i = 0
    for n in range(2, len(A)):
        if A[n] < A[j]:
            i = j
            j = n
        elif A[n] < A[i]:
            i = n
    return i


print(numbers)
print(find_sse(numbers))
