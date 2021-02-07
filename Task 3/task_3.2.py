def calc(N, A):
    visited = set()
    table = [0] * (N + 1)
    adj = dict()
    for e in A:
        if e[0] in adj:
            adj[e[0]].append(e[1])
        else:
            adj[e[0]] = [e[1]]
    for v in range(1, N + 1):
        if v not in visited:
            helper(v, adj, table, visited)
    count = 0
    for i in range(1, N + 1):
        count = max(count, table[i])
    return count


def helper(v, adj, table, visited):
    visited.add(v)
    try:
        for w in adj[v]:
            if w not in visited:
                helper(w, adj, table, visited)
            table[v] = max(table[v], table[w]+1)
    except KeyError:
        pass


print(calc(3, [[1, 2], [2, 3]]))
print(calc(5, [[3, 4], [1, 5], [1, 4], [4, 5], [2, 5]]))
print(calc(7, [[1, 2], [3, 4], [1, 5], [3, 7], [4, 6], [5, 7], [2, 3], [6, 7], [2, 6], [5, 6], [1, 6], [2, 5], [4, 7]]))
print(calc(6, [[2, 4], [4, 6], [2, 3], [5, 6], [3, 6], [1, 6], [1, 3], [3, 5]]))
