def calc_max_value(M):
    max_value = 0
    Z = [0, 1, 2, 3, 4, 5]
    for p in permutations(Z):
        val = 0
        for i in range(len(M)):
            val += M[i][p[i]]
        if val > max_value:
            max_value = val
    return max_value


def permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for p in permutations(lst[1:]):
            for i in range(len(lst)):
                yield p[:i] + lst[0:1] + p[i:]


M = [[8, 5, 17, 13, 9, 1],
     [2, 5, 9, 1, 4, 6],
     [12, 13, 15, 2, 3, 7],
     [4, 2, 2, 4, 1, 4],
     [11, 11, 5, 9, 4, 10],
     [2, 7, 16, 9, 7, 5]]

print(calc_max_value(M))
