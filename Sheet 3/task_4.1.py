import numpy as np
from scipy.optimize import linear_sum_assignment


def max_value(M):
    M2 = subtract_means(M)
    # print(M2)
    Z = np.zeros(6)
    rows = np.zeros(6)
    cols = np.zeros(6)
    while len(Z) < 6:
        max_idx = np.where(M2 == np.max(M2))
    return M2


def subtract_means(M):
    M2 = np.copy(M)
    M2 = M2 - np.mean(M2, axis=0) - np.mean(M2, axis=1) - np.mean(M2)
    return M2


M = np.array([[8, 5, 17, 13, 9, 1],
              [2, 5, 9, 1, 4, 6],
              [12, 13, 15, 2, 3, 7],
              [4, 2, 2, 4, 1, 4],
              [11, 11, 5, 9, 4, 10],
              [2, 7, 16, 9, 7, 5]])
print(max_value(M))

row, col = linear_sum_assignment(M, maximize=True)
'''print(f"Coordinates: {list(zip(row, col))}")
print(f"Max sum: {M[row, col].sum()}")
'''