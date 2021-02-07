def calc(N, A):
    visited = set()
    table = [0] * (N + 1)
    children = [[] for i in range(N)]
    for e in A:
        children[e[0]-1].append(e[1])
    for v in range(1, N + 1):
        if v not in visited:
            helper(v, children, table, visited)
    count = 0
    for i in range(1, N + 1):
        count = max(count, table[i])
    return count


def helper(v, children, table, visited):
    visited.add(v)
    for w in children[v-1]:
        if w not in visited:
            helper(w, children, table, visited)
        table[v] = max(table[v], table[w]+1)


print(calc(3, [[1, 2], [2, 3]]))
print(calc(5, [[3, 4], [1, 5], [1, 4], [4, 5], [2, 5]]))
print(calc(7, [[1, 2], [3, 4], [1, 5], [3, 7], [4, 6], [5, 7], [2, 3], [6, 7], [2, 6], [5, 6], [1, 6], [2, 5], [4, 7]]))
print(calc(6, [[2, 4], [4, 6], [2, 3], [5, 6], [3, 6], [1, 6], [1, 3], [3, 5]]))
