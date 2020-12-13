def max_value(M):
    mv = 0
    Z = [i for i in range(len(M))]
    for p in permutations(Z):
        v = 0
        for i in range(len(M)):
            v += M[i][p[i]]
        if v > mv:
            Z = p
            mv = v
    return Z, mv


def permutations(A):
    perms = []
    if len(A) <= 1:
        perms.append(A)
    else:
        for p in permutations(A[1:]):
            for i in range(len(A)):
                perms.append(p[:i] + A[0:1] + p[i:])
    return perms


M = [[8, 5, 17, 13, 9, 1],
     [2, 5, 9, 1, 4, 6],
     [12, 13, 15, 2, 3, 7],
     [4, 2, 2, 4, 1, 4],
     [11, 11, 5, 9, 4, 10],
     [2, 7, 16, 9, 7, 5]]

print(max_value(M))
