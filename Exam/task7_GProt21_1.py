def max_profit(W, n):
    G = [0 for x in range(n+1)]
    for i in range(0, n+1):
        if i == 0:
            G[i] = W[i]
        elif i == 1:
            G[i] = max(W[i], W[i+1])
        else:
            G[i] = max(G[i-1], W[i] + G[i-2])
    return G, G[n]


W = [2, 3, 4, 2, 4, 6, 2]
print(max_profit(W, len(W)-1))
