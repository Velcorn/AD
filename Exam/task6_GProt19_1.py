def binomial(n, k):
    table = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if j == 0 or j == i:
                table[i][j] = 1
            else:
                table[i][j] = table[i-1][j-1] + table[i-1][j]
    return table, table[n][k]


print(binomial(5, 2))
