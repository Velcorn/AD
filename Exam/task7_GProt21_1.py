def max_profit(W, n):
    G = [0 for x in range(n+1)]
    G[0] = W[0]
    for i in range(1, n+1):
        G[i] = max(G[i-1], W[i] + G[i-2])
    print(G)
    return G[n]


W = [2, 3, 4, 2, 4, 6, 2]
print(max_profit(W, len(W)-1))
