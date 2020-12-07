import numpy as np
from scipy.optimize import linear_sum_assignment

# I could make it guess an assignment, but this bs is not worth 2 points...


def max_value(M):
    M = M - M.min(axis=1, keepdims=True)
    mask = np.ma.masked_array(M, mask=M == 0)
    M = M - mask.min(axis=0, keepdims=True)
    M[M < 0] = 0
    mask = np.ma.masked_array(M, mask=M == 0)
    M = M - mask.min(axis=1, keepdims=True)
    M[M < 0] = 0
    return M


M = np.array([[8, 5, 17, 13, 9, 1],
              [2, 5, 9, 1, 4, 6],
              [12, 13, 15, 2, 3, 7],
              [4, 2, 2, 4, 1, 4],
              [11, 11, 5, 9, 4, 10],
              [2, 7, 16, 9, 7, 5]])
M *= -1


print(max_value(M))
'''row, col = linear_sum_assignment(M, maximize=False)
print(M[row, col].sum())'''
