def min_coins(C, V):
    n = len(C)
    table = [[0 for x in range(V+1)] for y in range(n+1)]
    table[0] = [x for x in range(V+1)]
    for i in range(1, n+1):
        table[i][0] = 0
        for j in range(V+1):
            if C[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = min(table[i-1][j], table[i][j-C[i-1]] + 1)
    for i in range(n+1):
        if i == 0:
            print(" ", table[i])
        else:
            print(C[i-1], table[i])
    return f"Min number of coins: {table[n][V]}"


def min_coins_gfg(C, V):
    n = len(C)
    table = [1000 for x in range(V + 1)]
    table[0] = 0
    for i in range(V + 1):
        for j in range(n):
            if C[j] <= i:
                table[i] = min(table[i], table[i - C[j]] + 1)
    if table[V] == 1000:
        return -1
    return table, table[V]


C = [1, 5, 6, 9]
V = 11
print(min_coins(C, V))
# print(min_coins_gfg(C, V))
