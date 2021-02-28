def binomial(n, k):
    b = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if j == 0 or j == i:
                b[i][j] = 1
            else:
                b[i][j] = b[i-1][j-1] + b[i-1][j]
    return b[n][k]


print(binomial(5, 2))
