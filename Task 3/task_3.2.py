def calc(N, A):
    visited = set()
    result = []
    adj = dict()

    for e in A:
        if e[0] in adj:
            adj[e[0]].append(e[1])
        else:
            adj[e[0]] = [e[1]]

    print(adj)

    def helper(v):
        if v not in visited:
            visited.add(v)
            try:
                for u in adj[v]:
                    helper(u)
                result.insert(0, v)
            except KeyError:
                result.insert(0, v)

    for i in range(1, N):
        helper(i)

    return result


print(calc(3, [[1, 2], [2, 3]]))
print(calc(5, [[3, 4], [1, 5], [1, 4], [4, 5], [2, 5]]))
print(calc(7, [[1, 2], [3, 4], [1, 5], [3, 7], [4, 6], [5, 7], [2, 3], [6, 7], [2, 6], [5, 6], [1, 6], [2, 5], [4, 7]]))
print(calc(6, [[2, 4], [4, 6], [2, 3], [5, 6], [3, 6], [1, 6], [1, 3], [3, 5]]))
