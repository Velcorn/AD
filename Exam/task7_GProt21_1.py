def max_profit(W, n):
    G = [0 for x in range(n+1)]
    G[0] = W[0]
    G[1] = max(W[0], W[1])
    for i in range(0, n+1):
        G[i] = max(G[i-1], W[i] + G[i-2])
    print(G)
    return G[n]


W = [2, 3, 4, 2, 4, 6, 2]
print(max_profit(W, len(W)-1))
