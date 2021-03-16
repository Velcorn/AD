def min_coins(C, V):
    n = len(C)
    table = [[0 for x in range(V+1)] for y in range(n+1)]
    table[0] = [x for x in range(V+1)]
    for i in range(1, n+1):
        for j in range(V+1):
            if C[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = min(table[i-1][j], table[i][j-C[i-1]] + 1)

    # Recursion magic.
    used_coins = calc_used_coins(table, [], V, n)

    # Silly printing stuff.
    for i, line in enumerate(table):
        for j, num in enumerate(line):
            if num < 10:
                table[i][j] = f" {num}"
    for i in range(n+1):
        if i == 0:
            print("   |", "  ".join(map(str, table[i])))
            print("----" + "----" * len(table[i]))
        else:
            print(f" {C[i-1]} |" if C[i-1] < 10 else f"{C[i-1]} |", "  ".join(map(str, table[i])))
    if sum(used_coins) != V:
        return "\nNo solution!"
    print(f"\nMin number of coins: {table[n][V]}")
    return "Used coin(s): " + ", ".join(map(str, sorted(used_coins, reverse=True)))


# "Calculate" which coins are used to reach value.
def calc_used_coins(table, used_coins, pos, n):
    while n != 0:
        if n == 1:
            used_coins.append(C[n-1])
            pos -= C[n-1]
            return used_coins
        elif table[n][pos] < table[n-1][pos]:
            used_coins.append(C[n-1])
            pos -= C[n-1]
        else:
            return calc_used_coins(table, used_coins, pos, n-1)


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


C = [3, 5, 6, 9]
V = 7
print(min_coins(C, V))
# print(min_coins_gfg(C, V))
