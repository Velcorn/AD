def min_coins(C, V):
    n = len(C)
    table = [1000 for x in range(V + 1)]
    table[0] = 0
    for i in range(V + 1):
        for j in range(n):
            if C[j] <= i:
                x = table[i - C[j]]
                if x + 1 < table[i]:
                    table[i] = x + 1
    if table[V] == 1000:
        return -1
    return table, table[V]


C = [9, 6, 5, 1]
V = 11
print(min_coins(C, V))
