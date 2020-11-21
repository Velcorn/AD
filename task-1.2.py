import random


def solution(A):
    # An array with less than 2 elements is already sorted.
    if len(A) < 2:
        return A

    # Partition into smaller, equal and greater.
    s, e, g = [], [], []

    # Pivot element.
    p = A[random.randint(0, len(A)-1)]

    # Pass over array elements and sort into partitions.
    for n in A:
        if n < p:
            s.append(n)
        elif n == p:
            e.append(n)
        else:
            g.append(n)

    # Recursive calls.
    return solution(s) + e + solution(g)


print(solution([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
print(solution([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
print(solution([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1])
