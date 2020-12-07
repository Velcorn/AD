from scipy.optimize import linear_sum_assignment

# I could make it guess an assignment, but this bs is not worth 2 points...

'''def max_value(M):
    M2 = M
    row_op(M2)
    no_zeros = 0
    for r in M2:
        if min(r) > 0:
            no_zeros += 1
    for c in range(len(M2)):
        if min([r[c] for r in M2]) > 0:
            no_zeros += 1
    if no_zeros > 0:
        max_value(M2)
    return M


def row_op(M):
    for i in range(len(M)):
        row_min = min(x for x in M[i] if x != 0)
        for j in range(len(M[i])):
            if M[i][j] != 0:
                M[i][j] -= row_min'''


M = [[8, 5, 17, 13, 9, 1],
     [2, 5, 9, 1, 4, 6],
     [12, 13, 15, 2, 3, 7],
     [4, 2, 2, 4, 1, 4],
     [11, 11, 5, 9, 4, 10],
     [2, 7, 16, 9, 7, 5]]
# M = [[-1 * i for i in row] for row in M]
# print(max_value(M))
print(linear_sum_assignment(M, maximize=True))
